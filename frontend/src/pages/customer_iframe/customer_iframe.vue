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
                  <p v-if="item.isText" v-html="item.text"></p>
                  <img :src="item.img" v-else @click='showBigImg(item.bigImg)'>
                </li>
              </div>
            </div>
          </li>
        </ul>
      </div>
      <Modal v-model="modalShowBigImg" width="auto">
        <p slot="header">
        </p>
        <div style="text-align:center">
            <img :src="bigImgSrc">
        </div>
        <div slot="footer">
        </div>
      </Modal>
      <div class="main-text"  @keydown="keyboardInputing">
        <Button-group>
          <Button @click="switchToCs">转接人工客服</Button>
          <Button @click="screenShot">截屏</Button>
          <Button @click="endSession">结束会话</Button>
          <Button @click="imageUpload">发送图片</Button>
        </Button-group>
        <p class="lead emoji-picker-container">
          <textarea class="textarea" placeholder="按 Ctrl+Enter 发送" v-model="chatlogData.text" rows="5" data-emojiable="true"></textarea>
        </p>
        <Button class="submit-button" @click="buttonInputing">发送</Button>
        <input id="inputFile" name="inputFile" type="file" multiple="mutiple" accept="image/png, image/jpeg, image/gif, image/jpg" style="display: none" @change="imageCompress">
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
/**
  * @description 接收文字消息放进sessionList
  */
function pushTextToSessionList (session, msg) {
  session.messages.push({
    text: msg,
    isText: true,
    date: new Date(),
    image: '../../../static/2.png'
  })
}
/**
  * @description 接收图片消息放进sessionList
  */
function pushImgToSessionList (session, bpic, spic) {
  session.messages.push({
    bigImg: bpic,
    img: spic,
    isText: false,
    date: new Date(),
    image: '../../../static/2.png'
  })
}
/**
  * @description 链接客服
  */
function connectToCs (cs, session, csID) {
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
function noCsAvailable (cs, session) {
  session.messages.push({
    text: '您好，现在没有客服在线哦，请您稍后重新连接',
    isText: true,
    date: new Date(),
    image: '../../../static/2.png'
  })
  cs.csID = '&Robot'
}
/**
  * @description 客户超时断开
  */
function customerExpire (cs, session) {
  session.messages.push({
    text: '您好，您已经超时并断开连接，请重新连接客服',
    isText: true,
    date: new Date(),
    image: '../../../static/2.png'
  })
  cs.csID = '&Robot'
}
/**
  * @description 初始化Socket
  */
function initSocket (cs, session, socket, customer) {
  return new Promise(function (resolve) {
    // 客服发送文字信息
    socket.on('cs send message', function (msg, enterpriseID, csID, customerID) {
      pushTextToSessionList(session, msg)
    })

    // 客服发送图片信息
    socket.on('cs send picture', function (bpic, spic, enterpriseID, csID, customerID) {
      pushImgToSessionList(session, bpic, spic)
    })

    socket.on('connect to cs', function (csID) {
      connectToCs(cs, session, csID)
      resolve()
    })

    socket.on('switch cs', function (enterpriseID, formerCsID) {
      socket.emit('switch cs', formerCsID, enterpriseID, customer.customerID, customer.customerInfomation)
      resolve()
    })

    socket.on('no cs available', function () {
      noCsAvailable(cs, session)
    })

    socket.on('customer expire', function () {
      customerExpire(cs, session)
    })

    socket.emit('assigned to cs', customer.enterpriseID, customer.customerID, customer.customerInfomation)
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
        customerID: 'null',
        customerName: 'null',
        enterpriseID: 'null',
        image: '../../../static/1.jpg',
        customerInfomation: []
      },

      // 客服列表
      cs: {
        csID: '&Robot',
        csName: 'null',
        enterpriseID: 'null',
        image: '../../../static/2.png'
      },

      // 会话列表
      session: {
        messages: [
          {
            text: '你好，我是机器人alpha. 你可以询问我任何想问的问题，如果需要转接人工客服，请点击窗口下方的转接按钮进行转接哦~',
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
      apiCustomerserviceDisplayrobotreplyShow: '../../api/customerservice_displayrobotreply_show/',
      apiChattinglogSendMessage: '../../api/chattinglog_send_message/',
      apiChattinglogGetCsId: '../../api/chattinglog_get_cs_ID/',
      apiBigimagelogSendImage: '../../api/bigimagelog_send_image/',
      apiSmallimagelogSendImage: '../../api/smallimagelog_send_image/',
      apiCustomerCheckInfo: '../../api/customer_check_info/',
      apiCustomerDisplayCustomerinfopropertyname: '../../api/customer_display_customerinfopropertyname/',
      robotReplyItem: {},
      saveTextItem: {},
      csIDItem: {},
      saveImgItem: {},
      saveBigImgItem: {},
      customerCheckItem: {},
      customerInfoNameCheckItem: {},

      databaseCsID: '',
      adminNickname: '',
      customerInfoNameArray: []
    }
  },

  created () {
    this.getCustomerInfoUrl()

    // 如果初次登录， 初始化
    if (this.customer.customerID === -1) {
      this.customer.customerID = (Math.random() * 1000).toString()
      this.customer.customerName = this.customer.customerID
    }

    // 如果刷新之前已转接为人工客服，自动连接服务器
    if (this.cs.csID.indexOf('&Robot') === -1) {
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

        this.socket.on('switch cs', function (enterpriseID, formerCsID) {
          that.socket.emit('switch cs', enterpriseID, formerCsID)
          resolve()
        })

        this.socket.emit('cs come back', that.customer.enterpriseID, that.cs.csID)
      }).then(function () {
        that.csIDItem = {
          'nickname': that.cs.csID
        }
        that.getCsIdApi()
      })
    } else {
      this.csIDItem = {
        'nickname': this.cs.csID
      }
      this.getCsIdApi()
    };

    /**
      * @description 对全局进行监听，接收到图片的base64编码后进行转码，实现截图的输出
      */
    let self = this
    window.addEventListener('message', function (e) {
      let canvasData = e.data
      let img = new Image()
      img.src = canvasData
      lrz(img.src, { width: 960, height: 960, quality: 1 })
        .then(function (rst) {
          self.chatlogData.bigImg = rst.base64
          lrz(rst.origin, { width: 300, height: 300, quality: 0.7 })
            .then(function (rst) {
              self.chatlogData.img = rst.base64
              self.imgInputing()
              return rst
            })
          return rst
        })
    }, false)
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
      * @description 替换换行符，实现多行文本输入
      */
    repstr (str) {
      return str.replace(new RegExp('\n', 'gm'), '<br/>')
    },
    /**
      * @description 键盘输入信息
      */
    keyboardInputing (e) {
      if (e.ctrlKey && e.keyCode === 13 && this.chatlogData.text.length) {
        let residual = document.getElementsByClassName('emoji-wysiwyg-editor textarea')[0]
        residual.innerHTML = ''
        this.chatlogData.text = this.repstr(this.chatlogData.text)
        this.session.messages.push({
          text: this.chatlogData.text,
          date: new Date(),
          isText: true,
          self: true,
          image: '../../../static/1.jpg'
        })
        // 存入数据库
        let index = this.session.messages.length
        this.saveText(1, index - 1)
        if (this.cs.csID.indexOf('&Robot') === -1) {
          this.socket.emit('customer send message', this.chatlogData.text, this.customer.enterpriseID, this.cs.csID, this.customer.customerID)
        } else {
          this.robotReplyItem = {
            'nickname': this.customer.enterpriseID,
            'customer_input': this.chatlogData.text
          }
          this.showRobotReplyApi()
        }
        this.chatlogData.text = ''
      }
    },
    /**
      * @description 按钮输入信息
      */
    buttonInputing (e) {
      if (this.chatlogData.text.length !== 0) {
        let residual = document.getElementsByClassName('emoji-wysiwyg-editor textarea')[0]
        residual.innerHTML = ''
        this.chatlogData.text = this.repstr(this.chatlogData.text)
        this.session.messages.push({
          text: this.chatlogData.text,
          date: new Date(),
          isText: true,
          self: true,
          image: '../../../static/1.jpg'
        })
        // 存入数据库
        let index = this.session.messages.length
        this.saveText(1, index - 1)
        if (this.cs.csID.indexOf('&Robot') === -1) {
          this.socket.emit('customer send message', this.chatlogData.text, this.customer.enterpriseID, this.cs.csID, this.customer.customerID)
        } else {
          this.robotReplyItem = {
            'nickname': this.customer.enterpriseID,
            'customer_input': this.chatlogData.text
          }
          this.showRobotReplyApi()
        }
        this.chatlogData.text = ''
      }
    },
    /**
      * @description 发送图片
      */
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
        let index = this.session.messages.length
        this.saveImg(1, index - 1)
        if (this.cs.csID.indexOf('&Robot') === -1) {
          this.socket.emit('customer send picture', this.chatlogData.bigImg, this.chatlogData.img, this.customer.enterpriseID, this.cs.csID, this.customer.customerID)
        }
        this.chatlogData.img = ''
        this.chatlogData.bigImg = ''
      }
    },
    /**
      * @description 点击按钮转接客服
      */
    switchToCs (e) {
      if (this.cs.csID.indexOf('&Robot') === -1) {
        alert('当前已为人工客服！')
        return
      }
      let that = this
      that.socket = io('http://localhost:3000')
      initSocket(that.cs, that.session, that.socket, that.customer).then(function () {
        that.csIDItem = {
          'nickname': that.cs.csID
        }
        that.getCsIdApi()
      })
    },
    /**
      * @description 图片压缩
      */
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
    /**
      * @description 显示大图片
      */
    showBigImg (bigImg) {
      this.bigImgSrc = bigImg
      this.modalShowBigImg = true
    },
    /**
      * @description 截图
      */
    screenShot () {
      window.parent.postMessage('Screen shot', '*')
    },
    /**
      * @description 获取机器人回复调用后端接口
      */
    showRobotReplyApi () {
      this.$http.post(this.apiCustomerserviceDisplayrobotreplyShow, this.robotReplyItem)
        .then((response) => {
          if (response.data === 'ERROR, wrong information.') {
            this.$Message.info('问题没得到解决？请转接人工客服或刷新页面')
          } else if (response.data === 'ERROR, incomplete information.') {
            this.$Message.info('问题没得到解决？请转接人工客服或刷新页面')
          } else if (response.data === 'ERROR, info is not exist.') {
            this.$Message.info('问题没得到解决？请转接人工客服或刷新页面')
          } else {
            let msg = response.data
            this.showRobotReply(msg)
          }
        }, (response) => {
          this.$Message.info('问题没得到解决？请转接人工客服或刷新页面')
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
      this.$http.post(this.apiChattinglogGetCsId, this.csIDItem)
        .then((response) => {
          this.databaseCsID = response.data
        }, (response) => {
          window.location.href = '../se_login/'
        })
    },
    /**
      * @description 保存文本接口
      */
    saveTextApi () {
      this.$http.post(this.apiChattinglogSendMessage, this.saveTextItem)
        .then((response) => {
          this.saveTextItem = {}
        }, (response) => {
          window.location.href = '../se_login/'
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
      this.saveTextApi()
    },
    /**
      * @description 保存图片接口
      */
    saveImgApi () {
      this.$http.post(this.apiSmallimagelogSendImage, this.saveImgItem)
        .then((response) => {
          if (response.data === 'ERROR, invalid data in serializer.') {
            window.location.href = '../notfound/'
          } else {
            this.saveImgItem = {}
          }
        }, (response) => {
          window.location.href = '../notfound/'
        })
    },
    /**
      * @description 保存大图接口
      */
    saveBigImgApi () {
      this.$http.post(this.apiBigimagelogSendImage, this.saveBigImgItem)
        .then((response) => {
          if (response.data === 'ERROR, invalid data in serializer.') {
            window.location.href = '../notfound/'
          } else {
            this.saveBigImgItem = {}
          }
        }, (response) => {
          window.location.href = '../notfound/'
        })
    },
    /**
      * @description 保存图片
      */
    saveImg (isClient, index) {
      let timestamp = new Date().getTime()
      let label = timestamp + this.customer.customerID
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
      this.saveImgApi()
      this.saveBigImgApi()
    },
    /**
      * @description 结束会话
      */
    endSession () {
      window.parent.postMessage('End session', '*')
    },
    /**
      * @description 从url中获取用户信息并检查
      */
    customerCheck () {
      this.customer.customerID = this.$utils.getUrlKey('userID')
      this.customer.customerName = this.$utils.getUrlKey('nickname')
      let signature = this.$utils.getUrlKey('signature')
      this.customerCheckItem = {
        'enterprise_id': this.adminNickname,
        'customer_id': this.customer.customerID,
        'cusotmer_name': this.customer.customerName,
        'hash_result': signature
      }
      this.customerCheckApi()
    },
    /**
      * @description 调用后端接口检查url是否为真
      */
    customerCheckApi () {
      this.$http.post(this.apiCustomerCheckInfo, this.customerCheckItem)
        .then((response) => {
          if (response.data === 'ERROR, incomplete information.') {
            window.location.href = '../not_found/'
          } else if (response.data === 'ERROR, wrong information.') {
            window.location.href = '../not_found/'
          } else if (response.data === 'ERROR, wrong nickname.') {
            window.location.href = '../not_found/'
          } else if (response.data === 'False') {
            window.location.href = '../not_found/'
          } else if (response.data === 'True') {
            this.customerInfoNameCheckApi()
          }
        }, (response) => {
          window.location.href = '../not_found/'
        })
    },
    /**
      * @description 调用后端接口获取企业自定义用户信息种类
      */
    customerInfoNameCheckApi () {
      this.$http.post(this.apiCustomerDisplayCustomerinfopropertyname, this.customerInfoNameCheckItem)
        .then((response) => {
          if (response.data === 'ERROR, incomplete information.') {
            window.location.href = '../not_found/'
          } else if (response.data === 'ERROR, wrong information.') {
            window.location.href = '../not_found/'
          } else if (response.data === 'ERROR, wrong nickname.') {
            window.location.href = '../not_found/'
          } else {
            this.customerInfoNameArray = response.data
            this.getCustomerInfo()
          }
        }, (response) => {
          window.location.href = '../not_found/'
        })
    },
    /**
      * @description 从url中获取用户信息并存储
      */
    getCustomerInfo () {
      this.customer.customerInfomation = []
      let tempUserID = {
        name: 'userID',
        content: this.customer.customerID
      }
      let tempNickname = {
        name: 'nickname',
        content: this.customer.customerName
      }
      this.customer.customerInfomation.push(tempUserID)
      this.customer.customerInfomation.push(tempNickname)
      for (let i = 0; i < this.customerInfoNameArray.length; i++) {
        let tempCustomerInfo = {
          name: this.customerInfoNameArray[i].name,
          content: this.$utils.getUrlKey(this.customerInfoNameArray[i].name)
        }
        this.customer.customerInfomation.push(tempCustomerInfo)
      }
      this.cs.csID = this.customer.enterpriseID + '&Robot'
      this.csIDItem = {
        'nickname': this.cs.csID
      }
      this.getCsIdApi()
    },
    /**
      * @description 获取weburl
      */
    getCustomerInfoUrl () {
      let url = window.location.href
      let urlArray = url.split('/')
      this.adminNickname = urlArray[4]
      this.customer.enterpriseID = this.adminNickname
      this.cs.enterpriseID = this.adminNickname
      this.customerInfoNameCheckItem = {
        'enterprise_id': this.adminNickname
      }
      this.customerCheck()
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

.emoji-wysiwyg-editor {
  line-height: 10px;
  padding: 5px;
}

.lead {
  font-size: 10px;
}

.ivu-btn {
  font-size: 10px;
}



/*主要界面*/

.container {
  height: 100%;
  width: 100%;
  vertical-align: center;
  border-radius: 4px;
  padding-right: 0;
  padding-left: 0;
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
  height: calc(100% - 120px);
}

.main-message {
  padding: 10px 15px;
  overflow-y: scroll;
  line-height: 1.25;
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
  font-size: 10px;
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
  padding: 0 5px;
  padding-top: 0.3rem;
  max-width: calc(80% - 40px);
  min-height: 30px;
  line-height: 1.5;
  font-size: 10px;
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
  padding-top: 0.3rem;
  max-width: calc(80% + 10px);
  min-height: 25px;
  line-height: 1.5;
  font-size: 10px;
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
  height: 100px;
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
  /* width: 10%; */
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

img {
  vertical-align: top;
}
</style>
