import { createWebHistory, createRouter } from "vue-router";

import Home from "../views/Home.vue";
import Class from "../views/Class.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", name: "Home", component: Home },
    { path: "/Class", name: "Class", component: Class },
  ],
});

export default router;
