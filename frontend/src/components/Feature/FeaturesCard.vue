<template>
  <div
    class="text-center mt-[30px] bg-white shadow-md shadow-gray-500 rounded-[8px] w-[80%] h-[90%] self-center p-5"
  >
    <slot>
      <dev class="text-[40px] mb-4">
        <slot name="icon"></slot>
      </dev>
      <p class="text-gray-800 text-[20px] font-bold mb-2.5">
        <slot name="title"></slot>
      </p>
      <p class="text-gray-800 text-[16px]">
        <slot name="text"></slot>
      </p>
    </slot>
  </div>
</template>
