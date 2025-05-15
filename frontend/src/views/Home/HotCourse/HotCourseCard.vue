<template>
  <Card class="course-card">
    <template #header>
      <div class="h-[200px] bg-gray-100 flex items-center justify-center">
        <img
          :src="course.image"
          :alt="course.title"
          class="w-full h-full object-cover"
        />
      </div>
    </template>
    <template #title>{{ course.title }}</template>
    <template #subtitle>
      <div class="flex justify-between items-center text-gray-600">
        <span>講師: {{ course.instructor }}</span>
        <Rating :model-value="course.rating" readonly />
      </div>
    </template>
    <template #content>
      <p class="text-gray-600 mb-4">{{ course.description }}</p>
    </template>
    <template #footer>
      <Button
        label="查看詳情"
        class="w-full"
        @click="$emit('show-details', course.id)"
      />
    </template>
  </Card>
</template>

<script setup>
import Button from "primevue/button";
import Card from "primevue/card";
import Rating from "primevue/rating";

defineProps({
  course: {
    type: Object,
    required: true,
    default: () => ({
      id: 1,
      title: "",
      instructor: "",
      rating: 0,
      description: "",
      image: "",
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
}

:deep(.p-card-footer) {
  padding: 1.5rem;
  padding-top: 0;
}
</style>
