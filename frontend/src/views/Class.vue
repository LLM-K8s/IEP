<template>
  <div class="Class">
    <NavBar />
    <div class="w-[90%] mx-[5%] pb-4">
      <div class="pt-20 w-[100%]">
        <router-link
          to="/MyCourse"
          class="bg-[#3498db] hover:bg-[#2d83bc] text-white text-[24px] px-6 rounded-lg h-fit"
          >返回</router-link
        >
        <span class="text-[24px] mt-20 mb-[16px] font-bold h-fit">
          課程內容
        </span>
        <hr class="border-2 border-gray-500 rounded-2xl mb-6" />
      </div>
      <div
        v-for="(week, index) in assignments"
        :key="week.dateRange"
        class="mb-8 bg-white rounded-2xl shadow p-4"
      >
        <h2
          class="text-xl font-bold text-purple-800 border-b-4 border-gray-200 pb-2 mb-4"
        >
          {{ week.dateRange }}
        </h2>
        <ul>
          <li
            v-for="item in week.items"
            :key="item.name"
            class="flex items-center space-x-2 py-1"
          >
            <span class="text-xl">{{ getIcon(item.type) }}</span>
            <span class="text-blue-700 hover:underline cursor-pointer">
              {{ item.name }}
            </span>
          </li>
        </ul>
        <!--展開按鈕-->
        <button
          @click="toggleSubmission(index)"
          class="mt-4 text-sm bg-[#3498db] text-white w-[100%] px-3 py-1 rounded hover:bg-[#2d83bc] transition"
        >
          {{ showSubmission[index] ? "收合作業繳交區 🔼" : "作業繳交區 🔽" }}
        </button>
        <!-- 繳交區塊 -->
        <div
          v-if="showSubmission[index]"
          class="mt-4 p-4 bg-gray-100 rounded-xl border border-purple-200"
        >
          <p class="mb-2 text-gray-700">請上傳你的作業：</p>
          <input
            type="file"
            class="block w-full text-sm text-gray-600 file:mr-4 file:py-1 file:px-4 file:border-0 file:bg-[#3498db] file:text-white file:rounded-md hover:file:bg-[#2d83bc]"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import NavBar from "../components/NavBar/NavBar.vue";
const assignments = [
  {
    dateRange: "02月24日 - 03月2日",
    items: [
      { name: "PPT文件1", type: "ppt" },
      { name: "PPT文件2", type: "ppt" },
    ],
  },
  {
    dateRange: "03月3日 - 03月9日",
    items: [
      { name: "PPT文件3", type: "ppt" },
      { name: "PPT文件4", type: "ppt" },
      { name: "Excel1", type: "excel" },
      { name: "Word1", type: "doc" },
    ],
  },
  {
    dateRange: "03月10日 - 03月16日",
    items: [
      { name: "Word2", type: "doc" },
      { name: "PPT文件5", type: "ppt" },
    ],
  },
];

// 狀態：每週是否顯示作業繳交區塊
const showSubmission = ref(assignments.map(() => false));

const toggleSubmission = (index) => {
  showSubmission.value[index] = !showSubmission.value[index];
};

const getIcon = (type) => {
  switch (type) {
    case "ppt":
      return "📊";
    case "excel":
      return "📈";
    case "doc":
      return "📄";
    default:
      return "📁";
  }
};
</script>

<style scoped>
.Class {
  background-image: url("../assets/images/email-pattern.png");
  min-height: 100vh;
}
</style>
