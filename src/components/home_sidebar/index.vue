<template>
  <div class="sidebar">
    <el-menu
      default-active="2"
      class="el-menu-vertical-demo"
      @open="handleOpen"
      @close="handleClose"
    >
      <el-menu-item index="1" @click="tobug">
        <el-icon><setting /></el-icon>
        <span>bug统计</span>
      </el-menu-item>
      <el-menu-item index="2" @click="toregister">
        <el-icon><setting /></el-icon>
        <span>账号注册</span>
      </el-menu-item>
      <el-menu-item index="3" @click="toadd">
        <el-icon><setting /></el-icon>
        <span>添加员工</span>
      </el-menu-item>
    </el-menu>
  </div>
</template>

<script setup lang="ts">
import { useRouter, useRoute } from 'vue-router';
const router = useRouter();
const handleOpen = (key: string, keyPath: string[]) => {
  console.log(key, keyPath);
};
const handleClose = (key: string, keyPath: string[]) => {
  console.log(key, keyPath);
};
const tobug = () => {
  router.push({ name: 'bug' });
};
const toregister = () => {
  router.push({ name: 'register' });
};
const toadd = () => {
  router.push({ name: 'add' });
};
</script>

<style scoped lang="scss">
.sidebar {
  height: 100%;
  width: 200px;
  position: fixed;
  top: 70px;
}
.el-menu-vertical-demo {
  height: 100%;
}
</style>
