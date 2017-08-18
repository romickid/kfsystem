<template>
  <div id='app'>
    <div class='main-content-head'>
      <h1>BIG5 在线客服系统</h1>
      <p>Everything you need to know about BIG5.</p>
    </div>
    <div class='main-content-body'>
      <div class='guide'>
        <h2>How the documentation is organized</h2>
        <p></p>
        <ul>
          <li>
            接入指南
          </li>
          <li>
            用户手册
          </li>
          <li>
            智能机器人
          </li>
          <li>
            其它
          </li>
        </ul>
      </div>
      <div class='line'></div>
      <div class='guide'>
        <h2>接入指南</h2>
        <p>Are you new to Django or to programming? This is the place to start!</p>
        <ul>
          <li>BIG5客服系统接入步骤一览: <a>Overview</a></li>
          <li>桌面网站web接入: <a>Part 1: Requests and responses</a></li>
          <li>桌面网站widget接入: <a>How to write reusable apps</a></li>
          <li>移动网站mobile接入: <a>How to write reusable apps</a></li>
          <li>机器人API调用流程: <a>How to write reusable apps</a></li>
        </ul>
      </div>
      <div class='line'></div>
      <div class='guide'>
        <h2>用户手册</h2>
        <p>Are you new to Django or to programming? This is the place to start!</p>
        <ul>
          <li>人员角色及对应权限: <a>Overview</a> | <a>Installation</a></li>
          <li>在线人工: <a>Part 1: Requests and responses</a></li>
          <li>Advanced Tutorials: <a>How to write reusable apps</a> | <a>Writing your first patch for Django</a></li>
        </ul>
      </div>
      <div class='line'></div>
      <div class='guide'>
        <h2>用户手册</h2>
        <p>Are you new to Django or to programming? This is the place to start!</p>
        <ul>
          <li>人员角色及对应权限: <a>Overview</a> | <a>Installation</a></li>
          <li>在线人工: <a>Part 1: Requests and responses</a></li>
          <li>Advanced Tutorials: <a>How to write reusable apps</a> | <a>Writing your first patch for Django</a></li>
        </ul>
      </div>
      <div class='line'></div>
      <div class='guide'>
        <h2>智能机器人</h2>
        <p>Are you new to Django or to programming? This is the place to start!</p>
        <ul>
          <li>知识库语料标准: <a>Overview</a> | <a>Installation</a></li>
          <li>知识库管理: <a>Part 1: Requests and responses</a></li>
          <li>智能学习: <a>How to write reusable apps</a></li>
          <li>夜莺机器人API: <a>How to write reusable apps</a></li>
        </ul>
      </div>
      <div class='line'></div>
      <div class='guide'>
        <h2>其它</h2>
        <p>Are you new to Django or to programming? This is the place to start!</p>
        <ul>
          <li>客户账户体系对接流程: <a>Overview</a> | <a>Installation</a></li>
          <li>BIG5新建系统API文档: <a>Part 1: Requests and responses</a></li>
          <li>关闭会话数据推送API接口文档: <a>How to write reusable apps</a></li>
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
