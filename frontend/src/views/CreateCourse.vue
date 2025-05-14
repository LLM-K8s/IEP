<template>
  <DefaultLayout>
    <div class="w-[90%] mx-[5%]">
      <PageTitle title="建立新課程 📚" />
      <div class="shadow-gray-500 rounded-[8px] w-[100%] self-center p-5">
        <Input
          id="course-name"
          v-model="courseName"
          label="課程名稱"
          placeholder="請輸入課程名稱"
        />

        <div class="mb-4">
          <label for="course-type" class="text-[20px] font-bold mb-[10px]"
            >課程類型</label
          >
          <select
            v-model="courseType"
            id="course-type"
            class="bg-white shadow-2xs shadow-gray-500 text-[16px] w-full border-1 border-solid border-[#ddd] rounded-[8px] p-2"
          >
            <option disabled value="" selected>請選擇類型</option>
            <option v-for="type in courseTypes" :key="type" :value="type">
              {{ type }}
            </option>
          </select>
        </div>

        <Input
          id="course-intro"
          v-model="courseIntro"
          label="課程簡介"
          placeholder="請輸入課程簡介"
        />

        <div class="mb-4">
          <label for="course-outline" class="text-[20px] font-bold mb-[10px]"
            >教學大綱</label
          >
          <textarea
            v-model="courseOutline"
            id="course-outline"
            class="bg-white shadow-2xs shadow-gray-500 text-[16px] w-full border-1 border-solid border-[#ddd] rounded-[8px] p-2"
            placeholder="請描述課程內容與學習目標"
            rows="5"
          ></textarea>
        </div>

        <FileUpload
          label="課程封面圖片(可選)"
          accept="image/*"
          @file-selected="handleFileSelected"
        />

        <Input
          id="course-price"
          v-model="coursePrice"
          type="number"
          label="課程價格 (新台幣 $TWD)"
          placeholder="請輸入課程價格"
        />

        <Button
          variant="primary"
          fullWidth
          @click="onSubmit"
          :disabled="!isFormValid"
        >
          提交審核
        </Button>
      </div>
    </div>
  </DefaultLayout>
</template>

<script setup>
import axios from "axios";
import swal from "sweetalert";
import { computed, onMounted, ref } from "vue";
import Button from "../components/common/Button.vue";
import FileUpload from "../components/common/FileUpload.vue";
import Input from "../components/common/Input.vue";
import PageTitle from "../components/common/PageTitle.vue";
import DefaultLayout from "../Layout/default.vue";
import { useAuthStore } from "../stores/auth";
import { courseTypes } from "../stores/courseType";
import { useUserStore } from "../stores/user";

const userStore = useUserStore();
const authStore = useAuthStore();

const courseName = ref("");
const courseType = ref("");
const courseIntro = ref("");
const courseOutline = ref("");
const courseImage = ref(null);
const coursePrice = ref(null);

const isFormValid = computed(() => {
  return (
    courseName.value &&
    courseType.value &&
    courseIntro.value &&
    courseOutline.value &&
    coursePrice.value !== null &&
    coursePrice.value >= 0
  );
});

const handleFileSelected = (file) => {
  courseImage.value = file;
};

const resetForm = () => {
  courseName.value = "";
  courseType.value = "";
  courseIntro.value = "";
  courseOutline.value = "";
  courseImage.value = null;
  coursePrice.value = null;
};

const submitCourse = async () => {
  const teacherId = userStore.currentUserInfo.user_id;

  const payload = {
    course_name: courseName.value,
    course_type: courseType.value,
    course_intro: courseIntro.value,
    course_outline: courseOutline.value,
    course_image: "",
    course_price: Number(coursePrice.value),
    course_content: [],
    teacher_id: teacherId,
    students: [],
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
    swal("課程提交失敗！", "請稍後再試。", "error");
    console.error("儲存失敗:", error);
  }
};

const onSubmit = () => {
  if (!isFormValid.value) {
    swal("請填寫所有必要欄位！", "", "warning");
    return;
  }
  submitCourse();
};

onMounted(() => {
  userStore.fetchUser();
});
</script>
