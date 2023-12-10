import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import home_top from './components/home_top/index.vue';
import home_sidebar from './components/home_sidebar/index.vue';
import '@/style/reset.scss';
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';

const app = createApp(App);
app.use(store).use(router);
app.use(ElementPlus);
app.component('home_top', home_top);
app.component('home_sidebar', home_sidebar);

app.mount('#app');
