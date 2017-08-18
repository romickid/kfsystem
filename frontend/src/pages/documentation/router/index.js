import Vue from 'vue'
import Router from 'vue-router'
import outline from '@/components/document_outline'
import accessGuide from '@/components/access_guide_doc'
import web from '@/components/web_access_doc'
import widget from '@/components/widget_access_doc'
import mobile from '@/components/mobile_access_doc'
import userInfo from '@/components/user_infomation_doc'
import robotKnowledegebase from '@/components/robot_knowledegebase_doc'
import csSetRobot from '@/components/cs_set_robot_doc'
import csWorking from '@/components/cs_working_doc'
import csSetProfile from '@/components/cs_set_profile_doc'
import additionFunction from '@/components/addition_function_doc'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'outline',
      component: outline
    },
    {
      path: '/access_guide',
      name: 'access_guide',
      component: accessGuide
    },
    {
      path: '/web',
      name: 'web',
      component: web
    },
    {
      path: '/widget',
      name: 'widget',
      component: widget
    },
    {
      path: '/mobile',
      name: 'mobile',
      component: mobile
    },
    {
      path: '/user_info',
      name: 'user_info',
      component: userInfo
    },
    {
      path: '/robot_knowledegebase',
      name: 'robot_knowledegebase',
      component: robotKnowledegebase
    },
    {
      path: '/cs_set_robot',
      name: 'cs_set_robot',
      component: csSetRobot
    },
    {
      path: '/cs_working',
      name: 'cs_working',
      component: csWorking
    },
    {
      path: '/cs_set_profile',
      name: 'cs_set_profile',
      component: csSetProfile
    },
    {
      path: '/addition_function',
      name: 'addition_function',
      component: additionFunction
    }
  ]
})
