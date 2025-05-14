<template>
  <DefaultLayout>
    <div class="w-[90%] mx-[5%]">
      <div class="pt-20 w-[100%]">
        <span class="text-[24px] mt-20 mb-[16px] font-bold h-fit">
          申請老師資格 🏫
        </span>
        <hr class="border-2 border-gray-500 rounded-2xl" />
      </div>
      <div class="shadow-gray-500 rounded-[8px] w-[100%] self-center p-5">
        <label for="course-name" class="text-[20px] font-bold mb-[10px]"
          >姓名</label
        >
        <InputText
          id="teacher-name"
          type="text"
          class="bg-white shadow-2xs shadow-gray-500 text-[16px] w-full border-1 border-solid border-[#ddd] rounded-[8px] p-2 mb-4"
          placeholder="請輸入真實姓名"
        />
        <label for="course-name" class="text-[20px] font-bold mb-[10px]"
          >身分證號</label
        >
        <InputText
          id="teacher-id"
          type="password"
          class="bg-white shadow-2xs shadow-gray-500 text-[16px] w-full border-1 border-solid border-[#ddd] rounded-[8px] p-2 mb-4"
          placeholder="輸入身分證號"
          v-model="password"
        />
        <label for="course-name" class="text-[20px] font-bold mb-[10px]"
          >E-Mail</label
        >
        <InputText
          id="teacher-email"
          type="text"
          class="bg-white shadow-2xs shadow-gray-500 text-[16px] w-full border-1 border-solid border-[#ddd] rounded-[8px] p-2 mb-4"
          placeholder="請輸入電子信箱"
        />
        <label for="course-outline" class="text-[20px] font-bold mb-[10px]"
          >自我介紹</label
        >
        <Editor
          v-model="aboutMe"
          editorStyle="height: 200px"
          class="mb-4"
        />
        <label for="course-outline" class="text-[20px] font-bold mb-[10px]"
          >授課類型</label
        >
        <div
          class="bg-white shadow-2xs shadow-gray-500 text-[16px] w-full border-1 border-solid border-[#ddd] rounded-[8px] p-2 mb-4"
          @click="focusInput"
        >
          <!-- 已添加的標籤 -->
          <span
            v-for="(tag, index) in tags"
            :key="index"
            class="inline-flex items-center bg-blue-200 text-gray-800 text-sm rounded-full px-3 py-1 mr-2"
          >
            {{ tag }}
            <button @click.stop="removeTag(index)" class="ml-1">X</button>
          </span>

          <!-- 輸入框 -->
          <InputText
            ref="input"
            v-model="inputTagValue"
            @keydown.enter="addTag"
            @keydown.delete="handleBackspace"
            class="flex-grow px-2 py-1 outline-none w-full"
            placeholder="輸入類型標籤後按 Enter 新增"
          />
        </div>
        <Button
          label="提交申請審核"
          class= "w-[100%]"
        />
      </div>
    </div>
  </DefaultLayout>
</template>

<script setup>
import Button from "primevue/button";
import Editor from "primevue/editor";
import InputText from "primevue/inputtext";
import { ref } from "vue";
import DefaultLayout from "../Layout/default.vue";

const tags = ref([]);
const inputTagValue = ref("");
const inputTag = ref(null);
const aboutMe = ref("");

const addTag = () => {
  const tag = inputTagValue.value.trim();
  if (tag && !tags.value.includes(tag)) {
    tags.value.push(tag);
    inputTagValue.value = "";
  }
};

const removeTag = (index) => {
  tags.value.splice(index, 1);
};

const handleBackspace = () => {
  if (inputTagValue.value === "" && tags.value.length > 0) {
    tags.value.pop();
  }
};

const focusInput = () => {
  inputTag.value.focus();
};

const password = ref("");
</script>
