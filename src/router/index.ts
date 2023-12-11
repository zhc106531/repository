import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/bug',
    name: 'bug',
    component: () => import('@/views/bugcounter/index.vue'),
  },
  {
    path: '/register',
    name: 'register',
    component: () => import('@/views/register/index.vue'),
  },
  {
    path: '/add',
    name: 'add',
    component: () => import('@/views/add/index.vue'),
  },
  {
    path: '/buglogin',
    name: 'buglogin',
    component: () => import('@/views/bugcounter/buglogin.vue'),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
