<template>
  <nav class="bg-gray-800 fixed w-[90%] top-0 z-10 mx-[5%] rounded-md transition-all">
    <div class="container mx-auto flex justify-between items-center p-2">
      <!-- Logo -->
      <Logo />

      <!-- Desktop Menu -->
      <div class="hidden md:flex space-x-2">
        <MenuLinks :isMobile="false" />
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
import { ref } from 'vue';
import Logo from './Logo.vue';
import MenuLinks from './MenuLinks.vue';
import MobileToggleBtn from './MobileToggleBtn.vue';

const isMenuOpen = ref(false);
const toggleMenu = () => (isMenuOpen.value = !isMenuOpen.value);
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