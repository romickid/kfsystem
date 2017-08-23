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
        <Button-group>
          <Button @click="switchToCs">转接人工客服</Button>
          <Button @click="imageUpload" icon="image"></Button>
        </Button-group>
        <p class="lead emoji-picker-container">
          <textarea class="textarea" placeholder="按Enter 发送" v-model="chatlogData.text" rows="5" data-emojiable="true"></textarea>
        </p>
        <Button class="submit-button" @click="buttonInputing">发送</Button>
        <input id="inputFile" name='inputFile' type='file' multiple='mutiple' accept="image/png, image/jpeg, image/gif, image/jpg" style="display: none" @change="imageCompress">
      </div>
    </div>
  </div>
</template>

<script>
import * as io from 'socket.io-client'
import Vue from 'vue'
import { formatDate } from '../../../static/js/date.js'
import lrz from '../../../node_modules/lrz/dist/lrz.bundle.js'
const key = 'VUE-Customer1'

// 接收文字消息放进sessionList
function pushTextToSessionList (session, msg) {
  console.log("function: pushTextToSessionList")
  session.messages.push({
    text: msg,
    isText: true,
    date: new Date(),
    image: '../../../static/2.png'
  })
}

// 接收图片消息放进sessionList
function pushImgToSessionList (session, bpic, spic) {
  console.log("function: pushTextToSessionList")
  session.messages.push({
    bigImg: bpic,
    img: spic,
    isText: false,
    date: new Date(),
    image: '../../../static/2.png'
  })
}

function connectToCs (cs, session, csID) {
  console.log("function: connectToCs")
  cs.csID = csID
  session.messages.push({
    text: '已成功为您转接客服' + csID,
    isText: true,
    date: new Date(),
    image: '../../../static/2.png'
  })
}
/**
  * @description 没有可连接客服
  */
function noServerAvailable (cs, session) {
  console.log("function: noServerAvailable")
  session.messages.push({
    text: '您好，现在没有客服在线哦，请您稍后重新连接',
    isText: true,
    date: new Date(),
    image: '../../../static/2.png'
  })
  cs.customerID = -1
}
/**
  * @description 初始化Socket
  */
function initSocket (cs, session, socket, customer) {
  return new Promise (function (resolve) {
    console.log("function: initSocket")

    socket.on('cs send message', function (msg, enterpriseID, csID, customerID) {
      console.log("socket: cs send message")
      pushTextToSessionList(session, msg)
    })

    socket.on('cs send picture', function (bpic, spic, enterpriseID, csID, customerID) {
      console.log("socket: cs send picture")
      pushImgToSessionList(session, bpic, spic)
    })

    socket.on('connect to cs', function (csID) {
      console.log("socket: connect to cs")
      connectToCs(cs, session, csID)
      resolve()
    })

    socket.on('no server available', function () {
      console.log("socket: no server available")
      noServerAvailable(cs, session)
    })

    socket.on('switch cs', function (enterpriseID, formerCsID) {
      console.log("socket: switch cs")
      socket.emit('switch cs', enterpriseID, formerCsID)
      resolve()
    })

    socket.on('no cs available', function () {
      alert('当前无在线客服！')
    })

    socket.emit('assigned to cs', customer.enterpriseID, customer.customerID)
    console.log("socket emit: assigned to cs")
  })
}
/**
  * @description 初始化数据
  */
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
        csID: 'nick2@robot.com',
        csName: 'MonsterSXF',
        enterpriseID: 'nick2',
        image: '../../../static/2.png'
      },

      // 会话列表
      session: {
        customerID: -1,
        enterpriseID: 'nick2',
        messages: [
          {
            text: '你好呀，我是机器人兔兔~如果想转接人工客服，请按窗口下方的转接按钮进行转接哦~',
            isText: true,
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

      socket: '',
      // 聊天数据
      chatlogData: {
        text: '',
        img: '',
        bigImg: ''
      },
      bigImgSrc: '',
      modalShowBigImg: false,

      // api接口
      apiCustomerserviceDisplayrobotreplyShow: '../api/customerservice_displayrobotreply_show/',
      apiChattinglogSendMessage: '../api/chattinglog_send_message/',
      apiChattinglogGetCsId: '../api/chattinglog_get_cs_ID/',
      apiBigimagelogSendImage: '../api/bigimagelog_send_image/',
      apiSmallimagelogSendImage: '../api/smallimagelog_send_image/',
      apiCustomerCheckInfo: '../api/customer_check_info/',
      robotReplyItem: {},
      saveTextItem: {},
      csEmailItem: {},
      saveImgItem: {},
      saveBigImgItem: {},
      customerCheckItem: {},

      databaseCsID: '',
      adminNickname: 'nick2'
    }
  },

  created () {
    this.customerCheck()
    // 如果初次登录， 初始化
    if (this.customer.customerID === -1) {
      this.customer.customerID = (Math.random() * 1000).toString()
      this.customer.customerName = this.customer.customerID
    }

    // 如果刷新之前已转接为人工客服，自动连接服务器
    if (this.cs.csID.indexOf("robot.com") === -1) {
      let that = this
      this.socket = io('http://localhost:3000')

      new Promise(function (resolve) {
        this.socket.on('cs send message', function (msg, enterpriseID, csID, customerID) {
          pushTextToSessionList(that.session, msg)
        })

        this.socket.on('cs send picture', function (bpic, spic, enterpriseID, csID, customerID) {
          pushImgToSessionList(that.session, bpic, spic)
        })

        this.socket.on('connect to cs', function (csID) {
          connectToCs(that.cs, that.session, csID)
          resolve()
        })

        this.socket.on('no server available', function () {
          noServerAvailable(that.cs, that.session)
        })

        this.socket.on('switch cs', function (enterpriseID, formerCsID) {
          that.socket.emit('switch cs', enterpriseID, formerCsID)
          resolve()
        })

        this.socket.emit('cs come back', that.customer.enterpriseID, that.cs.csID)
      }).then(function () {
        that.csEmailItem = {
          'email': that.cs.csID
        }
        console.log(that.csEmailItem)
        that.getCsIdApi()
      })
    } else {
      this.csEmailItem = {
        'email': this.cs.csID
      }
      console.log(this.csEmailItem)
      this.getCsIdApi()
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
    /**
      * @description 键盘输入信息
      */
   keyboardInputing (e) {
      console.log("method: keyboardInputing")
      if (e.keyCode === 13 && this.chatlogData.text.length) {
        let residual = document.getElementsByClassName('emoji-wysiwyg-editor textarea')[0]
        residual.innerHTML = ''
        this.session.messages.push({
          text: this.chatlogData.text,
          date: new Date(),
          isText: true,
          self: true,
          image: '../../../static/1.jpg'
        })
        console.log('keyboardInputing1')
        // 存入数据库
        let index = this.session.messages.length
        this.saveText(1, index - 1)
        console.log('keyboardInputing2')
        if (this.cs.csID.indexOf("robot.com") === -1) {
          this.socket.emit('customer send message', this.chatlogData.text, this.customer.enterpriseID, this.cs.csID, this.customer.customerID)
        } else {
          this.robotReplyItem = {
            'nickname': this.customer.enterpriseID,
            'customer_input': this.chatlogData.text
          }
          console.log(this.robotReplyItem)
          this.showRobotReplyApi()
        }
        this.chatlogData.text = ''
      }
    },
    /**
      * @description 按钮输入信息
      */
    buttonInputing (e) {
      console.log("method: buttonInputing")
      let residual = document.getElementsByClassName('emoji-wysiwyg-editor textarea')[0]
      residual.innerHTML = ''

      if (this.chatlogData.text.length !== 0) {
        this.session.messages.push({
          text: this.chatlogData.text,
          date: new Date(),
          isText: true,
          self: true,
          image: '../../../static/1.jpg'
        })
        console.log('buttonInputing1')
        // 存入数据库
        let index = this.session.messages.length
        this.saveText(1, index - 1)
        console.log('buttonInputing2')
        if (this.cs.csID.indexOf("robot.com") === -1) {
          this.socket.emit('customer send message', this.chatlogData.text, this.customer.enterpriseID, this.cs.csID, this.customer.customerID)
        } else {
          this.robotReplyItem = {
            'nickname': this.customer.enterpriseID,
            'customer_input': this.chatlogData.text
          }
          console.log(this.robotReplyItem)
          this.showRobotReplyApi()
        }
        this.chatlogData.text = ''
      }
    },

    imgInputing () {
      if (this.chatlogData.img !== '') {
        this.session.messages.push({
          img: this.chatlogData.img,
          bigImg: this.chatlogData.bigImg,
          isText: false,
          date: new Date(),
          self: true,
          image: '../../../static/1.jpg'
        })
        console.log('imgInputing1')
        let index = this.session.messages.length
        this.saveImg(1, index - 1)
        console.log('this.saveImg(1, index - 1)')
        if (this.cs.csID.indexOf("robot.com") === -1) {
          this.socket.emit('customer send picture', this.chatlogData.bigImg, this.chatlogData.img, this.customer.enterpriseID, this.cs.csID, this.customer.customerID)
          console.log('socket')
        }
        console.log('imgInputing2')
        this.chatlogData.img = ''
        this.chatlogData.bigImg = ''
      }
    },
    /**
      * @description 点击按钮转接客服
      */
    switchToCs (e) {
      console.log("method: switchToCs")
      // console.log(this.cs.csID.indexOf("robot.com"))
      if (this.cs.csID.indexOf("robot.com") === -1) {
        alert('当前已为人工客服！')
        return
      }
      let that = this
      that.socket = io('http://localhost:3000')
      initSocket(that.cs, that.session, that.socket, that.customer).then(function () {
        that.csEmailItem = {
          'email': that.cs.csID
        }
        console.log(that.csEmailItem)
        that.getCsIdApi()
      })
    },

    // 图片压缩
    imageCompress () {
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
    /**
      * @description 加载图片
      */
    imageUpload () {
      var file = document.getElementById('inputFile')
      file.click()
    },

    // 显示大图片
    showBigImg (bigImg) {
      this.bigImgSrc = bigImg
      this.modalShowBigImg = true
    },
    /**
      * @description 获取机器人回复调用后端接口
      */
    showRobotReplyApi () {
      this.$http.post(this.apiCustomerserviceDisplayrobotreplyShow, this.robotReplyItem)
        .then((response) => {
          if (response.data === 'ERROR, wrong information.') {
            // window.location.href = '../se_login'
            console.log('show_robot_reply_api1')
          } else if (response.data === 'ERROR, incomplete information.') {
            // this.$Message.info('您所填的信息不完整')
            console.log('show_robot_reply_api2')
          } else if (response.data === 'ERROR, info is not exist.') {
            // this.$Message.info('问题没得到解决？请转接人工客服')
            console.log('show_robot_reply_api3')
          } else {
            let msg = response.data
            this.showRobotReply(msg)
          }
        }, (response) => {
          // window.location.href = '../se_login'
          console.log('show_robot_reply_api4')
        })
    },
    /**
      * @description 显示机器人回复并存入数据库
      */
    showRobotReply (msg) {
      this.session.messages.push({
        text: msg,
        isText: true,
        date: new Date(),
        image: '../../../static/2.png'
      })
      // 存入数据库
      let index = this.session.messages.length
      this.saveText(0, index - 1)
    },
    /**
      * @description 通过email设置用户ID
      */
    getCsIdApi () {
      this.$http.post(this.apiChattinglogGetCsId, this.csEmailItem)
        .then((response) => {
          this.databaseCsID = response.data
          console.log('get_cs_id_api1')
          console.log(response.data)
        }, (response) => {
          // window.location.href = '../se_login'
          console.log('get_cs_id_api2')
        })
    },
    /**
      * @description 保存文本接口
      */
    saveTextApi () {
      this.$http.post(this.apiChattinglogSendMessage, this.saveTextItem)
        .then((response) => {
          console.log('save_text_api1')
          this.saveTextItem = {}
        }, (response) => {
          // window.location.href = '../se_login'
          console.log('save_text_api2')
        })
    },
    /**
      * @description 保存文本
      */
    saveText (isClient, index) {
      this.saveTextItem = {
        'client_id': this.customer.customerID,
        'service_id': this.databaseCsID,
        'content': this.session.messages[index].text,
        'is_client': isClient
      }
      console.log(this.saveTextItem)
      this.saveTextApi()
    },
    /**
      * @description 保存图片接口
      */
    saveImgApi () {
      this.$http.post(this.apiSmallimagelogSendImage, this.saveImgItem)
        .then((response) => {
          if (response.data === 'ERROR, invalid data in serializer.') {
            // window.location.href = '../notfound'
            console.log('save_img_api1')
          } else {
            this.saveImgItem = {}
            console.log('saveImgApi')
          }
        }, (response) => {
          // window.location.href = '../notfound'
          console.log('save_img_api2')
        })
    },
    /**
      * @description 保存大图接口
      */
    saveBigImgApi () {
      this.$http.post(this.apiBigimagelogSendImage, this.saveBigImgItem)
        .then((response) => {
          if (response.data === 'ERROR, invalid data in serializer.') {
            // window.location.href = '../notfound'
            console.log('save_bigImg_api1')
          } else {
            this.saveBigImgItem = {}
            console.log('saveBigImgApi')
          }
        }, (response) => {
          // window.location.href = '../notfound'
          console.log('save_bigImg_api2')
        })
    },
    /**
      * @description 保存图片
      */
    saveImg (isClient, index) {
      console.log('saveImg')
      let timestamp = new Date().getTime()
      console.log(timestamp)
      let label = timestamp + this.customer.customerID
      console.log('timestamp')
      this.saveImgItem = {
        'client_id': this.customer.customerID,
        'service_id': this.databaseCsID,
        'image': this.session.messages[index].img,
        'is_client': isClient,
        'label': label
      }
      this.saveBigImgItem = {
        'client_id': this.customer.customerID,
        'service_id': this.databaseCsID,
        'image': this.session.messages[index].bigImg,
        'is_client': isClient,
        'label': label
      }
      console.log(this.saveImgItem)
      console.log(this.saveBigImgItem)
      this.saveImgApi()
      this.saveBigImgApi()
    },
    customerCheck () {
      console.log('[methods]: customerCheck')
      let url = window.loction.href
      let urlArray = url.split('/')
      let adminName = urlArray[4]
      let userID = this.$utils.getUrlKey('userID')
      let userName = this.$utils.getUrlKey('userName')
      let signature = this.$utils.getUrlKey('signature')
      this.customerCheckItem = {
        'enterprise_id': adminName,
        'customer_id': userID,
        'cusotmer_name': userName,
        'hash_result': signature
      }
      this.customerCheckApi()
    },
    customerCheckApi () {
      console.log('[methods]: customerCheckApi')      
      this.$http.post(this.apiCustomerCheckInfo, this.customerCheckItem)
        .then((response) => {
          if (response.data === 'ERROR, incomplete information.') {
            // window.location.href = '../not_found'
            console.log('customerCheckApi1')
          } else if (response.data === 'ERROR, wrong information.') {
            // window.location.href = '../not_found'
            console.log('customerCheckApi2')
          } else if (response.data === 'ERROR, wrong nickname.') {
            // window.location.href = '../not_found'
            console.log('customerCheckApi3')
          } else {
            console.log('customerCheckApi4')
          }
        }, (response) => {
          // window.location.href = '../not_found'
            console.log('customerCheckApi5')
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

  components: {},

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

.send-pic {
  float: right;
  margin-right: 0.6em;
}

.ivu-btn-group .ivu-btn-icon-only .ivu-icon {
  font-size: 18px;
}
</style>
