<template>
    <div class="jbxx">
      <el-form class="demo-form-inline">
        <el-input placeholder="jira地址" />
        <el-input placeholder="统计版本" />
        <el-button class="elbutton" type="primary" round>统计</el-button>
      </el-form>
    </div>
    <div class="output"></div>
  </template>
  
  <script setup lang="ts">
  import router from '@/router';
  
  const buglogin = () =>{
    router.push('buglogin')
  }
  </script>
  
  <style scoped lang="scss">
  .jbxx {
    height: 400px;
    width: 1400px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center; /* 垂直居中 */
    margin: 0 auto; /* 水平居中 */
  }
  
  .output {
    width: 1400px;
    height: 450px;
  }
  
  .demo-form-inline {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px; /* 添加间距，以提高可读性 */
    width: 300px;
    height: 200px; /* 减小表单高度，以便适应容器高度 */
  }
  .elbutton{
    width: 300px;
  }
  
  </style>
  