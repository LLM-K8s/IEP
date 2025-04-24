<template>
  <div
    class="border-1 border-[#ddd] border-solid rounded-[8px] shadow-md shadow-gray-500 overflow-hidden mt-[30px]"
  >
    <div class="h-[150px] bg-[#eee]">
      <img alt="課程圖片" />
    </div>
    <div class="p-[15px]">
      <p class="text-gray-800 text-[20px] font-bold">課程名稱</p>
      <div class="flex justify-between text-[#666] text-[16px] mt-2 mb-4">
        <span class="text-gray-800">講師: </span>
        <span class="text-gray-800">5.0 ⭐</span>
      </div>
      <a
        @click="showDetails = true"
        class="bg-[#3498db] hover:bg-[#2d83bc] text-white rounded-lg p-2"
        >查看詳情</a
      >
    </div>
    <div
      v-if="showDetails"
      class="fixed top-0 left-0 w-full h-full flex items-center justify-center bg-gray-800/50"
    >
      <div class="bg-white p-8 rounded-lg w-[90%] shadow-lg md:w-[50%]">
        <h2 class="text-[24px] font-bold mb-4">課程大綱</h2>
        <div
          class="overflow-y-auto max-h-[300px] text-[16px] text-[#666] border border-[#ddd] rounded-lg p-4"
        >
          <p>課程大綱內容</p>
        </div>
        <button
          @click="showDetails = false"
          class="mt-4 bg-[#e74c3c] hover:bg-[#c0392b] text-white rounded-lg p-2"
        >
          關閉
        </button>
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref } from "vue";

const showDetails = ref(false);
</script>
<style scoped></style>
