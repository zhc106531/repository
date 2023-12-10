<template>
  <div class="container">
    <home_top></home_top>
    <home_sidebar></home_sidebar>
    <div class="content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped lang="scss">
.container {
  height: 100%;
  width: 100%;
  position: relative; // 父 --相对
  .content {
    position: absolute; //子 --绝对
    left: 200px;
    top: 70px;
  }
}
</style>
