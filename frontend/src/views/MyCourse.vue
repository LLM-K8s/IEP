<template>
  <DefaultLayout>
    <div class="w-[90%] mx-[5%]">
      <div class="pt-20 w-[100%]">
        <span class="text-[24px] mt-20 mb-[16px] font-bold h-fit">
          我的課程
        </span>
        <hr class="border-2 border-gray-500 rounded-2xl" />
      </div>
      <div class="grid gap-4 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 mt-5">
        <div
          v-for="course in courseStore.myCourses"
          :key="course.course_id"
          class="border-1 border-[#ddd] border-solid rounded-[8px] shadow-md shadow-gray-500 overflow-hidden"
        >
          <div class="h-[150px] bg-[#eee]">
            <img alt="課程圖片" />
          </div>
          <div class="p-[15px] bg-white">
            <p class="text-[20px] font-bold">{{ course.course_name }}</p>
            <div class="flex justify-between text-[#666] text-[16px] mt-2">
              <span>
                講師:
                {{
                  userStore.allUsersInfo.find(
                    (user) => user.user_id === course.teacher_id
                  )?.user_name || "未知的講師"
                }}
              </span>
              <span>上次進入:</span>
            </div>
            <p class="text-[#666] text-[16px] mt-2 mb-4">
              課程簡介: {{ course.course_intro }}
            </p>
            <router-link
              to="/Class"
              class="bg-[#3498db] hover:bg-[#2d83bc] text-white rounded-lg p-2 inline-block"
              >進入課程</router-link
            >
            <button
              @click="(showOutline = true), (checkCourse = course.course_id)"
              class="bg-[#3498db] hover:bg-[#2d83bc] text-white rounded-lg p-2 ml-5"
            >
              查看課程大綱
            </button>
          </div>
        </div>
      </div>
    </div>
    <div
      v-if="showOutline"
      class="fixed top-0 left-0 w-full h-full flex items-center justify-center bg-gray-800/50"
    >
      <CourseOutline>
        <template v-slot:Outline>
          <textarea
            v-model="
              courseStore.courses.find(
                (course) => course.course_id === checkCourse
              ).course_outline
            "
            class="w-full h-[300px] border-3 border-[#5e5e5e] rounded-lg p-4"
            readonly
          ></textarea>
        </template>
        <template v-slot:Button>
          <div class="flex justify-center">
            <button
              @click="showOutline = false"
              class="mt-4 bg-[#e74c3c] hover:bg-[#c0392b] text-white rounded-lg p-2 w-full"
            >
              關閉
            </button>
          </div>
        </template>
      </CourseOutline>
    </div>
  </DefaultLayout>
</template>

<script setup>
import { onMounted, ref } from "vue";
import CourseOutline from "../components/CourseOutline.vue";
import DefaultLayout from "../Layout/default.vue";
import { useCourseStore } from "../stores/course";
import { useUserStore } from "../stores/user";

const courseStore = useCourseStore();
const userStore = useUserStore();

const showOutline = ref(false);
const checkCourse = ref("");

onMounted(async () => {
  await userStore.fetchUser();
  await courseStore.fetchCourses();
  const userId = userStore.currentUserInfo.user_id;
  courseStore.getMyCourses(userId);
});
</script>
