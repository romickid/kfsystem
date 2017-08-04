<template>
  <div class="container">
    <div class="sidebar">
      <div class="m-card">
        <header>
          <img class="user-avatar" width="40" height="40" :alt="user.name" :src="user.image">
          <p class="user-name">{{ user.name }}</p>
        </header>
      </div>
      <div>
        <ul class="m-ul">
          <li class="m-list" v-for="item in userList"  :class="{ choosed: session.userId === item.id }" @click="select(item)">
            <a><img class="m-avatar"  width="30" height="30" :alt="item.name" :src="item.image">
              <p class="m-name">{{ item.name }}</p></a>
          </li>
        </ul>
      </div>
    </div>
    <div class="main">
      <div class="m-message" v-scroll-bottom="session.messages">
        <ul>
          <li class="message-list" v-for="item in session.messages">
            <p class="message-time"><span class="time-span">{{ item.date | time }}</span></p>
            <div class="massage-main" :class="{ self: item.self }">
              <img class="massage-avatar" width="30" height="30" :src="item.image"/>
              <div class="massage-text"><li>{{ item.text }}</li></div>
            </div>
          </li>
        </ul>
      </div>
      <div class="m-menu">
        <button class="human-service">人工客服</button>
      </div>
      <div class="m-text">
        <textarea class="textarea" placeholder="按 Ctrl + Enter 发送" v-model="text" @keyup="inputing"></textarea>
        <button class="submit-button" @click="buttoninputing">发送</button>
      </div>
    </div>
  </div>
</template>

<script>
const key = 'VUE-Customer1'
// 虚拟数据
if (!localStorage.getItem(key)) {
  let now = new Date()
  let userData = {
    // 登录用户
    user: {
      id: 1,
      name: 'coffce',
      image: '../../../static/1.jpg'
    },
    // 用户列表
    userList: [
      {
        id: 2,
        name: 'MonsterSXF',
        image: '../../../static/2.png'
      }
    ],
    // 会话列表
    sessionList: [
      {
        userId: 2,
        messages: [
          {
            text: 'Hello，这是一个基于Vue + Webpack构建的简单chat示例，聊天记录保存在localStorge。简单演示了Vue的基础特性和webpack配置。',
            date: now,
            image: '../../../static/2.png'
          },
          {
            text: '项目地址: https://sc.chinaz.com/jiaoben/',
            date: now,
            image: '../../../static/2.png'
          }
        ]
      }
    ]
  }
  localStorage.setItem(key, JSON.stringify(userData))
}
export default {
  el: '#chat',
  data () {
    let dataserver = JSON.parse(localStorage.getItem(key))
    return {
      // 登录用户
      user: dataserver.user,
      // 用户列表
      userList: dataserver.userList,
      // 会话列表
      sessionList: dataserver.sessionList,
      // 选中的会话Index
      sessionIndex: 0,
      // 文本框中输入的内容
      text: ''
    }
  },
  computed: {
    session () {
      return this.sessionList[this.sessionIndex]
    }
  },
  watch: {
    // 每当sessionList改变时，保存到localStorage中
    sessionList: {
      deep: true,
      handler () {
        localStorage.setItem(key, JSON.stringify({
          user: this.user,
          userList: this.userList,
          sessionList: this.sessionList
        }))
      }
    }
  },
  methods: {
    inputing (e) {
      if (e.ctrlKey && e.keyCode === 13 && this.text.length) {
        this.session.messages.push({
          text: this.text,
          date: new Date(),
          self: true,
          image: this.user.image
        })
        this.text = ''
      }
    },
    buttoninputing (e) {
      if (this.text.length !== 0) {
        this.session.messages.push({
          text: this.text,
          date: new Date(),
          self: true,
          image: this.user.image
        })
        this.text = ''
      }
    }
  },
  filters: {
    search (list) {
      let arr = []
      for (var i = 0; i < list.length; i++) {
        if (list[i].name.indexOf(this.searchname) > -1) {
          arr.push(list[i])
        }
      }
      return arr
    },
    // 筛选出用户头像
    // avatar (item,selfUser, sessionUser) {
    // // 如果是自己发的消息显示登录用户的头像
    //   let user = item.self ? selfUser : sessionUser
    //   return user && user.image
    // },
    // 将日期过滤为 hour:minutes
    time (date) {
      if (typeof date === 'string') {
        date = new Date(date)
      }
      return date.getYear() + '-' + date.getMonth() + '-' + date.getDate() + ' ' + date.getHours() + ':' + date.getMinutes()
    }
  },
  components: {}
}
</script>
<style>
  /*开头*/
  *, *:before, *:after {
    box-sizing: border-box;
  }
  body, html {
    height: 100%;
    overflow: hidden;
  }
  body, ul {
    margin: 0;
    padding: 0;
  }
  body {
    font: 14px/1.4em 'Helvetica Neue', Helvetica, 'Microsoft Yahei', Arial, sans-serif;
    background: #176994 url(../index/assets/newbg.jpg);
    background-size: cover;
  }
  ul {
    list-style: none;
  }
  /*主要界面*/
  .container {
    height: 70%;
    width: 80%;
    margin: 10% auto 10%;
    vertical-align: center;
    border-radius: 4px;
  }
  .sidebar, .main, .information {
    height: 100%;
  }
  .sidebar {
    float: left;
    width: 200px;
    color: #f4f4f4;
    background-color: #2e3238;
    overflow: hidden;
  }
  .main {
    position: relative;
    overflow: hidden;
    background-color: #eee;
  }
  .information {
    float: right;
    width: 200px;
    color: #f4f4f4;
    background-color: #2e3238;
    overflow: hidden;
  }
  .m-menu {
    position: absolute;
    width: 100%;
    bottom: 160px;
    left: 0;
    height: 20px;
    background-color: white;
  }
  .m-text {
    position: absolute;
    width: 100%;
    bottom: 0;
    left: 0;
    height: 160px;
  }
  /*似乎没有用到？*/
  .m-message {
    height: calc(100% - 180px);
  }
  .m-card {
    padding: 12px;
    border-bottom: solid 1px #24272C;
  }
  @font-face {
    font-family: 'iconfont';
    src: url('../index/assets/font/iconfont.eot');
    src: url('../index/assets/font/iconfont.eot?#iefix') format('embedded-opentype'),
    url('../index/assets/font/iconfont.woff') format('woff'),
    url('../index/assets/font/iconfont.ttf') format('truetype'),
    url('../index/assets/font/iconfont.svg#iconfont') format('svg');
  }
  .iconfont0 {
    font-family: "iconfont" !important;
    font-size: 40px;
    font-style: normal;
    -webkit-font-smoothing: antialiased;
    -webkit-text-stroke-width: 0.2px;
    -moz-osx-font-smoothing: grayscale;
  }
  .iconfont1 {
    font-family: "iconfont" !important;
    font-size: 16px;
    font-style: normal;
    -webkit-font-smoothing: antialiased;
    -webkit-text-stroke-width: 0.2px;
    -moz-osx-font-smoothing: grayscale;
  }
  .user-avatar, .user-name {
    vertical-align: middle;
  }
  .user-avatar {
    border-radius: 2px;
  }
  .user-name {
    display: inline-block;
    margin: 0 0 0 15px;
    font-size: 16px;
  }
  .m-ul {
    height: 600px;
  }
  .m-list {
    padding: 12px 15px;
    border-bottom: 1px solid #292C33;
    cursor: pointer;
    transition: background-color .1s;
  }
  .choosed {
    background-color: rgba(255, 255, 0, 0.1);
    display: block;
  }
  .m-list a:hover {
    background-color: rgba(255, 255, 255, 0.03);
    display: block;
  }
  .m-avatar, .m-name {
    vertical-align: middle;
  }
  .m-avatar {
    border-radius: 2px;
  }
  .m-name {
    display: inline-block;
    margin: 0 0 0 15px;
  }
  .m-message {
    padding: 10px 15px;
    overflow-y: scroll;
  }
  .message-list {
    margin-bottom: 15px;
  }
  .message-time {
    margin: 7px 0;
    text-align: center;
  }
  .time-span {
    display: inline-block;
    padding: 0 18px;
    font-size: 12px;
    color: #fff;
    border-radius: 2px;
    background-color: #dcdcdc;
  }
  .main .message-avatar {
    float: left;
    margin: 0 10px 0 0;
    border-radius: 3px;
  }
  .main .massage-text {
    left: 5px;
    display: inline-block;
    position: relative;
    padding: 0 10px;
    max-width: calc(80% - 40px);
    min-height: 30px;
    line-height: 2.5;
    font-size: 12px;
    text-align: left;
    word-break: break-all;
    background-color: #fafafa;
    border-radius: 4px;
  }
  .main .massage-text:before {
    content: " ";
    position: absolute;
    top: 9px;
    right: 100%;
    border: 6px solid transparent;
    border-right-color: #fafafa;
  }
  .self {
    text-align: right;
  }
  .self > img {
    float: right;
    margin: 0 0 0 10px;
  }
  .self > .massage-text {
    display: inline-block;
    position: relative;
    padding: 0 10px;
    max-width: calc(80% + 10px);
    min-height: 30px;
    line-height: 2.5;
    font-size: 12px;
    background-color: #b2e281;
    word-break: break-all;
    border-radius: 4px;
  }
  .self > .massage-text:before {
    content: " ";
    position: absolute;
    right: inherit;
    top: 9px;
    left: 100%;
    border: 6px solid transparent;
    border-right-color: transparent;
    border-left-color: #b2e281;
  }
  .m-text {
    height: 160px;
    border-top: solid 1px #ddd;
    background: white;
  }
  .textarea {
    padding: 10px;
    height: 100%;
    width: 86%;
    border: none;
    outline: none;
    font-family: "Micrsofot Yahei";
    resize: none;
  }
  .human-service {
    height: 100%;
    position: absolute;
    border-radius: 14px;
    color: white;
  }
  .submit-button {
    width: 10%;
    position: absolute;
    right: 2px;
    bottom: 2px;
    border-radius: 14px;
    color: white;
  }
  #chat {
    margin: 20px auto;
    width: 800px;
    height: 600px;
    overflow: hidden;
    border-radius: 3px;
  }
</style>
