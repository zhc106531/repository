import { createRouter, createWebHistory } from 'vue-router';
import { perRoutes } from './perRouter';
import type { App } from 'vue';
import type { RouteRecordRaw } from 'vue-router';

export const routes: Array<RouteRecordRaw> = [...perRoutes];

export const router = createRouter({
  history: createWebHistory(),
  routes,
});

export function setupRouter(app: App<Element>) {
  app.use(router);
}
// export default router;
