<template>
  <div id='app'>
    <div class='main-content-head'>
      <h1>额外功能</h1>
      <p>根据数据分析的结果，在机器人回答不正确的问题中，语料库的质量是占比最大的部分。因此保证语料库的质量是提高机器人的准确率至关重要的一环。</p>
    </div>
    <div class='main-content-body'>
      <div class='guide'>
        <h2>管理员概览</h2>
        <ul>
          <li>概览页面展现当前的系统概况，为监控人员、管理人员提供当日当前客服整体的一个概况，主要提供反应客服情况的主要数据，其中包含客服在线人数和人工处理中会话数</li>
        </ul>
      <div class='line'></div>
      <div class='guide'>
        <h2>找回密码</h2>
        <p>管理员与客服在忘记密码时都可以通过找回密码的功能来设置新密码</p>
        <ul>
          <li>在登录页面，点击忘记密码按钮
            <img src='./docPic/doc17.png'>
          </li>
          <li>输入注册邮箱，点击确定，验证连接将发送至注册邮箱</li>
          <li>点击验证连接，进入重置密码页
            <img src='./docPic/doc18.png'>
          </li>
          <li>输入新密码，点击确定，返回登录页，就可以使用新密码登录了</li>
        </ul>
      </div>
      <div class='line'></div>
      <div class='guide'>
        <h2>修改密码</h2>
        <p>管理员与客服都可以修改密码</p>
        <ul>
          <li>进入管理员页面或客服工作页面，将鼠标移至昵称处，选择修改密码项</li>
          <li>输入原密码与新密码，点击确定，即可修改密码</li>
        </ul>
      </div>
      <div class='line'></div>
      <div class='guide'>
        <h2>登出账号</h2>
        <p>管理员与客服都可以修改密码</p>
        <ul>
          <li>进入管理员页面或客服工作页面，将鼠标移至昵称处，选择登出项</li>
          <li>注意：若不登出账号直接关闭网页，下次进入将无需登录</li>
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
  font-size: 1.1em;
  padding: 1em 0em;
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

img {
  width: 600px;
  margin: 2em 0em;
}
</style>
