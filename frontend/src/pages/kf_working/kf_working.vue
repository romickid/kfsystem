<template>
  <div class="container">
    <div class="information">
      <ul v-if="hangon" class="userinfo">
        <li v-for="item in userInformation">{{ item }}</li>
      </ul>
    </div>
    <div class="sidebar">
      <div class="main-card">
        <header>
          <img class="user-avatar" width="40" height="40" :alt="user.name" :src="user.image">
          <Dropdown>
            <a href="javascript:void(0)">
              <p class="user-name">{{ user.name }}</p>
              <Icon type="arrow-down-b"></Icon>
            </a>
            <Dropdown-menu slot="list">
              <Dropdown-item>
                <Button @click="logout">
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
                    <Modal v-model="addSentence" title="增添语料" @on-ok="ok_add" @on-cancel="cancel_add">
                      <Form :label-width="80">
                        <Form-item label="问题">
                          <Input type="text" placeholder="请输入问题" v-model="question" @on-blur="checkQuestion" @on-focus="questionInput"></Input>
                          <i-label v-if="questionIsNull">
                            <p class='waring'>问题不能为空</p>
                          </i-label>
                        </Form-item>
                        <Form-item label="回答">
                          <Input type="text" placeholder="请输入回答" v-model="reply" @on-blur="checkReply" @on-focus="replyInput"></Input>
                          <i-label v-if="replyIsNull">
                            <p class='waring'>回答不能为空</p>
                          </i-label>
                        </Form-item>
                        <Form-item label="关键词">
                          <Input type="text" placeholder="请输入关键词" v-model="keyword" @on-blur="checkKeyword" @on-focus="keyWordInput"></Input>
                          <p>关键词最好为问题中的重点词汇</p>
                          <i-label v-if="keywordIsNotStandard">
                            <p class='waring'>关键词不合法</p>
                          </i-label>
                          <Button icon="ios-plus-empty" type="dashed" size="small" @click="handleAdd">添加关键词</Button>
                          <Tag v-for="item in robotKeyWord" :name="item" closable @on-close="handleClose">{{ item }}</Tag>
                        </Form-item>
                        <Form-item label="权重">
                          <Select v-model="modelSelect" style="width:200px">
                            <Option v-for="item in robotWeight" :value="item.value" :key="item.value">{{ item.label }}</Option>
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
          <li class="main-list" v-for="item in userList" :class="{ choosed: session.userId === item.id }" @click="select(item)">
            <a>
              <Badge :count="item.uncheck" overflow-count="999">
                <img class="main-avatar" width="30" height="30" :alt="item.name" :src="item.image">
              </Badge>
              <p class="main-name">{{ item.name }}</p>
            </a>
          </li>
        </ul>
        <ul v-if="!hangon">
          <div>
            <p align="center" color="#cccccc" @click="switchoff">
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
          <li class="message-list" v-for="item in hsession.messages">
            <p class="message-time">
              <span class="time-span">{{ item.date | time }}</span>
            </p>
            <div class="massage-main" :class="{ self: item.self }">
              <img class="massage-avatar" width="30" height="30" :src="item.image" />
              <div class="massage-text">
                <li>
                  <p v-if="item.isText">{{ item.text }}</p>
                  <img :src='item.img' v-else @click='showHistoryBigImg(item.label)'>
                </li>
              </div>
            </div>
          </li>
          <li v-if="currentNumber" class="message-list" v-for="item in session.messages">
            <p class="message-time">
              <span class="time-span">{{ item.date | time }}</span>
            </p>
            <div class="massage-main" :class="{ self: item.self }">
              <img class="massage-avatar" width="30" height="30" :src="item.image" />
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
      <Modal v-model="modal2" width='auto'>
        <p slot="header">
        </p>
        <div style="text-align:center">
            <img :src="bigImgBase64">
        </div>
        <div slot="footer">
        </div>
      </Modal>
      <div class="main-text" @keydown="inputing">
        <Button @click="showHistory">历史消息</Button>
        <Button @click="switchServer">转接</Button>
        <img @click="imgupload" src="./assets/pic.png" style="height:20px;width:20px" class="send-pic"></img>
        <p class="lead emoji-picker-container">
          <textarea class="textarea" placeholder="按 Enter 发送" v-model="text" rows="5" data-emojiable="true"></textarea>
        </p>
        <Button class="submit-button" @click="buttoninputing">发送</Button>
        <input id="inputFile" name='inputFile' type='file' accept="image/png, image/jpeg, image/gif, image/jpg" style="display: none" @change="fileup">
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
/**
  * @description 通过id找聊天记录的索引
  */
function findSessionIndexById (session, id) {
  for (let i = 0; i < session.length; i++) {
    if (session[i].userId === id) {
      return i
    }
  }
  return -1
}
/**
  * @description 通过id找客户的索引
  */
function findUserIndexById (users, id) {
  for (let i = 0; i < users.length; i++) {
    if (users[i].id === id) {
      return i
    }
  }
  return -1
}
/**
  * @description 接收消息放进消息列表
  */
function pushMessages (sessionList, index, msg, isText, img, bigImg) {
  sessionList[index].messages.push({
    text: msg,
    img: img,
    bigImg: bigImg,
    isText: isText,
    date: new Date(),
    image: '../../../static/3.jpg'
  })
}
/**
  * @description 创建用户
  */
function createUser (userId, name, informationString) {
  let informationList = JSON.parse(informationString)
  return {
    id: userId,
    name: name,
    image: '../../../static/3.jpg',
    uncheck: 0,
    information: informationList
  }
}
/**
  * @description 向服务器发送消息说用户已挂断
  */
function customerOutMessage (socket, customerId) {
  socket.emit('customer out', customerId)
}
/**
  * @description 在列表中添加用户
  */
function addCustomer (socket, userList, sessionList,
   historySessionList, timers, informationList, customer) {
  userList.splice(0, 0, customer)
  sessionList.splice(0, 0, {
    userId: customer.id,
    messages: []
  })
  historySessionList.splice(0, 0, {
    userId: customer.id,
    messages: []
  })
  // 从第一次添加用户开始计时
  let timer = setTimeout(function () {
    customerOutMessage(socket, customer.id)
  }, 10000000)
  timers.splice(0, 0, timer)
  informationList.splice(0, 0, [
    '用户名： ' + customer.information.userName,
    '用户ID： ' + customer.information.userId,
    '详细信息： ' + customer.information.information
  ])
}
/**
  * @description 接受新消息时对应消息和用户的上浮
  */
function popUp (list, index) {
  let item = list[index]
  list.splice(index, 1)
  list.splice(0, 0, item)
}
/**
  * @description 用户挂断时将其添加到以挂断列表
  */
function customerHangoff (userList, hangoffUserList,
  sessionList, hangoffSessionList,
  historySessionList, id) {
  let userIndex = findUserIndexById(userList, id)
  let sessionIndex = findSessionIndexById(sessionList, id)
  let customer = userList[userIndex]
  let session = sessionList[sessionIndex]
  pushMessages(sessionList, sessionIndex, '用户' + id + '已挂断', true, '', '')
  hangoffUserList.splice(0, 0, customer)
  hangoffSessionList.splice(0, 0, session)
}
/**
  * @description 用户挂断时将其从活跃列表中删除
  */
function deleteCustomer (userList, sessionList, historySessionList, timers, informationList, id) {
  let userIndex = findUserIndexById(userList, id)
  let sessionIndex = findSessionIndexById(sessionList, id)
  userList.splice(userIndex, 1)
  sessionList.splice(sessionIndex, 1)
  historySessionList.splice(sessionIndex, 1)
  informationList.splice(sessionIndex, 1)
  let timer = timers.splice(sessionIndex, 1)
  clearTimeout(timer)
}

// 虚拟数据
if (!sessionStorage.getItem(key)) {
  let userData = {
    // 登录用户
    user: {
      id: 1,
      name: 'coffce',
      image: '../../../static/1.jpg'
    },
    // 用户列表
    userList: [],
    hangoffUserList: [],
    // 会话列表
    sessionList: [],
    hangoffSessionList: [],
    historySessionList: [],
    informationList: [],
    sessionIndex: 0,
    hangoffSessionIndex: 0,
    hangon: true,
    customerNumber: 0,
    hangoffCustomerNumber: 0,
    transferable: true,
    isLogon: false,
    timers: []
  }
  sessionStorage.setItem(key, JSON.stringify(userData))
}
export default {
  el: '#chat',
  data () {
    let dataserver = JSON.parse(sessionStorage.getItem(key))
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
      informationList: dataserver.informationList,
      // 选中的会话Index
      sessionIndex: dataserver.sessionIndex,
      hangoffSessionIndex: dataserver.hangoffSessionIndex,
      // 显示活跃消息
      hangon: dataserver.hangon,
      // 增添语料对话框
      addSentence: false,
      // 修改语料对话框
      modifySentence: false,
      // 设置机器人
      modal1: false,
      // 客服对应的socket
      socket: '',
      // 当前正在服务人数
      customerNumber: dataserver.customerNumber,
      hangoffCustomerNumber: dataserver.hangoffCustomerNumber,
      // 判断是否转接成功
      transferable: dataserver.transferable,
      // 判断刷新之前是否处于登录状态
      isLogon: dataserver.isLogon,
      // 记录每个用户计时器的ID
      timers: dataserver.timers,
      // test
      item: {},
      apiChattinglogSendMessage: '../api/chattinglog_send_message/',
      apiChattinglogShowHistory: '../api/chattinglog_show_history/',
      apiCustomerserviceShowUserStatus: '../api/customerservice_show_user_status/',
      apiChattinglogGetCsId: '../api/chattinglog_get_cs_id/',
      apiBigimagelogSendImage: '../api/bigimagelog_send_image/',
      apiSmallimagelogSendImage: '../api/smallimagelog_send_image/',
      apiBigimagelogShowSingleHistory: '../api/bigimagelog_show_single_history/',
      apiLogShowHistory: '../api/log_show_history/',
      history: false,
      turnId: '',
      // 聊天数据
      text: '',
      isText: true,
      img: '',
      bigImg: '',
      bigImgBase64: '',
      // 机器人
      apiCustomerserviceSetrobotinfoCreate: '../api/customerservice_setrobotinfo_create/',
      modal2: false,
      modelSelect: 2,
      robotWeight: [
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
      robotKeyWord: [],
      keyword: '',
      question: '',
      reply: '',
      replyIsNull: false,
      questionIsNull: false,
      keywordIsNotStandard: false,
      robot_question_add: {},
      keywordIsExist: false,
      keyword_add: '',
      // api参数
      save_text_item: {},
      cs_email_item: {},
      save_img_item: {},
      save_bigImg_item: {},
      show_history_item: {},
      show_history_big_img_item: {}
    }
  },
  computed: {
    /**
      * @description 返回当前选中的活跃消息，用于在聊天对话框中显示
      */
    session () {
      if (this.hangon && this.userList.length) {
        return this.sessionList[this.sessionIndex]
      } else if (!this.hangon && this.hangoffUserList.length) {
        return this.hangoffSessionList[this.hangoffSessionIndex]
      } else {
        return {
          userId: -1,
          messages: []
        }
      }
    },
    /**
      * @description 返回当前选中用户的历史消息，用于在聊天对话框顶部显示历史消息
      */
    hsession () {
      if (!this.userList.length) {
        return {
          userId: -1,
          messages: []
        }
      }
      return this.historySessionList[this.sessionIndex]
    },
    /**
      * @description 返回当前选中用户的相关信息，用于在界面右侧显示用户信息
      */
    userInformation () {
      if (!this.userList.length) {
        return []
      }
      return this.informationList[this.sessionIndex]
    },
    /**
      * @description 用于判断当前左侧用户列表用户数是否为零
      */
    currentNumber () {
      return (this.hangon && this.userList.length) || (!this.hangon && this.hangoffUserList.length)
    }
  },
  created () {
    this.getCsInfomation()
    const that = this
    this.socket = io('http://localhost:3000')
    /**
      * @description 当接收到用户发来的信息时，将信息存到对应用户的消息数组中，并将对应数据上浮
      */
    this.socket.on('customer message', function (msg, isText, img, bigImg, fromId, toId) {
      let index = findSessionIndexById(that.sessionList, fromId)
      pushMessages(that.sessionList, index, msg, isText, img, bigImg)
      // // 存入数据库
      // let vm = that
      // that.item = { 'email': toId }
      // vm.$http.post(vm.apiChattinglogGetCsId, that.item)
      //   .then((response) => {
      //     vm.$set(that, 'turnId', response.data)
      //     vm.$set(that, 'item', { 'client_id': fromId, 'service_id': that.turnId, 'content': msg, 'is_client': 1 })
      //     that.savedata(that.item)
      //   }, (response) => {
      //     window.location.href = '../se_login'
      //   })
      if (index !== that.sessionIndex) {
        popUp(that.userList, index)
        popUp(that.sessionList, index)
        popUp(that.historySessionList, index)
        popUp(that.timers, index)
        popUp(that.informationList, index)
        // clearTimeout(this.timers[0])
        let customerId = that.userList[0].id
        let serverSocket = that.socket
        that.timers[0] = setTimeout(
          function () {
            customerOutMessage(serverSocket, customerId)
          }, 100000000)
        console.log('that.sessionIndex: ' + that.sessionIndex)
        if (that.sessionIndex < index) {
          console.log('++')
          that.sessionIndex++
        }
        that.userList[0].uncheck++
      } else {
        clearTimeout(that.timers[that.sessionIndex])
        let customerId = that.userList[that.sessionIndex].id
        let serverSocket = that.socket
        that.timers[0] = setTimeout(
          function () {
            customerOutMessage(serverSocket, customerId)
          }, 100000000)
      }
    })
    /**
      * @description 用户第一次登陆时，用于用户相关数据的初始化
      */
    this.socket.on('add client', function (fromId, information) {
      let customer = createUser(fromId, fromId, information)
      addCustomer(that.socket, that.userList, that.sessionList,
         that.historySessionList, that.timers, that.informationList, customer)
      if (that.userList.length !== 1) {
        customer.uncheck++
      }
      if (that.hangon && that.userList.length !== 1) {
        that.sessionIndex++
      }
      pushMessages(that.sessionList, 0, '用户' + fromId + '已上线', true, '', '')
    })
    /**
      * @description 当用户挂断时，将其从活跃列表中删除，添加到已挂断列表
      */
    this.socket.on('customer hang off', function (customerId) {
      customerHangoff(that.userList, that.hangoffUserList,
        that.sessionList, that.hangoffSessionList,
        that.historySessionList, customerId)
      if (that.sessionIndex !== 0) {
        that.sessionIndex--
      }
      deleteCustomer(that.userList, that.sessionList, that.historySessionList, that.timers, that.informationList, customerId)
    })
    /**
      * @description 对当前用户转接失败，设置提示
      */
    this.socket.on('switch failed', function () {
      alert('当前无可转接客服！')
      that.transferable = false
    })
    // 判断上次是刷新还是退出页面，并进行初始化
    if (!this.isLogon) {
      setTimeout(function () {
        that.socket.id = that.user.id
        that.socket.emit('server set id', that.socket.id)
        that.isLogon = true
      }, 1000)
    } else {
      this.socket.emit('server come back', that.user.id)
    }
    sessionStorage.setItem(key, JSON.stringify({
      user: this.user,
      userList: this.userList,
      hangoffUserList: this.hangoffUserList,
      sessionList: this.sessionList,
      hangoffSessionList: this.hangoffSessionList,
      historySessionList: this.historySessionList,
      informationList: this.informationList,
      sessionIndex: this.sessionIndex,
      hangoffSessionIndex: this.hangoffSessionIndex,
      hangon: this.hangon,
      customerNumber: this.customerNumber,
      hangoffCustomerNumber: this.hangoffCustomerNumber,
      transferable: this.transferable,
      isLogon: this.isLogon,
      timers: this.timers
    }))
  },
  watch: {
    // 每当sessionList改变时，保存到localStorage中
    sessionList: {
      deep: true,
      handler () {
        sessionStorage.setItem(key, JSON.stringify({
          user: this.user,
          userList: this.userList,
          hangoffUserList: this.hangoffUserList,
          sessionList: this.sessionList,
          hangoffSessionList: this.hangoffSessionList,
          historySessionList: this.historySessionList,
          informationList: this.informationList,
          sessionIndex: this.sessionIndex,
          hangoffSessionIndex: this.hangoffSessionIndex,
          hangon: this.hangon,
          customerNumber: this.customerNumber,
          hangoffCustomerNumber: this.hangoffCustomerNumber,
          transferable: this.transferable,
          isLogon: this.isLogon,
          timers: this.timers
        }))
      }
    }
  },
  methods: {
    /**
      * @description 设置当前选中的用户索引
      */
    select (value) {
      if (this.hangon) {
        this.sessionIndex = this.userList.indexOf(value)
        this.userList[this.sessionIndex].uncheck = 0
      } else {
        this.hangoffSessionIndex = this.hangoffUserList.indexOf(value)
      }
    },
    /**
      * @description 键盘发送消息
      */
    inputing (e) {
      if (e.keyCode === 13 && this.text.length && this.session.userId !== -1) {
        let residual = document.getElementsByClassName('emoji-wysiwyg-editor textarea')[0]
        residual.innerHTML = ''
        if (!this.hangon) {
          alert('该用户已挂断！')
          this.text = ''
          return
        }
        this.session.messages.push({
          text: this.text,
          img: '',
          bigImg: '',
          isText: true,
          date: new Date(),
          self: true,
          image: '../../../static/1.jpg'
        })
        // 存入数据库
        let index = this.session.messages.length
        this.save_text(index - 1)
        this.socket.emit('server message', this.text, true, '', '', this.user.id, this.session.userId)
        clearTimeout(this.timers[this.sessionIndex])
        let customerId = this.userList[this.sessionIndex].id
        let serverSocket = this.socket
        this.timers[this.sessionIndex] = setTimeout(
          function () {
            customerOutMessage(serverSocket, customerId)
          }, 100000000)
        this.text = ''
      }
    },
    /**
      * @description 按钮发送消息
      */
    buttoninputing (e) {
      if (!this.hangon) {
        alert('该用户已挂断！')
        this.text = ''
        return
      }
      if ((this.text.length !== 0 || this.img.length !== 0) && this.session.userId !== -1) {
        let residual = document.getElementsByClassName('emoji-wysiwyg-editor textarea')[0]
        residual.innerHTML = ''
        this.session.messages.push({
          text: this.text,
          img: this.img,
          bigImg: this.bigImg,
          isText: this.isText,
          date: new Date(),
          self: true,
          image: this.user.image
        })
        // 存入数据库
        let index = this.session.messages.length
        if (this.isText === true) {
          this.save_text(index - 1)
        } else {
          this.save_img(index - 1)
        }
        this.socket.emit('server message', this.text, this.isText, this.img, this.bigImg, this.user.id, this.session.userId)
        clearTimeout(this.timers[this.sessionIndex])
        let customerId = this.userList[this.sessionIndex].id
        let serverSocket = this.socket
        this.timers[this.sessionIndex] = setTimeout(
          function () {
            customerOutMessage(serverSocket, customerId)
          }, 100000000)
        this.text = ''
        this.img = ''
        this.bigImg = ''
        this.isText = true
      }
    },
    /**
      * @description 切换左侧列表状态
      */
    switchoff () {
      this.hangon = !this.hangon
      this.sessionIndex = 0
      this.hangoffSessionIndex = 0
    },
    /**
      * @description 点击按钮查看历史消息
      */
    showHistory (e) {
      if (!this.hangon) {
        alert('无法获取历史消息！')
        return
      }
      this.history = !this.history
      this.show_history_item = {
        'client_id': this.session.userId,
        'service_id': this.turnId
      }
      this.show_history_api()
    },
    /**
      * @description 获取客服信息，用于第一次登陆的初始化
      */
    getCsInfomation () {
      this.$http.post(this.apiCustomerserviceShowUserStatus)
        .then((response) => {
          if (response.data === 'ERROR, session is broken.') {
            window.location.href = '../se_login'
          } else if (response.data === 'ERROR, wrong email.') {
            window.location.href = '../se_login'
          } else {
            this.user.id = response.data.email
            this.user.name = response.data.nickname
            this.cs_email_item = { 'email': this.user.id }
            console.log(this.user.id)
            this.get_cs_id_api()
          }
        }, (response) => {
          window.location.href = '../se_login'
        })
    },
    /**
      * @description 点击按钮对当前用户进行转接，如果转接成功，将其转移到已挂断消息列表，不成功则给出提示
      */
    switchServer (e) {
      if (!this.hangon) {
        alert('无法为已挂断的用户进行转接！')
        return
      }
      let that = this
      let id = that.userList[that.sessionIndex].id
      this.socket.emit('switch server from server', that.userList[that.sessionIndex].id)
      setTimeout(function () {
        if (!that.transferable) {
          that.transferable = true
          return
        }
        pushMessages(that.sessionList, that.sessionIndex, '已成功为用户转接！')
        customerHangoff(that.userList, that.hangoffUserList,
          that.sessionList, that.hangoffSessionList,
          that.historySessionList, that.session.userId)
        if (that.sessionIndex !== 0) {
          that.sessionIndex--
        }
        deleteCustomer(that.userList, that.sessionList, that.historySessionList, that.timers, that.informationList, id)
        that.transferable = true
      }, 1000)
    },
    /**
      * @description 客服点击按钮登出账号
      */
    // logout (e) {
    //   this.socket.emit('log out')
    //   for (let i = 0; i < this.timers.length; i++) {
    //     clearTimeout(this.timers[i])
    //   }
    //   this.isLogon = false
    // },
    /**
      * @description 输出图片
      */
    fileup () {
      let self = this
      let obj = document.getElementById('inputFile')
      let file = obj.files[0]
      lrz(file, {width: 960, height: 960, quality: 1})
        .then(function (rst) {
          self.bigImg = rst.base64
          self.isText = false
          lrz(rst.origin, {width: 300, height: 300, quality: 0.7})
            .then(function (rst) {
              self.img = rst.base64
              self.buttoninputing()
              return rst
            })
          return rst
        })
      obj.value = ''
    },
    /**
      * @description 加载图片
      */
    imgupload () {
      var file = document.getElementById('inputFile')
      file.click()
    },
    /**
      * @description 显示大图
      */
    showBigImg (bigImg) {
      this.bigImgBase64 = bigImg
      this.modal2 = true
    },
    /**
      * @description 检查机器人回复
      */
    checkReply () {
      if (this.reply === '') {
        this.replyIsNull = true
      }
    },
    /**
      * @description 检查向机器人提出的问题
      */
    checkQuestion () {
      if (this.question === '') {
        this.questionIsNull = true
      }
    },
    /**
      * @description 检查添加的关键词格式（只能是英文）
      */
    checkKeyword () {
      let reg = /^[\u4E00-\u9FA5]+$/
      let standardContent = reg.test(this.keyword)
      if (this.keyword === '' || standardContent === false) {
        this.keywordIsNotStandard = true
      }
    },
    /**
      * @description 回复输入
      */
    replyInput () {
      this.replyIsNull = false
    },
    /**
      * @description 问题输入
      */
    questionInput () {
      this.questionIsNull = false
    },
    /**
      * @description 关键词输出
      */
    keyWordInput () {
      this.keywordIsNotStandard = false
    },
    /**
      * @description 添加关键词
      */
    handleAdd () {
      this.checkKeyword()
      for (let i = 0; i < this.robotKeyWord.length; i++) {
        if (this.keyword === this.robotKeyWord[i]) {
          this.keywordIsExist = true
        }
      }
      if (this.keyword === '' || this.keywordIsNotStandard === true) {
        this.$Message.info('关键词格式不正确')
      } else if (this.keywordIsExist === true) {
        this.$Message.info('该关键词已添加')
        this.keywordIsExist = false
      } else {
        this.robotKeyWord.push(this.keyword)
        this.keyword = ''
      }
    },
    /**
      * @description 删除关键词
      */
    handleClose (event, name) {
      const index = this.robotKeyWord.indexOf(name)
      this.robotKeyWord.splice(index, 1)
    },
    /**
      * @description 添加语料
      */
    ok_add () {
      if (this.question === '' || this.reply === '') {
        this.$Message.info('您所填的信息不能为空')
      } else {
        if (this.robotKeyWord.length !== 0) {
          this.keyword_add = this.robotKeyWord.join(' ')
        } else {
          this.keyword_add = ''
        }
        this.robot_question_add = {
          'question': this.question,
          'answer': this.reply,
          'keyword': this.keyword_add,
          'weight': this.modelSelect
        }
        this.set_robot_api()
      }
      this.cancel_add()
    },
    /**
      * @description 取消添加语料
      */
    cancel_add () {
      this.question = ''
      this.reply = ''
      this.keyword = ''
      this.modelSelect = 1
      this.replyIsNull = false
      this.questionIsNull = false
      this.keywordIsNotStandard = false
      this.robotKeyWord = []
    },
    /**
      * @description 设置机器人借口
      */
    set_robot_api () {
      this.$http.post(this.apiCustomerserviceSetrobotinfoCreate, this.robot_question_add)
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
    /**
      * @description 保存文本接口
      */
    save_text_api () {
      this.$http.post(this.apiChattinglogSendMessage, this.save_text_item)
        .then((response) => {
          this.save_text_item = {}
        }, (response) => {
          // window.location.href = '../se_login'
          console.log('save_text_api')
        })
    },
    /**
      * @description 通过Email找客服Id
      */
    get_cs_id_api () {
      this.$http.post(this.apiChattinglogGetCsId, this.cs_email_item)
        .then((response) => {
          this.turnId = response.data
          console.log(this.turnId)
        }, (response) => {
          // window.location.href = '../se_login'
          console.log('get_cs_id_api')
        })
    },
    /**
      * @description 保存聊天文字
      */
    save_text (index) {
      this.save_text_item = {
        'client_id': this.session.userId,
        'service_id': this.turnId,
        'content': this.session.messages[index].text,
        'is_client': 0
      }
      console.log(this.save_text_item)
      this.save_text_api()
    },
    /**
      * @description 保存图片接口
      */
    save_img_api () {
      this.$http.post(this.apiSmallimagelogSendImage, this.save_img_item)
        .then((response) => {
          if (response.data === 'ERROR, invalid data in serializer.') {
            // window.location.href = '../notfound'
            console.log('save_img_api1')
          } else {
            this.save_img_item = {}
          }
        }, (response) => {
          // window.location.href = '../notfound'
          console.log('save_img_api2')
        })
    },
    /**
      * @description 保存大图片
      */
    save_bigImg_api () {
      this.$http.post(this.apiBigimagelogSendImage, this.save_bigImg_item)
        .then((response) => {
          if (response.data === 'ERROR, invalid data in serializer.') {
            // window.location.href = '../notfound'
            console.log('save_bigImg_api1')
          } else {
            this.save_bigImg_item = {}
          }
        }, (response) => {
          // window.location.href = '../notfound'
          console.log('save_bigImg_api2')
        })
    },
    /**
      * @description 保存图片
      */
    save_img (index) {
      let timestamp = new Date().getTime()
      let label = timestamp + this.session.userId
      this.save_img_item = {
        'client_id': this.session.userId,
        'service_id': this.turnId,
        'image': this.session.messages[index].img,
        'is_client': false,
        'label': label
      }
      this.save_bigImg_item = {
        'client_id': this.session.userId,
        'service_id': this.turnId,
        'image': this.session.messages[index].bigImg,
        'is_client': false,
        'label': label
      }
      console.log(this.save_img_item)
      console.log(this.save_bigImg_item)
      this.save_img_api()
      this.save_bigImg_api()
    },
    /**
      * @description 获取历史消息
      */
    show_history_api () {
      this.$http.post(this.apiLogShowHistory, this.show_history_item)
        .then((response) => {
          if (response.data === 'ERROR, invalid data in serializer.') {
            // window.location.href = '../notfound'
            console.log('show_history_api1')
          } else {
            console.log(response.data)
            for (var p = 0; p < response.data.length; p++) {
              console.log(response.data[p].hasOwnProperty('content'))
              if (response.data[p].hasOwnProperty('content')) {
                if (response.data[p].is_client === false) {
                  this.hsession.messages.push({
                    text: response.data[p].content,
                    isText: true,
                    date: response.data[p].time,
                    self: true,
                    image: this.user.image
                  })
                } else {
                  this.hsession.messages.push({
                    text: response.data[p].content,
                    isText: true,
                    date: response.data[p].time,
                    image: '../../../static/3.jpg'
                  })
                }
              } else {
                if (response.data[p].is_client === false) {
                  this.hsession.messages.push({
                    img: response.data[p].image,
                    isText: false,
                    label: response.data[p].label,
                    date: response.data[p].time,
                    self: true,
                    image: this.user.image
                  })
                  let index = this.hsession.messages.length
                  console.log('this.hsession.messages1')
                  console.log(this.hsession.messages[index - 1])
                } else {
                  this.hsession.messages.push({
                    img: response.data[p].image,
                    isText: false,
                    label: response.data[p].label,
                    date: response.data[p].time,
                    image: '../../../static/3.jpg'
                  })
                  let index = this.hsession.messages.length
                  console.log('this.hsession.messages2')
                  console.log(this.hsession.messages[index - 1])
                }
              }
            }
          }
        }, (response) => {
          // window.location.href = '../notfound'
          console.log('show_history_api2')
        })
    },
    /**
      * @description 显示历史消息中的大图
      */
    showHistoryBigImg (label) {
      this.show_history_big_img_item = {
        'client_id': this.session.userId,
        'service_id': this.turnId,
        'label': label
      }
      this.show_history_big_img_api()
    },
    /**
      * @description 获取历史消息中的大图
      */
    show_history_big_img_api () {
      this.$http.post(this.apiBigimagelogShowSingleHistory, this.show_history_big_img_item)
        .then((response) => {
          if (response.data === 'ERROR, no history.') {
            // window.location.href = '../notfound'
            console.log('show_history_big_img_api1')
          } else {
            this.show_history_big_img_api = {}
            this.showBigImg(response.data)
          }
        }, (response) => {
          // window.location.href = '../notfound'
          console.log('show_history_big_img_api2')
        })
    }
  },
  filters: {
    /**
      * @description 格式化日期
      */
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
    /**
      * @description 发送消息后滚动到底部
      */
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

.userinfo {
  margin-top: 20%;
  margin-left: 5%;
  margin-right: 5%;
  line-height: 30px;
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

.waring {
  color: red;
}

.send-pic {
  float: right;
  margin-right: 0.6em;
}
</style>
