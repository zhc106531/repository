<template>
  <div class="hometop">
    <div class="homeTopImg">
      <img
        class="Timg"
        src="https://vv-web-assets.oss-accelerate.aliyuncs.com/vvOfficialWeb/pro-cn-4/images/6a684bc2fb15bb22053bbe8f5c97b2bb.png"
        alt="logo"
      />
    </div>
    <div class="experience_content-des">
      企业和个人的一站式数智化协同工作平台
    </div>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped lang="scss">
.hometop {
  height: 70px;
  // line-height: 70px;
  width: 100%;
  background-color: #fff;
  position: fixed;
  display: flex;
  justify-content: center;
  align-items: center;
  border-bottom: 1px solid #dddfe6;

  .homeTopImg {
    width: 200px;
    height: 50px;
    .Timg {
      // width: 100%;
      height: 50px;
    }
  }
  .experience_content-des {
    flex: 1;
    display: flex;
    justify-content: center;
    align-items: center;
    vertical-align: middle;
    font-weight: 300;
    font-size: 28px;
    color: #64646c;
  }
}
</style>
