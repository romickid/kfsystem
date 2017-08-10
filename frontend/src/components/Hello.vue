<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>Essential Links</h2>
    <ul>
      <li>
        <a href="https://vuejs.org" target="_blank">Core Docs</a>
      </li>
      <li>
        <a href="https://forum.vuejs.org" target="_blank">Forum</a>
      </li>
      <li>
        <a href="https://gitter.im/vuejs/vue" target="_blank">Gitter Chat</a>
      </li>
      <li>
        <a href="https://twitter.com/vuejs" target="_blank">Twitter</a>
      </li>
      <br>
      <li>
        <a href="http://vuejs-templates.github.io/webpack/" target="_blank">Docs for This Template</a>
      </li>
    </ul>
    <h2>Ecosystem</h2>
    <ul>
      <li>
        <a href="http://router.vuejs.org/" target="_blank">vue-router</a>
      </li>
      <li>
        <a href="http://vuex.vuejs.org/" target="_blank">vuex</a>
      </li>
      <li>
        <a href="http://vue-loader.vuejs.org/" target="_blank">vue-loader</a>
      </li>
      <li>
        <a href="https://github.com/vuejs/awesome-vue" target="_blank">awesome-vue</a>
      </li>
    </ul>

    <div>
      <div>hello</div>
      <div>{{ gridData }}</div>
      <button @click="test1()">Test1</button>
      <button @click="test2()">Test2</button>
      <button @click="test3()">Test3</button>
      <button @click="test4()">Test4</button>
      <button @click="test5()">Test5</button>
      <button @click="test6()">Test6</button>
      <button @click="test7()">Test7</button>
      <button @click="test8()">History</button>
    </div>

  </div>
</template>

<script>
export default {
  name: 'hello',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      // for test, do not delete it.
      api_admin_create: './api/admin_create/',
      api_admin_login: './api/admin_login/',
      api_admin_reset_password: './api/admin_reset_password/',
      api_admin_show_communication_key: './api/admin_show_communication_key/',
      api_admin_reset_communication_key: './api/admin_reset_communication_key/',
      api_admin_find_password_email_request: './api/admin_find_password_email_request/',
      api_admin_find_password_check_vid: './api/admin_find_password_check_vid/',

      api_customerservice_create: './api/customerservice_create/',
      api_customerservice_set_profile: './api/customerservice_set_profile/',
      api_customerservice_login: './api/customerservice_login/',

      api_chattinglog_send_message: './api/chattinglog_send_message/',
      api_chattinglog_delete_record: './api/chattinglog_delete_record/',
      api_chattinglog_get_data: './api/chattinglog_get_data/',
      api_chattinglog_delete_record_ontime: './api/chattinglog_delete_record_ontime/',
      api_chattinglog_status_change: './api/chattinglog_status_change/',
      api_chattinglog_show_history: './api/chattinglog_show_history/',

      item: {},
      gridData: '',
      test: {}

    }
  },

  // FOR TEST, DO NOT DELETE IT!
  methods: {
    test1: function () {
      var vm = this
      this.item = { 'email': 'test1@a.com', 'nickname': 'nick1', 'password': 'pass1', 'serials': 's1' }
      vm.$http.post(vm.api_admin_create, this.item)
        .then((response) => {
          vm.$set(this, 'item', {})
        })
    },
    test2: function () {
      var vm = this
      this.item = { 'email': 'test1@a.com', 'password': 'pass1' }
      vm.$http.post(vm.api_admin_login, this.item)
        .then((response) => {
          vm.$set(this, 'item', {})
        })
    },
    test3: function () {
      var vm = this
      this.item = { 'email': 'cs1@a.com', 'admin_email': 'test1@a.com' }
      vm.$http.post(vm.api_customerservice_create, this.item)
        .then((response) => {
          vm.$set(this, 'item', {})
        })
    },
    test4: function () {
      var vm = this
      this.item = { 'email': 'cs1@a.com', 'password': 'pass1', 'nickname': 'nickname1' }
      vm.$http.post(vm.api_customerservice_set_profile, this.item)
        .then((response) => {
          vm.$set(this, 'item', {})
        })
    },
    test5: function () {
      var vm = this
      this.item = { 'email': 'cs1@a.com', 'password': 'pass1' }
      vm.$http.post(vm.api_customerservice_login, this.item)
        .then((response) => {
          vm.$set(this, 'item', {})
        })
    },
    test8: function () {
      var vm = this
      this.item = { 'client_id': '1', 'service_id': '1' }
      vm.$http.post(vm.api_chattinglog_show_history, this.item)
        .then((response) => {
          vm.$set(this, 'gridData', response.data)
          for (var p in response.data) {
            alert(response.data[p].time + '' + response.data[p].content)
          }
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
