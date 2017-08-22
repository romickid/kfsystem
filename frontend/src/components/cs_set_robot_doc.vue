<template>
  <div id='app'>
    <div class='main-content-head'>
      <h1>设置机器人</h1>
      <p>从此开始你的客服之路</p>
    </div>
    <div class='main-content-body'>
      <div class='guide'>
        <h2>添加语料</h2>
        <p>企业语料库：添加企业专用语料，提高机器人服务率，降低人工成本</p>
        <ul>
          <li>1. 进入客服工作页面后，点击昵称－机器人－添加语料按钮
            <img src='./docPic/doc14.png'>
          </li>
          <li>2. 客服可以添加问题、回答、关键词及权重</li>
          <li>3、问题限制100字，回答限500字，关键词应为问题中包含的词汇，权重有高、中、低三档</li>
        </ul>
      </div>
      <div class='line'></div>
      <div class='guide'>
        <h2>查看语料</h2>
        <ul>
          <li>1. 进入客服工作页面后，点击昵称－机器人－查看语料按钮
            <img src='./docPic/doc15.png'>
          </li>
          <li>2. 显示企业当前所有已添加语料，客服可进行查看与删除操作</li>
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
