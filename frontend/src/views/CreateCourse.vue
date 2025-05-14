<template>
  <DefaultLayout>
    <div class="w-[90%] mx-[5%]">
      <PageTitle title="建立新課程 📚" />
      <div class="shadow-gray-500 rounded-[8px] w-[100%] self-center p-5">
        <div class="mb-6">
          <label for="course-type" class="text-[20px] font-bold mb-[10px] block"
            >課程名稱</label
          >
          <InputText
            id="course-name"
            v-model="courseName"
            placeholder="請輸入課程名稱"
            class="w-full"
          />
        </div>

        <div class="mb-6">
          <label for="course-type" class="text-[20px] font-bold mb-[10px] block"
            >課程類型</label
          >
          <AutoComplete
            v-model="courseType"
            :suggestions="filteredTypes"
            @complete="searchTypes"
            placeholder="請選擇或搜尋課程類型"
            class="w-full"
            :dropdown="true"
            forceSelection
          />
        </div>

        <div class="mb-6">
          <label for="course-type" class="text-[20px] font-bold mb-[10px] block"
            >課程簡介</label
          >
          <InputText
            id="course-intro"
            v-model="courseIntro"
            placeholder="請輸入課程簡介"
            class="w-full"
          />
        </div>

        <div class="mb-6">
          <label for="course-outline" class="text-[20px] font-bold mb-[10px] block"
            >教學大綱</label
          >
          <Editor
            v-model="courseOutline"
            id="course-outline"
            editorStyle="height: 200px"
            class="w-full"
          />
        </div>

        <div class="mb-6">
          <label for="course-type" class="text-[20px] font-bold mb-[10px] block"
            >課程封面圖片(可選)</label
          >
          <FileUpload
            accept="image/*"
            @file-selected="handleFileSelected"
          />
        </div>

        <div class="mb-6">
          <label for="course-type" class="text-[20px] font-bold mb-[10px] block"
            >課程價格 (新台幣 $TWD)</label
          >
          <InputText
            id="course-price"
            v-model="coursePrice"
            type="number"
            placeholder="請輸入課程價格"
            class="w-full"
          />
        </div>

        <Button
          label="提交審核"
          class="w-[100%] mt-4"
          @click="onSubmit"
          :disabled="!isFormValid"
        />
      </div>
    </div>
  </DefaultLayout>
</template>

<script setup>
import axios from "axios";
import swal from "sweetalert";
import { computed, onMounted, ref } from "vue";
import FileUpload from "../components/common/FileUpload.vue";
import PageTitle from "../components/common/PageTitle.vue";
import DefaultLayout from "../Layout/default.vue";
import Button from "primevue/button";
import InputText from "primevue/inputtext";
import AutoComplete from 'primevue/autocomplete';
import Editor from "primevue/editor";
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
const coursePrice = ref(0);
const filteredTypes = ref([]);

const convertHtmlToText = (html) => {
  const tempDiv = document.createElement('div');
  tempDiv.innerHTML = html;
  return tempDiv.textContent || tempDiv.innerText || '';
};

const searchTypes = (event) => {
  const query = event.query.toLowerCase();
  filteredTypes.value = courseTypes.filter(type =>
    type.toLowerCase().includes(query)
  );
};

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
  coursePrice.value = 0;
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
