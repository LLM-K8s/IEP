<template>
  <div class="CreateCourse">
    <NavBar />
    <div class="w-[90%] mx-[5%]">
      <div class="pt-20 w-[100%]">
        <span class="text-[24px] mt-20 mb-[16px] font-bold h-fit">
          建立新課程 📚
        </span>
        <hr class="border-2 border-gray-500 rounded-2xl" />
      </div>
      <div class="shadow-gray-500 rounded-[8px] w-[100%] self-center p-5">
        <label for="course-name" class="text-[20px] font-bold mb-[10px]"
          >課程名稱</label
        >
        <input
          id="course-name"
          type="text"
          class="bg-white shadow-2xs shadow-gray-500 text-[16px] w-full border-1 border-solid border-[#ddd] rounded-[8px] p-2 mb-4"
          placeholder="請輸入課程名稱"
        />
        <label for="course-type" class="text-[20px] font-bold mb-[10px]"
          >課程類型</label
        >
        <select
          id="course-type"
          class="bg-white shadow-2xs text-[16px] w-full border-1 border-solid border-[#ddd] rounded-[8px] p-2 mb-4"
        >
          <option>請選擇類型</option>
          <option>程式設計</option>
        </select>
        <label for="course-intro" class="text-[20px] font-bold mb-[10px]"
          >課程簡介</label
        >
        <input
          id="course-intro"
          type="text"
          class="bg-white shadow-2xs text-[16px] w-full border-1 border-solid border-[#ddd] rounded-[8px] p-2 mb-4"
          placeholder="請輸入課程簡介"
        />
        <label for="course-outline" class="text-[20px] font-bold mb-[10px]"
          >教學大綱</label
        >
        <textarea
          id="course-outline"
          type="text"
          class="bg-white shadow-2xs text-[16px] w-full border-1 border-solid border-[#ddd] rounded-[8px] p-2 mb-4"
          placeholder="請描述課程內容與學習目標"
          rows="5"
        ></textarea>
        <label for="course-image" class="text-[20px] font-bold mb-[10px]"
          >課程封面圖片</label
        >
        <input
          id="course-image"
          type="file"
          class="bg-white shadow-2xs text-[16px] w-full border-1 border-solid border-[#ddd] rounded-[8px] p-2 mb-4 hover:bg-gray-300"
        />
        <label for="course-price" class="text-[20px] font-bold mb-[10px]"
          >課程價格 (新台幣 $TWD)</label
        >
        <input
          id="course-price"
          type="number"
          class="bg-white shadow-2xs text-[16px] w-full border-1 border-solid border-[#ddd] rounded-[8px] p-2 mb-4"
          placeholder="請輸入課程價格"
        />
        <button
          class="bg-[#3498db] text-white w-[100%] rounded-lg p-2 mt-[16px] hover:bg-[#2d83bc]"
        >
          提交審核
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import NavBar from "../components/NavBar/NavBar.vue";
</script>

<style scoped>
.CreateCourse {
  background-image: url("../assets/images/email-pattern.png");
  height: 100vh;
}
</style>
