<template>
  <DefaultLayout>
    <div class="w-[90%] mx-[5%]">
      <div class="pt-20 w-[100%]">
        <span class="text-[24px] mt-20 mb-[16px] font-bold h-fit">
          課程列表
        </span>
        <hr class="border-2 border-gray-500 rounded-2xl" />
      </div>
      <div class="shadow-gray-500 rounded-[8px] w-[100%] self-center p-5">
        <input
          v-model="searchQuery"
          id="search-course-name"
          type="text"
          class="bg-white shadow-2xs shadow-gray-500 text-[16px] w-full border-1 border-solid border-[#ddd] rounded-[8px] p-2 mb-4"
          placeholder="搜尋課程..."
        />
        <select
          v-model="selectedType"
          id="course-type"
          class="bg-white shadow-2xs shadow-gray-500 text-[16px] w-full border-1 border-solid border-[#ddd] rounded-[8px] p-2"
        >
          <option value="">所有類型</option>
          <option v-for="type in courseTypes" :key="type" :value="type">
            {{ type }}
          </option>
        </select>
      </div>
      <div
        class="grid gap-4 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 mx-[16px] pb-6"
      >
        <div
          v-for="course in filteredCourses"
          :key="course.course_id"
          class="border-1 border-[#ddd] border-solid rounded-[8px] shadow-md shadow-gray-500 overflow-hidden"
        >
          <div class="h-[150px] bg-[#eee]">
            <img :src="course.course_image || defaultImage" alt="課程圖片" />
          </div>
          <div class="p-[15px] bg-white">
            <p class="text-[20px] font-bold">{{ course.course_name }}</p>
            <div class="flex justify-between text-[#666] text-[16px] mt-2">
              <span>講師: </span>
              <span>5.0 ⭐</span>
            </div>
            <p class="text-[#666] text-[16px] mt-2">
              課程簡介: {{ course.course_intro }}
            </p>
            <div class="flex justify-between text-[#666] text-[16px] mb-4">
              <span>NT$ {{ course.course_price }}</span>
              <span>課程時數</span>
            </div>
            <button
              @click="(showDetails = true), (checkCourse = course.course_id)"
              class="bg-[#3498db] hover:bg-[#2d83bc] text-white rounded-lg p-2"
            >
              查看詳情
            </button>
            <p class="text-[#666] text-[16px] mt-4">
              課程類型: {{ course.course_type }}
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- 浮動介面 -->
    <div
      v-if="showDetails"
      class="fixed top-0 left-0 w-full h-full flex items-center justify-center bg-gray-800/50"
    >
      <div class="bg-white p-8 rounded-lg w-[90%] shadow-lg md:w-[50%]">
        <h2 class="text-[24px] font-bold mb-4">課程大綱</h2>
        <div
          class="overflow-y-auto max-h-[300px] text-[16px] text-[#666] border border-[#ddd] rounded-lg p-4"
        >
          <p>
            {{
              courseStore.courses.find(
                (course) => course.course_id === checkCourse
              ).course_outline
            }}
          </p>
        </div>
        <button
          @click="showDetails = false"
          class="mt-4 bg-[#e74c3c] hover:bg-[#c0392b] text-white rounded-lg p-2"
        >
          關閉
        </button>
        <button
          class="mt-4 bg-[#3498db] hover:bg-[#2d83bc] text-white rounded-lg p-2 float-end"
        >
          選擇課程
        </button>
      </div>
    </div>
  </DefaultLayout>
</template>

<script setup>
import { computed, onMounted, ref } from "vue";
import DefaultLayout from "../Layout/default.vue";
import { useCourseStore } from "../stores/course";
import { courseTypes } from "../stores/courseType";

const showDetails = ref(false);
const courseStore = useCourseStore();
const searchQuery = ref("");
const selectedType = ref("");
const checkCourse = ref("");
const defaultImage = "../assets/images/default-course.png";

const filteredCourses = computed(() => {
  return courseStore.courses.filter((course) => {
    const matchesQuery = !searchQuery.value
      || course.course_name
        .toLowerCase()
        .includes(searchQuery.value.toLowerCase());
    const matchesType = !selectedType.value || course.course_type === selectedType.value;
    return matchesQuery && matchesType;
  });
});

onMounted(() => {
  courseStore.fetchCourses();
});
</script>

<style scoped>
.SelectCourse {
  background-image: url("../assets/images/email-pattern.png");
  min-height: 100vh;
}
</style>
