<template>
  <div id='app'>
    <div class='main-content-head'>
      <h1>桌面网站widget接入</h1>
      <p>从此开始你的客服之路</p>
    </div>
    <div class='main-content-body'>
      <div class='guide'>
        <h2>桌面网站widget接入样例</h2>
      </div>
      <div class='line'></div>
      <div class='guide'>
        <h2>widget咨询页面接入说明</h2>
        <p>将script代码嵌入企业网站</p>
        <ul>
          <li>1. 申请系统后，在多渠道-桌面网站-widget中查看</li>
          <li>2. 将对应代码嵌入到前端页面中</li>
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
