<template>
  <Card class="feature-card">
    <template #header>
      <div class="text-4xl text-center py-4">{{ feature.icon }}</div>
    </template>
    <template #title>{{ feature.title }}</template>
    <template #content>
      <p class="text-gray-600">{{ feature.description }}</p>
    </template>
  </Card>
</template>

<script setup>
import Card from "primevue/card";

defineProps({
  feature: {
    type: Object,
    required: true,
    default: () => ({
      icon: "",
      title: "",
      description: "",
    }),
  },
});
</script>

<style scoped>
.feature-card {
  transition: transform 0.2s ease-in-out;
  height: 100%;
}

.feature-card:hover {
  transform: translateY(-5px);
}

:deep(.p-card) {
  border-radius: 1rem;
  box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
}

:deep(.p-card-header) {
  background-color: #f8fafc;
  border-top-left-radius: 1rem;
  border-top-right-radius: 1rem;
  padding: 0;
}

:deep(.p-card-title) {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1e293b;
  text-align: center;
  margin-bottom: 1rem;
}

:deep(.p-card-content) {
  padding: 1.5rem;
}
</style>
