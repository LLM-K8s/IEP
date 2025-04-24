<script setup>
import { useKeycloak } from "../../plugins/keycloak";
import { useRouter } from "vue-router";
import { computed } from "vue";

const router = useRouter();
const { isAuthenticated, username, keycloak } = useKeycloak();

function login() {
  keycloak.login();
}

function logout() {
  keycloak.logout();
}

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
    { name: "雲端開發平台" },
  ];

  if (isAuthenticated.value) {
    return [
      ...baseLinks,
      { name: username.value, to: "/profile" },
      { name: "登出", action: logout }
    ];
  } else {
    return [
      ...baseLinks,
      { name: "登入", action: login }
    ];
  }
});
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
