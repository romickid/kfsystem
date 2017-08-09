import Vue from 'vue'
import App from './App'
import VueResource from 'vue-resource'
import iView from 'iview'
import 'iview/dist/styles/iview.css'

Vue.use(VueResource)
Vue.use(iView)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  template: '<App/>',
  components: {
    App
  }
})
