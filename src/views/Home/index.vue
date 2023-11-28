<template>
  <div>
    这是home页面
    <homeHeader></homeHeader>
    <homeMainContent></homeMainContent>
    <homeMultiWordSideba></homeMultiWordSideba>
  </div>
</template>

<script setup lang="ts">
import homeHeader from './components/Header.vue';
import homeMainContent from './components/MainContent.vue';
import homeMultiWordSideba from './components/MultiWordSidebar.vue';
</script>

<style scoped></style>
