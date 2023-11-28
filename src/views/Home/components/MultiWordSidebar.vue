<template>
  <el-row class="tac">
    <el-col :span="12">
      <el-menu
        default-active="2"
        class="el-menu-vertical-demo"
        @open="handleOpen"
        @close="handleClose"
      >
        <el-sub-menu index="1">
          <template #title>
            <el-icon><location /></el-icon>
            <span>测试工具</span>
          </template>
          <el-menu-item index="1-1" @click="toBugCounter">bug统计</el-menu-item>
          <el-menu-item index="1-2">账号注册</el-menu-item>
        </el-sub-menu>
        <el-menu-item index="2" disabled>
          <el-icon><icon-menu /></el-icon>
          <span>预留...</span>
        </el-menu-item>
        <el-menu-item index="3" disabled>
          <el-icon><document /></el-icon>
          <span>预留...</span>
        </el-menu-item>
        <el-menu-item index="4" disabled>
          <el-icon><setting /></el-icon>
          <span>预留...</span>
        </el-menu-item>
      </el-menu>
    </el-col>
  </el-row>
</template>

<script lang="ts" setup>
import { router } from '@/router';
import {
  // eslint-disable-next-line no-unused-vars
  Document,
  Menu as IconMenu,
  // eslint-disable-next-line no-unused-vars
  Location,
  Setting,
} from '@element-plus/icons-vue';
const handleOpen = (key: string, keyPath: string[]): void => {
  console.log(key, keyPath);
};

const handleClose = (key: string, keyPath: string[]) => {
  console.log(key, keyPath);
};

const toBugCounter = () => {
  // router.push({ name: 'bug' });
  router.push({
    path: '/bug',
    query: {
      aaa: 'bbb',
    },
  });
};
</script>

<style>
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 400px;
}
</style>
