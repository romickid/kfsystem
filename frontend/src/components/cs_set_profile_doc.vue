<template>
  <div id='app'>
    <div class='main-content-head'>
      <h1>客服接入</h1>
      <p>从此开始你的客服之路</p>
    </div>
    <div class='main-content-body'>
      <div class='guide'>
        <h2>客服完善信息</h2>
        <p>客服初次登录，录入个人信息</p>
        <ul>
          <li>1、管理员添加客服后，客服需在1小时内点击邮件中的验证连接（图片）</li>
          <li>2、进入客服完善信息页，客服填入个人信息（图片）</li>
          <li>3、点击确定按钮，跳转至客服登录界面（图片）</li>
          <li>4、输入正确邮箱和密码，进入客服工作界面（图片）</li>
          <li>准备工作完成，可以开始你的回话啦！</li>
        </ul>
      </div>
      <div class='line'></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'web'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#app {
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  color: #2c3e50;
}
/*= font-size
-----------------------------------------------------------------*/

h1 {
  font-size: 3em;
  font-weight: normal;
}

h2 {
  font-size: 2.1em;
  font-weight: normal;
}

h3 {
  font-size: 1.8em;
  font-weight: normal;
}

h4 {
  font-size: 1em;
  font-weight: normal;
}

h5 {
  font-size: 0.5em;
  font-weight: normal;
}

p {
  font-size: 1.3em;
}

.guide li {
  font-size: 1.3em;
}
/*= main
-----------------------------------------------------------------*/

.main-content-head h1 {
  margin-bottom: 0;
}

.main-content-head {
  padding-bottom: 2em;
}

.main-content-body ul {
  list-style-type: disc;
  padding: 0.7em 1.3em;
}

.line {
  margin: 2em 0em;
  border: 1px solid #2a333b;
  border-top: 0px;
}

.guide a {
  color: #9d2933;
}
</style>
