import Vue from 'vue'
import KfWorking from './kf_working.vue'
import VueResource from 'vue-resource'
import iView from 'iview'
import 'iview/dist/styles/iview.css'

Vue.config.debug = true
Vue.config.productionTip = false
Vue.use(iView)
Vue.use(VueResource)

/* eslint-disable no-new */
new Vue({
  el: '#chat',
  template: '<KfWorking/>',
  components: {
    KfWorking
  }
})
