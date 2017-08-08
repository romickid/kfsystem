<template>
  <div id="app">
    <img src="./assets/logo.png">
    <div>
      <h2>
        <a href="./en_login">跳转至企业登录页面</a>
        <a href="./en_folders">跳转至企业注册页面</a>
        <br>
        <a href="./se_login">跳转至客服登录页面</a>
        <a href="./se_folders">跳转至客服注册页面</a>
        <br>
        <a href="./en_password_retrieval">跳转至企业找回密码页面</a>
        <a href="./se_password_retrieval">跳转至客服找回密码页面</a>
        <br>
        <a href="../kf_working/kf_working.html">客服工作页面工作界面！</a>
        <a href="../customer_newlabel/customer_newlabel.html">用户新标签页面</a>
      </h2>
    </div>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      value: [20, 50]
    }
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
  margin-top: 60px;
}
</style>
