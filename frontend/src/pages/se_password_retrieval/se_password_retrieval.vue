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
          <a href="../documentation" class='ceiling-item'>帮助中心</a> |
          <a href="../en_login" class='ceiling-item'>企业登录</a> |
          <a href="../en_folders" class='ceiling-item'>企业注册</a> |
          <a href="../se_login" class='ceiling-item'>客服入口</a>
        </div>
      </div>
    </div>    
    <form>
      <div class="all">
        <div class="container">
          <div class="div">
            <label id="title">找回密码</label>
          </div>
          <div class="div">
            <label class="label">新密码：</label>
            <input type="password" v-model="newPassword" name="newPassword" class="text" @blur="checkNewPassword" @focus="newPasswordInput" id="input-password">
            <i-label v-if="passwordNonStandard">
              <p>密码只能且必须包含大小写字母和数字，长度6-20位！</p>
            </i-label>
          </div>
          <div class="div">
            <label class="label">确认密码：</label>
            <input type="password" v-model="newPasswordConfirm" name="newPasswordConfirm" class="text" @blur="checkNewPassword" @focus="newPasswordInput" id="input-password-confirm">
            <i-label v-if="passwordInConsistent">
              <p>两次密码输入不一致！</p>
            </i-label>
          </div>
          <div class="div">
            <Button type="primary" shape="circle" size="large" id="finish" @click="finish">完成</Button>
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
      newPassword: '',
      newPasswordConfirm: '',
      passwordNonStandard: false,
      passwordInConsistent: false,
      apiCustomerserviceForgetPasswordCheckVid: '../api/customerservice_forget_password_check_vid/',
      apiCustomerserviceForgetPasswordSaveData: '../api/customerservice_forget_password_save_data/',
      customerserviceFindPassword: {},
      customerserviceResetPassword: {},
      newVid: ''
    }
  },
  methods: {
    /**
      * @description 用来判断新密码的安全性，格式需要符合：长度在6-20位且必须包含大写字母、小写字母和数字
      */
    checkNewPassword () {
      if (this.newPassword !== this.newPasswordConfirm && this.newPassword !== '' && this.newPasswordConfirm !== '') {
        this.passwordInConsistent = true
      }
      let reg = /^(?![a-z]+$)(?!\d+$)(?![A-Z]+$)(?![a-z\d]+$)(?![a-zA-Z]+$)(?![\dA-Z]+$)[a-zA-Z\d]{6,20}$/
      let standardContent = reg.test(this.newPassword)
      if (standardContent === false && this.newPassword !== '') {
        this.passwordNonStandard = true
      } else {
        this.passwordNonStandard = false
      }
    },
    /**
      * @description 当新密码输入框聚焦的时候，取消对新密码格式不合法的提示，用户体验更友好
      */
    newPasswordInput () {
      this.passwordInConsistent = false
      this.passwordNonStandard = false
    },
    /**
      * @description 对完成按钮进行监听，在信息无格式错误且完整的前提下调用resetPassword函数与后端进行交互
      */
    finish () {
      if (this.newPassword === '' || this.newPasswordConfirm === '') {
        this.$Message.info('您的信息不完善！')
      } else {
        if (this.passwordInConsistent === false && this.passwordNonStandard === false) {
          // 与后端链接进行信息传输和验证
          this.customerserviceResetPassword = {
            'email': this.customerserviceFindPassword.email,
            'newpassword': this.hashPassword(),
            'vid': this.newVid
          }
          this.resetPassword()
        } else {
          this.$Message.info('您的密码不合法！')
        }
      }
    },
    /**
      * @description 检查进入网页的链接是否合法（真的还是伪造的），若不合法则跳转到404页
      */
    verify () {
      this.$http.post(this.apiCustomerserviceForgetPasswordCheckVid, this.customerserviceResetPassword)
        .then((response) => {
          if (response.data === 'ERROR, incomplete information.') {
            window.location.href = '../notfound'
          } else if (response.data === 'ERROR, wrong information.') {
            window.location.href = '../notfound'
          } else if (response.data === 'ERROR, wrong email or vid.') {
            window.location.href = '../notfound'
          } else if (response.data === 'ERROR, vid is expired.') {
            window.location.href = '../timeout'
          } else if (response.data === 'ERROR, invalid data in serializer.') {
            window.location.href = '../notfound'
          } else {
            this.newVid = response.data
          }
        }, (response) => {
          window.location.href = '../notfound'
        })
    },
    /**
      * @description 把用户设置的新密码传输到后端进行交互，并得到反馈
      */
    resetPassword () {
      this.$http.post(this.apiCustomerserviceForgetPasswordSaveData, this.adminResetPassword)
        .then((response) => {
          if (response.data === 'ERROR, incomplete information.') {
            window.location.href = '../notfound'
          } else if (response.data === 'ERROR, wrong information.') {
            window.location.href = '../notfound'
          } else if (response.data === 'ERROR, wrong email or vid.') {
            window.location.href = '../notfound'
          } else if (response.data === 'ERROR, vid is expired.') {
            window.location.href = '../timeout'
          } else if (response.data === 'ERROR, invalid data in serializer.') {
            window.location.href = '../notfound'
          } else {
            window.location.href = '../se_login'
          }
        }, (response) => {
          window.location.href = '../notfound'
        })
    },
    /**
      * @description 对密码进行hash操作，提高传输的安全性
      */
    hashPassword () {
      var sha512 = require('js-sha512').sha512
      var hash = sha512.create()
      hash.update(this.newPassword)
      return hash.hex()
    },
    /**
      * @description 传输时保证vid的安全性
      */
    hashNewVid () {
      var sha512 = require('js-sha512').sha512
      var hash = sha512.create()
      hash.update(this.newVid)
      return hash.hex()
    }
  },
  /**
    * @description 利用钩子函数，在打印页面前验证链接的真实性
    */
  created () {
    this.customerserviceFindPassword = {
      'email': this.$utils.getUrlKey('email'),
      'vid': this.$utils.getUrlKey('key')
    }
    this.verify()
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

.ceiling a {
  margin-left: 1em;
}

.ceiling-main {
  float: right;
  margin-right: 5em;
  padding-top: 0.6em;
}

.ceiling-main a {
  color: #9ba7b5;
  padding-left: 1em;
  padding-right: 1em;
  font-size: 11pt;
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
  background: url(../../../static/password.jpg) no-repeat;
  height: 100%;
  width: 100%;
  overflow: hidden;
  background-size: cover;
}

.all {
  width: 40%;
  height: 350px;
  margin: 6% 0 0 30%;
  border-radius: 25px;
  background: rgba(243, 243, 243, 0.7);
}

.container {
  display: flex;
  width: 100%;
  height: 280px;
  padding: 20px 14.16%;
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

#finish {
  width: 100%;
  margin-top: 10px;
  flex: 1 1 100%;
}

a {
  font-weight: bold;
  font-size: 9pt;
  color: #4876FF;
}

p {
  color: red;
}
</style>

