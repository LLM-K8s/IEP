import axios from "axios";
import { UserManager, WebStorageStateStore } from "oidc-client-ts";

const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;

const config = {
  authority: "http://172.16.1.16:8081/realms/coder", // 請替換為您的 OIDC 提供者網址
  client_id: "vue", // 請替換為您的客戶端 ID
  redirect_uri: 'http://your-backend-domain/api/auth/callback', // TODO: Update this to your actual backend callback URL
  response_type: "code",
  scope: "openid profile email", // Ensure 'offline_access' scope is requested if not already for refresh tokens
  post_logout_redirect_uri: `${window.location.origin}/`, // Redirect to homepage after logout. TODO: Ensure this URI (e.g., http://localhost:5173/) is in Keycloak client's valid post-logout redirect URIs.
  userStore: new WebStorageStateStore({ store: window.localStorage }),
  useRefreshToken: true, // Enable refresh token usage
  // automaticSilentRenew: true, // Disabled in favor of refresh token mechanism
  // silent_redirect_uri: `${window.location.origin}/silent-renew.html`, // No longer needed
  // accessTokenExpiringNotificationTime: 60, // Not essential with refresh tokens; oidc-client handles timing
};

const userManager = new UserManager(config);

// 監聽用戶加載事件
// This event is triggered when userManager.storeUser() is called, or after successful silent renew.
userManager.events.addUserLoaded((user) => {
  // storeUser(user.access_token); // Removed: storeUser calls /api/me, which is now handled by storeTokensAndFetchUser in auth.js store.
  // The Pinia store (auth.js) is responsible for updating its state based on this loaded user,
  // typically via setAuthState(user) called within storeTokensAndFetchUser.
  // The primary role here is for oidc-client-ts internal state and potentially logging.
  console.log("用戶已加載 (userManager.events.addUserLoaded)", user);
});

// 監聽用戶卸載事件
userManager.events.addUserUnloaded(() => {
  console.log("用戶已卸載");
});

// 監聽無聲刷新錯誤事件
userManager.events.addSilentRenewError((error) => {
  console.error("Token 刷新失敗:", error);
});

const login = async () => {
  try {
    await userManager.signinRedirect();
  } catch (error) {
    console.error("登入失敗:", error);
    throw error;
  }
};

const logout = async () => {
  try {
    await userManager.signoutRedirect();
  } catch (error) {
    console.error("登出失敗:", error);
    throw error;
  }
};

const handleRedirect = async () => {
  // This function is typically for handling the redirect from the OIDC provider
  // directly on the frontend (e.g., in a /callback route component).
  // In the new flow, the backend handles the OIDC callback.
  // This function is likely no longer used for the main login redirect,
  // but might still be relevant if silent_redirect_uri or post_logout_redirect_uri
  // pages attempt to use it for specific oidc-client-ts interactions.
  try {
    await userManager.signinRedirectCallback();
  } catch (error) {
    console.error("處理回調時發生錯誤:", error);
  }
};

const isAuthenticated = async () => {
  try {
    const user = await userManager.getUser();
    return !!user;
  } catch (error) {
    return false;
  }
};

const getUser = async () => {
  try {
    return await userManager.getUser();
  } catch (error) {
    return null;
  }
};

const storeUser = async (access_token) => {
  try {
    await axios.get(`${apiBaseUrl}/api/me/`, {
      headers: {
        Authorization: `Bearer ${access_token}`,
      },
    });
  } catch (error) {
    console.error("無法儲存使用者資料", error);
    throw error;
  }
};

export const authService = {
  login,
  logout,
  handleRedirect,
  isAuthenticated,
  getUser,
  userManager,
};
