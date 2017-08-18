<template>
  <div id='app'>
    <div class='main-content-head'>
      <h1>桌面网站web接入</h1>
      <p>从此开始你的客服之路</p>
    </div>
    <div class='main-content-body'>
      <div class='guide'>
        <h2>桌面网站web接入样例（web样例）</h2>
      </div>
      <div class='line'></div>
      <div class='guide'>
        <h2>获取页面网址</h2>
        <p>在企业网站中嵌入web咨询页面的网址</p>
        <ul>
          <li>申请系统后，在多渠道-web中获取页面网址。（图片）</li>
        </ul>
      </div>
      <div class='line'></div>
      <div class='guide'>
        <h2>入口样式简介</h2>
        <p>企业可参考如下几种方式进行入口样式的设计</p>
        <ul>
          <li>1.banner样式（图片）</li>
          <li>2.文字链样式（图片）</li>
          <li>3.浮层样式（图片）</li>
        </ul>
      </div>
      <div class='line'></div>
      <div class='guide'>
        <h2>参数传递</h2>
        <p>用户信息参数传递规则 请参考<a></a></p>
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
