// main.ts
import { createApp } from 'vue';
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';
import App from './App.vue';

import { setupRouter } from '@/router';
const app = createApp(App);

//设置路由
setupRouter(app);

app.use(ElementPlus).mount('#app');
