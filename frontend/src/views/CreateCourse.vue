<template>
  <DefaultLayout>
    <div class="w-[90%] mx-[5%]">
      <div class="pt-20 w-[100%]">
        <span class="text-[24px] mt-20 mb-[16px] font-bold h-fit">
          建立新課程 📚
        </span>
        <hr class="border-2 border-gray-500 rounded-2xl" />
      </div>
      <div class="shadow-gray-500 rounded-[8px] w-[100%] self-center p-5">
        <label for="course-name" class="text-[20px] font-bold mb-[10px]"
          >課程名稱</label
        >
        <input
          v-model="courseName"
          id="course-name"
          type="text"
          class="bg-white shadow-2xs shadow-gray-500 text-[16px] w-full border-1 border-solid border-[#ddd] rounded-[8px] p-2 mb-4"
          placeholder="請輸入課程名稱"
        />
        <label for="course-type" class="text-[20px] font-bold mb-[10px]"
          >課程類型</label
        >
        <select
          v-model="courseType"
          id="course-type"
          class="bg-white shadow-2xs shadow-gray-500 text-[16px] w-full border-1 border-solid border-[#ddd] rounded-[8px] p-2 mb-4"
        >
          <option disabled value="" selected>請選擇類型</option>
          <option v-for="type in courseTypes" :key="type" :value="type">
            {{ type }}
          </option>
        </select>
        <label for="course-intro" class="text-[20px] font-bold mb-[10px]"
          >課程簡介</label
        >
        <input
          v-model="courseIntro"
          id="course-intro"
          type="text"
          class="bg-white shadow-2xs shadow-gray-500 text-[16px] w-full border-1 border-solid border-[#ddd] rounded-[8px] p-2 mb-4"
          placeholder="請輸入課程簡介"
        />
        <label for="course-outline" class="text-[20px] font-bold mb-[10px]"
          >教學大綱</label
        >
        <textarea
          v-model="courseOutline"
          id="course-outline"
          type="text"
          class="bg-white shadow-2xs shadow-gray-500 text-[16px] w-full border-1 border-solid border-[#ddd] rounded-[8px] p-2 mb-4"
          placeholder="請描述課程內容與學習目標"
          rows="5"
        ></textarea>
        <label for="course-image" class="text-[20px] font-bold mb-[10px]"
          >課程封面圖片(可選)</label
        >
        <input
          ref="fileInput"
          @change="uploadFile"
          id="course-image"
          type="file"
          class="bg-white shadow-2xs shadow-gray-500 text-[16px] w-full border-1 border-solid border-[#ddd] rounded-[8px] p-2 mb-4 hover:bg-gray-300"
        />
        <label for="course-price" class="text-[20px] font-bold mb-[10px]"
          >課程價格 (新台幣 $TWD)</label
        >
        <input
          id="course-price"
          v-model="coursePrice"
          type="number"
          class="bg-white shadow-2xs shadow-gray-500 text-[16px] w-full border-1 border-solid border-[#ddd] rounded-[8px] p-2 mb-4"
          placeholder="請輸入課程價格"
        />
        <button
          @click="onSubmit"
          class="bg-[#3498db] text-white w-[100%] rounded-lg p-2 mt-[16px] hover:bg-[#2d83bc]"
        >
          提交審核
        </button>
      </div>
    </div>
  </DefaultLayout>
</template>
<script setup>
import DefaultLayout from "../Layout/default.vue";
import { courseTypes } from "../stores/courseType";
import { ref, onMounted } from "vue";
import { useUserStore } from "../stores/user";
import { useAuthStore } from "../stores/auth";
import axios from "axios";
import swal from "sweetalert";

const userStore = useUserStore();
const authStore = useAuthStore();

const fileInput = ref(null);
const courseName = ref("");
const courseType = ref("");
const courseIntro = ref("");
const courseOutline = ref("");
const courseImage = ref(null);
const coursePrice = ref(null);
const errorMessage = ref("");

const resetForm = () => {
  courseName.value = "";
  courseType.value = "";
  courseIntro.value = "";
  courseOutline.value = "";
  courseImage.value = null;
  coursePrice.value = null;
  errorMessage.value = "";
};

const submitCourse = async () => {
  const teacherId = userStore.userInfo.user_id;

  console.log("提交的課程資料:", {
    course_name: courseName.value,
    course_type: courseType.value,
    course_intro: courseIntro.value,
    course_outline: courseOutline.value,
    course_image: courseImage.value,
    course_price: Number(coursePrice.value),
    teacher_id: teacherId,
  });

  const payload = {
    course_name: courseName.value,
    course_type: courseType.value,
    course_intro: courseIntro.value,
    course_outline: courseOutline.value,
    course_image: "",
    course_price: Number(coursePrice.value),
    course_content: [],
    teacher_id: teacherId,
  };

  try {
    const response = await axios.post(
      "http://localhost:8000/api/courses/",
      payload,
      {
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${authStore.currentUser.access_token}`,
        },
      }
    );
    swal("課程新增成功！", "", "success");
    console.log("儲存成功:", response.data);
    resetForm();
  } catch (error) {
    errorMessage.value = error.response?.data?.detail || "儲存失敗，請稍後再試";
    swal("課程提交失敗！", "請稍後再試。", "error");
    console.error("儲存失敗:", error);
  }
};

// 處理檔案上傳事件
function uploadFile(event) {
  const files = event.target.files;
  if (files && files.length > 0) {
    courseImage = files[0]; // 取第一個檔案
  } else {
    courseImage = null;
  }
}

// 送出申請
function onSubmit() {
  console.log(coursePrice.value);
  if (
    courseName.value === "" ||
    courseType.value === "" ||
    courseIntro.value === "" ||
    courseOutline.value === "" ||
    coursePrice.value === null
  ) {
    swal("請填寫所有欄位，才能提交審核！", "", "warning");
    return;
  } else if (coursePrice.value < 0) {
    swal("課程價格不能為負數！", "", "warning");
    return;
  }
  submitCourse();
}

onMounted(() => {
  userStore.fetchUser();
});
</script>
