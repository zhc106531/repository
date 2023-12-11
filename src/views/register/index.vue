<template>
  <div class="jbxx">
    <el-form class="demo-form-inline">
      <div class="contenttop">
        <!-- <el-input class="elinput" placeholder="请输入要注册的个数" /> -->
        <el-input-number class="elinput" v-model="registerNum" :min="1" :max="10" controls-position="right" />
        <el-button class="elbutton" type="primary" @click="register">注册</el-button>
      </div>
      <div class="contentbutton">
        <el-radio-group v-model="radio">
          <el-radio :label="1">test2</el-radio>
          <el-radio :label="2">test3</el-radio>
          <el-radio :label="3">uat</el-radio>
          <el-radio :label="4">pre</el-radio>
        </el-radio-group>
      </div>
    </el-form>
  </div>
  <div class="output">
    <el-table :data="tableData" height="400" style="width: 100%">
      <el-table-column prop="name" label="姓名" />
      <el-table-column prop="phone" label="手机号" />
      <el-table-column prop="account" label="账号" />
      <el-table-column prop="password" label="密码" />
    </el-table>
  </div>
</template>

<script setup lang="ts">

import { ref } from 'vue';
import axios from 'axios';


const registerNum = ref(1)
const tableData = ref([]);


axios.defaults.baseURL = 'http://127.0.0.1:5000';

const register = async () => {
  try {
    const response = await axios.get('/api/register', {
      params: {
        num: registerNum.value
      }
    });

    // 清空原有数据，将新数据添加到 tableData 中
    tableData.value = response.data.accounts;
    // alert(`注册成功，接口返回：${response.message}`);
  } catch (error) {
    console.error('Error:', error);
    alert(`注册失败，错误信息：${error.message}`);
  }
};

</script>

<style scoped lang="scss">
.contenttop {
  display: flex;
}

.elinput {
  flex: 8;
  width: 80px;
}

::v-deep(.elbutton) {
  flex: 2;
}

.jbxx {
  height: 350px;
  width: 1400px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  /* 垂直居中 */
  margin: 0 auto;
  /* 水平居中 */
}

.output {
  width: 1400px;
  height: 450px;
}


.demo-form-inline {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  /* 添加间距，以提高可读性 */
  width: 300px;
  height: 200px;
  /* 减小表单高度，以便适应容器高度 */
}

.elbutton {
  width: 300px;
}
</style>
