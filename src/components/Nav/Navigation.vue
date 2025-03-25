<template>
  <nav
    class="bg-gray-800 fixed w-[90%] top-0 z-10 mx-[5%] rounded-md transition-all"
  >
    <div class="container mx-auto flex justify-between items-center p-2">
      <!-- Logo -->
      <router-link
        to="/"
        class="text-white text-xl font-bold flex items-center"
      >
        <img
          src="../../assets/Logo.svg"
          alt="Logo"
          class="w-15 h-auto box-content self-center"
        />
        <span class="text-gray-200 ml-1 text-[24px]">整合式教學平台</span>
      </router-link>
      <!-- Menu -->
      <div class="hidden md:flex space-x-2">
        <router-link
          to="/CreateCourse"
          class="text-gray-300 text-[16px] hover:text-white hover:bg-gray-600 rounded-lg p-2"
          >我要開課</router-link
        >
        <router-link
          to="/SelectCourse"
          class="text-gray-300 text-[16px] hover:text-white hover:bg-gray-600 rounded-lg p-2"
          >我要選課</router-link
        >
        <router-link
          to="/MyCourse"
          class="text-gray-300 text-[16px] hover:text-white hover:bg-gray-600 rounded-lg p-2"
          >我的課程</router-link
        >
        <router-link
          class="text-gray-300 text-[16px] hover:text-white hover:bg-gray-600 rounded-lg p-2"
          >雲端開發平台</router-link
        >
        <router-link
          class="text-gray-300 text-[16px] hover:text-white hover:bg-gray-600 rounded-lg p-2"
          >登入</router-link
        >
      </div>
      <!-- Mobile Menu Button -->
      <div class="md:hidden">
        <button
          @click="toggleMenu"
          class="text-gray-300 hover:text-white focus:outline-none"
        >
          <svg
            class="w-6 h-6"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M4 6h16M4 12h16m-7 6h7"
            ></path>
          </svg>
        </button>
      </div>
    </div>
    <!-- Mobile Menu -->
    <transition name="slide-fade">
      <div v-if="isMenuOpen" class="md:hidden space-y-3 mb-3">
        <hr class="border-2 border-gray-500 rounded-full" />
        <router-link
          to="/CreateCourse"
          @click="toggleMenu"
          class="block text-gray-300 text-center hover:text-white hover:bg-gray-600 rounded-lg p-2"
          >我要開課</router-link
        >
        <router-link
          to="/SelectCourse"
          @click="toggleMenu"
          class="block text-gray-300 text-center hover:text-white hover:bg-gray-600 rounded-lg p-2"
          >我要選課</router-link
        >
        <router-link
          to="/MyCourse"
          @click="toggleMenu"
          class="block text-gray-300 text-center hover:text-white hover:bg-gray-600 rounded-lg p-2"
          >我的課程</router-link
        >
        <router-link
          @click="toggleMenu"
          class="block text-gray-300 text-center hover:text-white hover:bg-gray-600 rounded-lg p-2"
          >雲端開發平台</router-link
        >
        <router-link
          @click="toggleMenu"
          class="block text-gray-300 text-center hover:text-white hover:bg-gray-600 rounded-lg p-2"
          >登入</router-link
        >
      </div>
    </transition>
  </nav>
</template>

<script setup>
import { ref } from "vue";
const isMenuOpen = ref(false);
const toggleMenu = () => (isMenuOpen.value = !isMenuOpen.value);
</script>

<style scoped>
/* menu 的淡化效果 */
.slide-fade-leave-active {
  transition: all 0.5s ease;
}
.slide-fade-leave-to {
  transform: translateY(-10px);
  opacity: 0;
}
</style>
