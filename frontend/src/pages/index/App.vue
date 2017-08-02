<template>
<div id="app">
  <!-- Header -->
  <header class='header'>
    <h1 class='header-logo'><a>logo</a></h1>
    <ul class='header-menu'>
      <li class='header-item'><a href='./'>首页</a></li>
      <li class='header-item'><a href='./product'>产品介绍</a></li>
      <li class='header-item'><a href='./help'>帮助中心</a></li>
      <li class='header-item'><a href='./login'>登录</a></li>
      <li class='header-item'><a href='./register'>注册</a></li>
    </ul>
  </header>
  <!-- Banner -->
  <section class='banner'>
      <img src="./assets/slider02.jpg"  alt="" />
    <div class='banner-content'>
      <h1>连接你的用户 高效你的客服</h1>
      <p>智能机器人 实时在线沟通 一键接入 多渠道汇聚</p>
      <a>立即加入我们</a>
    </div>
  </section>
  <!-- One -->
  <div id='jump1' class='jumper'>
  </div>
  <section class='introduction-one'>
    <div class='introduction-one-content'>
      <h2>产品概述</h2>
      <div class='line'></div>
      <p>百度大数据环境下，依托于先进的业界技术，一群热爱互联网的年轻人抓住机遇，迎接挑战、只做业界最先进的客服平台-夜莺。</p>
      <p>我们一步一步加快产品迭代，现在夜莺有智能的会学习的机器人、全面数据可视化的在线人工操作并全面融合了微信、微博、app等用户访问渠道。智能、易用、安全是我们的所推崇的、省钱、方便、放心是夜莺能承诺的。</p>
    </div>
    <div class='introduction-one-row'>
      <div class='one-row-box'>
        <div>
        <div class='one-box-icon'>
          <span class="fa fa-trophy">logo</span>
        </div>
        <div class='one-box-content'>
          <h3>机器人应答</h3>
          <p>7*24小时全天候服务<br>自定义语料库量身定制<br>大幅降低人工成本</p>
        </div>
        </div>
      </div>
      <div class='one-row-box'>
        <div>
        <div class='one-box-icon'>
          <span class="fa fa-trophy">logo</span>
        </div>
        <div class='one-box-content'>
          <h3>高效率人工</h3>
          <p>人机无缝衔接<br>用户问题自动分配<br>客服分级管理</p>
        </div>
        </div>
      </div>
      <div class='one-row-box'>
        <div>
        <div class='one-box-icon'>
          <span class="fa fa-trophy">logo</span>
        </div>
        <div class='one-box-content'>
          <h3>多渠道接入</h3>
          <p>web端<br>手机端<br>邮件</p>
        </div>
        </div>
      </div>
      <div class='one-row-box'>
        <div>
        <div class='one-box-icon'>
          <span class="fa fa-trophy">logo</span>
        </div>
        <div class='one-box-content'>
          <h3>实时管理</h3>
          <p>权限责任分明<br>客服资源合理配置<br>问题适时调度</p>
        </div>
        </div>
      </div>
    </div>
  </section>
  <!-- Two -->
  <section class='introduction-two'>
    <div class='introduction-two-text'>
      <h2>产品优势</h2>
      <div class="line"></div>
      <p>仿人脑的智能机器人、无缝转接在线人工、客服无障碍协同、客服管理实时监控、数据报表一键生成、百度亿级流量产品实战检验</p>
    </div>
    <div class='introduction-two-box'>
      <span>
      <img src='./assets/about.jpg' alt=''>
      </span>
      <div class='two-box-container'>
        <div class='two-box-header'>
          <h3>产品优势</h3>
          <p>仿人脑的智能机器人、无缝转接在线人工、客服无障碍协同、客服管理实时监控、数据报表一键生成、百度亿级流量产品实战检验</p>
          <div class='line'></div>
          <div class='two-box-text'>
          <p>仿人脑的智能机器人、无缝转接在线人工、客服无障碍协同、客服管理实时监控、数据报表一键生成、百度亿级流量产品实战检验</p>
          <p>仿人脑的智能机器人、无缝转接在线人工、客服无障碍协同、客服管理实时监控、数据报表一键生成、百度亿级流量产品实战检验</p>
          <p>仿人脑的智能机器人、无缝转接在线人工、客服无障碍协同、客服管理实时监控、数据报表一键生成、百度亿级流量产品实战检验</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  color: #2c3e50;
}

.header {
  background-color: #1c1d26;
  position: fixed;
  width: 100%;
  z-index: 1;
}

.header-logo {
  display: inline;
  padding-left: 2em;
}

.header-menu {
  display: inline;
  float: right;
  padding-right: 2em;
}

.header-item {
  display: inline;
  padding-left: 1em;
  padding-right: 1em;
}

.header a {
  color: #f9f9f9;
}

.banner {
  position: relative;
  top: 3em;
  z-index: -1;
}

.banner img {
  width: 100%;
}

.banner-content {
  color: #f9f9f9;
  text-align: right;
  position: absolute;
  top: 10em;
  left: 38em;
}

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

.introduction-one {
  background-color: #f0f2f4;
  text-align: center;
  padding-bottom: 6em;
  padding-left: 6em;
  padding-right: 6em;
  position: relative;
}

.introduction-one-content h2{
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
  display: inline-block;
  padding: 2em 0em;
  margin: 0 2em;
  margin-top: 2em;
}

.one-row-box:hover {
  background:#1ABB9C;
  color:#fff;
}

.one-box-content {
  padding: 1em;
}

.introduction-two {
  text-align: center;
}

.introduction-two-text {
  margin-top: 3em;
  margin-bottom: 5em;
}

.introduction-two-box {
  text-align: left;
  position: relative;
}

.introduction-two-box span{
  position: absolute;
}

.introduction-two-box img {
  width: 42em;
}

.two-box-container {
  text-align: left;
  position: absolute;
  left: 44em;
}

.two-box-container p {
  font-size: 0.9em;
  padding-right: 3em;
}

.two-box-text p {
  padding-top: 1.5em;
}

.element1 {
  position: absolute;
  top: 8em;
  left: 3em;
  padding-right: 22em;
}

.element2 {
  position: absolute;
  top: 8em;
  left: 23em;
  padding-right: 2em;
}

.element3 {
  position: absolute;
  top: 19em;
  left: 3em;
  padding-right: 22em;
}

.element4 {
  position: absolute;
  top: 19em;
  left: 23em;
  padding-right: 2em;
}

.right-element-icon {
  position : relative;
  top: 1.2em;
  right: 3em;
}

.introduction-three {
  position: absolute;
  right: 0;
  left: 0;
}

</style>