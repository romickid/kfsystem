<template>
  <div id="app">
    <img src="./assets/logo.png">
    <div>
      <h2>
        <a href="./en_login">跳转至企业登录页面</a>
        <a href="./se_folders">跳转至客服注册页面</a>
      </h2>
    </div>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
