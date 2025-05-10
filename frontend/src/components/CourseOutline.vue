<template>
  <div class="bg-white p-8 rounded-lg w-[90%] shadow-lg md:w-[50%]">
    <h2 class="text-[24px] font-bold mb-4 flex justify-center">課程大綱</h2>
    <hr class="border-2 border-gray-500 rounded-2xl mb-5" />
    <slot name="Outline"></slot>
    <slot name="Button"></slot>
  </div>
</template>
