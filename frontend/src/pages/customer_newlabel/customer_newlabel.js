import Vue from 'vue'
import CustomerNewlabel from './customer_newlabel.vue'
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
  template: '<CustomerNewlabel/>',
  components: {
    CustomerNewlabel
  }
})
