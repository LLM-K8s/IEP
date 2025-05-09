import { createApp } from "vue";
import "./style.css";
import { createPinia } from "pinia";
import App from "./App.vue";
import router from "./router/index.js";
import { useAuthStore } from "./stores/auth";

const app = createApp(App);
const pinia = createPinia();

app.use(router);
app.use(pinia);

// 設置 token 刷新監聽器
const authStore = useAuthStore(pinia);
authStore.setupTokenRefreshListener();

app.mount("#app");
