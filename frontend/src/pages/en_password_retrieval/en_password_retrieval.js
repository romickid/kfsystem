// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import EnPasswordRetrieval from './en_password_retrieval.vue'
import VueResource from 'vue-resource'
import iView from 'iview'
import 'iview/dist/styles/iview.css'
import utils from './utils'

Vue.use(VueResource)
Vue.use(iView)
Vue.config.productionTip = false
Vue.prototype.$utils = utils

/* eslint-disable no-new */
new Vue({
  el: '#app',
  template: '<EnPasswordRetrieval/>',
  components: {
    EnPasswordRetrieval
  }
})
