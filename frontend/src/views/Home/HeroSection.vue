<template>
  <section
    ref="heroRef"
    class="h-screen bg-[url('@/assets/images/teamwork.jpg')] bg-cover bg-center bg-black/30 transition-opacity duration-100 ease-out"
  >
    <div
      class="container mx-auto h-full flex flex-col items-center justify-center text-center"
    >
      <div class="bg-white/60 rounded-2xl p-6 m-4 shadow-xl backdrop-blur-sm">
        <h1 class="text-gray-800 text-4xl font-extrabold mb-4">
          整合式教學平台
        </h1>
        <p class="text-gray-800 text-base font-medium leading-relaxed">
          探索豐富的課程，隨時隨地學習新知識，提升自己的能力。我們提供最優質的線上教學體驗，讓學習更有效率、更有樂趣。
        </p>
        <div class="flex justify-center gap-6 mt-6">
          <Button
          label="平台特色"
          raised
          @click="scrollToFeatures"
          />
          <Button
          label="熱門課程"
          raised
          @click="scrollToHotCourse"
          />
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import Button from "primevue/button";
import { onBeforeUnmount, onMounted, ref } from "vue";

const heroRef = ref(null);

const scrollToFeatures = () => {
  const featuresSection = document.getElementById("features");
  if (featuresSection) {
    featuresSection.scrollIntoView({ behavior: "smooth" });
  }
};

const handleScroll = () => {
  if (!heroRef.value) return;
  const scrollTop = window.scrollY;
  const height = window.innerHeight;
  heroRef.value.style.opacity = `${1 - scrollTop / height}`;
};

const scrollToHotCourse = () => {
  const hotCourseSection = document.getElementById("hotcourse");
  if (hotCourseSection) {
    hotCourseSection.scrollIntoView({ behavior: "smooth" });
  }
};

onMounted(() => {
  window.addEventListener("scroll", handleScroll);
});
onBeforeUnmount(() => {
  window.removeEventListener("scroll", handleScroll);
});
</script>
