import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'
import App from '../App.vue';
import About from '../views/About.vue';

import iniciarSesion from '../views/iniciarSesion.vue'

const routes = [
  {
    path: '/',
    name: 'root',
    component: App
  },
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
    path: '/admin/logIn',
    name: "iniciarSesion",
    component: iniciarSesion
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes
});

export default router