<template>
  <Card class="course-card">
    <template #header>
      <div class="h-[200px] bg-gray-100 flex items-center justify-center">
        <img
          :src="course.image"
          :alt="course.name"
          class="w-full h-full object-cover"
        />
      </div>
    </template>
    <template #title>
      <div class="flex justify-between items-center">
        <span>{{ course.course_name }}</span>
        <span class="text-sm text-gray-500"
          >課程類型: {{ course.course_type }}</span
        >
      </div>
    </template>
    <template #subtitle>
      <div class="flex justify-between items-center text-gray-600">
        <span>
          講師:
          {{
            userStore.allUsersInfo.find(
              (user) => user.user_id === course.teacher_id
            )?.user_name || "未知的講師"
          }}
        </span>
        <Rating v-if="selectMode" :model-value="course.rating" readonly />
      </div>
    </template>
    <template #content>
      <p class="text-gray-600 mb-4">{{ course.course_intro }}</p>
    </template>
    <template #footer>
      <Button
        v-if="selectMode"
        :label="
          course.students.includes(userStore.currentUserInfo.user_id)
            ? '已加入課程'
            : '查看詳情'
        "
        class="w-full"
        @click="$emit('show-details', course.course_id)"
        :disabled="course.students.includes(userStore.currentUserInfo.user_id)"
      />
      <div class="flex justify-between gap-4">
        <Button
          v-if="!selectMode"
          label="進入課程"
          @click="
            $emit('moved-class', course.course_id),
              $router.push({ name: 'Class' })
          "
          class="w-1/2"
        />
        <Button
          v-if="!selectMode"
          label="查看課程大綱"
          @click="$emit('show-details', course.course_id)"
          class="w-1/2"
        />
      </div>
      <span v-if="selectMode" class="float-right"
        >NT$ {{ course.course_price }}</span
      >
    </template>
  </Card>
</template>

<script setup>
import { useUserStore } from "@/stores/user";
import Button from "primevue/button";
import Card from "primevue/card";
import Rating from "primevue/rating";

const userStore = useUserStore();

const defaultImage = "../assets/images/default-course.png";

defineProps({
  course: {
    type: Object,
    required: true,
    default: () => ({
      course_id: "",
      course_name: "",
      course_type: "",
      course_intro: "",
      course_outline: "",
      course_price: 0,
      course_image: defaultImage,
      teacher_id: "",
      students: "",
      rating: 0,
    }),
  },
  selectMode: {
    type: Boolean,
    default: false,
  },
});

defineEmits(["show-details", "moved-class"]);
</script>

<style scoped>
.course-card {
  transition: transform 0.2s ease-in-out;
  height: 100%;
}

.course-card:hover {
  transform: translateY(-5px);
}

:deep(.p-card) {
  border-radius: 1rem;
  box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
}

:deep(.p-card-header) {
  background-color: #f8fafc;
  border-top-left-radius: 1rem;
  border-top-right-radius: 1rem;
  padding: 0;
}

:deep(.p-card-title) {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1e293b;
  margin-bottom: 0.5rem;
}

:deep(.p-card-subtitle) {
  margin-bottom: 1rem;
}

:deep(.p-card-content) {
  padding: 1.5rem;
}

:deep(.p-card-footer) {
  padding: 1.5rem;
  padding-top: 0;
}
</style>
