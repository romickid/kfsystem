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
        <a href="../se_folders" class='ceiling-item'>客服入口</a>
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
          <h2>Support Django!</h2>
          <div class='line'></div>
          <div class='support-us'>
            <img src='./assets/support.png' alt=''>
            <p>Henrik Ossipoff Hansen donated to the Django Software Foundation to support Django development. Donate today!
            </p>
          </div>
        </div>
        <div class='complementary-box'>
          <h2>Browse</h2>
          <div class='line'></div>
          <ul>
            <li class='browse'>Prev: <a>Django documentation contents</a></li>
            <li class='browse'>Next: <a>Getting started</a></li>
            <li class='browse'><a>Table of contents</a></li>
            <li class='browse'><a>General Index</a></li>
            <li class='browse'><a>Python Module Index</a></li>
          </ul>
        </div>
        <div class='complementary-box'>
          <h2>You are here:</h2>
          <div class='line'></div>
          <ul>
            <li class='you-are-here'>Django documentation contents</li>
          </ul>
        </div>
        <div class='complementary-box'>
          <h2>Getting help</h2>
          <div class='line'></div>
          <ul>
            <li class='getting-help'>
              <h3>FAQ</h3>
              <p>Try the FAQ — it's got answers to many common questions.</p>
            </li>
            <li class='getting-help'>
              <h3>FAQ</h3>
              <p>Try the FAQ — it's got answers to many common questions.</p>
            </li>
            <li class='getting-help'>
              <h3>FAQ</h3>
              <p>Try the FAQ — it's got answers to many common questions.</p>
            </li>
          </ul>
        </div>
        <div class='complementary-box'>
          <h2>Download:</h2>
          <div class='line'></div>
          <p class='download'>Offline (Django 1.11): <a>HTML</a> | <a>PDF</a><br>Provided by Read the Docs.</p>
        </div>
      </i-col>
    </Row>
  </section>
  <!-- SubFooter -->
  <section class='subfooter'>
    <Row class='subfooter-container'>
      <i-col span='7' class='subfooter-container-box'>
        <h3>Learn More</h3>
        <ul>
          <li>About Django</li>
          <li>Getting Started with Django</li>
          <li>Team Organization</li>
          <li>Django Software Foundation</li>
          <li>Code of Conduct</li>
          <li>Diversity Statement</li>
        </ul>
      </i-col>
      <i-col span='7' class='subfooter-container-box'>
        <h3>Get Involved</h3>
        <ul>
          <li>Join a Group</li>
          <li>Contribute to Django</li>
          <li>Submit a Bug</li>
          <li>Report a Security Issue</li>
        </ul>
      </i-col>
      <i-col span='7' class='subfooter-container-box'>
        <h3>Follow Us</h3>
        <ul>
          <li>GitHub</li>
          <li>Twitter</li>
          <li>News RSS</li>
          <li>Django Users Mailing List</li>
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
        &copy; Big5 - Customer Service System &nbsp2017 - 8&nbsp All rights reserved. &nbsp&nbspDesign: Xiaochen Gao<a></a>
      </div>
    </div>
  </footer>
</div>
</template>

<script>
export default {
  name: 'app'
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

.ceiling a {
  margin-left: 1em;
}

.ceiling-main {
  float: right;
  margin-right: 5em;
  padding-top: 1em;
}

.ceiling-main a {
  color: #9ba7b5;
  padding-left: 1em;
  padding-right: 1em;

}

.ceiling-item .document {
  color: #9d2933;
  border-bottom: 1px solid #9d2933;
}

.ceiling-item:hover {
  color: #9d2933;
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
  padding: 6em 2em;
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

.getting-help {
  padding: 1em;
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
  font-size: 1.2em;
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