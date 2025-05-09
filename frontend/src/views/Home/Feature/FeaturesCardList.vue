<template>
  <div>
    <p class="text-gray-800 text-[24px] text-center mt-[120px] font-bold">
      平台特色
    </p>
    <hr class="my-4 border-2 border-gray-500 rounded-2xl" />
    <div
      class="grid gap-4 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 mx-[16px] place-items-center place-content-center"
    >
      <slot name="featureCol1"></slot>
    </div>
    <div
      class="grid gap-4 grid-cols-1 sm:grid-cols-2 lg:grid-cols-2 lg:gap-x-0 mx-[16px] place-items-center place-content-cente"
    >
      <slot name="featureCol2"></slot>
    </div>
  </div>
</template>
