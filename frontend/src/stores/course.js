import { defineStore } from "pinia";
import { ref } from "vue";

export const useCourseStore = defineStore("course", () => {
  // 定義課程欄位狀態
  const courseName = ref("");
  const courseType = ref("");
  const courseIntro = ref("");
  const courseOutline = ref("");
  const courseImage = ref(null); // 檔案物件
  const coursePrice = ref(null);

  // 清空表單
  function resetForm() {
    courseName.value = "";
    courseType.value = "";
    courseIntro.value = "";
    courseOutline.value = "";
    courseImage.value = null;
    coursePrice.value = null;
  }

  // 模擬送出資料 (可改成呼叫 API)
  function submitCourse() {
    // 這裡可以改成 axios.post 送到後端
    console.log("送出的課程資料", {
      courseName: courseName.value,
      courseType: courseType.value,
      courseIntro: courseIntro.value,
      courseOutline: courseOutline.value,
      courseImage: courseImage.value,
      coursePrice: coursePrice.value,
    });
    // 送出後清空
    resetForm();
  }

  return {
    courseName,
    courseType,
    courseIntro,
    courseOutline,
    courseImage,
    coursePrice,
    resetForm,
    submitCourse,
  };
});
