import Vue from 'vue'
import Router from 'vue-router'
import system from '@/components/system'
import outline from '@/components/outline'
import team from '@/components/team'
import web from '@/components/web'
import widget from '@/components/widget'
import mobile from '@/components/mobile'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'outline',
      component: outline
    },
    {
      path: '/system',
      name: 'system',
      component: system
    },
    {
      path: '/team',
      name: 'team',
      component: team
    },
    {
      path: '/web',
      name: 'web',
      component: web
    },
    {
      path: '/widget',
      name: '/widget',
      component: widget
    },
    {
      path: '/mobile',
      name: 'mobile',
      component: mobile
    }
  ]
})
