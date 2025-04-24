import { createWebHistory, createRouter } from "vue-router";

import Home from "../views/Home.vue";
import SelectCourse from "../views/SelectCourse.vue";
import CreateCourse from "../views/CreateCourse.vue";
import MyCourse from "../views/MyCourse.vue";
import Class from "../views/Class.vue";
import Teacher from "../views/Teacher.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", name: "Home", component: Home },
    { path: "/CreateCourse", name: "CreateCourse", component: CreateCourse },
    { path: "/SelectCourse", name: "SelectCourse", component: SelectCourse },
    { path: "/MyCourse", name: "MyCourse", component: MyCourse },
    { path: "/Class", name: "Class", component: Class },
    { path: "/Teacher", name: "Teacher", component: Teacher },
  ],
});

export default router;
