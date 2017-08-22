<template>
  <div>
    <div class="header">
      <div class="ceiling">
        <a href='../main'>
          <img src="../../../static/logo5.png" alt="" style="height:40px;width:40px">
          <img src="../../../static/name.png" alt="" style="height:40px">
        </a>
        <div class="ceiling-main">
          <a href='../main' class='ceiling-item'>首页</a> |
          <a href="../main/#jump" class='ceiling-item'> 产品介绍</a> |
          <a href="../documentation" class='ceiling-item'> 帮助中心</a> |
          <a href="../en_folders" class='ceiling-item'> 注册</a> |
          <a href="../se_login" class='ceiling-item'> 客服入口</a>
        </div>
      </div>
    </div>
    <form>
      <div class="all">
        <div class="container">
          <div class="div">
            <label id="title">用户登录</label>
          </div>
          <div class="div">
            <label class="label">登录邮箱：</label>
            <input type="text" v-model="email" name="email" class="text" @blur="checkEmail" @focus="emailInput" id='input-email'>
            <i-label v-if="emailIllegal">
              <p id="p">请输入正确的邮箱！</p>
            </i-label>
          </div>
          <div class="div" @keydown="loginEnter">
            <label class="label">登录密码：</label>
            <input type="password" v-model="password" name="password" class="text" id="password">
          </div>
          <div class="div">
            <Button type="primary" shape="circle" size="large" id="login" @click="login">登录</Button>
          </div>
          <div id="butt">
            <en-forget-password ref="enForgetPassword"></en-forget-password>
          </div>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import enForgetPassword from '../../components/en_forget_password'
export default {
  name: 'app',
  components: {
    enForgetPassword
  },
  data () {
    return {
      email: '',
      password: '',
      emailIllegal: false,
      api_login: '../api/admin_login/',
      item: {}
    }
  },
  methods: {
    /**
      * @description 用来判断登陆时邮箱的格式
      */
    checkEmail () {
      let reg = /^[a-z0-9]([a-z0-9]*[-_]?[a-z0-9]+)*@([a-z0-9]*[-_]?[a-z0-9]+)+[\.][a-z]{2,3}([\.][a-z]{2})?$/i
      let legal = reg.test(this.email)
      if (legal === false && this.email !== '') {
        this.emailIllegal = true
      } else {
        this.emailIllegal = false
      }
    },
    /**
      * @description 当邮箱输入框聚焦的时候，取消对邮箱不合法的提示，用户体验更友好
      */
    emailInput () {
      this.emailIllegal = false
    },
    /**
      * @description 向后端传输没有格式问题的登陆信息，取回验证结果并给出反馈
      */
    communicate () {
      this.$http.post(this.api_login, this.item)
        .then((response) => {
          if (response.data === 'ERROR, wrong email or password.') {
            this.$Message.info('错误的账号或密码！')
          } else if (response.data === 'ERROR, wrong information.') {
            window.location.href = '../notfound'
          } else if (response.data === 'ERROR, incomplete information.') {
            window.location.href = '../notfound'
          } else {
            window.location.href = '../administrator'
          }
        }, (response) => {
          window.location.href = '../notfound'
        })
    },
    /**
      * @description 点击登陆按钮时的监听，首先对格式进行验证，没有格式问题后调用communicate函数与后端联系
      */
    login () {
      if (this.email === '' || this.password === '') {
        this.$Message.info('您的信息不完善！')
      } else if (this.emailIllegal === true) {
        this.$Message.info('您的输入的邮箱格式不正确！')
      } else {
        // 与后端链接进行信息传输和验证
        this.item = {
          'email': this.email,
          'password': this.hashPassword()
        }
        this.communicate()
      }
    },
    /**
      * @description 按下Enter键的监听，首先对格式进行验证，没有格式问题后调用communicate函数与后端联系
      */
    loginEnter (e) {
      if (e.keyCode === 13) {
        if (this.email === '' || this.password === '') {
          this.$Message.info('您的信息不完善！')
        } else if (this.emailIllegal === true) {
          this.$Message.info('您的输入的邮箱格式不正确！')
        } else {
          // 与后端链接进行信息传输和验证
          this.item = {
            'email': this.email,
            'password': this.hashPassword()
          }
          this.communicate()
        }
      }
    },
    /**
      * @description 对密码进行hash操作，提高传输的安全性
      */
    hashPassword () {
      var sha512 = require('js-sha512').sha512
      var hash = sha512.create()
      hash.update(this.password)
      return hash.hex()
    }
  }
}
</script>

<style>
.header {
  width: 100%;
  overflow: hidden;
  z-index: 1;
}

.ceiling {
  background-color: #1c1d26;
  padding: 1em 0 0;
  overflow: hidden;
}

.ceiling a {
  margin-left: 1em;
}

.ceiling-main {
  float: right;
  margin-right: 5em;
  padding-top: 1em;
}

.ceiling-main a {
  color: #9ba7b5;
  padding-left: 1em;
  padding-right: 1em;
}

.ceiling-main .mainpage {
  color: #9d2933;
  border-bottom: 1px solid #9d2933;
}

.ceiling-item:hover {
  color: #9d2933;
  border-bottom: 1px solid #9d2933;
}

body {
  background: url(../../../static/back.jpg) no-repeat;
  /* height: 100%;
  width: 100%; */
  overflow: hidden;
  background-size: cover;
}

.all {
  width: 40%;
  height: 350px;
  margin: 40px 0 0 5%;
  border-radius: 20px;
  background: rgba(230, 230, 250, 0.5);
}

.container {
  display: flex;
  width: 100%;
  height: 280px;
  padding: 3.78% 14.16%;
  flex-wrap: wrap;
}

.div {
  margin-top: 8px;
  flex: 1 1 100%;
}

#title {
  font-size: 15pt;
  font-weight: bold;
  text-align: center;
  padding-left: 38%;
  margin-bottom: 15px;
  flex: 1 1 100%;
}

.label {
  font-weight: bold;
  font-size: 15px;
  padding-top: 20px;
  padding-bottom: 40px;
  flex: 1 1 100%;
}

.text {
  border: 2px solid #E3E3E3;
  border-radius: 5px;
  font-size: 11pt;
  color: #808080;
  font-weight: bold;
  text-align: center;
  width: 100%;
  height: 38px;
  margin-bottom: 5px;
  margin-top: 5px;
  flex: 1 1 100%;
}

#login {
  width: 100%;
  margin-top: 10px;
  margin-bottom: 10px;
  flex: 1 1 100%;
}

#butt {
  padding-left: 75%;
}

a {
  font-weight: bold;
  font-size: 9pt;
  color: #4876FF;
}

#p {
  color: red;
}
</style>
