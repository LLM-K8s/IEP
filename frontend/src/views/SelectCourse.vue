<template>
  <div class="SelectCourse">
    <NavBar />
    <div class="flex flex-col h-screen mx-[64px] pb-[64px]">
      <p class="text-[24px] mt-20 mb-[16px] font-bold w-[100%] h-fit">
        課程列表
      </p>
      <div
        class="bg-white shadow-gray-500 rounded-[8px] w-[100%] self-center p-5"
      >
        <input
          id="search-course-name"
          type="text"
          class="text-[16px] w-full border-1 border-solid border-[#ddd] rounded-[8px] p-2 mb-4"
          placeholder="搜尋課程..."
        />
        <select
          id="course-type"
          class="text-[16px] w-full border-1 border-solid border-[#ddd] rounded-[8px] p-2"
        >
          <option>所有類型</option>
          <option>程式設計</option>
        </select>
      </div>
      <div class="grid gap-1 grid-cols-3 mx-4 mt-[24px]">
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
              <span>5.0 ⭐</span>
            </div>
            <p class="text-[#666] text-[16px] mt-2">課程簡介</p>
            <div class="flex justify-between text-[#666] text-[16px] mb-4">
              <span>NT$</span>
              <span>課程時數</span>
            </div>
            <a
              href="#"
              class="bg-[#3498db] hover:bg-[#2d83bc] text-white rounded-lg p-2"
              >查看詳情</a
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
.SelectCourse {
  background-image: url("../assets/images/email-pattern.png");
}
</style>
