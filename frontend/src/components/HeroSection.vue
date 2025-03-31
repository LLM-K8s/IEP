<template>
  <section ref="heroRef" class="h-screen bg-[url('@/assets/images/teamwork.jpg')] bg-cover bg-center bg-black/30 transition-opacity duration-100 ease-out">
    <div class="container mx-auto h-full flex flex-col items-center justify-center text-center">
      <div class="bg-white/60 rounded-2xl p-6 m-4 shadow-xl backdrop-blur-sm">
        <h1 class="text-black text-4xl font-extrabold mb-4">整合式教學平台</h1>
        <p class="text-black text-base font-medium leading-relaxed">
          探索豐富的課程，隨時隨地學習新知識，提升自己的能力。我們提供最優質的線上教學體驗，讓學習更有效率、更有樂趣。
        </p>
        <div class="flex justify-center gap-6 mt-6">
          <a
            href="#features"
            class="bg-gray-800 text-gray-100 hover:bg-gray-600 hover:text-white rounded-lg px-4 py-2 transition"
          >
            平台特色
          </a>
          <a
            href="#hotcourse"
            class="bg-gray-800 text-gray-100 hover:bg-gray-600 hover:text-white rounded-lg px-4 py-2 transition"
          >
            熱門課程
          </a>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from "vue";

const heroRef = ref(null);

const handleScroll = () => {
  if (!heroRef.value) return;
  const scrollTop = window.scrollY;
  const height = window.innerHeight;
  heroRef.value.style.opacity = `${1 - scrollTop / height}`;
};

onMounted(() => {
  window.addEventListener("scroll", handleScroll);
});
onBeforeUnmount(() => {
  window.removeEventListener("scroll", handleScroll);
});
</script>