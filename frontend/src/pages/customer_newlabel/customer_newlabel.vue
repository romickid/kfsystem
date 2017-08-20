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
              <img class="massage-avatar" wIDth="30" height="30" :src="item.image" />
              <div class="massage-text">
                <li>{{ item.text }}</li>
              </div>
            </div>
          </li>
        </ul>
      </div>
      <div class="main-text">
        <Button @click="switchToCs">转接人工客服</Button>
        <p class="lead emoji-picker-container">
          <textarea class="textarea" placeholder="按 Ctrl + Enter 发送" v-model="text" @keyup="keyboardInputing" data-emojiable="true"></textarea>
        </p>
        <Button class="submit-button" @click="buttonInputing">发送</Button>
      </div>
    </div>
  </div>
</template>

<script>
import * as io from 'socket.io-client'
import Vue from 'vue'
import { formatDate } from '../../../static/js/date.js'
const key = 'VUE-Customer1'

// 接收文字消息放进sessionList
function pushTestToSessionList (session, msg) {
  console.log("function: pushTestToSessionList")
  session.messages.push({
    text: msg,
    date: new Date(),
    image: '../../../static/2.png'
  })
}

function connectToCs (cs, session, csID) {
  console.log("function: connectToCs")
  cs.csID = csID
  session.messages.push({
    text: '已成功为您转接客服' + csID,
    date: new Date(),
    image: '../../../static/2.png'
  })
}

function noServerAvailable (cs, session) {
  console.log("function: noServerAvailable")
  session.messages.push({
    text: '您好，小怪兽麻麻喊小怪兽回家吃饭啦~请您稍后重新连接哦',
    date: new Date(),
    image: '../../../static/2.png'
  })
  cs.customerID = -1
}

// 初始化Socket
function initSocket (cs, session, socket, customer) {
  console.log("function: initSocket")
  let that = this

  socket.on('cs send message', function (msg, enterpriseID, csID, customerID) {
    console.log("socket: cs send message")
    pushTestToSessionList(session, msg, csID, customerID)
  })

  socket.on('connect to cs', function (csID) {
    console.log("socket: connect to cs")
    connectToCs(cs, session, csID)
  })

  socket.on('no server available', function () {
    console.log("socket: no server available")
    noServerAvailable(cs, session)
  })

  socket.on('switch cs', function (enterpriseID, formerCsID) {
    console.log("socket: switch cs")
    this.socket.emit('switch cs', enterpriseID, formerCsID)
  })

  socket.emit('assigned to cs', customer.enterpriseID, customer.customerID)
  console.log("socket emit: assigned to cs")
}

// 数据初始化
function initData (key) {
  // 虚拟数据
  if (!sessionStorage.getItem(key)) {
    let now = new Date()
    let userData = {
      // 登录客户
      customer: {
        customerID: -1,
        customerName: 'coffce',
        enterpriseID: 'nick2',
        image: '../../../static/1.jpg'
      },

      // 客服列表
      cs: {
          csID: -1,
          csName: 'MonsterSXF',
          enterpriseID: 'nick2',
          image: '../../../static/2.png'
        },
      

      // 会话列表
      session: 
        {
          customerID: -1,
          enterpriseID: 'nick2',
          messages: [
            {
              text: '你好呀，我是机器人兔兔~如果想转接人工客服，请按窗口下方的转接按钮进行转接哦~',
              date: now,
              image: '../../../static/2.png'
            }
          ]
        },
      timer: ''
    }
    sessionStorage.setItem(key, JSON.stringify(userData))
  }
}

export default {
  el: '#chat',

  data () {
    initData(key)
    let dataserver = JSON.parse(sessionStorage.getItem(key))
    return {
      // 登录用户
      customer: dataserver.customer,
      // 用户列表
      cs: dataserver.cs,
      // 会话列表
      session: dataserver.session,
      // 计时器
      timer: dataserver.timer,
      // 文本框中输入的内容
      text: '',
      socket: ''
    }
  },

  created () {
    // 如果初次登录， 初始化
    if (this.customer.customerID === -1) {
      this.customer.customerID = (Math.random() * 1000).toString()
      this.customer.customerName = this.customer.customerID
    }

    // 如果刷新之前已转接为人工客服，自动连接服务器
    if (this.cs.csID !== -1) {
      let that = this
      this.socket = io('http://localhost:3000')

      this.socket.on('cs send message', function (msg, enterpriseID, csID, customerID) {
        pushTestToSessionList(that.session, msg, csID, customerID)
      })

      this.socket.on('connect to cs', function (csID) {
        connectToCs(that.cs, that.session, csID)
      })

      this.socket.on('no server available', function () {
        noServerAvailable(that.cs, that.session)
      })

      this.socket.on('switch cs', function (enterpriseID, formerCsID) {
        that.socket.emit('switch cs', enterpriseID, formerCsID)
      })

      this.socket.emit('cs come back', that.customer.enterpriseID, that.cs.csID)
    }
  },

  watch: {
    // 每当session改变时，保存到localStorage中
    session: {
      deep: true,
      handler () {
        sessionStorage.setItem(key, JSON.stringify({
          customer: this.customer,
          cs: this.cs,
          session: this.session,
          timer: this.timer
        }))
      }
    }
  },

  methods: {
    keyboardInputing (e) {
      console.log("method: keyboardInputing")
      if (e.ctrlKey && e.keyCode === 13 && this.text.length) {
        this.session.messages.push({
          text: this.text,
          date: new Date(),
          self: true,
          image: '../../../static/1.jpg'
        })
        this.socket.emit('customer send message', this.text, this.customer.enterpriseID, this.cs.csID, this.customer.customerID)
        this.text = ''
      }
    },

    buttonInputing (e) {
      console.log("method: buttonInputing")
      if (this.text.length !== 0) {
        this.session.messages.push({
          text: this.text,
          date: new Date(),
          self: true,
          image: '../../../static/1.jpg'
        })
        this.socket.emit('customer send message', this.text, this.customer.enterpriseID, this.cs.csID, this.customer.customerID)
        this.text = ''
      }
    },

    switchToCs (e) {
      console.log("method: switchToCs")
      if (this.cs.csID !== -1) {
        alert('当前已为人工客服！')
        return
      }
      let that = this
      that.socket = io('http://localhost:3000')
      initSocket(that.cs, that.session, that.socket, that.customer)
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

  components: {},

  directives: {
    // 发送消息后滚动到底部
    'scroll-bottom' () {
      Vue.nextTick(() => {
        let message = document.getElementsByClassName('main-message')
        message[0].scrollTop = message[0].scrollHeight
      })
    }
  }
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
  overflow: hIDden;
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
  wIDth: 80%;
  margin: 10% auto 10%;
  vertical-align: center;
  border-radius: 4px;
}

.main {
  height: 100%;
  position: relative;
  overflow: hIDden;
  background-color: #eee;
}

.main-text {
  position: absolute;
  wIDth: 100%;
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
  max-wIDth: calc(80% - 40px);
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
  border: 6px solID transparent;
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
  max-wIDth: calc(80% + 10px);
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
  border: 6px solID transparent;
  border-right-color: transparent;
  border-left-color: #b2e281;
}

.main-text {
  height: 160px;
  border-top: solID 1px #ddd;
  background: white;
}

.textarea {
  padding: 10px;
  height: 100%;
  wIDth: 86%;
  border: none;
  outline: none;
  font-family: "Micrsofot Yahei";
  resize: none;
}

.submit-button {
  wIDth: 10%;
  position: absolute;
  right: 2px;
  bottom: 2px;
}

#chat {
  margin: 20px auto;
  wIDth: 800px;
  height: 600px;
  overflow: hIDden;
  border-radius: 3px;
}
</style>
