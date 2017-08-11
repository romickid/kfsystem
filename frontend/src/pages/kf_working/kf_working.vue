<template>
  <div class="container">
    <div class="information">
      Place Customer Information Here...
    </div>
    <div class="sidebar">
      <div class="main-card">
        <header>
          <img class="user-avatar" width="40" height="40" :alt="user.name" :src="user.image">
          <p class="user-name">{{ user.name }}</p>
          <div class="status-manage">
              <i class="iconfont1">&#xe6a6;</i>
              <ul class="managebox">
                <li>
                  <Button>
                    <a href="../se_login">退出账号</a>
                  </Button>
                </li>
                <li>
                  <Button @click="modal1 = true">机器人设置</Button>
                  <Modal v-model="modal1" title="机器人设置" @on-ok="ok" @on-cancel="cancel">
                    <p>增添预料</p>
                    <input type="text" placeholder="请输入需要增添的语料">
                    <button>确认增添</button>
                    <div>
                      <p>更改语料</p>
                      <br>
                      <p>删除语料</p>
                    </div>
                  </Modal>
                </li>
              </ul>
          </div>
        </header>
      </div>
      <div class="main-ul">
        <ul v-if="hangon">
          <div>
            <p @click="switchoff">
              <a>点击切换已挂断聊天消息</a>
            </p>
          </div>
          <li class="main-list" v-for="item in userList" :class="{ choosed: session.userId === item.id }" @click="select(item)">
            <a>
              <img class="main-avatar" width="30" height="30" :alt="item.name" :src="item.image">
              <p class="main-name">{{ item.name }}</p>
            </a>
          </li>
        </ul>
        <ul v-if="!hangon">
          <div>
            <p @click="switchoff">
              <a>点击切换活跃聊天消息</a>
            </p>
          </div>
          <li class="main-list" v-for="item in hangoffUserList" :class="{ choosed: session.userId === item.id }" @click="select(item)">
            <a>
              <img class="main-avatar" width="30" height="30" :alt="item.name" :src="item.image">
              <p class="main-name">{{ item.name }}</p>
            </a>
          </li>
        </ul>
      </div>
    </div>
    <div class="main">
      <div class="main-message" v-scroll-bottom="session.messages">
        <ul>
          <li v-if="history" class="message-list" v-for="item in hsession.messages">
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
        <Button @click="showHistory">历史消息</Button>
        <Button @click="switchServer">转接</Button>
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
const key = 'VUE-CHAT-v6'
// 通过id找聊天记录的索引
function findSessionIndexById (session, id) {
  for (let i = 0; i < session.length; i++) {
    if (session[i].userId === id) {
      return i
    }
  }
}
// 通过id找客服的索引
function findUserIndexById (users, id) {
  for (let i = 0; i < users.length; i++) {
    if (users[i].id === id) {
      return i
    }
  }
}
// 接受消息放进消息列表
function pushMessages (sessionList, index, msg) {
  sessionList[index].messages.push({
    text: msg,
    date: new Date(),
    image: '../../../static/3.jpg'
  })
}
// 创建用户
function createUser (userId, name) {
  return {
    id: userId,
    name: name,
    image: '../../../static/3.jpg'
  }
}
// 在列表中添加用户
function addCustomer (userList, sessionList, historySessionList, customer) {
  userList.splice(0, 0, customer)
  sessionList.splice(0, 0, {
    userId: customer.id,
    messages: []
  })
  historySessionList.splice(0, 0, {
    userId: customer.id,
    messages: []
  })
}
// 消息和用户的上浮
function popUp (list, index) {
  let item = list[index]
  list.splice(index, 1)
  list.splice(0, 0, item)
}
// 用户挂断
function customerHangoff (userList, hangoffUserList,
   sessionList, hangoffSessionList,
    historySessionList, id) {
  let userIndex = findUserIndexById(id)
  let sessionIndex = findSessionIndexById(id)
  let customer = userList[userIndex]
  let session = sessionList[sessionIndex]
  pushMessages(sessionList, sessionIndex, '用户' + id + '已挂断')
  userList.splice(userIndex, 1)
  sessionList.splice(sessionIndex, 1)
  historySessionList.splice(sessionIndex, 1)
  hangoffUserList.splice(0, 0, customer)
  hangoffSessionList.splice(0, 0, session)
}
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
        name: '小怪兽',
        image: '../../../static/2.png'
      },
      {
        id: 3,
        name: '独角兽',
        image: '../../../static/3.jpg'
      }
    ],
    hangoffUserList: [
      {
        id: 4,
        name: 'MonsterSXF',
        image: '../../../static/2.png'
      },
      {
        id: 5,
        name: '独角兽🦄',
        image: '../../../static/3.jpg'
      },
      {
        id: 6,
        name: '飞天小女警',
        image: '../../../static/1.jpg'
      }
    ],
    // 会话列表
    sessionList: [
      {
        userId: 2,
        messages: [
          {
            text: '你好，我是客户小怪兽！！',
            date: now,
            image: '../../../static/2.png'
          },
          {
            text: '有个问题想请你帮助我~',
            date: now,
            image: '../../../static/2.png'
          }
        ]
      },
      {
        userId: 3,
        messages: [
          {
            text: '你好，我是客户独角兽🦄',
            date: now,
            image: '../../../static/3.jpg'
          },
          {
            text: '你可以帮我嘛~',
            date: now,
            image: '../../../static/3.jpg'
          },
          {
            text: '嘻嘻嘻',
            date: now,
            image: '../../../static/3.jpg'
          }
        ]
      }
    ],
    // 已挂断会话列表
    hangoffSessionList: [
      {
        userId: 4,
        messages: [
          {
            text: '你好，我是客户小怪兽！！',
            date: now,
            image: '../../../static/2.png'
          },
          {
            text: '我已经挂断了哦',
            date: now,
            image: '../../../static/2.png'
          }
        ]
      },
      {
        userId: 5,
        messages: [
          {
            text: '你好，我是客户独角兽🦄',
            date: now,
            image: '../../../static/3.jpg'
          },
          {
            text: '你可以帮我嘛~',
            date: now,
            image: '../../../static/3.jpg'
          },
          {
            text: '嘻嘻嘻',
            date: now,
            image: '../../../static/3.jpg'
          }
        ]
      },
      {
        userId: 6,
        messages: [
          {
            text: '你好，我是客户飞天小女警',
            date: now,
            image: '../../../static/3.jpg'
          },
          {
            text: '你可以帮我嘛~~',
            date: now,
            image: '../../../static/3.jpg'
          },
          {
            text: '嘻嘻嘻',
            date: now,
            image: '../../../static/3.jpg'
          }
        ]
      }
    ],
    historySessionList: [
      {
        userId: 2,
        messages: [
          {
            text: 'This is a history message',
            date: now,
            image: '../../../static/3.jpg'
          }
        ]
      },
      {
        userId: 3,
        messages: [
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
      hangoffUserList: dataserver.hangoffUserList,
      // 会话列表
      sessionList: dataserver.sessionList,
      hangoffSessionList: dataserver.hangoffSessionList,
      historySessionList: dataserver.historySessionList,
      // 选中的会话Index
      sessionIndex: 0,
      hangoffSessionIndex: 0,
      // 文本框中输入的内容
      text: '',
      // 显示活跃消息
      hangon: true,
      // 设置机器人
      modal1: false,
      // 客服对应的socket
      socket: '',
      // 当前正在服务人数
      customerNumber: 2,
      transferable: true,
      // test
      item: {},
      api_chattinglog_show_history: '../api/chattinglog_show_history/',
      history: false
    }
  },
  computed: {
    session () {
      if (this.hangon) {
        return this.sessionList[this.sessionIndex]
      } else {
        return this.hangoffSessionList[this.hangoffSessionIndex]
      }
    },
    hsession () {
      return this.historySessionList[this.sessionIndex]
    }
  },
  created () {
    const that = this
    this.socket = io('http://localhost:3000')
    that.socket.id = (Math.random() * 1000).toString()
    this.user.id = that.socket.id
    this.user.name = that.socket.id
    // 接收消息
    this.socket.on('customer message', function (msg, fromId, toId) {
      let index = findSessionIndexById(that.sessionList, fromId)
      pushMessages(that.sessionList, index, msg)
      popUp(that.userList, index)
      popUp(that.sessionList, index)
      popUp(that.historySessionList, index)
    })
    this.socket.on('add client', function (fromId) {
      let customer = createUser(fromId, fromId)
      addCustomer(that.userList, that.sessionList, that.historySessionList, customer)
      that.customerNumber++
      pushMessages(that.sessionList, 0, '用户' + fromId + '已上线')
    })
    this.socket.on('customer hang off', function (customerId) {
      customerHangoff(that.userList, that.hangoffUserList,
        that.sessionList, that.hangoffSessionList,
         that.historySessionList, customerId)
    })
    this.socket.on('switch failed', function () {
      alert('当前无可转接客服！')
      that.transferable = false
    })
    this.socket.emit('server set id', that.socket.id)
  },
  watch: {
    // 每当sessionList改变时，保存到localStorage中
    sessionList: {
      deep: true,
      handler () {
        localStorage.setItem(key, JSON.stringify({
          user: this.user,
          userList: this.userList,
          hangoffUserList: this.hangoffUserList,
          sessionList: this.sessionList,
          hangoffSessionList: this.hangoffSessionList,
          historySessionList: this.historySessionList
        }))
      }
    }
  },
  methods: {
    select (value) {
      if (this.hangon) {
        this.sessionIndex = this.userList.indexOf(value)
      } else {
        this.hangoffSessionIndex = this.hangoffUserList.indexOf(value)
      }
    },
    inputing (e) {
      if (e.ctrlKey && e.keyCode === 13 && this.text.length) {
        if (!this.hangon) {
          alert('该用户已挂断！')
          this.text = ''
          return
        }
        this.session.messages.push({
          text: this.text,
          date: new Date(),
          self: true,
          image: '../../../static/1.jpg'
        })
        this.socket.emit('server message', this.text, this.user.id, this.session.userId)
        this.text = ''
      }
    },
    buttoninputing (e) {
      if (!this.hangon) {
        alert('该用户已挂断！')
        this.text = ''
        return
      }
      if (this.text.length !== 0) {
        this.session.messages.push({
          text: this.text,
          date: new Date(),
          self: true,
          image: this.user.image
        })
        this.socket.emit('server message', this.text, this.user.id, this.session.userId)
        this.text = ''
      }
    },
    switchoff () {
      this.hangon = !this.hangon
      this.sessionIndex = 0
      this.hangoffSessionIndex = 0
    },
    showHistory (e) {
      if (!this.hangon) {
        alert('无法获取历史消息！')
        return
      }
      this.history = !this.history
      // var vm = this
      // this.item = { 'client_id': '1', 'service_id': '1' }
      // vm.$http.post(vm.api_chattinglog_show_history, this.item)
      //   .then((response) => {
      //     vm.$set(this, 'my_test', response.data)
      //     console.log('接收到啦！')
      //     console.log(this.my_test)
      //     for (var p in response.data) {
      //       alert(response.data[p].time + ' ' + response.data[p].content)
      //       this.hsession.messages.push({
      //         text: response.data[p].content,
      //         date: response.data[p].time,
      //         self: response.data[p].is_client,
      //         image: this.user.image
      //       })
      //     }
      //   })
    },
    switchServer (e) {
      if (!this.hangon) {
        alert('无法为已挂断的用户进行转接！')
        return
      }
      this.socket.emit('switch server from server', this.session.userId)
      if (!this.transferable) {
        this.transferable = true
        return
      }
      pushMessages(this.sessionList, this.sessionIndex, '已成功为用户转接！')
      customerHangoff(this.userList, this.hangoffUserList,
        this.sessionList, this.hangoffSessionList,
         this.historySessionList, this.session.userId)
      this.transferable = true
    }
  },
  filters: {
    // 将日期过滤为 hour:minutes
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
  background: #176994 url(../index/assets/bg.jpg);
  background-size: cover;
}

ul {
  list-style: none;
}

 ::-webkit-scrollbar {
  width: 8px;
}

 ::-webkit-scrollbar-track {
  background-color: #bee1eb;
}

 ::-webkit-scrollbar-thumb {
  background-color: #00aff0;
}

 ::-webkit-scrollbar-thumb<a href="https://www.baidu.com/s?wd=%3Ahover&tn=44039180_cpr&fenlei=mv6quAkxTZn0IZRqIHckPjm4nH00T1YdnHT4rHIWm1fdujPWPjbL0ZwV5Hcvrjm3rH6sPfKWUMw85HfYnjn4nH6sgvPsT6KdThsqpZwYTjCEQLGCpyw9Uz4Bmy-bIi4WUvYETgN-TLwGUv3EP1RkPjRYP1TvPHf3rjRsnW0Y" target="_blank" class="baidu-highlight">:hover</a> {
  background-color: #9c3
}

 ::-webkit-scrollbar-thumb:active {
  background-color: #00aff0
}

/*主要界面*/

.container {
  height: 100%;
  width: 100%;
}

.sidebar,
.main,
.information {
  height: 100%;
}

.sidebar {
  float: left;
  width: 20%;
  color: #f4f4f4;
  background-color: #2e3238;
  overflow-x: hidden;
  overflow-y: visible;
}

.main {
  position: relative;
  overflow: hidden;
  background-color: #eee;
  width: 60%;
}

.information {
  float: right;
  width: 20%;
  color: #f4f4f4;
  background-color: #2e3238;
  overflow: hidden;
}

.main-menu {
  position: absolute;
  width: 100%;
  bottom: 160px;
  left: 0;
  height: 20px;
  background-color: white;
}

.main-text {
  position: absolute;
  width: 100%;
  bottom: 0;
  left: 0;
  height: 160px;
}

.main-message {
  height: calc(100% - 180px);
}

.main-card {
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

.user-avatar,
.user-name {
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

.managebox {
  display: none;
  width: 100px;
  border: 1px solid #eee;
  background-color: #FFF;
  border-radius: 4px;
  position: absolute;
  top: 20px;
  left: 100px;
  cursor: pointer;
  overflow: visible;
}

.managebox li {
  height: auto;
  font-size: small;
  text-align: center;
  color: grey;
  border: 1px solid #eee;
}

.managebox li a:hover {
  background-color: rgba(255, 255, 0, 0.1);
  display: block;
}

.status-manage {
  float: right;
}

.status-manage:hover .managebox {
  display: block;
  float: left;
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

.main-ul {
  height: calc(100% - 105px);
  overflow-y: scroll;
  overflow-x: hidden;
}

.main-ul a:hover {
  cursor: pointer;
  background-color: gray;
}

.main-list {
  padding: 12px 15px;
  border-bottom: 1px solid #292C33;
  cursor: pointer;
  transition: background-color .1s;
}

.choosed {
  background-color: rgba(255, 255, 0, 0.1);
  display: block;
}

.main-list a:hover {
  background-color: rgba(255, 255, 255, 0.03);
  display: block;
}

.main-avatar,
.m-name {
  vertical-align: middle;
}

.main-avatar {
  border-radius: 2px;
}

.main-name {
  display: inline-block;
  margin: 0 0 0 15px;
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

.r-modal {
  position: absolute;
  background: white;
  padding: 270px;
}

#chat {
  margin: 20px auto;
  width: 800px;
  height: 600px;
  overflow: hidden;
  border-radius: 3px;
}
</style>
