<template>
<div id="app">
  <!-- Header -->
  <div class="header">
    <div class="ceiling">
      <img src="./assets/logo.png" alt="" style="height:40px;width:40px">
      <img src="./assets/name.png" alt="" style="height:40px">
      <div class="ceiling-main">
        <a href="../main" class='ceiling-item'>首页</a> |
        <a href="../en_login" class='ceiling-item'>登录</a> |
        <a href="../en_folders" class='ceiling-item'>注册</a> |
        <a href="../se_login" class='ceiling-item'>客服入口</a>
      </div>
    </div>
  </div>
  <!-- Main -->
  <section class='main'>
    <Row type='flex'>
      <i-col span='16' class='main-content'>
        <router-view></router-view>
      </i-col>
      <i-col span='8' class='complementary'>
        <div class='complementary-box'>
          <h2>Support BIG5 !</h2>
          <div class='line'></div>
          <div class='support-us'>
            <img src='./assets/support.png' alt='点此支持' @click='supportModal=true' style='width: 60px; height: 60px;'>
            <p>
              BIG5在线客服系统<br>由南开大学软件学院2015级BIG5小组完成<br>如果您觉得这个项目有价值，请支持我们吧！！！<br>
              <Button type='text' @click='supportModal=true' style='padding-left: 0;'>点此支持</Button>
              <Modal v-model='supportModal' style='text-align: center;'>
                <p slot='header'></p>
                <img src='../../../static/support.jpeg' style='width: 300px;'>
                <div slot='footer'></div>
              </Modal>
          </div>
        </div>
        <div class='complementary-box'>
          <h2>Browse</h2>
          <div class='line'></div>
          <ul>
            <li class='browse'>Prev: <router-link :to='prevPage.router'>{{ prevPage.string }}</router-link></li>
            <li class='browse'>Next: <router-link :to='nextPage.router'>{{ nextPage.string }}</router-link></li>
          </ul>
        </div>
        <div class='complementary-box'>
          <h2>You are here:</h2>
          <div class='line'></div>
          <ul>
            <li class='you-are-here'>{{ youAreHere }}</li>
          </ul>
        </div>
        <div class='complementary-box'>
          <h2>Download:</h2>
          <div class='line'></div>
           <p class='download'><a href='https://se.jisuanke.com/custom-service/Group3' alt='BIG5 Customer Service System'>点此下载项目</a><br>Provided by jisuanke.</p>
        </div>
      </i-col>
    </Row>
  </section>
  <!-- SubFooter -->
  <section class='subfooter'>
    <Row class='subfooter-container'>
      <i-col span='7' class='subfooter-container-box'>
        <h3>我们的特色</h3>
        <ul>
          <li>智能机器人 24小时回复</li>
          <li>查看用户信息 让您更了解您的客户</li>
          <li>多渠道汇聚 全方面完善用户体验</li>
          <li>实时查看 资源有效分配</li>
          <li>一键接入 无需繁琐操作</li>
        </ul>
      </i-col>
      <i-col span='7' class='subfooter-container-box'>
        <h3>关于我们</h3>
        <ul>
          <li>组长：魏久骐</li>
          <li>组员：吴文竹</li>
          <li>组员：孙晓菲</li>
          <li>组员：黄侣淳</li>
          <li>组员：高小宸</li>
        </ul>
      </i-col>
      <i-col span='7' class='subfooter-container-box'>
        <h3>前端技术支持</h3>
        <ul>
          <li><a href='https://www.djangoproject.com/'>Django</a></li>
          <li><a href='https://cn.vuejs.org/'>Vue</a></li>
          <li><a href='https://www.iviewui.com/'>iview</a></li>
          <li><a href='https://github.com/think2011/localResizeIMG'>lrz</a></li>
        </ul>
      </i-col>
      <i-col span='3'>&nbsp</i-col>
    </Row>
  </section>
  <Back-top></Back-top>
  <!-- Footer -->
  <footer class="footer">
    <div class="footer-container">
      <div>
        &copy; Big5 - Customer Service System &nbsp2017 - 8&nbsp All rights reserved.<a></a>
      </div>
    </div>
  </footer>
</div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      supportModal: false,
      routerName: [
        {
          name: 'outline',
          router: '/',
          string: 'BIG5 在线客服系统 帮助文档大纲'
        },
        {
          name: 'access_guide',
          router: '/access_guide',
          string: 'BIG5客服系统接入步骤一览'
        },
        {
          name: 'web',
          router: '/web',
          string: '桌面网站web接入'
        },
        {
          name: 'widget',
          router: '/widget',
          string: '桌面网站widget接入'
        },
        {
          name: 'mobile',
          router: '/mobile',
          string: '移动网站web接入'
        },
        {
          name: 'user_info',
          router: '/user_info',
          string: '客户账户体系对接流程'
        },
        {
          name: 'robot_knowledegebase',
          router: '/robot_knowledegebase',
          string: '知识库语料标准'
        },
        {
          name: 'cs_set_robot',
          router: '/cs_set_robot',
          string: '设置机器人'
        },
        {
          name: 'cs_working',
          router: '/cs_working',
          string: '客服工作指南'
        },
        {
          name: 'cs_set_profile',
          router: '/cs_set_profile',
          string: '客服接入'
        },
        {
          name: 'addition_function',
          router: '/addition_function',
          string: '额外功能'
        }
      ],
      prevPage: {
        router: '',
        string: ''
      },
      nextPage: {
        router: '',
        string: ''
      }
    }
  },
  computed: {
    youAreHere () {
      for (let i = 0; i < this.routerName.length; i++) {
        if (this.$route.name === this.routerName[i].name) {
          if (i === 0) {
            this.prevPage.string = '无'
            this.nextPage.string = this.routerName[i + 1].string
            this.nextPage.router = this.routerName[i + 1].router
          } else if (i === this.routerName.length - 1) {
            this.prevPage.string = this.routerName[i - 1].string
            this.nextPage.string = '无'
            this.prevPage.router = this.routerName[i - 1].router
          } else {
            this.prevPage.string = this.routerName[i - 1].string
            this.prevPage.router = this.routerName[i - 1].router
            this.nextPage.string = this.routerName[i + 1].string
            this.nextPage.router = this.routerName[i + 1].router
          }
          return this.routerName[i].string
        }
      }
    }
  }
}
</script>

<style>
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
  font-size: 1.5em;
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

/*= header
-----------------------------------------------------------------*/

.header {
  position: relative;
  border: 1px solid #d7dde4;
  border-radius: 4px;
  overflow: hidden;
  z-index: 1;
}

.ceiling {
  background-color: #1c1d26;
  padding: 1em 0 0;
  overflow: hidden;
}

.ceiling-main {
  float: right;
  margin-right: 5em;
  padding-top: 1em;
}

.ceiling-main a {
  color: #9ba7b5;
  padding-left: 1.5em;
  padding-right: 1.5em;
}

.ceiling-item .document {
  color: #9d2933;
  border-bottom: 1px solid #9d2933;
}

.ceiling-item:hover {
  color: #9d2933;
  padding-bottom: 1em;
  border-bottom: 1px solid #9d2933;
}

/*= main
-----------------------------------------------------------------*/
.main {
  position: relative;
}

.main-content {
  padding: 2em 3em;
}

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

.complementary {
  background-color: #f8f8f9;
  padding: 3em 2em;
  padding-top: 0em;
}

.complementary-box {
  margin-top: 3em;
}

.complementary p {
  font-size: 1em;
}

.complementary h3 {
  font-weight: lighter;
}

.browse {
  padding: 1em;
}

.you-are-here {
  padding: 1em;
}

.download {
  padding: 1em;
}

.support-us {
  display: inline-flex;
}

.support-us p {
  padding-left: 2em;
}

/*= subfooter
-----------------------------------------------------------------*/

.subfooter {
  background-color: #2a333b;
  color: #fff;
  padding: 1em 0em;
  padding-bottom: 2em;
}

.subfooter-container-box {
  padding-left: 6%;
}

.subfooter-container-box ul {
  padding-top: 1em;
  font-size: 1em;
}

/*= footer
-----------------------------------------------------------------*/

.footer {
  background-color: #1c1d26;
  color: #f0f2f4;
  font-size: 0.5em;
  height: 4em;
  padding-top: 2.5em;
  width: 100%;
}

.footer-container {
  padding-left: 6.5em;
}
</style>