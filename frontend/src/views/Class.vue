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
      <button
        @click="toggleNewChapter"
        :class="[
          'bg-[#3498db] hover:bg-[#2d83bc] text-white text-[20px] px-6 rounded-lg',
          showNewChapter ? 'mb-0' : 'mb-5',
        ]"
      >
        {{ showNewChapter ? "新增課程章節 🔼" : "新增課程章節 🔽" }}
      </button>
      <div v-if="showNewChapter" class="mb-8 bg-white rounded-2xl shadow p-4">
        <div class="mb-2">
          <label class="block text-gray-600 mb-1">章節名稱：</label>
          <input
            v-model="newChapter"
            type="text"
            class="w-full border rounded px-2 py-1"
            placeholder="輸入章節名稱"
          />
        </div>
        <button
          @click="addNewChapter"
          class="mt-2 bg-[#3498db] hover:bg-[#2d83bc] text-white w-[100%] px-4 py-1 rounded-md"
        >
          新增章節
        </button>
      </div>
      <div
        v-for="(week, index) in assignments"
        :key="week.chapter"
        class="mb-8 bg-white rounded-2xl shadow p-4"
      >
        <h2
          class="text-xl font-bold text-purple-800 border-b-4 border-gray-200 pb-2 mb-4"
        >
          {{ week.chapter }}
          <button
            @click="removeChapter(index)"
            class="text-sm text-red-500 hover:underline ml-4"
          >
            刪除章節 🗑️
          </button>
        </h2>
        <ul>
          <li
            v-for="(item, itemIndex) in week.items"
            :key="item.name"
            class="flex items-center space-x-2 py-1"
          >
            <span class="text-xl">{{ getIcon(item.type) }}</span>
            <span class="text-blue-700 hover:underline cursor-pointer">
              {{ item.name }}
            </span>
            <button
              @click="removeItem(index, itemIndex)"
              class="text-sm text-red-500 hover:underline ml-auto"
            >
              刪除🗑️
            </button>
          </li>
        </ul>

        <!--新增檔案內容-->
        <button
          @click="toggleFileEditor(index)"
          class="mt-4 text-sm bg-green-500 text-white w-full px-3 py-1 rounded hover:bg-green-600 transition"
        >
          {{ showFileEditor[index] ? "新增課程內容 ➖" : "新增課程內容 ➕" }}
        </button>
        <div
          v-if="showFileEditor[index]"
          class="mt-4 p-4 bg-gray-100 border border-green-300 rounded-xl"
        >
          <div class="mb-2">
            <label class="block text-gray-600 mb-1">檔案名稱：</label>
            <input
              v-model="newContent[index].name"
              type="text"
              class="w-full border rounded px-2 py-1"
              placeholder="教學報告"
            />
          </div>
          <div class="mb-2">
            <label class="block text-gray-600 mb-1">類型：</label>
            <select
              v-model="newContent[index].type"
              class="w-full border rounded px-2 py-1"
            >
              <option value="ppt">PPT</option>
              <option value="excel">Excel</option>
              <option value="doc">Word</option>
              <option value="vedio">Vedio</option>
            </select>
          </div>
          <button
            @click="addContent(index)"
            class="mt-2 bg-[#3498db] hover:bg-[#2d83bc] text-white px-4 py-1 rounded"
          >
            儲存內容
          </button>
        </div>

        <!--展開按鈕-->
        <button
          @click="toggleFileSubmission(index)"
          class="mt-4 text-sm bg-[#3498db] text-white w-[100%] px-3 py-1 rounded hover:bg-[#2d83bc] transition"
        >
          {{ showFileSubmission[index] ? "作業繳交區 🔼" : "作業繳交區 🔽" }}
        </button>

        <!-- 繳交檔案區塊 -->
        <div
          v-if="showFileSubmission[index]"
          class="mt-4 p-4 bg-gray-100 rounded-xl border border-blue-300"
        >
          <p class="mb-2 text-gray-700">請上傳你的作業：</p>
          <input
            type="file"
            class="block w-full text-sm text-gray-600 file:mr-4 file:py-1 file:px-4 file:border-0 file:bg-[#3498db] file:text-white file:rounded-md hover:file:bg-[#2d83bc]"
          />
          <button
            class="mt-2 bg-[#3498db] hover:bg-[#2d83bc] text-white px-4 py-1 rounded-md"
          >
            上傳作業
          </button>
        </div>
        <button
          @click="toggleReviewPanel(index)"
          class="mt-4 text-sm bg-[#3498db] text-white w-[100%] px-3 py-1 rounded hover:bg-[#2d83bc] transition"
        >
          查看檔案與評分
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import NavBar from "../components/NavBar/NavBar.vue";

// 課程資料
const assignments = ref([
  {
    chapter: "02月24日 - 03月2日",
    items: [
      { name: "PPT文件1", type: "ppt" },
      { name: "PPT文件2", type: "ppt" },
    ],
  },
  {
    chapter: "03月3日 - 03月9日",
    items: [
      { name: "PPT文件3", type: "ppt" },
      { name: "PPT文件4", type: "ppt" },
      { name: "Excel1", type: "excel" },
      { name: "Word1", type: "doc" },
    ],
  },
  {
    chapter: "03月10日 - 03月16日",
    items: [
      { name: "Word2", type: "doc" },
      { name: "PPT文件5", type: "ppt" },
    ],
  },
]);

// 展開狀態
const showFileSubmission = ref(assignments.value.map(() => false));
const showFileEditor = ref(assignments.value.map(() => false));
const showNewChapter = ref(false);
const newContent = ref(
  assignments.value.map(() => ({ name: "", type: "ppt" }))
);
const newChapter = ref("");

// 展開控制
const toggleFileSubmission = (index) => {
  showFileSubmission.value[index] = !showFileSubmission.value[index];
};

const toggleFileEditor = (index) => {
  showFileEditor.value[index] = !showFileEditor.value[index];
};

const toggleNewChapter = () => {
  showNewChapter.value = !showNewChapter.value;
};

// 新增內容
const addContent = (index) => {
  const content = newContent.value[index];
  if (!content.name || !content.type) {
    alert("請完整填寫內容！");
    return;
  }
  assignments.value[index].items.push({ ...content });
  newContent.value[index] = { name: "", type: "ppt" };
  showFileEditor.value[index] = false;
};

// 刪除檔案
const removeItem = (weekIndex, itemIndex) => {
  assignments.value[weekIndex].items.splice(itemIndex, 1);
};

//刪除週次
const removeChapter = (index) => {
  if (confirm("確定要刪除這章節的所有課程內容嗎？")) {
    assignments.value.splice(index, 1);
    showFileSubmission.value.splice(index, 1);
    showFileEditor.value.splice(index, 1);
    newContent.value.splice(index, 1);
  }
};

const addNewChapter = () => {
  if (!newChapter.value) {
    alert("章節名稱不能為空！");
    return;
  }
  assignments.value.push({
    chapter: newChapter.value, // Add the new chapter name here
    items: [], // No items initially
  });
  showFileSubmission.value.push(false);
  showFileEditor.value.push(false);
  newContent.value.push({ name: "", type: "ppt" }); // icon 顯示
  newChapter.value = ""; // Clear the input
};

// icon 顯示
const getIcon = (type) => {
  switch (type) {
    case "ppt":
      return "📊";
    case "excel":
      return "📈";
    case "doc":
      return "📄";
    case "vedio":
      return "🎦";
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
