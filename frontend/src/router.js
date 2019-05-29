import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'

Vue.use(Router)

export default new Router({
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/auth/login/',
      name: 'login',
      component: () => import('./views/Login.vue'),
      data: 'hello'
    },
    {
      path: '/auth/register/',
      name: 'register',
      component: () => import('./views/Register.vue')
    },
    {
      path: '/profile_get/',
      name: 'profile_get',
      component: () => import('./views/Profile_get.vue'),
      props: { default: true }
    },
    {
      path: '/profile_put/',
      name: 'profile_put',
      component: () => import('./views/Profile_put.vue')
    }
  ]
})
