<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '../stores/auth'; // Assuming path is correct

const router = useRouter();
const authStore = useAuthStore();

onMounted(async () => {
  try {
    const hash = window.location.hash.substring(1); // Remove '#'
    const params = new URLSearchParams(hash);
    const accessToken = params.get('access_token');
    const idToken = params.get('id_token');
    const refreshToken = params.get('refresh_token'); // Extract refresh token
    // const state = params.get('state'); // Optional: if you need to use the state

    if (accessToken && idToken) { // Refresh token is optional but highly recommended for session persistence
      await authStore.storeTokensAndFetchUser(accessToken, idToken, refreshToken);
      // Redirect to a protected route or home page after successful login
      router.push('/MyCourse'); // Or any other target route like '/dashboard' or '/'
    } else {
      console.error('Access token or ID token not found in URL hash.');
      // Redirect to an error page or home if tokens are missing
      router.push('/'); // Or '/login-error'
    }
  } catch (error) {
    console.error('Error processing backend callback:', error);
    router.push('/'); // Redirect to home or an error page
  }
});
</script>

<template>
  <div>
    <p>Processing authentication...</p>
    <!-- You can add a loading spinner or a more user-friendly message here -->
  </div>
</template>
