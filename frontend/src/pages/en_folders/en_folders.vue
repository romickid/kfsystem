<template>
  <div>
    <div class="header">
      <div class="ceiling">
        <a href="../main/">
          <img src="../../../static/logo5.png" alt="" style="height:40px;width:40px">
          <img src="../../../static/name.png" alt="" style="height:40px">
        </a>
        <div class="ceiling-main">
          <a href="../main/" class="ceiling-item">首页</a> |
          <a href="../documentation/" class="ceiling-item">帮助中心</a> |
          <a href="../en_login/" class="ceiling-item">企业登录</a> |
          <a href="../en_folders/" class="ceiling-item current-page">企业注册</a> |
          <a href="../se_login/" class="ceiling-item">客服入口</a>
        </div>
      </div>
    </div>
    <form>
      <div class="all">
        <div class="container">
          <div class="div">
            <h1 id="title">企业账号注册</h1>
          </div>
          <div class="div">
            <label class="label">邮箱：</label>
            <input type="text" v-model="email" name="email" @blur="checkEmail" @focus="emailInput" id="input-email" class="text">
            <i-label v-if="emailIllegal">
              <p>请输入正确的邮箱！</p>
            </i-label>
          </div>
          <div class="div">
            <label class="label">密码：</label>
            <input type="password" v-model="password" name="password" @blur="checkPassword" @focus="passwordInput" id="input-password" class="text">
            <i-label v-if="passwordNonStandard">
              <p>密码只能且必须包含大小写字母和数字，长度6-20位！</p>
            </i-label>
          </div>
          <div class="div">
            <label class="label">确认密码：</label>
            <input type="password" v-model="passwordConfirm" name="passwordConfirm" @blur="checkPassword" @focus="passwordInput" id="input-password-confirm" class="text">
            <i-label v-if="passwordInConsistent">
              <p>两次密码输入不一致！</p>
            </i-label>
          </div>
          <div class="div">
            <label class="label">企业昵称：</label>
            <input type="text" v-model="nickname" name="nickname" class="text">
          </div>
          <div class="div" @keydown="registerEnter">
            <label class="label">产品序列号：</label>
            <input type="text" v-model="serialNumber" name="serialNumber" class="text">
          </div>
          <div class="div">
            <Button type="primary" shape="circle" size="large" id="finish" @click="register">注册</Button>
          </div>
          <div class="div">
            <label id="la">已有账号，直接</label>
            <a href="../en_login" id="login">登录</a>
          </div>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      email: '',
      password: '',
      passwordConfirm: '',
      nickname: '',
      serialNumber: '',
      emailIllegal: false,
      passwordNonStandard: false,
      passwordInConsistent: false,
      apiCreate: '../api/admin_create/',
      item: {}
    }
  },
  methods: {
    /**
      * @description 用来判断注册时邮箱的格式
      */
    checkEmail () {
      let reg = /^[a-z0-9]([a-z0-9]*[-_]?[a-z0-9]+)*@([a-z0-9]*[-_]?[a-z0-9]+)+[\.][a-z]{2,3}([\.][a-z]{2,3})?$/i
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
      * @description 对用户输入的注册密码安全性和两次输入的一致性进行验证，格式需要符合：长度在6-20位且必须包含大写字母、小写字母和数字
      */
    checkPassword () {
      if (this.password !== this.passwordConfirm && this.password !== '' && this.passwordConfirm !== '') {
        this.passwordInConsistent = true
      }
      let reg = /^(?![a-z]+$)(?!\d+$)(?![A-Z]+$)(?![a-z\d]+$)(?![a-zA-Z]+$)(?![\dA-Z]+$)[a-zA-Z\d]{6,20}$/
      let standardContent = reg.test(this.password)
      if (standardContent === false && this.password !== '') {
        this.passwordNonStandard = true
      } else {
        this.passwordNonStandard = false
      }
    },
    /**
      * @description 当密码输入框聚焦的时候，取消对密码格式不合法的提示，用户体验更友好
      */
    passwordInput () {
      this.passwordInConsistent = false
      this.passwordNonStandard = false
    },
    /**
      * @description 在信息无格式错误且完整的前提下与后端进行交互，并给出反馈
      */
    communicate () {
      this.$http.post(this.apiCreate, this.item)
        .then((response) => {
          if (response.data === 'ERROR, invalid data in serializer.') {
            window.location.href = '../notfound/'
          } else if (response.data === 'ERROR, incomplete information.' || response.data === 'ERROR, wrong information.') {
            window.location.href = '../notfound/'
          } else if (response.data === 'ERROR, serials is invalid.') {
            this.$Message.info('请输入正确的产品序列号！')
          } else if (response.data === 'ERROR, email has been registered.') {
            this.$Message.info('该邮箱已被注册！')
          } else if (response.data === 'ERROR, nickname has been used.') {
            this.$Message.info('该昵称已被注册!')
          } else {
            window.location.href = '../en_login/'
          }
        }, (response) => {
          window.location.href = '../notfound/'
        })
    },
    /**
      * @description 对注册完成按钮进行监听，在信息无格式错误且完整的前提下调用communicate函数与后端进行交互
      */
    register () {
      if (this.email === '' || this.password === '' || this.passwordConfirm === '' || this.nickname === '' || this.serialNumber === '') {
        this.$Message.info('您的信息不完善！')
      } else if (this.emailIllegal === true) {
        this.$Message.info('您的输入的邮箱格式不正确！')
      } else if (this.passwordNonStandard === true) {
        this.$Message.info('您的输入的密码格式不正确！')
      } else if (this.passwordInConsistent === true) {
        this.$Message.info('您两次输入的密码不一致！')
      } else {
        // 与后端链接进行信息传输和验证
        this.item = {
          'email': this.email,
          'nickname': this.nickname,
          'password': this.hashPassword(),
          'serials': this.serialNumber
        }
        this.communicate()
      }
    },
    /**
      * @description 对注册使用Enter键进行监听，在信息无格式错误且完整的前提下调用communicate函数与后端进行交互
      */
    registerEnter (e) {
      if (e.keyCode === 13) {
        if (this.email === '' || this.password === '' || this.passwordConfirm === '' || this.nickname === '' || this.serialNumber === '') {
          this.$Message.info('您的信息不完善！')
        } else if (this.emailIllegal === true) {
          this.$Message.info('您的输入的邮箱格式不正确！')
        } else if (this.passwordNonStandard === true) {
          this.$Message.info('您的输入的密码格式不正确！')
        } else if (this.passwordInConsistent === true) {
          this.$Message.info('您两次输入的密码不一致！')
        } else {
          // 与后端链接进行信息传输和验证
          this.item = {
            'email': this.email,
            'nickname': this.nickname,
            'password': this.hashPassword(),
            'serials': this.serialNumber
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
  border-radius: 4px;
  overflow: hidden;
  z-index: 1;
}

.ceiling {
  background-color: #1c1d26;
  padding: 1em 0 0;
  overflow: hidden;
}

.ceiling-main {
  float: right;
  margin-right: 3em;
  padding-top: 1em;
}

.ceiling-main a {
  color: #9ba7b5;
  padding-left: 1em;
  padding-right: 1em;
  font-size: 11pt;
}

.celling-main .current-page {
  color: #9d2933;  
}

.ceiling-item:hover {
  color: #9d2933;
}

body {
  background: url(../../../static/center.jpg) no-repeat;
  height: 100%;
  width: 100%;
  /* overflow: hidden; */
  background-size: cover;
   line-height: 1; 
}

.all {
  width: 40%;
  min-height: 525px;
  margin: 1.5% 0 0 30%;
  border-radius: 25px;
  background: rgba(243, 243, 243, 0.7);
}

.container {
  display: flex;
  width: 100%;
  height: 500px;
  padding: 5.67% 14.16%;
  flex-wrap: wrap;
}

.div {
  margin-top: 1.78%;
  flex: 1 1 100%;
}

#title {
  font-size: 15pt;
  font-weight: bold;
  text-align: center;
  flex: 1 1 100%;
}

.label {
  font-weight: bold;
  font-size: 15px;
  padding-top: 30px;
  padding-bottom: 40px;
  flex: 1 1 100%;
}

.text {
  border: 2px solid #E3E3E3;
  border-radius: 5px;
  font-size: 11pt;
  color: #808080;
  font-weight: bold;
  margin-bottom: 5px;
  margin-top: 5px;
  width: 100%;
  height: 38px;
  flex: 1 1 100%;
  padding-left: 1em;
}

.explain {
  font-weight: bold;
  font-size: 9pt;
  color: #808080;
  flex: 1 1 100%;
}

a {
  font-weight: bold;
  font-size: 9pt;
  color: #4876FF;
}

#finish {
  width: 100%;
  margin-bottom: 10px;
  flex: 1 1 100%;
}

#la {
  margin-left: 35%;
}

p {
  color: red;
}
</style>
