import { defineStore } from "pinia";
import axios from "axios";

export const useCourseStore = defineStore("courseStore", {
  state: () => ({
    courses: [], // 存儲課程列表
    loading: false, // 加載狀態
    error: null, // 錯誤訊息
  }),
  actions: {
    async fetchCourses() {
      this.loading = true;
      this.error = null;
      try {
        const response = await axios.get("http://localhost:8000/api/courses/");
        this.courses = response.data; // 將課程數據存入狀態
      } catch (error) {
        this.error = error.response?.data?.detail || "無法獲取課程資料";
        console.error("Fetch courses error:", error);
      } finally {
        this.loading = false;
      }
    },
  },
});
