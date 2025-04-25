<script setup>
import { computed, ref } from "vue";
import { useAuthStore } from "../../stores/auth";

const authStore = useAuthStore()

const props = defineProps({
  isMobile: Boolean,
});

const emit = defineEmits(["itemClick"]);

const links = computed(() => {
  const baseLinks = [
    { name: "成為老師", to: "/Teacher" },
    { name: "我要開課", to: "/CreateCourse" },
    { name: "我要選課", to: "/SelectCourse" },
    { name: "我的課程", to: "/MyCourse" },
    { name: "雲端開發平台", to: "https://coder.yang-lin.dev/api/v2/users/oidc/callback" },
  ];
  return [
    ...baseLinks,
    authStore.isAuthenticated
      ? { name: "登出", action: authStore.logout }
      : { name: "登入", action: authStore.login }
  ];
  }
);
</script>

<template>
  <div :class="isMobile ? 'space-y-3' : 'flex space-x-2'">
    <a
      v-for="(link, index) in links"
      :key="index"
      :href="link.to || '#'"
      :class="[
        'text-gray-300 hover:text-white hover:bg-gray-600 rounded-lg p-2 cursor-pointer',
        isMobile ? 'block text-center' : 'text-[16px]',
      ]"
      @click="link.action ? link.action() : (isMobile ? emit('itemClick') : null)"
    >
      {{ link.name }}
    </a>
  </div>
</template>
