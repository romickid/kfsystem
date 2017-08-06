<template>
<div id="app">
  <!-- Header -->
  <div class="header">
    <div class="ceiling">
      <a href='./'><img src="./assets/logo.png" alt=""></a>
      <div class="ceiling-main">
        <a class='ceiling-item mainpage'>首页</a> |
        <a href="#jump" class='ceiling-item'>产品介绍</a> |
        <a href="../documentation" class='ceiling-item'>帮助中心</a> |
        <a href="../en_login" class='ceiling-item'>登录</a> |
        <a href="../en_folders" class='ceiling-item'>注册</a> |
        <a href="../se_folders" class='ceiling-item'>客服入口</a>
      </div>
    </div>
  </div>
  <!-- Banner -->
  <section class='banner'>
    <div class='banner-content'>
      <h1>连接你的用户 高效你的客服</h1>
      <p>智能机器人 实时在线沟通 一键接入 多渠道汇聚</p>
    </div>
  </section>
  <!-- One -->
  <div id='jump'>
  </div>
  <section class='introduction-one'>
    <div class='introduction-one-content'>
      <h2>产品概述</h2>
      <div class='line'></div>
      <p>百度大数据环境下，依托于先进的业界技术，一群热爱互联网的年轻人抓住机遇，迎接挑战、只做业界最先进的客服平台-夜莺。</p>
      <p>我们一步一步加快产品迭代，现在夜莺有智能的会学习的机器人、全面数据可视化的在线人工操作并全面融合了微信、微博、app等用户访问渠道。智能、易用、安全是我们的所推崇的、省钱、方便、放心是夜莺能承诺的。</p>
    </div>
    <Row :gutter='48' class='one-row'>
      <i-col span='2'>&nbsp</i-col>
      <i-col span='5'>
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
      <i-col span='5'>
        <div class='one-row-box'>
        <div class='one-box-icon'>
          <Icon type="cloud" size=25></Icon>
        </div>
        <div class='one-box-content'>
          <h3>高效率人工</h3>
          <p>人机无缝衔接<br>用户问题自动分配<br>客服分级管理</p>
        </div>
        </div>
      </i-col>
      <i-col span='5'>
        <div class='one-row-box'>
        <div class='one-box-icon'>
          <Icon type="cloud" size=25></Icon>
        </div>
        <div class='one-box-content'>
          <h3>多渠道接入</h3>
          <p>web端<br>手机端<br>邮件</p>
        </div>
        </div>
      </i-col>
      <i-col span='5'>
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
      <i-col span='2'>&nbsp</i-col>
    </Row>
  </section>
  <!-- Two -->
  <section class='introduction-two'>
    <div class='introduction-two-text'>
      <h2>产品优势</h2>
      <div class="line"></div>
      <p>仿人脑的智能机器人、无缝转接在线人工、客服无障碍协同、客服管理实时监控、数据报表一键生成、百度亿级流量产品实战检验</p>
    </div>
    <Row class='introduction-two-box'>
      <i-col span='11'>
      <img src='./assets/about.jpg' alt=''>
      </i-col>
      <i-col span='1'>&nbsp</i-col>
      <i-col span='12' class='two-box-container'>
        <div class='two-box-header'>
          <h3>产品优势</h3>
          <p>仿人脑的智能机器人、无缝转接在线人工、客服无障碍协同、客服管理实时监控、数据报表一键生成、百度亿级流量产品实战检验</p>
        </div>
        <div class='line'></div>
        <div class='two-box-content'>
          <div class='row'>
            <div class="box-right-element">
              <div class='element1'>
                <div class="right-element-icon">
                  <Icon type="cloud" size=30></Icon>
                </div>
                <div class="right-element-text">
                  <h4>Plugin Development</h4>
                  <p>依托于业界领先的智能机器人技术，建立强大的语料知识库，随时响应用户的咨询问答</p>
                </div>
              </div>
            </div>
            <div class="box-right-element">
              <div class='element2'>
                <div class="right-element-icon">
                  <Icon type="cloud" size=30></Icon>
                </div>
                <div class="right-element-text">
                  <h4>Plugin Development</h4>
                  <p>依托于业界领先的智能机器人技术，建立强大的语料知识库，随时响应用户的咨询问答</p>
                </div>
              </div>
            </div>
          </div>
          <div class='row'>
            <div class="box-right-element">
              <div class='element3'>
                <div class="right-element-icon">
                  <Icon type="cloud" size=30></Icon>
                </div>
                <div class="right-element-text">
                  <h4>Plugin Development</h4>
                  <p>依托于业界领先的智能机器人技术，建立强大的语料知识库，随时响应用户的咨询问答</p>
                </div>
              </div>
            </div>
            <div class="box-right-element">
              <div class='element4'>
                <div class="right-element-icon">
                  <Icon type="cloud" size=30></Icon>
                </div>
                <div class="right-element-text">
                  <h4>Plugin Development</h4>
                  <p>依托于业界领先的智能机器人技术，建立强大的语料知识库，随时响应用户的咨询问答</p>
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
      <h2>产品概述</h2>
      <div class='line'></div>
      <p>百度大数据环境下，依托于先进的业界技术，一群热爱互联网的年轻人抓住机遇，迎接挑战、只做业界最先进的客服平台-夜莺。</p>
      <p>我们一步一步加快产品迭代，现在夜莺有智能的会学习的机器人、全面数据可视化的在线人工操作并全面融合了微信、微博、app等用户访问渠道。智能、易用、安全是我们的所推崇的、省钱、方便、放心是夜莺能承诺的。</p>
    </div>
  </section>
  <!--Four-->
  <section class='contact-us'>
    <div class='contact-us-container'>
      <div class='contact-content'>
        <div class='contact-content-box'>
          <h4>Who we are</h4>
          <img src="./assets/logo.png" alt="">
          <p>It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.</p>
        </div>
        <div class='contact-content-box'>
          <h4>Latest works</h4>
          <div class='lastest-works'>
            <span class='row'>
              <img src='./assets/place-1.jpg' alt=''/>
              <img src='./assets/place-2.jpg' alt=''/>
            </span>
            <span class='row'>
              <img src='./assets/place-3.jpg' alt=''/>
              <img src='./assets/place-4.jpg' alt=''/>
            </span>
          </div>
        </div>
        <div class='contact-content-box'>
          <h4>Get In Touch</h4>
          <p>The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters.</p>
          <div class='get-in-touch'>
            <ul>
              <li> 99 Green Street, White Plaza</li>
              <li> +1 123 456 8899</li>
              <li><a> info@dummy.com</a></li>
            </ul>
          </div>
        </div>
        <div class='contact-content-box'>
          <h4>Weekly Newsletter</h4>
          <p>As opposed to using 'Content here, content here', making it look like readable English.</p>
          <i-button type="button" class='button-register' @click='gotoregister'>REGISTER</i-button>
        </div>
      </div>
    </div>
  </section>
  <!-- Footer -->
  <footer class="footer">
    <div class="footer-container">
      <div>
        &copy; Big5 - Customer Service System &nbsp2017 - 8&nbsp All rights reserved. &nbsp&nbspDesign: Xiaochen Gao<a></a>
      </div>
    </div>
  </footer>
  <Back-top></Back-top>
</div>
</template>

<script>
export default {
  name: 'app',
  methods: {
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
}

/*= header
--------------------------------------------------------------------*/

.header {
  position: fixed;
  width: 100%;
  border-radius: 4px;
  overflow: hidden;
  z-index: 1;
}

.ceiling {
  background-color: #1c1d26;
  padding: 1em 0;
  overflow: hidden;
}

.ceiling a {
  margin-left: 1em;
}

.ceiling-main {
  float: right;
  margin-right: 5em;
  padding-top: 0.5em;
}

.ceiling-main a {
  color: #9ba7b5;
  padding-left: 1em;
  padding-right: 1em;

}

.ceiling-main .mainpage {
  color: #9d2933;
  border-bottom: 1px solid #9d2933;
}

.ceiling-item:hover {
  color: #9d2933;
  border-bottom: 1px solid #9d2933;
}

/*= banner
--------------------------------------------------------------------*/

.banner {
  position: relative;
  top: 3.3em;
  z-index: -1;
  background-image: url('./assets/slider02.jpg');
  height: 90vh;
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
  margin-top: 1em;
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
  margin-top: 4em;
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

.get-in-touch ul {
  list-style-type: none;
  padding: 0;
}

.get-in-touch li {
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

</style>