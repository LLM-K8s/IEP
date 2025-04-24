import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import router from "./router/index.js";
import { vueKeycloak } from "./plugins/keycloak";

const app = createApp(App);

app.use(router);
app.use(vueKeycloak, {
  config: {
    url: "http://172.16.1.16:8081/",
    realm: "coder",
    clientId: "vue",
  },
  initOptions: {
    onLoad: "check-sso", // 初次載入不強制登入
    checkLoginIframe: false,
    pkceMethod: 'S256',
    silentCheckSsoRedirectUri: window.location.origin + '/silent-check-sso.html',

  },
  onReady() {
    console.log("Keycloak ready");
  },
  onError(error) {
    console.error("Keycloak error:", error);
  }
});
app.mount("#app");
