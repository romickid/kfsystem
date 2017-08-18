<template>
  <div id='app'>
    <div class='main-content-head'>
      <h1>BIG5客服系统接入步骤一览</h1>
      <p>从此开始你的客服之路</p>
    </div>
    <div class='main-content-body'>
      <div class='guide'>
        <h2>First steps</h2>
        <p>创建系统</p>
        <ul>
          <li>1. 在BIG5首页（http://http://192.168.55.33:8000/main/）点击注册按钮，注册企业管理员账号（首页图片）</li>
          <li>2. 跳转至注册页面，填入个人信息，完成注册（注册页图片）</li>
          <li>3. 点击注册按钮，跳转至登录页面，填入刚刚注册的邮箱和密码，点击登录（登录页图片）</li>
          <li>4. 跳转至管理员界面，开始使用你的系统吧！（管理员页图片）</li>
        </ul>
      </div>
      <div class='line'></div>
      <div class='guide'>
        <h2>Second steps</h2>
        <p>功能使用</p>
        <ul>
          <li>系统创建后，可通过简单配置开始试用</li>
          <li>团队管理——配置客服（管理员页团队管理）</li>
          <li>添加客服: 点击添加客服按钮（添加按钮图片）</li>
          <li>在弹出的输入框中填入你要添加的客服邮箱，点击确定按钮（输入框图片）</li>
          <li>最新添加的客服已显示在客服人员列表中，今后您可以在此查看您所有的客服信息（客服列表图片）</li>
          <li>此时该客服状态为未验证，客服必须要经过验证后才能正常使用</li>
        </ul>
      </div>
      <div class='line'></div>
      <div class='guide'>
        <h2>Second steps</h2>
        <p>接入准备</p>
        <ul>
          <li>1. 引入客服团队，熟悉BIG5，为正式使用做准备</li>
          <li>2. 确定接入渠道用户端样式，在多渠道中完成配置:</li>
          <li>我们提供三种用户端的样式，分别是web、widget、mobile，点击可以查看相关配置（多渠道图片）</li>
          <li>3. 客服入口样式设计:</li>
          <li>确认各渠道需上线的页面在线客服的入口设置，引入设计师完成设计工作（企业页面图片）</li>
        </ul>
      </div>
      <div class='line'></div>
      <div class='guide'>
        <h2>Third steps</h2>
        <p>开发上线</p>
        <ul>
          <li>接入准备工作完成后，即可进入开发测试阶段</li>
          <li>上线后，注意观察和监控流量</li>
          <li>1. 可在概览中查看最近客服系统使用情况，供企业进行战略调整（概览图片）</li>
          <li>2. 可在客服列表中实时查看客服情况，包括在线情况和连接人数，随时调度（客服列表图片）</li>
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
