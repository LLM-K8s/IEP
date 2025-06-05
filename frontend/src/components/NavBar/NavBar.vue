<template>
  <nav
    class="bg-gray-800/20 backdrop-blur-md fixed w-full md:w-[90%] top-0 z-10 md:mx-[5%] md:rounded-xl transition-all mt-4"
  >
    <div
      class="container mx-auto px-4 md:px-[64px] flex justify-between items-center py-2"
    >
      <!-- Logo -->
      <Logo :logoTextColor="menuTextColor" />

      <!-- Desktop Menu -->
      <div class="hidden md:flex space-x-2">
        <MenuLinks :isMobile="false" :menuLinkColor="menuTextColor" />
      </div>

      <!-- Mobile Menu Button -->
      <MobileToggleBtn @toggle="toggleMenu" />
    </div>

    <!-- Mobile Menu -->
    <transition name="slide-fade">
      <div v-if="isMenuOpen" class="md:hidden space-y-3 mb-3">
        <hr class="border-2 border-gray-500 rounded-full" />
        <MenuLinks :isMobile="true" @itemClick="toggleMenu" />
      </div>
    </transition>
  </nav>
</template>

<script setup>
import { ref, computed, watch } from "vue";
import { useRoute } from "vue-router";
import Logo from "./Logo.vue";
import MenuLinks from "./MenuLinks.vue";
import MobileToggleBtn from "./MobileToggleBtn.vue";

const route = useRoute();

const isMenuOpen = ref(false);
const isHeroSection = ref(false);
const menuTextColor = ref("text-gray-800");

const toggleMenu = () => (isMenuOpen.value = !isMenuOpen.value);

const onScroll = () => {
  const scrollTop = window.scrollY;
  isHeroSection.value = scrollTop < 600;
  console.log(isHeroSection);
  if (isHeroSection.value === true) {
    menuTextColor.value = "text-gray-200";
  } else {
    menuTextColor.value = "text-gray-800";
  }
};

const setupScrollListener = () => {
  window.addEventListener("scroll", onScroll);
  onScroll();
};

const removeScrollListener = () => {
  window.removeEventListener("scroll", onScroll);
};

watch(
  () => route.path,
  (newPath) => {
    console.log(route.path);
    if (newPath === "/") {
      // 在首頁，啟用滾動監聽
      console.log("root");
      setupScrollListener();
    } else {
      console.log("not root");
      // 非首頁，移除監聽並固定顏色
      removeScrollListener();
      menuTextColor.value = "text-gray-800";
    }
  },
  { immediate: true }
);
</script>

<style scoped>
.slide-fade-leave-active {
  transition: all 0.5s ease;
}
.slide-fade-leave-to {
  transform: translateY(-10px);
  opacity: 0;
}
</style>
