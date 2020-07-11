import Vue from 'vue'
import Router from 'vue-router'
import SpecialCaseContainer from '@/components/SpecialCaseContainer'
import AboutTheApp from "@/components/AboutTheApp";

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'SpecialCaseContainer',
      component: SpecialCaseContainer
    },
    {
      path: '/acerca-de',
      name: 'AboutTheApp',
      component: AboutTheApp
    }
  ]
})
