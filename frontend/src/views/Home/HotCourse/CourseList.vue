<template>
  <div class="max-w-7xl mx-auto">
    <p class="text-gray-800 text-[24px] text-center mt-[120px] font-bold">
      熱門課程
    </p>
    <hr class="my-4 border-2 border-gray-500 rounded-2xl" />
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
      <CourseCard
        v-for="course in courses"
        :key="course.id"
        :course="course"
        @show-details="showCourseDetails"
      />
    </div>

    <Dialog
      v-model:visible="showDetails"
      modal
      header="課程大綱"
      :style="{ width: '90vw', maxWidth: '600px' }"
    >
      <div class="overflow-y-auto max-h-[300px] text-gray-600 border border-gray-200 rounded-lg p-4">
        <p>{{ selectedCourseDetails }}</p>
      </div>
    </Dialog>
  </div>
</template>

<script setup>
import Dialog from "primevue/dialog";
import { ref } from "vue";
import CourseCard from "./CourseCard.vue";

const showDetails = ref(false);
const selectedCourseDetails = ref("");

const courses = [
  {
    id: 1,
    title: "Python 基礎入門",
    instructor: "王小明",
    rating: 5.0,
    description: "從零開始學習 Python 程式設計，掌握基礎語法和實用技巧",
    image: "https://placehold.co/600x400/e2e8f0/1e293b?text=Python Course",
  },
  {
    id: 2,
    title: "Web 開發全端實戰",
    instructor: "李小華",
    rating: 4.9,
    description: "學習現代網頁開發技術，包含前端框架和後端 API 開發",
    image: "https://placehold.co/600x400/e2e8f0/1e293b?text=Web Development",
  },
  {
    id: 3,
    title: "資料結構與演算法",
    instructor: "張大偉",
    rating: 4.8,
    description: "深入理解資料結構與演算法，提升程式設計能力",
    image: "https://placehold.co/600x400/e2e8f0/1e293b?text=Algorithm",
  },
];

const courseDetails = {
  1: "課程大綱：\n1. Python 環境設置\n2. 基本語法介紹\n3. 資料型態與變數\n4. 控制流程\n5. 函式與模組\n6. 物件導向程式設計\n7. 檔案處理\n8. 實務專案練習",
  2: "課程大綱：\n1. HTML5 與 CSS3 基礎\n2. JavaScript 進階\n3. React 框架入門\n4. Node.js 後端開發\n5. RESTful API 設計\n6. 資料庫整合\n7. 部署與優化\n8. 全端專案實作",
  3: "課程大綱：\n1. 基礎資料結構\n2. 進階資料結構\n3. 排序演算法\n4. 搜尋演算法\n5. 圖論基礎\n6. 動態規劃\n7. 貪婪演算法\n8. 演算法優化技巧",
};

const showCourseDetails = (courseId) => {
  selectedCourseDetails.value = courseDetails[courseId];
  showDetails.value = true;
};
</script>

<style scoped>
:deep(.p-dialog) {
  border-radius: 1rem;
}

:deep(.p-dialog-header) {
  border-top-left-radius: 1rem;
  border-top-right-radius: 1rem;
  background-color: #f8fafc;
}

:deep(.p-dialog-content) {
  padding: 1.5rem;
}

:deep(.p-dialog-footer) {
  border-bottom-left-radius: 1rem;
  border-bottom-right-radius: 1rem;
  background-color: #f8fafc;
  padding: 1rem 1.5rem;
}
</style>
