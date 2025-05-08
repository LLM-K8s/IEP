import { defineStore } from "pinia";
import axios from "axios";

export const useUserStore = defineStore("userStore", {
  state: () => ({
    userInfo: "", // 存儲使用者
    loading: false, // 加載狀態
    error: null, // 錯誤訊息
  }),
  actions: {
    async fetchUser() {
      this.loading = true;
      this.error = null;
      this.authInfo = JSON.parse(
        localStorage.getItem(
          "oidc.user:http://172.16.1.16:8081/realms/coder:vue"
        )
      );
      try {
        const response = await axios.get(
          "http://localhost:8000/api/current_user/",
          {
            headers: {
              Authorization: `Bearer ${this.authInfo.access_token}`,
            },
          }
        );
        this.userInfo = response.data;
      } catch (error) {
        this.error = error.response?.data?.detail || "無法獲取使用者資料";
        console.error("Fetch user error:", error);
      } finally {
        this.loading = false;
      }
    },
  },
});
