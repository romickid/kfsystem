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
                    <Modal v-model="addSentence" title="增添语料" @on-ok="robotSentenceAddOk" @on-cancel="robotSentenceAddCancel">
                      <Form :label-width="80">
                        <Form-item label="问题">
                          <Input type="text" placeholder="请输入问题" v-model="robotSentence.question" @on-blur="checkQuestion" @on-focus="questionInput"></Input>
                          <i-label v-if="robotSentence.questionIsNull">
                            <p class='waring'>问题不能为空</p>
                          </i-label>
                        </Form-item>
                        <Form-item label="回答">
                          <Input type="text" placeholder="请输入回答" v-model="robotSentence.reply" @on-blur="checkReply" @on-focus="replyInput"></Input>
                          <i-label v-if="robotSentence.replyIsNull">
                            <p class='waring'>回答不能为空</p>
                          </i-label>
                        </Form-item>
                        <Form-item label="关键词">
                          <Input type="text" placeholder="请输入关键词" v-model="robotSentence.keyword" @on-blur="checkKeyword" @on-focus="keywordInput"></Input>
                          <p>关键词最好为问题中的重点词汇</p>
                          <i-label v-if="robotSentence.keywordIsNotStandard">
                            <p class='waring'>关键词不合法</p>
                          </i-label>
                          <Button icon="ios-plus-empty" type="dashed" size="small" @click="robotKeywordAdd">添加关键词</Button>
                          <Tag v-for="item in robotSentence.keywordArray" :name="item" closable @on-close="robotKeywordClose">{{ item }}</Tag>
                        </Form-item>
                        <Form-item label="权重">
                          <Select v-model="robotSentence.weight" style="width:200px">
                            <Option v-for="item in robotSentence.weightArray" :value="item.value" :key="item.value">{{ item.label }}</Option>
                          </Select>
                        </Form-item>
                      </Form>
                    </Modal>
                  </Dropdown-item>
                  <Dropdown-item>
                    <Button @click="modifySentence=true">编辑语料</Button>
                    <Modal v-model="modifySentence" title="编辑语料" z-index=40>
                      <robot-setting ref="robotSetting"></robot-setting>
                      <div slot="footer"></div>
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
                <li>
                  <p v-if="item.isText">{{ item.text }}</p>
                  <img :src='item.img' v-else @click='showHistoryBigImg(item.label)'>
                </li>
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
                <li>
                  <p v-if="item.isText">{{ item.text }}</p>
                  <img :src='item.img' v-else @click='showBigImg(item.bigImg)'>
                </li>
              </div>
            </div>
          </li>
        </ul>
      </div>
      <Modal v-model="modalShowBigImg" width='auto'>
        <p slot="header">
        </p>
        <div style="text-align:center">
            <img :src="bigImgSrc">
        </div>
        <div slot="footer">
        </div>
      </Modal>
      <div class="main-text" @keydown="keyboardInputing">
        <Button @click="showHistory">历史消息</Button>
        <Button @click="switchAnotherCs">转接</Button>
        <img @click="imageUpload" src="./assets/pic.png" style="height:20px;width:20px" class='send-pic'></img>
        <p class="lead emoji-picker-container">
          <textarea class="textarea" placeholder="按 Enter 发送" v-model="chatlogData.text" rows="5" data-emojiable="true"></textarea>
        </p>
        <Button class="submit-button" @click="buttonInputing">发送</Button>
        <input id="inputFile" name='inputFile' type='file' accept="image/png, image/jpeg, image/gif, image/jpg" style="display: none" @change="imageCompress">
      </div>
    </div>
  </div>
</template>

<script>
import * as io from 'socket.io-client'
import Vue from 'vue'
import robotSetting from '../../components/robot_setting'
import lrz from '../../../node_modules/lrz/dist/lrz.bundle.js'
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
  return findOnlineListByCustomerID(offlineList, customerID)
}

// 接收文字消息放进onlinelist
function pushTextToOnlineList (onlineList, index, msg) {
  console.log('[function: pushTextToOnlineList]')
  onlineList[index].messages.push({
    text: msg,
    isText: true,
    date: new Date(),
    image: '../../../static/3.jpg'
  })
}

// 接收文字消息放进offlinelist
function pushTextToOfflineList (offlineList, index, msg) {
  return pushTextToOnlineList(offlineList, index, msg)
}

// 接收图片消息放进onlinelist
function pushImgToOnlineList (onlineList, index, bpic, spic) {
  console.log('[function: pushTextToOnlineList]')
  onlineList[index].messages.push({
    img: spic,
    bigImg: bpic,
    isText: false,
    date: new Date(),
    image: '../../../static/3.jpg'
  })
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
      uncheck: 0
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

      // 修改语料对话框
      modifySentence: false,

      // 增添语料对话框
      addSentence: false,

      // 设置机器人
      robotSentence: {
        question: '',
        keyword: '',
        keywordArray: [],
        reply: '',
        weight: 2,
        weightArray: [
          {
            value: 3,
            label: '高'
          },
          {
            value: 2,
            label: '中'
          },
          {
            value: 1,
            label: '低'
          }
        ],
        questionIsNull: false,
        replyIsNull: false,
        keywordIsNotStandard: false
      },

      // 聊天数据
      // 文本框中输入的内容
      chatlogData: {
        text: '',
        img: '',
        bigImg: ''
      },

      // 显示大图片
      bigImgSrc: '',
      modalShowBigImg: false,

      // api参数
      saveTextItem: {},
      csEmailItem: {},
      saveImgItem: {},
      saveBigImgItem: {},
      showHistoryItem: {},
      showHistoryBigImgItem: {},
      robotSentenceAddItem: {},

      // 客服对应的socket
      socket: '',

      // api
      apiChattinglogSendMessage: '../api/chattinglog_send_message/',
      apiChattinglogShowHistory: '../api/chattinglog_show_history/',
      apiCustomerserviceShowUserStatus: '../api/customerservice_show_user_status/',
      apiChattinglogGetCsId: '../api/chattinglog_get_cs_ID/',
      apiBigimagelogSendImage: '../api/bigimagelog_send_image/',
      apiSmallimagelogSendImage: '../api/smallimagelog_send_image/',
      apiBigimagelogShowSingleHistory: '../api/bigimagelog_show_single_history/',
      apiLogShowHistory: '../api/log_show_history/',
      apiCustomerserviceSetrobotinfoCreate: '../api/customerservice_setrobotinfo_create/',
      apiCustomerserviceLogout: '../api/customerservice_logout/',

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
          historyMessages: []
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
      let onlineIndex = findOnlineListByCustomerID(that.onlineList, customerID)
      pushTextToOnlineList(that.onlineList, onlineIndex, msg)

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
        that.onlineList[0].uncheck++ // 因此uncheck也要++
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
    this.socket.on('customer send picture', function (bpic, spic, enterpriseID, csID, customerID) {
      console.log('socket: customer send picture')
      let onlineIndex = findOnlineListByCustomerID(that.onlineList, customerID)
      pushImgToOnlineList(that.onlineList, onlineIndex, bpic, spic)

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

    this.socket.on('cs reload old socket', function (former_customerinfo) {
      console.log('socket: cs reload old socket')
      console.log(former_customerinfo)
      for (let i=0; i<former_customerinfo.length; i++) {
        let customer = createCustomer(former_customerinfo[i].customer_id, former_customerinfo[i].customer_id, former_customerinfo[i].enterprise_id)
        addCustomer(that.socket, that.onlineList, customer)
        console.log(that.onlineList)
        if (that.onlineList.length !== 1) { // 新增客服显示未读消息
          customer.uncheck++
        }
        if (that.hangon && that.onlineList.length !== 1) { // 如果是处于Hangon, 当前显示的要位于列表第二位
          that.onlineIndex++
        }
      }
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
    onlineList: {
      deep: true,
      handler () {
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
    // // 保存文字信息
    // saveChattingLog (obj) {
    //   console.log('[method: saveChattingLog]')
    //   let vm = this
    //   vm.$http.post(vm.apiChattinglogSendMessage, obj)
    //     .then((response) => {
    //       vm.$set(this, 'item', {})
    //     }, (response) => {
    //       alert('save chatting log error!')
    //       alert(obj)
    //       window.location.href = '../se_login'
    //     })
    // },

    // // 获取历史信息
    // getHistoryLog (obj) {
    //   console.log('[method: getHistoryLog]')
    //   let vm = this
    //   vm.$http.post(vm.apiChattinglogShowHistory, obj)
    //     .then((response) => {
    //       for (var p in response.data) {
    //         if (response.data[p].is_client === false) {
    //           this.currentOnlineObject.historyMessages.push({
    //             text: response.data[p].content,
    //             date: response.data[p].time,
    //             self: true,
    //             image: this.cs.image
    //           })
    //         } else {
    //           this.currentOnlineObject.historyMessages.push({
    //             text: response.data[p].content,
    //             date: response.data[p].time,
    //             image: '../../../static/3.jpg'
    //           })
    //         }
    //       }
    //     })
    // },

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

    // enter操作
    keyboardInputing (e) {
      console.log('[method: keyboardInputing]')
      if (e.keyCode === 13 && this.chatlogData.text.length && this.currentOnlineObject.customerID !== -1) {
        if (!this.hangon) {
          alert('该用户已挂断！')
          this.chatlogData.text = ''
          return
        }

        this.currentOnlineObject.messages.push({
          text: this.chatlogData.text,
          isText: true,
          date: new Date(),
          self: true,
          image: this.cs.image
        })
        // 存入数据库
        let index = this.currentOnlineObject.messages.length
        this.saveText(index - 1)

        this.socket.emit('cs send message', this.chatlogData.text, this.currentOnlineObject.enterpriseID, this.cs.csID, this.currentOnlineObject.customerID)
        clearTimeout(this.onlineList[this.onlineIndex].timer)
        let customerID = this.onlineList[this.onlineIndex].customerID
        let csSocket = this.socket
        this.onlineList[this.onlineIndex].timer = setTimeout(
          function () {
            customerOutMessage(csSocket, customerID)
          }, 1000000)
        this.chatlogData.text = ''
      }
    },

    // 发送按钮
    buttonInputing (e) {
      console.log('[method: buttonInputing]')
      if (!this.hangon) {
        alert('该用户已挂断！')
        this.chatlogData.text = ''
        return
      }

      if (this.chatlogData.text.length !== 0 && this.currentOnlineObject.customerID !== -1) {
        this.currentOnlineObject.messages.push({
          text: this.chatlogData.text,
          date: new Date(),
          isText: true,
          self: true,
          image: this.cs.image
        })
        // 存入数据库
        let index = this.currentOnlineObject.messages.length
        this.saveText(index - 1)

        this.socket.emit('cs send message', this.chatlogData.text, this.currentOnlineObject.enterpriseID, this.cs.csID, this.currentOnlineObject.customerID)
        clearTimeout(this.onlineList[this.onlineIndex].timer)
        let customerID = this.onlineList[this.onlineIndex].customerID
        let csSocket = this.socket
        this.onlineList[this.onlineIndex].timer = setTimeout(
          function () {
            customerOutMessage(csSocket, customerID)
          }, 1000000)
        this.chatlogData.text = ''
      }
    },

    imgInputing () {
      console.log('[method: imgInputing]')
      if (!this.hangon) {
        alert('该用户已挂断！')
        this.chatlogData.img = ''
        return
      }
      if (this.chatlogData.img !== 0 && this.currentOnlineObject.customerID !== -1) {
        this.currentOnlineObject.messages.push({
          img: this.chatlogData.img,
          bigImg: this.chatlogData.bigImg,
          isText: false,
          date: new Date(),
          self: true,
          image: this.cs.image
        })
        let index = this.currentOnlineObject.messages.length
        this.saveImg(index - 1)
        this.socket.emit('cs send picture', this.chatlogData.bigImg, this.chatlogData.img, this.currentOnlineObject.enterpriseID, this.cs.csID, this.currentOnlineObject.customerID)
        clearTimeout(this.onlineList[this.onlineIndex].timer)
        let customerID = this.onlineList[this.onlineIndex].customerID
        let csSocket = this.socket
        this.onlineList[this.onlineIndex].timer = setTimeout(
          function () {
            customerOutMessage(csSocket, customerID)
          }, 1000000)
        this.chatlogData.img = ''
        this.chatlogData.bigImg = ''
      }
    },

    // 点击切换查看历史记录信息或当前记录信息
    switchoff () {
      console.log('[method: switchoff]')
      this.hangon = !this.hangon
      this.onlineIndex = 0
      this.offlineIndex = 0
    },

    // 获取客服信息
    getCsInfomation () {
      console.log('[method: getCsInfomation]')
      var that = this
      that.$http.post(that.apiCustomerserviceShowUserStatus)
        .then((response) => {
          if (response.data === 'ERROR, session is broken.') {
            // window.location.href = '../se_login'
            console.log('getCsInfomation1')
          } else if (response.data === 'ERROR, wrong email.') {
            // window.location.href = '../se_login'
            console.log('getCsInfomation2')
          } else {
            that.cs.csID = response.data.email
            that.cs.csName = response.data.nickname
            that.cs.enterpriseID = response.data.admin_nickname
            that.csEmailItem = { 'email': that.cs.csID }
            console.log(that.cs.csID)
            that.getCsIdApi()
          }
        }, (response) => {
          // window.location.href = '../se_login'
          console.log('getCsInfomation3')
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
      this.csLogoutApi()
    },

    csLogoutApi () {
      console.log('[method: csLogoutApi]')
      this.$http.post(this.apiCustomerserviceLogout)
        .then((response) => {
          if (response.data === 'ERROR, session is broken.') {
            // window.location.href = '../se_login'
            console.log('csLogoutApi1')
          } else if (response.data === 'ERROR, wrong email.') {
            // window.location.href = '../se_login'
            console.log('csLogoutApi2')
          } else {
            window.location.href = '../se_login'
          }
        }, (response) => {
          // window.location.href = '../se_login'
          console.log('csLogoutApi3')
        })
    },

    // 机器人语料检查问题输入
    checkQuestion () {
      console.log('[method: checkQuestion]')
      if (this.robotSentence.question === '') {
        this.robotSentence.questionIsNull = true
      }
    },

    // 机器人语料检查回答输入
    checkReply () {
      console.log('[method: checkReply]')
      if (this.robotSentence.reply === '') {
        this.robotSentence.replyIsNull = true
      }
    },

    // 机器人语料检查关键词输入
    checkKeyword () {
      console.log('[method: checkKeyword]')
      let reg = /^[\u4E00-\u9FA5]+$/
      let standardContent = reg.test(this.robotSentence.keyword)
      if (this.robotSentence.keyword === '' || standardContent === false) {
        this.robotSentence.keywordIsNotStandard = true
      }
    },

    // 正在输入回答
    replyInput () {
      console.log('[method: replyInput]')
      this.robotSentence.replyIsNull = false
    },

    // 正在输入问题
    questionInput () {
      console.log('[method: questionInput]')
      this.robotSentence.questionIsNull = false
    },

    // 正在输入关键词
    keywordInput () {
      console.log('[method: keywordInput]')
      this.robotSentence.keywordIsNotStandard = false
    },

    // 添加关键词按钮
    robotKeywordAdd () {
      console.log('[method: robotKeywordAdd]')
      this.checkKeyword()
      let keywordIsExist = false
      for (let i = 0; i < this.robotSentence.keywordArray.length; i++) {
        if (this.robotSentence.keyword === this.robotSentence.keywordArray[i]) {
          keywordIsExist = true
        }
      }
      if (this.robotSentence.keyword === '' || this.robotSentence.keywordIsNotStandard === true) {
        this.$Message.info('关键词格式不正确')
      } else if (keywordIsExist === true) {
        this.$Message.info('该关键词已添加')
      } else {
        this.robotSentence.keywordArray.push(this.robotSentence.keyword)
        this.robotSentence.keyword = ''
      }
    },

    // 删除关键词
    robotKeywordClose (event, name) {
      console.log('[method: robotKeywordClose]')
      const index = this.robotSentence.keywordArray.indexOf(name)
      this.robotSentence.keywordArray.splice(index, 1)
    },

    // 确认添加机器人语料
    robotSentenceAddOk () {
      console.log('[method: robotSentenceAddOk]')
      let keywordString = ''
      if (this.robotSentence.question === '' || this.robotSentence.reply === '') {
        this.$Message.info('您所填的信息不能为空')
      } else {
        if (this.robotSentence.keywordArray.length !== 0) {
          keywordString = this.robotSentence.keywordArray.join(' ')
        } else {
          keywordString = ''
        }
        this.robotQuestionAdd = {
          'question': this.question,
          'answer': this.reply,
          'keyword': keywordString,
          'weight': this.modelSelect
        }
        this.setRobotApi()
      }
      this.robotSentenceAddCancel()
    },

    // 取消添加机器人语料
    robotSentenceAddCancel () {
      console.log('[method: robotSentenceAddCancel]')
      this.robotSentence.question = ''
      this.robotSentence.reply = ''
      this.robotSentence.keyword = ''
      this.robotSentence.weight = 2
      this.robotSentence.replyIsNull = false
      this.robotSentence.questionIsNull = false
      this.robotSentence.keywordIsNotStandard = false
      this.robotSentence.keywordArray = []
    },

    // 设置机器人语料访问后端接口
    setRobotApi () {
      console.log('[method: setRobotApi]')
      this.$http.post(this.apiCustomerserviceSetrobotinfoCreate, this.robotSentenceAddItem)
        .then((response) => {
          if (response.data === 'ERROR, invalid data in serializer.') {
            // window.location.href = '../se_login'
            console.log('set_robot_api1')
          } else if (response.data === 'ERROR, incomplete information.') {
            this.$Message.info('您所填的信息不完整')
          } else if (response.data === 'ERROR, wrong information.') {
            // window.location.href = '../se_login'
            console.log('set_robot_api2')
          } else if (response.data === 'ERROR, session is broken.') {
            // window.location.href = '../se_login'
            console.log('set_robot_api3')
          } else if (response.data === 'ERROR, wrong email.') {
            // window.location.href = '../se_login'
            console.log('set_robot_api4')
          } else if (response.data === 'ERROR, info is exist.') {
            this.$Message.info('该问题已存在')
          } else {
            this.$Message.info('添加成功')
            this.$refs.robotSetting.show_robot_question_api()
          }
        }, (response) => {
          // window.location.href = '../se_login'
          console.log('set_robot_api5')
        })
    },

    // 文件压缩
    imageCompress () {
      console.log('[method: imageCompress]')
      let self = this
      let obj = document.getElementById('inputFile')
      let file = obj.files[0]
      lrz(file, {width: 1280, height: 1280, quality: 1})
        .then(function (rst) {
          self.chatlogData.bigImg = rst.base64
          lrz(rst.origin, {width: 300, height: 300, quality: 0.7})
            .then(function (rst) {
              self.chatlogData.img = rst.base64
              self.imgInputing()
              return rst
            })
          return rst
        })
      obj.value = ''
    },

    // 上传图片
    imageUpload () {
      console.log('[method: imageUpload]')
      var file = document.getElementById('inputFile')
      file.click()
    },

    // 显示大图片
    showBigImg (bigImg) {
      console.log('[method: showBigImg]')
      this.bigImgSrc = bigImg
      this.modalShowBigImg = true
    },

    // 保存文字
    saveText (index) {
      console.log('[method: saveText]')
      this.saveTextItem = {
        'client_id': this.currentOnlineObject.customerID,
        'service_id': this.databaseCsID,
        'content': this.currentOnlineObject.messages[index].text,
        'is_client': 0
      }
      console.log(this.saveTextItem)
      this.saveTextApi()
    },

    // 保存文字调用后端api
    saveTextApi () {
      console.log('[method: saveTextApi]')
      this.$http.post(this.apiChattinglogSendMessage, this.saveTextItem)
        .then((response) => {
          this.saveTextItem = {}
        }, (response) => {
          // window.location.href = '../se_login'
          console.log('save_text_api')
        })
    },

    // 获取databaseCsID
    getCsIdApi () {
      console.log('[method: getCsIdApi]')
      this.$http.post(this.apiChattinglogGetCsId, this.csEmailItem)
        .then((response) => {
          this.databaseCsID = response.data
          console.log(this.databaseCsID)
        }, (response) => {
          // window.location.href = '../se_login'
          console.log('get_cs_id_api')
        })
    },

    // 存小图片调用后端api
    saveImgApi () {
      console.log('[method: saveImgApi]')
      this.$http.post(this.apiSmallimagelogSendImage, this.saveImgItem)
        .then((response) => {
          if (response.data === 'ERROR, invalid data in serializer.') {
            // window.location.href = '../notfound'
            console.log('save_img_api1')
          } else {
            this.saveImgItem = {}
          }
        }, (response) => {
          // window.location.href = '../notfound'
          console.log('save_img_api2')
        })
    },

    // 存大图片调用后端api
    saveBigImgApi () {
      console.log('[method: saveBigImgApi]')
      this.$http.post(this.apiBigimagelogSendImage, this.saveBigImgItem)
        .then((response) => {
          if (response.data === 'ERROR, invalid data in serializer.') {
            // window.location.href = '../notfound'
            console.log('save_bigImg_api1')
          } else {
            this.saveBigImgItem = {}
          }
        }, (response) => {
          // window.location.href = '../notfound'
          console.log('save_bigImg_api2')
        })
    },

    // 存图片的函数
    saveImg (index) {
      console.log('[method: saveImg]')
      let timestamp = new Date().getTime()
      let label = timestamp + this.databaseCsID
      this.saveImgItem = {
        'client_id': this.currentOnlineObject.customerID,
        'service_id': this.databaseCsID,
        'image': this.currentOnlineObject.messages[index].img,
        'is_client': false,
        'label': label
      }
      this.saveBigImgItem = {
        'client_id': this.currentOnlineObject.customerID,
        'service_id': this.databaseCsID,
        'image': this.currentOnlineObject.messages[index].bigImg,
        'is_client': false,
        'label': label
      }
      console.log(this.saveImgItem)
      console.log(this.saveBigImgItem)
      this.saveImgApi()
      this.saveBigImgApi()
    },

    // 显示历史记录按钮的响应函数
    showHistory (e) {
      console.log('[method: showHistory]')
      if (!this.hangon) {
        alert('无法获取历史消息！')
        return
      }
      this.showHistoryItem = {
        'client_id': this.currentOnlineObject.customerID,
        'service_id': this.databaseCsID
      }
      console.log(this.showHistoryItem)
      this.showHistoryApi()
    },

    // 显示历史记录调用后端api
    showHistoryApi () {
      console.log('[method: showHistoryApi]')
      this.$http.post(this.apiLogShowHistory, this.showHistoryItem)
        .then((response) => {
          if (response.data === 'ERROR, invalid data in serializer.') {
            // window.location.href = '../notfound'
            console.log('show_history_api1')
          } else {
            console.log(response.data)
            let historyArray = response.data
            this.printHistoryMessages(historyArray)
          }
        }, (response) => {
          // window.location.href = '../notfound'
          console.log('show_history_api2')
        })
    },

    // 打印历史消息函数
    printHistoryMessages (historyArray) {
      console.log('[method: printHistoryMessages]')
      for (var p = 0; p < historyArray.length; p++) {
        console.log(historyArray[p].hasOwnProperty('content'))
        if (historyArray[p].hasOwnProperty('content')) {
          if (historyArray[p].is_client === false) {
            this.currentOnlineObject.historyMessages.push({
              text: historyArray[p].content,
              isText: true,
              date: historyArray[p].time,
              self: true,
              image: this.cs.image
            })
          } else {
            this.currentOnlineObject.historyMessages.push({
              text: historyArray[p].content,
              isText: true,
              date: historyArray[p].time,
              image: '../../../static/3.jpg'
            })
          }
        } else {
          if (historyArray[p].is_client === false) {
            this.currentOnlineObject.historyMessages.push({
              img: historyArray[p].image,
              isText: false,
              label: historyArray[p].label,
              date: historyArray[p].time,
              self: true,
              image: this.cs.image
            })
            let index = this.currentOnlineObject.historyMessages.length
            console.log('this.hsession.messages1')
            console.log(this.currentOnlineObject.historyMessages[index - 1])
          } else {
            this.currentOnlineObject.historyMessages.push({
              img: historyArray[p].image,
              isText: false,
              label: historyArray[p].label,
              date: historyArray[p].time,
              image: '../../../static/3.jpg'
            })
            let index = this.currentOnlineObject.historyMessages.length
            console.log('this.hsession.messages2')
            console.log(this.currentOnlineObject.historyMessages[index - 1])
          }
        }
      }
    },

    // 历史记录显示大图片
    showHistoryBigImg (label) {
      console.log('[method: showHistoryBigImg]')
      this.showHistoryBigImgItem = {
        'client_id': this.currentOnlineObject.customerID,
        'service_id': this.databaseCsID,
        'label': label
      }
      this.showHistoryBigImgApi()
    },

    // 历史记录显示大图片调用后端api
    showHistoryBigImgApi () {
      console.log('[method: showHistoryBigImgApi]')
      this.$http.post(this.apiBigimagelogShowSingleHistory, this.showHistoryBigImgItem)
        .then((response) => {
          if (response.data === 'ERROR, no history.') {
            // window.location.href = '../notfound'
            console.log('show_history_big_img_api1')
          } else {
            this.showHistoryBigImgItem = {}
            this.showBigImg(response.data)
          }
        }, (response) => {
          // window.location.href = '../notfound'
          console.log('show_history_big_img_api2')
        })
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

.send-pic {
  float: right;
  margin-right: 0.6em;
}
</style>
