<template>
  <div id="app">
    <div class='main-content'>
      <div class='user-info'>{{ user_info }}</div>
      <div class='div-button'><a href="./en_folders"><button class='button'>免费注册</button></a></div>
      <div class='div-button'><a href="./en_login"><button class='button'>用户登录</button></a></div>
      <div class='div-button'><a :href='webUrl'><button class='button'>联系客服</button></a></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      user_info: '未登录',
      apiCustomerShowUserInfo: '../api/customer_show_user_info/',
      apiCustomerGetWebUrl: '../api/customer_get_web_url/',
      webUrl: ''
    }
  },
  methods: {
    getUserInfoApi () {
      this.$http.post(this.apiCustomerShowUserInfo)
        .then((response) => {
          if (response.data === 'ERROR, session is broken.') {
            console.log('getUserInfoApi1')
          } else if (response.data === 'ERROR, wrong email.') {
            console.log('getUserInfoApi2')
          } else {
            this.user_info = response.data.email
          }
        })
    },
    getWebUrl () {
      this.$http.post(this.apiCustomerGetWebUrl)
        .then((response) => {
          if (response.data === 'ERROR, communication key is not exist') {
            console.log('getUserInfoApi1')
          } else {
            this.webUrl = response.data
          }
        })
    }
  },
  created () {
    this.getUserInfoApi()
    this.getWebUrl()
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

body {
  overflow-y: scroll;
  margin: 0;
  background-image: url('./assets/background.png');
  background-size: 100%;
}

.main-content {
  height: 11780px;
}

.user-info {
  width: 400px;
  height: 31px;
  background-color: #383d46;
  border-bottom: 1px solid #50575f;
  margin-left: 54.6em;
  color: #fff;
  padding-top: 10px;
  text-align: right;
}

.div-button {
  display: inline;
  float: right;
}

.button {
  color: #fff;
  background-color: #1bc3d4;
  border: 0;
  font-size: 1em;
  padding: 1.28em 2em;
  border-left: 1px solid #383d46;
}
</style>
