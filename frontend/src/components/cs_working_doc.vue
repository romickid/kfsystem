<template>
  <div id='app'>
    <div class='main-content-head'>
      <h1>客服工作指南</h1>
      <p>从此开始你的客服之路</p>
    </div>
    <div class='main-content-body'>
      <div class='guide'>
        <h2>开始聊天</h2>
        <p>当有用户接入时，客服可以开始会话</p>
        <ul>
          <li>1、用户点击转接人工客服后，系统自动转接至目前连接人数最少的在线客服</li>
          <li>2、客服收到用户接入，即可开始聊天（图片）</li>
          <li>3、当客服同时与多个活跃用户聊天时，未读用户消息会显示红色气泡（图片）</li>
        </ul>
      </div>
      <div class='line'></div>
      <div class='guide'>
        <h2>消息挂断</h2>
        <ul>
          <li>1、用户2分钟未发送任何消息系统将发送提示，超过5分钟未发送任何消息将挂断该会话（图片）</li>
          <li>2、当用户挂断消息后，客服与该用户的聊天将进入已挂断消息列表（图片）</li>
          <li>3、用户点击切换按钮，可以在活跃消息列表与已挂断消息列表间进行切换（图片）</li>
        </ul>
      </div>
      <div class='line'></div>
      <div class='guide'>
        <h2>查看历史消息</h2>
        <ul>
          <li>1、在聊天窗口，客服上拉消息框可以看到与该用户的当次聊天记录（图片）</li>
          <li>2、点击查看历史消息按钮，客服可以上拉消息框查看该用户与客服和智能机器人的所有消息记录（图片）</li>
        </ul>
      </div>
      <div class='line'></div>
      <div class='guide'>
        <h2>转接给其它客服</h2>
        <ul>
          <li>1、当该客服无法处理用户问题时可以选择转接给其他客服</li>
          <li>2、点击转接按钮，用户将被转接给另一个连接数最少的在线客服（图片）</li>
          <li>3、当消息转接后，客服将不再能看到该用户的任何消息（图片）</li>
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
