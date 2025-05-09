<template>
  <DefaultLayout>
    <HeroSection />
    <div class="w-[90%] mx-[5%]">
      <section id="features" class="features-section px-[64px]">
        <FeaturesCardList>
          <template te v-slot:featureCol1>
            <FeaturesCard
               ><template v-slot:icon>📚</template
              ><template v-slot:title>豐富的課程資源</template
              ><template v-slot:text
                >涵蓋各種領域的優質課程，從程式設計到語言學習，應有盡有</template
              ></FeaturesCard>
            <FeaturesCard
              ><template v-slot:icon>📈</template
              ><template v-slot:title>提升學習效率</template
              ><template v-slot:text
                >學生可以更專注於學習和實作，減少因環境問題等造成不必要的困擾</template
              ></FeaturesCard>
            <FeaturesCard
              ><template v-slot:icon>🌐</template
              ><template v-slot:title>雲端開發</template
              ><template v-slot:text
                >可以透過網路在線上進行開發，並且手機、平板、電腦都可以使用</template
              ></FeaturesCard
            >
          </template>
          <template v-slot:featureCol2>
            <FeaturesCard
              ><template v-slot:icon>🏗️</template
              ><template v-slot:title>客製化開發環境</template
              ><template v-slot:text
                >減少學生在設定環境配置上的困難，讓他們能夠更快地進入學習狀態</template
              ></FeaturesCard
            >
            <FeaturesCard
              ><template v-slot:icon>🎯</template
              ><template v-slot:title>靈活學習</template
              ><template v-slot:text
                >可以在任何時間、任何地點通過網路連線至平台進行學習和實作</template
              ></FeaturesCard
            >
          </template>
        </FeaturesCardList>
      </section>

      <section id="hotcourse" class="hotcourse-section mt-[120px] px-[64px]">
        <HotCourseLayout>
          <HotCourse />
          <HotCourse />
          <HotCourse />
          <HotCourse />
        </HotCourseLayout>
      </section>
    </div>
  </DefaultLayout>
</template>

<script setup>
import DefaultLayout from "../../Layout/default.vue";
import FeaturesCard from "./Feature/FeaturesCard.vue";
import FeaturesCardList from "./Feature/FeaturesCardList.vue";
import HeroSection from "./HeroSection.vue";
import HotCourse from "./HotCourse/HotCourse.vue";
import HotCourseLayout from "./HotCourse/HotCourseLayout.vue";
</script>

<style scoped>
.features-section,
.hotcourse-section {
  padding: 2rem 0;
}
</style>
