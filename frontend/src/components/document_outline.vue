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
            接入指南：面向企业管理员，解答接入BIG5在线客服系统的诸多问题
          </li>
          <li>
            用户手册：面向企业客服，解答客服使用系统中遇到的问题
          </li>
          <li>
            智能机器人：介绍机器人知识库的构建标准
          </li>
          <li>
            其它：系统的部分功能介绍
          </li>
        </ul>
      </div>
      <div class='line'></div>
      <div class='guide'>
        <h2>接入指南</h2>
        <p>Are you new to BIG5? This is the place to start!</p>
        <ul>
          <li><router-link to='/access_guide'>BIG5客服系统接入步骤一览</router-link></li>
          <li><router-link to='/web'>桌面网站web接入</router-link></li>
          <li><router-link to='/widget'>桌面网站widget接入</router-link></li>
          <li><router-link to='/mobile'>移动网站mobile接入</router-link></li>
          <li><router-link to='/user_info'>客户账户体系对接流程</router-link></li>
        </ul>
      </div>
      <div class='line'></div>
      <div class='guide'>
        <h2>用户手册</h2>
        <p>供给客服人员的专业指南</p>
        <ul>
          <li><router-link to='/cs_working'>客服工作指南</router-link></li>
          <li><router-link to='/cs_set_profile'>客服人员接入</router-link></li>
          <li><router-link to='/cs_set_robot'>设置机器人</router-link></li>
        </ul>
      </div>
      <div class='line'></div>
      <div class='guide'>
        <h2>智能机器人</h2>
        <p>智能机器人，解放80%的人力资源</p>
        <ul>
          <li><router-link to='/robot_knowledegebase'>知识库语料标准</router-link></li>
        </ul>
      </div>
      <div class='line'></div>
      <div class='guide'>
        <h2>其它</h2>
        <p>人性化客服系统，提高客服效率</p>
        <ul>
          <li><router-link to='/addition_function'>部分功能介绍</router-link></li>
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
