<template>
  <div>
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
      adminFindPassword: {},
      adminResetPassword: {},
      apiAdminFindPasswordCheckVid: '../api/admin_forget_password_check_vid/',
      apiAdminForgetPasswordSaveData: '../api/admin_forget_password_save_data/',
      newVid: ''
    }
  },
  methods: {
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
    newPasswordInput () {
      this.passwordInConsistent = false
      this.passwordNonStandard = false
    },
    finish () {
      if (this.newPassword === '' || this.newPasswordConfirm === '') {
        this.$Message.info('您的信息不完善！')
      } else {
        if (this.passwordInConsistent === false && this.passwordNonStandard === false) {
          // 与后端链接进行信息传输和验证
          this.adminResetPassword = {
            'email': this.adminFindPassword.email,
            'newpassword': this.hashPassword(),
            'vid': this.hashNewVid()
          }
          this.resetPassword()
        } else {
          this.$Message.info('您输入的密码不合法！')
        }
      }
    },
    verify () {
      this.$http.post(this.apiAdminFindPasswordCheckVid, this.adminFindPassword)
        .then((response) => {
          if (response.data === 'ERROR, incomplete information.') {
            window.location.href = '../notfound'
          } else if (response.data === 'ERROR, wrong information.') {
            window.location.href = '../notfound'
          } else if (response.data === 'ERROR, wrong email or vid.') {
            window.location.href = '../notfound'
          } else if (response.data === 'ERROR, invalid data in serializer.') {
            window.location.href = '../notfound'
          } else {
            this.newVid = response.data
          }
        }, (response) => {
          window.location.href = '../notfound'
        })
    },
    resetPassword () {
      this.$http.post(this.apiAdminForgetPasswordSaveData, this.adminResetPassword)
        .then((response) => {
          if (response.data === 'ERROR, incomplete information.') {
            window.location.href = '../notfound'
          } else if (response.data === 'ERROR, wrong information.') {
            window.location.href = '../notfound'
          } else if (response.data === 'ERROR, wrong email or vid.') {
            window.location.href = '../notfound'
          } else if (response.data === 'ERROR, invalid data in serializer.') {
            window.location.href = '../notfound'
          } else {
            window.location.href = '../en_login'
          }
        }, (response) => {
          window.location.href = '../notfound'
        })
    },
    hashPassword () {
      var sha512 = require('js-sha512').sha512
      var hash = sha512.create()
      hash.update(this.newPassword)
      return hash.hex()
    },
    hashNewVid () {
      var sha512 = require('js-sha512').sha512
      var hash = sha512.create()
      hash.update(this.newVid)
      return hash.hex()
    }
  },
  created () {
    this.adminFindPassword = {
      'email': this.$utils.getUrlKey('email'),
      'vid': this.$utils.getUrlKey('key')
    }
    this.verify()
  }
}
</script>

<style>
body {
  background: url(../../../static/password.jpg) no-repeat;
  height: 100%;
  width: 100%;
  overflow: hidden;
  background-size: cover;
}

.all {
  width: 32%;
  height: 350px;
  margin: 170px 0 0 55%;
  border-radius: 10px;
  background: rgba(127, 255, 170, 0.3);
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
  text-align: center;
  margin-bottom: 5px;
  margin-top: 5px;
  width: 100%;
  height: 38px;
  flex: 1 1 100%;
}

#finish {
  width: 100%;
  margin-bottom: 10px;
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

