import { createWebHistory, createRouter } from "vue-router";

import Home from "../views/Home.vue";
import SelectCourse from "../views/SelectCourse.vue";
import CreateCourse from "../views/CreateCourse.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", name: "Home", component: Home },
    { path: "/CreateCourse", name: "CreateCourse", component: CreateCourse },
    { path: "/SelectCourse", name: "SelectCourse", component: SelectCourse },
  ],
});

export default router;
