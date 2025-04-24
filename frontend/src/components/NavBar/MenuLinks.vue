<script setup>
const props = defineProps({
  isMobile: Boolean,
});

const emit = defineEmits(["itemClick"]);

const links = [
  { name: "成為老師", to: "/Teacher" },
  { name: "我要開課", to: "/CreateCourse" },
  { name: "我要選課", to: "/SelectCourse" },
  { name: "我的課程", to: "/MyCourse" },
  { name: "雲端開發平台" },
  { name: "登入" },
];
</script>

<template>
  <div :class="isMobile ? 'space-y-3' : 'flex space-x-2'">
    <router-link
      v-for="(link, index) in links"
      :key="index"
      :to="link.to || '#'"
      :class="[
        'text-gray-300 hover:text-white hover:bg-gray-600 rounded-lg p-2',
        isMobile ? 'block text-center' : 'text-[16px]',
      ]"
      @click="isMobile ? emit('itemClick') : null"
    >
      {{ link.name }}
    </router-link>
  </div>
</template>
