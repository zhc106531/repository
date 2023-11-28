<template>
    <!-- 页面头部 -->
    <header>
      <!-- Logo 容器 -->
      <div class="logo-container">
        <!-- Logo 图片 -->
        <img id="vvLog" src="https://vv-web-assets.oss-accelerate.aliyuncs.com/vvOfficialWeb/pro-cn-0/images/6a684bc2fb15bb22053bbe8f5c97b2bb.png" alt="logo">
      </div>
      <!-- 标题容器 -->
      <div class="title-container">
        <!-- 页面标题 -->
        <h1>工作互联 生态共赢</h1>
      </div>
    </header>
  </template>
  
  <script>
  export default {
    name: 'AppHeader', // 修改组件名称为多个单词的形式，例如 'AppHeader'
  };
  </script>
  
  <style scoped>
  /* 添加组件样式 */
  header {
    background-color: #c2c5c9;
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: space-around; /* 修改为 space-around 以更均匀地分配空间 */
    padding: 10px; /* 可选：为更好的外观添加内边距 */
  }
  
  .logo-container img {
    height: 40px; /* 设置 Logo 的高度，根据需要调整 */
  }
  
  .title-container {
    flex: 1; /* 允许标题容器根据需要扩展并占据可用空间 */
    text-align: center; /* 居中标题文本 */
  }
  
  .title-container h1 {
    margin: 0; /* 移除默认的边距 */
  }
  </style>
  