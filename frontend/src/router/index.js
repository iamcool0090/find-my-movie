import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MoviesView from '../views/MoviesView.vue'
import LanguageView from '../views/MovieLanguage.vue'
import AboutVIew from '@/views/AboutVIew.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/movies',
      name: 'movies',
      component: LanguageView
    },
    {
      path: '/movies/:language',
      name: 'movies-language',
      component: MoviesView,
      props: true
    },
    {
      path: '/about',
      name: 'about',
      component: AboutVIew
    }
  ]
})

export default router
