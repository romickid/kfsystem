<template>
  <div class="container">
    <div class="information">
      Place Customer Information Here...
    </div>
    <div class="sidebar">
      <div class="m-card">
        <header>
          <img class="user-avatar" width="40" height="40" :alt="user.name" :src="user.image">
          <p class="user-name">{{ user.name }}</p>
        </header>
        <footer>
          <input class="search" type="text" placeholder="search user..." v-model="search">
        </footer>
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
          <li class="message-list"v-for="item in session.messages">
            <p class="message-time"><span class="time-span">{{item.date | time}}</span></p>
            <div class="massage-main" :class="{ self: item.self }">
              <img class="massage-avatar" width="30" height="30" :src="item | avatar" />
              <div class="massage-text">{{ item.text }}</div>
            </div>
          </li>
        </ul>
      </div>
      <div class="m-text">
        <textarea class="textarea" placeholder="按 Ctrl + Enter 发送" v-model="text" @keyup="inputing"></textarea>
      </div>
    </div>
    <div class="information">
      Place Customer Information Here...
    </div>
  </div>
</template>

<script>
export default {
  el: '#chat',
  data () {
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
        },
        {
          id: 3,
          name: 'yayaya',
          image: '../../../static/3.jpg'
        }
      ],
      // 会话列表
      sessionList: [
        {
          userId: 2,
          messages: [
            {
              text: 'Hello，这是一个基于Vue + Webpack构建的简单chat示例，聊天记录保存在localStorge。简单演示了Vue的基础特性和webpack配置。',
              date: now
            },
            {
              text: '项目地址: https://sc.chinaz.com/jiaoben/',
              date: now
            }
          ]
        },
        {
          userId: 3,
          messages: [
            {
              text: 'Hello，这是一个基于Vue + Webpack构建的简单chat示例，聊天记录保存在localStorge。简单演示了Vue的基础特性和webpack配置。',
              date: now
            },
            {
              text: '项目地址: https://sc.chinaz.com/jiaoben/',
              date: now
            },
            {
              text: 'xixixi',
              date: now
            }
          ]
        }
      ]
    }
    return {
      // 登录用户
      user: userData.user,
      // 用户列表
      userList: userData.userList,
      // 会话列表
      sessionList: userData.sessionList,
      // 搜索key
      search: '',
      // 选中的会话Index
      sessionIndex: 0
    }
  },
  computed: {
    session () {
      return this.sessionList[this.sessionIndex]
    },
    sessionUser () {
      let users = this.userList.filter(item => item.id === this.session.userId)
      return users[0]
    }
  },
  watch: {
    // 每当sessionList改变时，保存到localStorage中
    sessionList: {
      deep: true,
      handler () {
        this.userData.user = this.user
        this.userData.userList = this.userList
        this.userData.sessionList = this.sessionList
      }
    }
  },
  methods: {
    select (value) {
      this.sessionIndex = this.userList.indexOf(value)
    }
  },
  filters: {
    search (item) {
      return item.name.indexOf(this.search) > -1
    },
    // 筛选出用户头像
    // avatar (item) {
    // // 如果是自己发的消息显示登录用户的头像
    //   let user = item.self ? this.user : this.sessionUser
    //   return user && user.img
    // },
    // 将日期过滤为 hour:minutes
    time (date) {
      if (typeof date === 'string') {
        date = new Date(date)
      }
      return date.getHours() + ':' + date.getMinutes()
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
    background: #176994 url(../index/assets/bg.jpg);
    background-size: cover;
  }
  ul {
    list-style: none;
  }
  /*主要界面*/
  .container {
    height: 100%;
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
  .m-text {
    position: absolute;
    width: 100%;
    bottom: 0;
    left: 0;
  }
  /*似乎没有用到？*/
  .m-message {
    height: ~'calc(100% - 160px)';
  }
  .m-card {
    padding: 12px;
    border-bottom: solid 1px #24272C;
  }
  footer {
    margin-top: 10px;
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
  .search {
    padding: 0 10px;
    width: 100%;
    font-size: 12px;
    color: #fff;
    height: 30px;
    line-height: 30px;
    border: solid 1px #3a3a3a;
    border-radius: 4px;
    outline: none;
    background-color: #26292E;
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
  .message-avatar {
    float: left;
    margin: 0 10px 0 0;
    border-radius: 3px;
  }
  .massage-text {
    display: inline-block;
    position: relative;
    padding: 0 10px;
    max-width: ~'calc(100% - 40px)';
    min-height: 30px;
    line-height: 2.5;
    font-size: 12px;
    text-align: left;
    word-break: break-all;
    background-color: #fafafa;
    border-radius: 4px;
  }
  .massage-text :before {
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
  .self .avatar {
    float: right;
    margin: 0 0 0 10px;
  }
  .text {
    background-color: #b2e281;
  }
  .text :before {
    right: inherit;
    left: 100%;
    border-right-color: transparent;
    border-left-color: #b2e281;
  }
  .m-text {
    height: 160px;
    border-top: solid 1px #ddd;
  }
  .textarea {
    padding: 10px;
    height: 100%;
    width: 100%;
    border: none;
    outline: none;
    font-family: "Micrsofot Yahei";
    resize: none;
  }
  #chat {
    margin: 20px auto;
    width: 800px;
    height: 600px;
    overflow: hidden;
    border-radius: 3px;
  }
</style>
