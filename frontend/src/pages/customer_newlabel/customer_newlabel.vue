<template>
  <div class="container">
    <div class="main">
      <div class="main-message" v-scroll-bottom="session.messages">
        <ul>
          <li class="message-list" v-for="item in session.messages">
            <p class="message-time">
              <span class="time-span">{{ item.date | time }}</span>
            </p>
            <div class="massage-main" :class="{ self: item.self }">
              <img class="massage-avatar" width="30" height="30" :src="item.image" />
              <div class="massage-text">
                <li>{{ item.text }}</li>
              </div>
            </div>
          </li>
        </ul>
      </div>
      <div class="main-text">
        <p class="lead emoji-picker-container">
          <textarea class="textarea" placeholder="按 Ctrl + Enter 发送" v-model="text" @keyup="inputing" data-emojiable="true"></textarea>
        </p>
        <Button class="submit-button" @click="buttoninputing">发送</Button>
      </div>
    </div>
  </div>
</template>

<script>
import * as io from 'socket.io-client'
import {formatDate} from '../../../static/js/date.js'
const key = 'VUE-Customer1'
localStorage.clear()
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
      text: '',
      socket: ''
    }
  },
  computed: {
    session () {
      return this.sessionList[this.sessionIndex]
    }
  },
  created () {
    const that = this
    this.socket = io('http://localhost:3000')
    that.socket.id = (Math.random() * 1000).toString()
    this.user.id = that.socket.id
    this.user.name = that.socket.id
    // 接收消息
    this.socket.on('server message', function (msg, fromId, toId) {
      that.sessionList[0].messages.push({
        text: msg,
        date: new Date(),
        image: that.userList[0].image
      })
    })
    this.socket.on('connect to server', function (toId) {
      that.userList[0].id = toId
      that.sessionList[0].messages.push({
        text: '已成功为您转接客服' + toId,
        date: new Date(),
        image: that.userList[0].image
      })
    })
    this.socket.on('no server available', function () {
      that.sessionList[0].messages.push({
        text: '您好，小怪兽麻麻喊小怪兽回家吃饭啦~请您稍后重新连接哦',
        date: new Date(),
        image: that.userList[0].image
      })
    })
    this.socket.on('switch server', function (formerId) {
      that.socket.emit('switch server', formerId)
    })
    this.socket.emit('customer set id', that.socket.id)
    this.socket.emit('assigned to server', that.socket.id)
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
        this.socket.emit('customer message', this.text, this.user.id, this.userList[0].id)
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
        this.socket.emit('customer message', this.text, this.user.id, this.userList[0].id)
        this.text = ''
      }
    }
  },
  filters: {
    time (date) {
      if (typeof date === 'string') {
        date = new Date(date)
      }
      return formatDate(date, 'yyyy-MM-dd hh:mm')
    }
  },
  components: {}
}
</script>
<style>
/*开头*/

*,
*:before,
*:after {
  box-sizing: border-box;
}

body,
html {
  height: 100%;
  overflow: hidden;
}

body,
ul {
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

.main {
  height: 100%;
  position: relative;
  overflow: hidden;
  background-color: #eee;
}

.main-text {
  position: absolute;
  width: 100%;
  bottom: 0;
  left: 0;
  height: 160px;
}

/*似乎没有用到？*/
.main-message {
  height: calc(100% - 180px);
}

.main-message {
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

.self>img {
  float: right;
  margin: 0 0 0 10px;
}

.self>.massage-text {
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

.self>.massage-text:before {
  content: " ";
  position: absolute;
  right: inherit;
  top: 9px;
  left: 100%;
  border: 6px solid transparent;
  border-right-color: transparent;
  border-left-color: #b2e281;
}

.main-text {
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

.submit-button {
  width: 10%;
  position: absolute;
  right: 2px;
  bottom: 2px;
}

#chat {
  margin: 20px auto;
  width: 800px;
  height: 600px;
  overflow: hidden;
  border-radius: 3px;
}
</style>
