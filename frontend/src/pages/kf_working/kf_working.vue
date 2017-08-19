<template>
  <div class="container">
    <div class="information">
      Place Customer Information Here...
    </div>
    <div class="sIDebar">
      <div class="main-card">
        <header>
          <img class="customer-avatar" wIDth="40" height="40" :alt="cs.csName" :src="cs.image">
          <Dropdown>
            <a href="javascript:voID(0)">
              <p class="customer-name">{{ cs.csName }}</p>
              <Icon type="arrow-down-b"></Icon>
            </a>
            <Dropdown-menu slot="list">
              <Dropdown-item>
                <Button @click="csLogout">
                  <!-- <a href="../se_login">退出账号</a> -->
                  退出账号
                </Button>
              </Dropdown-item>
              <Dropdown placement="right-start">
                <Dropdown-item>
                  机器人设置
                  <Icon type="ios-arrow-right"></Icon>
                </Dropdown-item>
                <Dropdown-menu slot="list">
                  <Dropdown-item>
                    <Button @click="addSentence=true">增添语料</Button>
                    <Modal v-model="addSentence" title="增添语料" @on-ok="ok" @on-cancel="cancel">
                      <p>增添语料</p>
                      <div>
                        <Input type="text" placeholder="请输入问题">
                      </div>
                      <div>
                        <Input type="text" placeholder="请输入回答">
                      </div>
                      <Button>确认增添</Button>
                    </Modal>
                  </Dropdown-item>
                  <Dropdown-item>
                    <Button @click="modifySentence=true">编辑语料</Button>
                    <Modal v-model="modifySentence" title="编辑语料" @on-ok="ok" @on-cancel="cancel" z-index=40>
                      <robot-setting ref="robotSetting"></robot-setting>
                    </Modal>
                  </Dropdown-item>
                </Dropdown-menu>
              </Dropdown>
            </Dropdown-menu>
          </Dropdown>
        </header>
      </div>
      <div class="main-ul">
        <ul v-if="hangon">
          <div>
            <p align="center" color="#cccccc" @click="switchoff">
              <a>点击切换已挂断聊天消息</a>
            </p>
          </div>
          <li class="main-list" v-for="item in onlineList" :class="{ choosed: currentOnlineObject.customerID === item.customerID }" @click="displayCustomerList(item)">
            <a>
              <Badge :count="item.uncheck" overflow-count="999">
                <img class="main-avatar" wIDth="30" height="30" :alt="item.customerID" :src="item.image">
              </Badge>
              <p class="main-name">{{ item.customerID }}</p>
            </a>
          </li>
        </ul>
        <ul v-if="!hangon">
          <div>
            <p align="center" color="#cccccc" @click="switchoff">
              <a>点击切换活跃聊天消息</a>
            </p>
          </div>
          <li class="main-list" v-for="item in offlineList" :class="{ choosed: currentOnlineObject.customerID === item.customerID }" @click="displayCustomerList(item)">
            <a>
              <img class="main-avatar" wIDth="30" height="30" :alt="item.customerID" :src="item.image">
              <p class="main-name">{{ item.customerID }}</p>
            </a>
          </li>
        </ul>
      </div>
    </div>
    <div class="main">
      <div class="main-message" v-scroll-bottom="currentOnlineObject.messages">
        <ul>
          <li class="message-list" v-for="item in currentOnlineObject.historyMessages">
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
          <li v-if="currentNumber" class="message-list" v-for="item in currentOnlineObject.messages">
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
        <Button @click="showHistory">历史消息</Button>
        <Button @click="switchAnotherCs">转接</Button>
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
import robotSetting from '../../components/robot_setting'
import { formatDate } from '../../../static/js/date.js'
const key = 'VUE-CHAT-v6'



// 通过customerID找会话组的索引
function findOnlineListByCustomerID (onlineList, customerID) {
  console.log('[function: findOnlineListByCustomerID]')
  for (let i = 0; i < onlineList.length; i++) {
    if (onlineList[i].customerID === customerID) {
      return i
    }
  }
  return -1
}

// 通过customerID找l离线组的索引
function findOfflineListByCustomerID (offlineList, customerID) {
  return findOnlineListByCustomerID (onlineList, customerID)
}

// 接收文字消息放进onlinelist
function pushTextToOnlineList (onlineList, index, msg) {
  console.log('[function: pushTextToOnlineList]')
  onlineList[index].messages.push({
    text: msg,
    date: new Date(),
    image: '../../../static/3.jpg'
  })
}

// 接收文字消息放进offlinelist
function pushTextToOfflineList (offlineList, index, msg) {
  return pushTextToOnlineList (offlineList, index, msg)
}

// 根据已有信息创建一个客户, 返回一个客户对象
function createCustomer (customerID, customerName, enterpriseID) {
  console.log('[function: createCustomer]')
  return {
    customerID: customerID,
    customerName: customerName,
    enterpriseID: enterpriseID,
    image: '../../../static/3.jpg',
    uncheck: 0  // 未读消息数
  }
}

// 发送消息称用户已挂断
function customerOutMessage (socket, customerID) {
  console.log('[function: customerOutMessage]')
  socket.emit('customer out', customerID)
}

// 在所有显示列表中添加用户
function addCustomer (cs_socket, onlineList, customer) {
  console.log('[function: addCustomer]')

  let timer = setTimeout(function () {
    customerOutMessage(cs_socket, customer.customerID)
  }, 1000000)

  onlineList.splice(0, 0, 
    {
      enterpriseID: customer.enterpriseID,
      customerID: customer.customerID,
      customer: customer,
      messages: [],
      historyMessages: [],
      timer: timer,
      uncheck: 0,
    }
  )
}

// 消息和用户的上浮, 用于显示
function popUp (onlineList, index) {
  console.log('[function: popUp]')
  let temp_onlineObject = onlineList[index]
  onlineList.splice(index, 1)
  onlineList.splice(0, 0, temp_onlineObject)
}

// 客户挂断
function customerHangoff (onlineList, offlineList, customerID) {
  console.log('[function: customerHangoff]')
  let onlineIndex = findOnlineListByCustomerID(onlineList, customerID)
  let customer = onlineList[onlineIndex].customer
  let messages = onlineList[onlineIndex].messages
  pushTextToOnlineList(onlineList, onlineIndex, '用户' + customerID + '已挂断')
  offlineList.splice(0, 0, {
    enterpriseID: customer.enterpriseID,
    customerID: customer.customerID,
    customer: customer,
    messages: messages
  })
}

// 删除客户
function customerDelete (onlineList, offlineList, customerID) {
  console.log('[function: customerDelete]')
  
  let onlineIndex = findOnlineListByCustomerID(onlineList, customerID)
  let timer = onlineList[onlineIndex].timer
  clearTimeout(timer)
  onlineList.splice(onlineIndex, 1)
}

// 虚拟数据
if (!sessionStorage.getItem(key)) {
  let userData = {
    // 登录客服
    cs: {
      csID: -1,
      enterpriseID: -1,
      csName: 'coffce',
      image: '../../../static/1.jpg'
    },

    // 在线列表
    onlineList: [],
    onlineIndex: 0,

    // 离线列表
    offlineList: [],
    offlineIndex: 0,

    hangon: true,
    isLogon: false,
    customerNumber: 0,
    hangoffCustomerNumber: 0
  }
  sessionStorage.setItem(key, JSON.stringify(userData))
}

export default {
  el: '#chat',
  data () {
    let dataserver = JSON.parse(sessionStorage.getItem(key))
    return {
      // 登录客服
      cs: dataserver.cs,

      onlineList: dataserver.onlineList,
      onlineIndex: dataserver.onlineIndex,

      offlineList: dataserver.offlineList,
      offlineIndex: dataserver.offlineIndex,

      // is活跃消息栏
      hangon: dataserver.hangon,

      // 判断刷新之前是否处于登录状态
      isLogon: dataserver.isLogon,

      // 当前正在服务人数
      customerNumber: dataserver.customerNumber,
      hangoffCustomerNumber: dataserver.hangoffCustomerNumber,

      // 文本框中输入的内容
      text: '',

      // 增添语料对话框
      addSentence: false,

      // 修改语料对话框
      modifySentence: false,

      // 设置机器人
      modal1: false,

      // 客服对应的socket
      socket: '',

      // test
      apiChattinglogSendMessage: '../api/chattinglog_send_message/',
      apiChattinglogShowHistory: '../api/chattinglog_show_history/',
      apiCustomerserviceShowUserStatus: '../api/customerservice_show_user_status/',
      apiChattinglogGetCsID: '../api/chattinglog_get_cs_ID/',
      item: {},
      databaseCsID: '',
      tempCustomerID: ''
    }
  },

  computed: {
    // 返回在线消息当前显示对象
    currentOnlineObject () {
      if (this.hangon && this.onlineList.length) {
        return this.onlineList[this.onlineIndex]
      } else if (!this.hangon && this.offlineList.length) {
        return this.offlineList[this.offlineIndex]
      } else {
        return {
          enterpriseID: -1,
          customerID: -1,
          messages: [],
          historyMessages: [],
        }
      }
    },

    currentNumber () {
      return (this.hangon && this.onlineList.length) || (!this.hangon && this.offlineList.length)
    }
  },

  created () {
    const that = this
    this.getCsInfomation()
    this.socket = io('http://localhost:3000')

    // socket响应 接收用户发送的文字信息
    this.socket.on('customer send message', function (msg, enterpriseID, csID, customerID) {
      console.log('socket: customer send message')
      let vm = that
      let onlineIndex = findOnlineListByCustomerID(that.onlineList, customerID)
      pushTextToOnlineList(that.onlineList, onlineIndex, msg)
      // 将信息存入数据库
      that.item = {'email': csID }
      vm.$http.post(vm.apiChattinglogGetCsID, that.item)
        .then((response) => {
          vm.$set(that, 'databaseCsID', response.data)
          vm.$set(that, 'item', {'client_id': customerID, 'service_id': that.databaseCsID, 'content': msg, 'is_client': 1 })
          that.saveChattingLog(that.item)
        }, (response) => {
          alert('customer send message error!')
          window.location.href = '../se_login'
        })

      that.tempCustomerID = customerID
      // 将信息展示至界面
      // 如果收到消息的session 与 当前显示的session不同
      if (onlineIndex !== that.onlineIndex) {
        var customerID = that.tempCustomerID
        popUp(that.onlineList, onlineIndex)

        clearTimeout(that.onlineList[0].timer)
        let customerID = that.onlineList[0].customerID
        let csSocket = that.socket
        that.onlineList[0].timer = setTimeout(
          function () {
            customerOutMessage(csSocket, customerID)
          }, 1000000)
        
        // 当前显示的是应该变成列表第2位，因此要++
        if (that.onlineIndex < onlineIndex) {
          that.onlineIndex++
        }
        that.customerList[0].uncheck++ // 因此uncheck也要++
      } else {
        var customerID = that.tempCustomerID
        clearTimeout(that.onlineList[onlineIndex].timer)
        let customerID = that.onlineList[onlineIndex].customerID
        let csSocket = that.socket
        that.onlineList[0].timer = setTimeout(
          function () {
            customerOutMessage(csSocket, customerID)
          }, 1000000)
      }
    })

    // 接受图片信息

    // socket响应 增加客服
    this.socket.on('add customer', function (enterpriseID, customerID) {
      console.log('socket: add customer')
      let customer = createCustomer(customerID, customerID, enterpriseID)
      addCustomer(that.socket, that.onlineList, customer)
      if (that.onlineList.length !== 1) { // 新增客服显示未读消息
        customer.uncheck++
      }
      if (that.hangon && that.onlineList.length !== 1) { // 如果是处于Hangon, 当前显示的要位于列表第二位
        that.onlineIndex++
      }
      pushTextToOnlineList(that.onlineList, 0, '用户' + customerID + '已上线')
    })

    // socket响应 客户挂断
    this.socket.on('customer hang off', function (enterpriseID, customerID) {
      customerHangoff(that.onlineList, that.offlineList, customerID)
      let onlineIndex = findOnlineListByCustomerID(that.onlineList, customerID)
      if (that.onlineIndex >= onlineIndex) {
        that.onlineIndex--
      }

      customerDelete(that.onlineList, that.offlineList, customerID)
    })

    // 无法转接
    this.socket.on('switch failed', function () {
      console.log('socket: switch failed')
      alert('当前无可转接客服！')
    })

    this.socket.on('switch succeed', function () {
      console.log('socket: switch succeed')
      let customerID = that.onlineList[that.onlineIndex].customerID
      pushTextToOnlineList(that.onlineIndex, that.onlineIndex, '已成功为用户转接！')
      customerHangoff(that.onlineIndex, that.offlineList, customerID)
      if (that.onlineIndex !== 0) {
        that.onlineIndex--
      }
      customerDelete(that.onlineIndex, that.offlineList, customerID)
    })

    // 客服登录
    // 判断上次是刷新还是退出页面，并进行初始化
    if (!this.isLogon) {
      console.log('socket: !this.isLogon')
      setTimeout(function () {
        that.socket.enterprise_ID = that.cs.enterpriseID
        that.socket.cs_ID = that.cs.csID
        that.socket.emit('cs login', that.cs.enterpriseID, that.cs.csID)
        that.isLogon = true
      }, 1000)
    } else {
      console.log('socket: this.isLogon')
      that.socket.enterprise_ID = that.cs.enterpriseID
      that.socket.cs_ID = that.cs.csID
      that.socket.emit('cs come back', that.socket.enterprise_ID, that.socket.cs_ID)
    }

    sessionStorage.setItem(key, JSON.stringify({
      cs: this.cs,

      onlineList: this.onlineList,
      onlineIndex: this.onlineIndex,

      offlineList: this.offlineList,
      offlineIndex: this.offlineIndex,
      hangon: this.hangon,
      isLogon: this.isLogon,
      customerNumber: this.customerNumber,
      hangoffCustomerNumber: this.hangoffCustomerNumber
    }))
  },

  watch: {
    // 每当sessionList改变时，保存到localStorage中
    sessionList: {
      deep: true,
      handler() {
        sessionStorage.setItem(key, JSON.stringify({
          cs: this.cs,

          onlineList: this.onlineList,
          onlineIndex: this.onlineIndex,

          offlineList: this.offlineList,
          offlineIndex: this.offlineIndex,
          hangon: this.hangon,
          isLogon: this.isLogon,
          customerNumber: this.customerNumber,
          hangoffCustomerNumber: this.hangoffCustomerNumber
        }))
      }
    }
  },

  methods: {
    // 保存文字信息
    saveChattingLog (obj) {
      console.log('[method: saveChattingLog]')
      let vm = this
      vm.$http.post(vm.apiChattinglogSendMessage, obj)
        .then((response) => {
          vm.$set(this, 'item', {})
        }, (response) => {
          alert('save chatting log error!')
          alert(obj)
          window.location.href = '../se_login'
        })
    },

    // 获取历史信息
    getHistoryLog (obj) {
      console.log('[method: getHistoryLog]')
      let vm = this
      vm.$http.post(vm.apiChattinglogShowHistory, obj)
        .then((response) => {
          for (var p in response.data) {
            if (response.data[p].is_client === false) {
              this.currentOnlineObject.historyMessages.push({
                text: response.data[p].content,
                date: response.data[p].time,
                self: true,
                image: this.cs.image
              })
            } else {
              this.currentOnlineObject.historyMessages.push({
                text: response.data[p].content,
                date: response.data[p].time,
                image: '../../../static/3.jpg'
              })
            }
          }
        })
    },

    //  显示用户列表
    displayCustomerList (value) {
      console.log('[method: displayCustomerList]')

      if (this.hangon) {
        this.onlineIndex = this.onlineList.indexOf(value)
        this.onlineList[this.onlineIndex].uncheck = 0
      } else {
        this.offlineIndex = this.offlineList.indexOf(value)
      }
    },

    // ctrl+enter操作
    keyboardInputing (e) {
      console.log('[method: keyboardInputing]')
      if (e.ctrlKey && e.keyCode === 13 && this.text.length) {
        if (!this.hangon) {
          alert('该用户已挂断！')
          this.text = ''
          return
        }

        // 存入数据库，下标考虑
        let index = this.currentOnlineObject.messages.length
        let vm = this
        let that = this
        // 输入为空直接退出
        if (that.text.length === 0) {
          return
        }

        that.item = { 'email': this.cs.csID }
        vm.$http.post(vm.apiChattinglogGetCsID, that.item)
          .then((response) => {
            vm.$set(that, 'databaseCsID', response.data)
            vm.$set(that, 'item', {'client_id': that.currentOnlineObject.customerID, 'service_id': that.databaseCsID, 'content': that.currentOnlineObject.messages[index].text, 'is_client': 0 })
            this.saveChattingLog(that.item)
          }, (response) => {
          alert('cs keyboard inputing error!')
          window.location.href = '../se_login'
        })

        this.currentOnlineObject.messages.push({
          text: this.text,
          date: new Date(),
          self: true,
          image: this.cs.image
        })

        this.socket.emit('cs send message', this.text, this.currentOnlineObject.enterpriseID, this.cs.csID, this.currentOnlineObject.customerID)
        clearTimeout(this.onlineList[this.onlineIndex].timer)
        let customerID = this.onlineList[this.onlineIndex].customerID
        let csSocket = this.socket
        this.onlineList[this.onlineIndex].timer = setTimeout(
          function () {
            customerOutMessage(csSocket, customerID)
          }, 1000000)
        this.text = ''
      }
    },

    // 发送按钮
    buttonInputing (e) {
      console.log('[method: buttonInputing]')
      if (!this.hangon) {
        alert('该用户已挂断！')
        this.text = ''
        return
      }

      // 将输入的信息存入数据库，下标考虑
      let index = this.currentOnlineObject.messages.length
      let vm = this
      // 输入为空直接退出
      if (this.text.length === 0) {
        return
      }

      this.item = { 'email': this.cs.csID }
      vm.$http.post(vm.apiChattinglogGetCsID, this.item)
        .then((response) => {
          vm.$set(this, 'databaseCsID', response.data)
          vm.$set(this, 'item', { 'client_id': this.currentOnlineObject.customerID, 'service_id': this.databaseCsID, 'content': this.currentOnlineObject.messages[index].text, 'is_client': 0 })
          this.saveChattingLog(this.item)
        }, (response) => {
          alert('cs button inputing error!')
          window.location.href = '../se_login'
        })

      if (this.text.length !== 0) {
        this.currentOnlineObject.messages.push({
          text: this.text,
          date: new Date(),
          self: true,
          image: this.cs.image
        })
        this.socket.emit('cs send message', this.text, this.currentOnlineObject.enterpriseID, this.cs.csID , this.currentOnlineObject.customerID)
        clearTimeout(this.onlineList[this.onlineIndex].timer)
        let customerID = this.onlineList[this.onlineIndex].customerID
        let csSocket = this.socket
        this.onlineList[this.onlineIndex].timer = setTimeout(
          function () {
            customerOutMessage(csSocket, customerID)
          }, 1000000)
        this.text = ''
      }
    },

    // 点击切换查看历史记录信息或当前记录信息
    switchoff () {
      console.log('[method: switchoff]')
      this.hangon = !this.hangon
      this.onlineIndex = 0
      this.offlineIndex = 0
    },

    // 显示历史记录按钮
    showHistory (e) {
      console.log('[method: showHistory]')
      if (!this.hangon) {
        alert('无法获取历史消息！')
        return
      }

      var vm = this
      this.item = { 'email': this.cs.csID }
      vm.$http.post(vm.apiChattinglogGetCsID, this.item)
        .then((response) => {
          vm.$set(this, 'databaseCsID', response.data)
          vm.$set(this, 'item', {'client_id': this.currentOnlineObject.customerID, 'service_id': this.databaseCsID })
          this.getHistoryLog(this.item)
        })
    },

    // 获取客服信息
    getCsInfomation () {
      console.log('[method: getCsInfomation]')
      var that = this
      that.$http.post(that.apiCustomerserviceShowUserStatus)
        .then((response) => {
          if (response.data === 'ERROR, currentOnlineObject is broken.') {
            window.location.href = '../se_login'
          } else if (response.data === 'ERROR, wrong email.') {
            window.location.href = '../se_login'
          } else {
            that.cs.csID = response.data.email
            that.cs.csName = response.data.nickname
            that.cs.enterpriseID = response.data.admin_nickname
          }
        }, (response) => {
          window.location.href = '../se_login'
        })
    },

    // 转接用户按钮
    switchAnotherCs (e) {
      console.log('[method: switchAnotherCs]')
      if (!this.hangon) {
        alert('无法为已挂断的用户进行转接！')
        return
      }

      let that = this
      let customerID = that.onlineList[that.onlineIndex].customerID
      let enterpriseID = that.onlineList[that.onlineIndex].enterpriseID
      that.socket.emit('cs apply to transfer for customer', enterpriseID, customerID)
    },

    // 登出按钮
    csLogout (e) {
      console.log('[method: csLogout]')
      this.socket.emit('log out')
      for (let i = 0; i < this.onlineList.length; i++) {
        clearTimeout(this.onlineList[i].timer)
      }
      this.isLogon = false
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

  components: {
    robotSetting
  },

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
  background: #176994 url(../index/assets/bg.jpg);
  background-size: cover;
}

ul {
  list-style: none;
}

 ::-webkit-scrollbar {
  wIDth: 8px;
}

 ::-webkit-scrollbar-track {
  background-color: #bee1eb;
}

 ::-webkit-scrollbar-thumb {
  background-color: #00aff0;
}

 ::-webkit-scrollbar-thumb<a href="https://www.baIDu.com/s?wd=%3Ahover&tn=44039180_cpr&fenlei=mv6quAkxTZn0IZRqIHckPjm4nH00T1YdnHT4rHIWm1fdujPWPjbL0ZwV5Hcvrjm3rH6sPfKWUMw85HfYnjn4nH6sgvPsT6KdThsqpZwYTjCEQLGCpyw9Uz4Bmy-bIi4WUvYETgN-TLwGUv3EP1RkPjRYP1TvPHf3rjRsnW0Y" target="_blank" class="baIDu-highlight">:hover</a> {
  background-color: #9c3
}

 ::-webkit-scrollbar-thumb:active {
  background-color: #00aff0
}



/*主要界面*/

.container {
  height: 100%;
  wIDth: 100%;
}

.sIDebar,
.main,
.information {
  height: 100%;
}

.sIDebar {
  float: left;
  wIDth: 20%;
  color: #f4f4f4;
  background-color: #2e3238;
  overflow-x: hIDden;
  overflow-y: visible;
}

.main {
  position: relative;
  overflow: hIDden;
  background-color: #eee;
  wIDth: 60%;
}

.information {
  float: right;
  wIDth: 20%;
  color: #f4f4f4;
  background-color: #2e3238;
  overflow: hIDden;
}

.main-menu {
  position: absolute;
  wIDth: 100%;
  bottom: 160px;
  left: 0;
  height: 20px;
  background-color: white;
}

.main-text {
  position: absolute;
  wIDth: 100%;
  bottom: 0;
  left: 0;
  height: 160px;
}

.main-message {
  height: calc(100% - 180px);
}

.main-card {
  padding: 12px;
  border-bottom: solID 1px #24272C;
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
  -webkit-text-stroke-wIDth: 0.2px;
  -moz-osx-font-smoothing: grayscale;
}

.iconfont1 {
  font-family: "iconfont" !important;
  font-size: 16px;
  font-style: normal;
  -webkit-font-smoothing: antialiased;
  -webkit-text-stroke-wIDth: 0.2px;
  -moz-osx-font-smoothing: grayscale;
}

.customer-avatar,
.customer-name {
  vertical-align: mIDdle;
}

.customer-avatar {
  border-radius: 2px;
}

.customer-name {
  display: inline-block;
  margin: 0 0 0 15px;
  font-size: 16px;
}

.managebox {
  display: none;
  wIDth: 100px;
  border: 1px solID #eee;
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
  border: 1px solID #eee;
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
  wIDth: 100%;
  font-size: 12px;
  color: #fff;
  height: 30px;
  line-height: 30px;
  border: solID 1px #3a3a3a;
  border-radius: 4px;
  outline: none;
  background-color: #26292E;
}

.main-ul {
  height: calc(100% - 105px);
  overflow-y: scroll;
  overflow-x: hIDden;
}

.main-ul a:hover {
  cursor: pointer;
  background-color: gray;
}

.main-list {
  padding: 12px 15px;
  border-bottom: 1px solID #292C33;
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
  vertical-align: mIDdle;
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

.r-modal {
  position: absolute;
  background: white;
  padding: 270px;
}

#chat {
  margin: 20px auto;
  wIDth: 800px;
  height: 600px;
  overflow: hIDden;
  border-radius: 3px;
}
</style>
