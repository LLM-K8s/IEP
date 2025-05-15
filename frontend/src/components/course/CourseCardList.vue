<template>
  <div class="grid gap-4 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 mt-5">
    <CourseCard
      v-for="course in courses"
      :key="course.course_id"
      :course="course"
      @show-details="showCourseDetails"
    />
    <Dialog
      :visible="showDetails"
      modal
      header="課程大綱"
      :style="{ width: '90vw', maxWidth: '600px' }"
      :closable="false"
    >
      <div
        class="overflow-y-auto max-h-[300px] text-gray-600 border border-gray-200 rounded-lg p-4"
      >
        <p>
          {{ selectedCourseDetails.course_outline }}
        </p>
      </div>
      <div class="flex justify-end gap-2 mt-4">
        <Button
          type="button"
          label="關閉"
          severity="secondary"
          @click="showDetails = false"
        ></Button>
        <Button
          v-if="selectMode"
          type="button"
          label="選擇此課程"
          @click="
            $emit('select-course', selectedCourseDetails.course_id),
              (showDetails = false)
          "
        ></Button>
      </div>
    </Dialog>
  </div>
</template>

<script setup>
import { ref } from "vue";
import CourseCard from "./CourseCard.vue";
import Button from "primevue/button";

const props = defineProps({
  courses: {
    type: Array,
    default: () => [],
  },
  selectMode: {
    type: Boolean,
    default: false,
  },
});

defineEmits(["select-course"]);

const showDetails = ref(false);
const selectedCourseDetails = ref([]);

const showCourseDetails = (courseId) => {
  console.log(courseId);
  selectedCourseDetails.value = props.courses.find(
    (course) => course.course_id === courseId
  );
  showDetails.value = true;
};
</script>
