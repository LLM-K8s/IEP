<template>
  <p class="text-gray-800 text-[24px] text-center mt-[120px] font-bold">
    平台特色
  </p>
  <hr class="my-4 border-2 border-gray-500 rounded-2xl" />
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
    <FeatureCard
      v-for="feature in features"
      :key="feature.id"
      :feature="feature"
    />
  </div>
</template>

<script setup>
import FeatureCard from "./FeatureCard.vue";

const features = [
  {
    id: 1,
    icon: "📚",
    title: "豐富的課程資源",
    description: "涵蓋各種領域的優質課程，從程式設計到語言學習，應有盡有",
  },
  {
    id: 2,
    icon: "📈",
    title: "提升學習效率",
    description: "學生可以更專注於學習和實作，減少因環境問題等造成不必要的困擾",
  },
  {
    id: 3,
    icon: "🌐",
    title: "雲端開發",
    description: "可以透過網路在線上進行開發，並且手機、平板、電腦都可以使用",
  },
  {
    id: 4,
    icon: "🏗️",
    title: "客製化開發環境",
    description: "減少學生在設定環境配置上的困難，讓他們能夠更快地進入學習狀態",
  },
  {
    id: 5,
    icon: "🎯",
    title: "靈活學習",
    description: "可以在任何時間、任何地點通過網路連線至平台進行學習和實作",
  },
  {
    id: 6,
    icon: "📊",
    title: "學習分析",
    description: "提供詳細的學習數據分析，幫助學生了解自己的學習進度和強項，制定更有效的學習策略",
  },
];
</script>
