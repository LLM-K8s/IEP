import { defineStore } from "pinia";
import { ref } from "vue";
import axios from "axios";
import swal from "sweetalert";

export const useCourseStore = defineStore("course", () => {
  const courseName = ref("");
  const courseType = ref("");
  const courseIntro = ref("");
  const courseOutline = ref("");
  const courseImage = ref(null);
  const coursePrice = ref(null);
  const errorMessage = ref("");

  function resetForm() {
    courseName.value = "";
    courseType.value = "";
    courseIntro.value = "";
    courseOutline.value = "";
    courseImage.value = null;
    coursePrice.value = null;
    errorMessage.value = "";
  }

  async function submitCourse() {
    console.log("提交的課程資料:", {
      course_name: courseName.value,
      course_type: courseType.value,
      course_intro: courseIntro.value,
      course_outline: courseOutline.value,
      course_image: courseImage.value,
      course_price: Number(coursePrice.value), // 確保為數字
    });

    const payload = {
      course_name: courseName.value,
      course_type: courseType.value,
      course_intro: courseIntro.value,
      course_outline: courseOutline.value,
      course_image: "",
      course_price: Number(coursePrice.value),
      course_content: [],
    };

    try {
      const response = await axios.post(
        "http://localhost:8000/api/courses/",
        payload,
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );
      swal("課程新增成功！", "", "success");
      console.log("儲存成功:", response.data);
      resetForm();
    } catch (error) {
      errorMessage.value =
        error.response?.data?.detail || "儲存失敗，請稍後再試";
      swal("課程提交失敗！", "請稍後再試。", "error");
      console.error("儲存失敗:", error);
    }
  }

  return {
    courseName,
    courseType,
    courseIntro,
    courseOutline,
    courseImage,
    coursePrice,
    errorMessage,
    resetForm,
    submitCourse,
  };
});
