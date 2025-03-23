<template>
  <section class="hero-section h-screen bg-cover bg-center bg-blend-overlay">
    <div
      class="container mx-auto h-full flex flex-col items-center justify-center text-center"
    >
      <div class="bg-neutral-100/60 rounded-2xl p-4 m-4">
        <h1 class="text-black text-4xl font-bold mb-4">整合式教學平台</h1>
        <p class="text-black text-[16px]">
          探索豐富的課程，隨時隨地學習新知識，提升自己的能力。我們提供最優質的線上教學體驗，讓學習更有效率、更有樂趣。
        </p>
      </div>
      <a
        href="#features"
        class="bg-gray-800 text-gray-300 text-[16px] hover:text-white hover:bg-gray-600 rounded-lg p-2"
        >平台特色</a
      >
      <a
        href="#hotcourse"
        class="bg-gray-800 text-gray-300 text-[16px] hover:text-white hover:bg-gray-600 rounded-lg p-2"
        >熱門課程</a
      >
    </div>
  </section>
</template>
<script setup>
import { onMounted, onBeforeUnmount } from "vue";
const handleScroll = () => {
  const hero = document.querySelector(".hero-section");
  const scrollTop = window.scrollY;
  const height = window.innerHeight;
  hero.style.opacity = 1 - scrollTop / height;
};
onMounted(() => {
  window.addEventListener("scroll", handleScroll);
});
onBeforeUnmount(() => {
  window.removeEventListener("scroll", handleScroll);
});
</script>
<style scoped>
.hero-section {
  background-image: url("../assets/images/teamwork.jpg");
  background-color: rgba(0, 0, 0, 0.3);
  transition: opacity 0.1 ease-out;
}
</style>
