<template>
  <div class="Home">
    <HeroSection />
    <FeaturesCardList id="features">
      <FeaturesCard
        ><template v-slot:icon>📚</template
        ><template v-slot:title>豐富的課程資源</template
        ><template v-slot:text
          >涵蓋各種領域的優質課程，從程式設計到語言學習，應有盡有。</template
        ></FeaturesCard
      >
      <FeaturesCard
        ><template v-slot:icon>🔄</template
        ><template v-slot:title>靈活的學習方式</template
        ><template v-slot:text
          >線上學習，自由掌握進度，隨時隨地都能學習。</template
        ></FeaturesCard
      >
      <FeaturesCard
        ><template v-slot:icon>👨‍👩‍👧‍👦</template
        ><template v-slot:title>互動式學習社群</template
        ><template v-slot:text
          >與來自世界各地的學習者交流，共同進步。</template
        ></FeaturesCard
      >
      <FeaturesCard
        ><template v-slot:icon>👨‍👩‍👧‍👦</template
        ><template v-slot:title>互動式學習社群</template
        ><template v-slot:text
          >與來自世界各地的學習者交流，共同進步。</template
        ></FeaturesCard
      >
    </FeaturesCardList>
    <div class="h-screen"></div>
  </div>
</template>

<script setup>
import HeroSection from "../components/HeroSection.vue";
import FeaturesCardList from "../components/Feature/FeaturesCardList.vue";
import FeaturesCard from "../components/Feature/FeaturesCard.vue";
</script>

<style scoped>
.Home {
  background-image: url("../assets/images/email-pattern.png");
}
</style>
