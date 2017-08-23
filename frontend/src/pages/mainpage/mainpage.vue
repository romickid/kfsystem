<template>
<div id="app">
  <!-- Header -->
  <div class="header">
    <div class="ceiling">
      <a href='./'><img src="./assets/name.png" alt="首页" style="height:40px"></a>
      <div class="ceiling-main">
        <a href='./' class='ceiling-item mainpage'>首页</a> |
        <a href="#jump" class='ceiling-item'>产品介绍</a> |
        <a href="../documentation" class='ceiling-item'>帮助中心</a> |
        <a href="../en_login" class='ceiling-item'>企业登录</a> |
        <a href="../en_folders" class='ceiling-item'>企业注册</a> |
        <a href="../se_login" class='ceiling-item'>客服入口</a>
      </div>
    </div>
  </div>
  <!-- Banner -->
  <section class='banner'>
    <div class='banner-content'>
      <h1 style='font-family: "楷体","楷体_GB2312";'>连接你的用户 高效你的客服</h1>
      <p style='font-family: "楷体","楷体_GB2312";'>智能机器人 实时在线沟通 一键接入 多渠道汇聚</p>
    </div>
  </section>
  <div class='jump'>
    <a href="#jump"><Icon type="chevron-down"></Icon></a>
  </div>
  <!-- One -->
  <div id='jump'>
  </div>
  <section class='introduction-one'>
    <div class='introduction-one-content'>
      <h2>产品介绍</h2>
      <div class='line'></div>
      <p>强大的功能支撑，企业客服更轻松
        <br>让企业快速拥有互联网全渠道在线咨询功能，让客户可快速的通过互联网联系到企业
        <br>清晰直观的工作台，强大的客户管理，实时监控平台，知识库，智能聊天机器人，寒暄、业务咨询完美支持都是我们的优势
      </p>
    </div>
    <Row class='one-row'>
      <i-col :xs='boxOne.xs' :sm='boxOne.sm' :md='boxOne.md' :lg='boxOne.lg'>
        <div class='one-row-box'>
        <div class='one-box-icon'>
          <Icon type="cloud" size=25></Icon>
        </div>
        <div class='one-box-content'>
          <h3>机器人应答</h3>
          <p>7*24小时全天候服务<br>自定义语料库量身定制<br>大幅降低人工成本</p>
        </div>
        </div>
      </i-col>
      <i-col :xs='boxTwo.xs' :sm='boxTwo.sm' :md='boxTwo.md' :lg='boxTwo.lg'>
        <div class='one-row-box'>
        <div class='one-box-icon'>
          <Icon type="cloud" size=25></Icon>
        </div>
        <div class='one-box-content'>
          <h3>高效率人工</h3>
          <p>人机无缝衔接<br>用户自动分配<br>客服高效管理</p>
        </div>
        </div>
      </i-col>
      <i-col :xs='boxThree.xs' :sm='boxThree.sm' :md='boxThree.md' :lg='boxThree.lg'>
        <div class='one-row-box'>
        <div class='one-box-icon'>
          <Icon type="cloud" size=25></Icon>
        </div>
        <div class='one-box-content'>
          <h3>多渠道接入</h3>
          <p>桌面web<br>移动web<br>桌面嵌入式</p>
        </div>
        </div>
      </i-col>
      <i-col :xs='boxFour.xs' :sm='boxFour.sm' :md='boxFour.md' :lg='boxFour.lg'>
        <div class='one-row-box'>
        <div class='one-box-icon'>
          <Icon type="cloud" size=25></Icon>
        </div>
        <div class='one-box-content'>
          <h3>实时管理</h3>
          <p>权限责任分明<br>客服资源合理配置<br>问题适时调度</p>
        </div>
        </div>
      </i-col>
    </Row>
  </section>
  <!-- Two -->
  <section class='introduction-two'>
    <div class='introduction-two-text'>
      <h2>产品优势</h2>
      <div class="line"></div>
      <p>仿人脑的智能机器人、无缝转接在线人工、客服无障碍协同、客服管理实时监控、数据报表一键生成</p>
    </div>
    <Row class='introduction-two-box'>
      <i-col span='11'>
      <img src='./assets/about.png' alt=''>
      </i-col>
      <i-col span='1'>&nbsp</i-col>
      <i-col span='12' class='two-box-container'>
        <div class='two-box-header'>
          <h3>BIG5带来更丰富的沟通方式</h3>
          <p>多种沟通方式，为客户考虑周到，提升满意度。界面清晰 | 操作简单，图片、表情、文字一应俱全</p>
        </div>
        <div class='line'></div>
        <div class='two-box-content'>
          <div class='row'>
            <div class="box-right-element">
              <div class='element1'>
                <div class="right-element-icon">
                  <Icon type="image" size=30></Icon>
                </div>
                <div class="right-element-text">
                  <h4>图片</h4>
                  <p>双向图片传输，压缩上传，与客服斗图不再是梦想</p>
                </div>
              </div>
            </div>
            <div class="box-right-element">
              <div class='element2'>
                <div class="right-element-icon">
                  <Icon type="android-happy" size=30></Icon>
                </div>
                <div class="right-element-text">
                  <h4>表情</h4>
                  <p>选用当前最流行的emoji－picker，可选种类多，样式丰富</p>
                </div>
              </div>
            </div>
          </div>
          <div class='row'>
            <div class="box-right-element">
              <div class='element3'>
                <div class="right-element-icon">
                  <Icon type="edit" size=30></Icon>
                </div>
                <div class="right-element-text">
                  <h4>文字</h4>
                  <p>支持多行输入，多空格输入，让您的用户使用更友好</p>
                </div>
              </div>
            </div>
            <div class="box-right-element">
              <div class='element4'>
                <div class="right-element-icon">
                  <Icon type="scissors" size=30></Icon>
                </div>
                <div class="right-element-text">
                  <h4>截图</h4>
                  <p>用户嵌入式支持当前页面截图，让客服更了解用户</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </i-col>
    </Row>
  </section>
  <!-- Three -->
  <section class='introduction-three'>
    <div class='introduction-three-content'>
      <h2>BIG5 在线客服系统</h2>
      <div class='line'></div>
      <p>多样化的沟通功能，客户随时享受专业服务&nbsp&nbsp&nbsp全方位数据分析，客服管理游刃有余&nbsp&nbsp&nbsp全方面展示客户信息，让服务更懂客户
        <br>依托于先进的业界技术，一群热爱互联网的年轻人抓住机遇，迎接挑战、只做业界最先进的客服平台-BIG5。
      </p>
    </div>
  </section>
  <!--Four-->
  <section class='contact-us'>
    <div class='contact-us-container'>
      <div class='contact-content'>
        <div class='contact-content-box' style="padding-left: 0;">
          <h4>&nbsp</h4>
          <img src="./assets/logo.png" alt="">
        </div>
        <div class='contact-content-box' style="margin-left: 8em;">
          <h4>技术支持</h4>
          <div class='lastest-works'>
            <span class='row'>
              <a href='https://cn.vuejs.org/'><img src='./assets/place-3.png' alt=''/></a>
              <a href='https://www.iviewui.com/'><img src='./assets/place-2.png' alt=''/></a>
            </span>
            <span class='row'>
              <a href='https://www.djangoproject.com/'><img src='./assets/place-1.png' alt=''/></a>
              <a href='http://html2canvas.hertzen.com/'><img src='./assets/place-4.jpeg' alt=''/></a>
            </span>
          </div>
        </div>
        <div class='contact-content-box'>
          <h4>联系我们</h4>
          <div class='get-in-touch'>
            <ul>
              <li>南开大学软件学院</li>
              <li>+86 15822558489</li>
              <li>big5_nankai@163.com</li>
            </ul>
          </div>
        </div>
        <div class='contact-content-box'>
          <h4>心动不如行动</h4>
          <ul>
            <li>现在选择BIG5<br>让你的每一位客户更满意</li>
          </ul>
          <i-button type="button" class='button-register' @click='gotoregister'>跑去注册！</i-button>
        </div>
      </div>
    </div>
  </section>
  <!-- Footer -->
  <footer class="footer">
    <div class="footer-container">
      <div>
        &copy; Big5 - Customer Service System &nbsp2017 - 8&nbsp All rights reserved.<a></a>
      </div>
    </div>
  </footer>
  <Back-top></Back-top>
</div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      boxOne: {
        lg: {
          span: 4,
          offset: 1
        },
        md: {
          span: 4,
          offset: 1
        },
        sm: {
          span: 8,
          offset: 3
        },
        xs: {
          span: 16,
          offset: 4
        }
      },
      boxTwo: {
        lg: {
          span: 4,
          offset: 2
        },
        md: {
          span: 4,
          offset: 2
        },
        sm: {
          span: 8,
          offset: 2
        },
        xs: {
          span: 16,
          offset: 4
        }
      },
      boxThree: {
        lg: {
          span: 4,
          offset: 2
        },
        md: {
          span: 4,
          offset: 2
        },
        sm: {
          span: 8,
          offset: 3
        },
        xs: {
          span: 16,
          offset: 4
        }
      },
      boxFour: {
        lg: {
          span: 4,
          offset: 2
        },
        md: {
          span: 4,
          offset: 2
        },
        sm: {
          span: 8,
          offset: 2
        },
        xs: {
          span: 16,
          offset: 4
        }
      }
    }
  },
  methods: {
    /**
      * @description 前往登录页面
      */
    gotoregister () {
      window.location.href = './en_folders'
    }
  }
}
</script>

<style>
#app {
  font-family: "Helvetica Neue", Helvetica,"PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  color: #2c3e50;
  position: relative;
  margin: 0 auto;
}

/*= font-size
--------------------------------------------------------------------*/

h1 {
  font-size: 3em;
}

h2 {
  font-size: 2em;
}

h3 {
  font-size: 1.5em;
}

h4 {
  font-size: 1em;
}

h5 {
  font-size: 0.5em;
}

p {
  font-size: 1.2em;
  line-height: 1.5em;
}

/*= header
--------------------------------------------------------------------*/

.header {
  position: fixed;
  width: 100%;
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
  padding-top: 0.6em;
}

.ceiling-main a {
  color: #9ba7b5;
  padding-left: 1em;
  padding-right: 1em;
  font-size: 11pt;
}

.ceiling-main .mainpage {
  color: #9d2933;
}

.ceiling-item:hover {
  color: #9d2933;
}

/*= banner
--------------------------------------------------------------------*/

.banner {
  position: relative;
  top: 3.3em;
  z-index: -1;
  background-image: url('./assets/slider02.jpg');
  height: 95vh;
  background-color: #FFF;
  background-position: center;
  background-size: cover;
  overflow: hidden;
}

.banner-content {
  color: #f9f9f9;
  text-align: right;
  margin-top: 15%;
  margin-right: 6%;
}

.banner-content h1 {
  font-size: 4em;
}

.banner-content p {
  font-size: 1.5em;
}

/*= one
--------------------------------------------------------------------*/

.introduction-one {
  background-color: #f0f2f4;
  text-align: center;
  padding-bottom: 6em;
  padding-left: 6em;
  padding-right: 6em;
  position: relative;
  overflow: hidden;
}

.introduction-one-content h2 {
  margin-bottom: 0;
  padding-top: 4em;
}

.line {
background: #1ABB9C;
width: 55px;
height: 1px;
margin: 20px auto 40px;
}

.introduction-one-content p {
  margin-top: 2em;
  margin-bottom: 2em;
}

.one-row-box {
  background: #fff;
}

.one-box-icon {
  padding-top: 1em;
}

.one-box-content h3 {
  margin-top: 0;
  padding-bottom: 0.5em;
}

.one-row-box:hover {
  background:#1ABB9C;
  color:#fff;
}

.one-box-content {
  padding-bottom: 1em;
  padding-top: 0.5em;
}

.one-row {
  padding-top: 2em;
}

/*= two
--------------------------------------------------------------------*/

.introduction-two {
  text-align: center;
  overflow: hidden;
}

.introduction-two-text {
  margin-top: 3em;
  margin-bottom: 5em;
}

.introduction-two-box {
  text-align: left;
}

.introduction-two-box img {
  width: 100%;
}

.two-box-container {
  text-align: left;
}

.two-box-container h3 {
  margin-top: 0;
  margin-bottom: 0.4em
}

.two-box-container p {
  font-size: 0.9em;
  padding-right: 3em;
}

 .two-box-container .row {
  display: inline-flex;
  padding-bottom: 15%;
}

.right-element-icon {
  float: left;
  padding-right: 1em;
}

/*= three
--------------------------------------------------------------------*/

.introduction-three {
  background-color: #2a333b;
  text-align: center;
  padding: 10em 10em;
  padding-top: 8em;
  color: #f9f9f9;
  overflow: hidden;
}

/*= four
--------------------------------------------------------------------*/

.contact-us {
  background-color: #f0f2f4;
  width: 100%;
  padding-bottom: 5%;
  padding-top: 3%;
  overflow: hidden;
}

.contact-content {
  display: inline-flex;
}

.contact-content-box {
  width: 25%;
  height: 15em;
  padding: 2em 3em;
}

.lastest-works img {
  width: 6em;
  height: 5em
}

.lastest-works .row {
  display: inline-flex;
  padding-bottom: 5%;
}

.contact-us ul {
  list-style-type: none;
  padding: 0;
}

.contact-us li {
  padding-top: 0.2em;
}

.contact-content-box button {
  color: #fff;
  background-color: #1ABB9C;
  margin-top: 1em;
}

.contact-content-box h4 {
  padding-bottom: 3%;
}

/*= footer
--------------------------------------------------------------------*/

.footer {
  background-color: #2a333b;
  color: #f0f2f4;
  font-size: 0.5em;
  height: 4em;
  padding-top: 1.5em;
  width: 100%;
}

.footer-container {
  padding-left: 3em;
}

.jump {
  text-align: center;
  font-size: 2em;
}

.jump a {
  color: #e9eaec;
}

.jump a:hover {
  color: #fff;
}
</style>