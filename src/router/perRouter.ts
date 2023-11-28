import type { RouteRecordRaw } from 'vue-router';

export const perRoutes: Array<RouteRecordRaw> = [
  {
    name: 'home',
    path: '/home',
    component: () => import('@/views/Home/index.vue'),
    children: [],
  },
  {
    name: 'login',
    path: '/login',
    component: () => import('@/views/Login/index.vue'),
    children: [],
  },
  {
    name: 'bug',
    path: '/bug',
    component: () => import('@/views/Tools/index.vue'),
    children: [],
  },
];
