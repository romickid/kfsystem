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
      <div>{{gridData}}</div>
      <button @click="test1()">Test1</button>
      <button @click="test2()">Test2</button>
      <button @click="test3()">Test3</button>
      <button @click="test4()">Test4</button>
      <button @click="test5()">Test5</button>
      <button @click="test6()">empty</button>
      <button @click="test7()">empty</button>
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
      api_create: './api/customerservice_create/',
      api_set_profile: './api/customerservice_set_profile/',
      api_login: './api/customerservice_login/',
      api_reset_password: './api/customerservice_reset_password/',
      api_validity: './api/serialnumber_validity/',
      api_mark_used: './api/serialnumber_mark_used/',
      item: {},
      gridData: ''

    }
  },

  // FOR TEST, DO NOT DELETE IT!
  methods: {
    test1: function () {
      var vm = this
      this.item = { 'email': 'test2@a.com' }
      vm.$http.post(vm.api_create, this.item)
        .then((response) => {
          vm.$set(this, 'item', {})
        })
    },

    test2: function () {
      var vm = this
      this.item = { 'email': 'test4@a.com' }
      vm.$http.post(vm.api_create, this.item)
        .then((response) => {
          vm.$set(this, 'item', {})
        })
    },

    test3: function () {
      var vm = this
      this.item = { 'email': 'test4@a.com', 'password': 'pass4' }
      vm.$http.post(vm.api_set_profile, this.item)
        .then((response) => {
          vm.$set(this, 'item', {})
        })
    },

    test4: function () {
      var vm = this
      this.item = { 'email': 'test4@a.com', 'nickname': 'nick4'}
      vm.$http.post(vm.api_set_profile, this.item)
        .then((response) => {
          vm.$set(this, 'item', {})
        })
    },

    test5: function () {
      var vm = this
      this.item = { 'email': 'test4@a.com', 'nickname': 'nick4', 'password': 'pass4' }
      vm.$http.post(vm.api_set_profile, this.item)
        .then((response) => {
          vm.$set(this, 'item', {})
        })
    },

    test6: function () {
      var vm = this
      this.item = { 'serials': 'abc124' }
      vm.$http.post(vm.api_mark_used, this.item)
        .then((response) => {
          vm.$set(this, 'item', {})
        })
    },

    test7: function () {
      var vm = this
      this.item = { 'serials': 'abc123' }
      vm.$http.post(vm.api_mark_used, this.item)
        .then((response) => {
          vm.$set(this, 'item', {})
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
