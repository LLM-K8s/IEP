<template>
  <div class="MyCourse">
    <NavBar />
    <div class="w-[90%] mx-[5%]">
      <div class="pt-20 w-[100%]">
        <span class="text-[24px] mt-20 mb-[16px] font-bold h-fit">
          我的課程
        </span>
        <hr class="border-2 border-gray-500 rounded-2xl" />
      </div>
      <div
        class="grid gap-1 grid-cols-3 shadow-gray-500 rounded-[8px] w-[100%] self-center p-5"
      >
        <div
          class="border-1 border-[#ddd] border-solid rounded-[8px] shadow-md shadow-gray-500 overflow-hidden"
        >
          <div class="h-[150px] bg-[#eee]">
            <img alt="課程圖片" />
          </div>
          <div class="p-[15px] bg-white">
            <p class="text-[20px] font-bold">課程名稱</p>
            <div class="flex justify-between text-[#666] text-[16px] mt-2">
              <span>講師: </span>
              <span>上次進入: </span>
            </div>
            <p class="text-[#666] text-[16px] mt-2 mb-4">課程簡介</p>
            <router-link
              to="/Class"
              class="bg-[#3498db] hover:bg-[#2d83bc] text-white rounded-lg p-2"
              >進入課程</router-link
            >
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import NavBar from "../components/NavBar/NavBar.vue";
</script>

<style scoped>
.MyCourse {
  background-image: url("../assets/images/email-pattern.png");
  height: 100vh;
}
</style>
