<template>
<div id="app">
  <!-- Header -->
  <header class='header'>
    <h1 class='header-logo'><a>logo</a></h1>
    <ul class='header-menu'>
      <li class='header-item'><a href='./'>首页</a></li>
      <li class='header-item'><a href='./login'>登录</a></li>
      <li class='header-item'><a href='./register'>注册</a></li>
    </ul>
  </header>
  <!-- Main -->
  <section class='main'>
    <div class='main-content'>
      <div class='main-content-head'>
        <h1>Django documentation</h1>
        <p>Everything you need to know about Django.</p>
      </div>
      <div class='main-content-body'>
        <div class='guide'>
          <h2>How the documentation is organized</h2>
          <p>Django has a lot of documentation. A high-level overview of how it’s organized will help you know where to look for certain things:</p>
          <ul>
            <li>
              <p>Tutorials take you by the hand through a series of steps to create a Web application. Start here if you’re new to Django or Web application development. Also look at the “First steps” below.</p>
            </li>
            <li>
              <p>Topic guides discuss key topics and concepts at a fairly high level and provide useful background information and explanation.</p>
            </li>
            <li>
              <p>Reference guides contain technical reference for APIs and other aspects of Django’s machinery. They describe how it works and how to use it but assume that you have a basic understanding of key concepts.</p>
            </li>
            <li>
              <p>How-to guides are recipes. They guide you through the steps involved in addressing key problems and use-cases. They are more advanced than tutorials and assume some knowledge of how Django works.</p>
            </li>
          </ul>
        </div>
        <div class='line'></div>
        <div class='guide'>
          <h2>First steps</h2>
          <p>Are you new to Django or to programming? This is the place to start!</p>
          <ul>
            <li>From scratch: <a>Overview</a> | <a>Installation</a></li>
            <li>Tutorial: <a>Part 1: Requests and responses</a> | <a>Part 2: Models and the admin site</a> | <a>Part 3: Views and templates</a> | <a>Part 7: Customizing the admin site</a> | <a>Part 4: Forms and generic views</a> | <a>Part 5: Testing</a> | <a>Part 6: Static files</a></li>
            <li>Advanced Tutorials: <a>How to write reusable apps</a> | <a>Writing your first patch for Django</a></li>
          </ul>
        </div>
        <div class='line'></div>
        <div class='guide'>
          <h2>First steps</h2>
          <p>Are you new to Django or to programming? This is the place to start!</p>
          <ul>
            <li>From scratch: <a>Overview</a> | <a>Installation</a></li>
            <li>Tutorial: <a>Part 1: Requests and responses</a> | <a>Part 2: Models and the admin site</a> | <a>Part 3: Views and templates</a> | <a>Part 7: Customizing the admin site</a> | <a>Part 4: Forms and generic views</a> | <a>Part 5: Testing</a> | <a>Part 6: Static files</a></li>
            <li>Advanced Tutorials: <a>How to write reusable apps</a> | <a>Writing your first patch for Django</a></li>
          </ul>
        </div>
        <div class='line'></div>
      </div>
    </div>
  </section>
  <!-- SubFooter -->
  <section class='subfooter'>
    <div class='subfooter-container'>
      <div class='subfooter-container-box'>
        <h3>Learn More</h3>
        <ul>
          <li>About Django</li>
          <li>Getting Started with Django</li>
          <li>Team Organization</li>
          <li>Django Software Foundation</li>
          <li>Code of Conduct</li>
          <li>Diversity Statement</li>
        </ul>
      </div>
      <div class='subfooter-container-box'>
        <h3>Get Involved</h3>
        <ul>
          <li>Join a Group</li>
          <li>Contribute to Django</li>
          <li>Submit a Bug</li>
          <li>Report a Security Issue</li>
        </ul>
      </div>
      <div class='subfooter-container-box'>
        <h3>Follow Us</h3>
        <ul>
          <li>GitHub</li>
          <li>Twitter</li>
          <li>News RSS</li>
          <li>Django Users Mailing List</li>
        </ul>
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
  width: 100%;
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

.header-item:hover a{
  color: #9d2933;
}

.header a {
  color: #f9f9f9;
}

h1 {
  font-size: 2em;
}
h2 {
  font-size: 1.5em;
}

.main {
  padding: 0em 4em;
  padding-bottom: 4em;
}

.main-content-head h1 {
  margin-bottom: 0;
}

.main-content-head {
  padding-bottom: 1em;
}

.main-content-body ul {
  padding: 0 1.1em;
}

.line {
  margin: 2em 0em;
  border: 1px solid #2a333b;
  border-top: 0px;
}

.guide a{
  color: #9d2933;
}

.subfooter {
  background-color: #2a333b;
  color: #fff;
}

.subfooter-container {
  display: inline-flex;
}

.subfooter-container-box {
  width: 25em;
  padding-top: 1em;
  padding-bottom: 2em;
}

.subfooter-container-box h3 {
  padding-left: 4em;
}

.subfooter-container-box ul {
  list-style-type: none;
  padding: 0;
  padding-left: 5.3em;
  font-size: 0.9em;
}


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