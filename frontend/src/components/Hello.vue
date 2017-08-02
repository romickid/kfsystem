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
      <button @click="getData()">getData</button>
      <button @click="postData()">postData</button>
      <button @click="deleteData()">deleteData</button>
    </div>
  
  </div>
</template>

<script>
export default {
  name: 'hello',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      m_api: './api/',
      item: {},
      gridData: ''

    }
  },

  methods: {
    getData: function () {
      var vm = this
      vm.$http.get(vm.m_api)
        .then((response) => {
          vm.$set(this, 'gridData', response.data)
        })
    },

    postData: function () {
      var vm = this
      this.item = { name: 'a1' }
      vm.$http.post(vm.m_api, this.item)
        .then((response) => {
          vm.$set(this, 'item', {})
          vm.getData()
        })
    },

    deleteData: function () {
      var vm = this
      this.item = { name: 'a1' }
      vm.$http.delete(vm.m_api + '8/')
        .then((response) => {
          vm.getData()
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
