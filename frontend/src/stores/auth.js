import axios from "axios";
import { defineStore } from "pinia";
import { computed, ref } from "vue";
import { authService } from "../services/auth";
import swal from "sweetalert";
import { jwtDecode } from "jwt-decode"; // Added for parsing ID token

const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;

export const useAuthStore = defineStore("auth", () => {
  // 狀態
  const state = ref({
    user: null,
  });

  // 計算屬性
  const isAuthenticated = computed(() => state.value.user !== null);
  const currentUser = computed(() => state.value.user);

  // 方法
  const setAuthState = (user = null) => {
    state.value = { user };
  };

  // 監聽 token 刷新事件
  const setupTokenRefreshListener = () => {
    authService.userManager.events.addUserLoaded(async (user) => {
      console.log("Token 已刷新，更新 store 狀態");
      setAuthState(user);
    });
  };

  const login = async () => {
    try {
      // This will redirect the user to the OIDC provider.
      // The rest of the authentication flow (token exchange, user fetching)
      // is handled by the backend and then by BackendCallbackHandler.vue
      // which calls storeTokensAndFetchUser.
      await authService.login();
    } catch (error) {
      console.error("登入失敗:", error);
      // This error typically occurs if the redirect to OIDC provider fails.
      throw error;
    }
  };

  const logout = async () => {
    try {
      await authService.logout();
      setAuthState();
    } catch (error) {
      console.error("登出失敗:", error);
      throw error;
    }
  };

  const handleRedirect = async () => {
    // This action was previously used with a frontend-only OIDC callback handler.
    // In the new flow, the backend handles the OIDC callback, and then redirects
    // to BackendCallbackHandler.vue. This store action is likely no longer
    // directly part of the main login flow.
    // The setupTokenRefreshListener might still be relevant but is now called
    // from storeTokensAndFetchUser.
    try {
      await authService.handleRedirect(); // This calls userManager.signinRedirectCallback()
      // setupTokenRefreshListener(); // Moved to storeTokensAndFetchUser
    } catch (error) {
      console.error("處理回調時發生錯誤 (handleRedirect action):", error);
    }
  };

  const checkAuth = async () => {
    try {
      // 先檢查本地認證狀態
      const isAuth = await authService.isAuthenticated();
      const user = isAuth ? await authService.getUser() : null;
      setAuthState(user);
      if (!isAuth) {
        return false;
      }

      // 再向後端驗證權限
      await axios.get(`${apiBaseUrl}/api/me/`, {
        headers: {
          Authorization: `Bearer ${user.access_token}`,
        },
      });
      return true;
    } catch (error) {
      if (
        error.response &&
        (error.response.status === 401 || error.response.status === 403)
      ) {
        await logout();
        swal({
          title: "系統自動登出",
          text: "您的登入已過期，請重新登入",
          icon: "warning",
          button: "OK",
        });
      }
      return false;
    }
  };

  return {
    // 計算屬性
    currentUser,
    isAuthenticated,

    // 方法
    login,
    logout,
    handleRedirect,
    checkAuth,
    setupTokenRefreshListener,
    storeTokensAndFetchUser, // Expose the new action
  };
});

// Helper function to store tokens and update user state
// This is the new action for the store
async function storeTokensAndFetchUser(accessToken, idToken, refreshToken = null) { // Add refreshToken parameter
  const authStore = useAuthStore(); // Get instance of the store

  try {
    if (!accessToken || !idToken) { // refreshToken is optional but recommended
      throw new Error("Access token or ID token is missing.");
    }

    // Decode ID token to get profile and expiration
    const decodedIdToken = jwtDecode(idToken);
    const profile = decodedIdToken; // The whole decoded token can serve as a profile
    const expires_at = decodedIdToken.exp;

    // Create a user object compatible with oidc-client-ts
    // This helps if other parts of authService.userManager rely on a stored user.
    const user = {
      access_token: accessToken,
      id_token: idToken,
      refresh_token: refreshToken, // Add refresh_token to the user object
      scope: decodedIdToken.scope || "openid profile email", // Adjust scope as needed
      profile: profile,
      expires_at: expires_at,
      token_type: "Bearer", // Common token type
    };
    
    if (!refreshToken) {
      console.warn("storeTokensAndFetchUser: Refresh token is missing. Session may not persist long-term or allow for silent refresh via refresh tokens.");
    }

    // Store the user using oidc-client-ts UserManager
    // This will also trigger userManager.events.addUserLoaded if listeners are active
    await authService.userManager.storeUser(user);
    authStore.setAuthState(user); // Update Pinia store state
    
    // Call setupTokenRefreshListener here to ensure it's active whenever a user is successfully loaded/stored.
    // This is important for handling token refreshes via oidc-client-ts.
    authStore.setupTokenRefreshListener(); 

    console.log("Tokens stored, user state updated in Pinia, and token refresh listener configured.");

    // Verify user with backend /api/me endpoint
    // The /api/me call is crucial for confirming the token is valid on the backend
    // and fetching potentially more up-to-date user information.
    try {
      const response = await axios.get(`${apiBaseUrl}/api/me/`, {
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      });
      console.log("User verified with backend /api/me:", response.data);
      // Optionally, update user profile in store with data from /api/me.
      // If response.data contains the full user profile as the backend sees it,
      // it might be better to use this to set the auth state.
      // For example: authStore.setAuthState({ ...user, profile: response.data });
      // This ensures frontend state matches backend's view of the user.
      // For now, we'll assume the token's profile is primary and /me is a validation step.
    } catch (error) {
      console.error("Failed to verify user with backend /api/me after storing tokens:", error);
      authStore.setAuthState(); // Clear auth state if /me fails, as user is not truly authenticated with backend
      throw new Error(`Failed to verify user with backend: ${error.message}`);
    }

  } catch (error) {
    console.error("Error in storeTokensAndFetchUser:", error);
    authStore.setAuthState(); // Clear auth state on any error during this critical process
    throw error; // Re-throw to be caught by the calling component
  }
}
