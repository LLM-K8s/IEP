<template>
  <div class="background-image">
    <NavBar />
    <slot />
  </div>
</template>

<script setup>
import NavBar from "../components/NavBar/NavBar.vue";

</script>

<style scoped>
.background-image {
  background-image: url("../assets/images/email-pattern.png");
  min-height: 100vh;
}
</style>