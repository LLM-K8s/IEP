<template>
  <Card class="course-card">
    <template #header>
      <div class="h-[200px] bg-gray-100 flex items-center justify-center">
        <img
          :src="
            course.course_image?.length ? course.course_image : defaultImage
          "
          :alt="course.course_name"
          class="w-full h-full object-cover"
        />
      </div>
    </template>
    <template #title>
      <p>{{ course.course_name }}</p>
      <p class="text-sm text-gray-500">課程類型: {{ course.course_type }}</p>
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
        <Rating :model-value="course.rating" readonly />
      </div>
    </template>
    <template #content>
      <p class="text-gray-600">
        {{ course.course_intro }}
      </p>
    </template>
    <template #footer>
      <Button
        :label="'查看詳情'"
        class="w-full"
        @click="$emit('show-details', course.course_id)"
      />
      <span class="float-right">NT$ {{ course.course_price }}</span>
    </template>
  </Card>
</template>

<script setup>
import { useUserStore } from "@/stores/user";
import Button from "primevue/button";
import Card from "primevue/card";
import Rating from "primevue/rating";
import defaultImage from "../../../assets/images/default-course.jpg";

const userStore = useUserStore();

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
      course_image: "",
      teacher_id: "",
      students: "",
      rating: 0,
    }),
  },
});

defineEmits(["show-details"]);
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
  border-width: 2px;
  border-radius: 10px;
  border-color: gray;
}

:deep(.p-card-footer) {
  padding: 1.5rem;
  padding-top: 0;
}
</style>
