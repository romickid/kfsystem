import Vue from 'vue'
import App from './App'
import VueResource from 'vue-resource'

Vue.config.debug = true
Vue.config.productionTip = false

Vue.use(VueResource)
new Vue({
  el: '#chat',
  template: '<App/>',
  components: {
    App
  }
})
