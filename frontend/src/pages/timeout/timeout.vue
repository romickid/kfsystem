<template>
  <div id="app">
    <Row class='content'>
      <i-col :xs="{ span: 0}" :md="{ span: 6, offset: 5 }" :lg="{ span: 6, offset: 5 }">
        <div class='picture'>
          <div class='left'>
            <p>OPPS! ERROR!</p>
          </div>
        </div>
      </i-col>
      <i-col :xs="{ span: 11, offset: 2 }" :lg="{ span: 11, offset: 2 }">
        <div class='right'>
          <h1>TimeOut</h1>
          <p>您的链接已失效，请重新申请</p>
          <i-button class='button' @click='home'>TAKE ME HOME</i-button>
        </div>
      </i-col>
    </Row>
  </div>
</template>

<script>
export default {
  name: 'app',
  methods: {
    /**
      * @description 返回主页
      */
    home () {
      window.location.href = '../main/'
    }
  }
}
</script>

<style>
#app {
  font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
  background-color: #f8f8f9;
  height: 100vh;
}

.content {
  padding-top: 10%;
  position: relative;
}

h1 {
  font-weight: bolder;
  font-size: 10em;
  color: #75664d;
}

.left {
  position: absolute;
  left: 10em;
  top: 1.5em;
  font-size: 1.3em;
  font-weight: bolder;
  color: #75664d;

}

.right p {
  font-size: 2em;
  font-weight: bolder;
  padding-bottom: 1em;
  color: #75664d;
}

.button {
  color: #75664d;
}

.picture {
  background-image: url('./images/timg.png');
  height: 25em;
  background-size: cover;
  background-position: center;
}



</style>