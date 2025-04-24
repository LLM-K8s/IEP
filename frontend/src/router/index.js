import { createWebHistory, createRouter } from "vue-router";
import { useKeycloak } from "../plugins/keycloak";

import Home from "../views/Home.vue";
import SelectCourse from "../views/SelectCourse.vue";
import CreateCourse from "../views/CreateCourse.vue";
import MyCourse from "../views/MyCourse.vue";
import Class from "../views/Class.vue";
import Teacher from "../views/Teacher.vue";
import Profile from "../views/Profile.vue";

const routes =  [
    { path: "/", name: "Home", component: Home },
    { path: "/CreateCourse", name: "CreateCourse", component: CreateCourse },
    { path: "/SelectCourse", name: "SelectCourse", component: SelectCourse },
    { path: "/MyCourse", name: "MyCourse", component: MyCourse },
    { path: "/Class", name: "Class", component: Class },
    { path: "/Teacher", name: "Teacher", component: Teacher },
    { path: "/Profile", name: "Profile", component: Profile },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, _, next) => {
  const { isAuthenticated } = useKeycloak();
  if (to.meta.requiresAuth && !isAuthenticated.value) {
    const kc = useKeycloak().keycloak;
    kc.login();
  } else {
    next();
  }
});
export default router;
