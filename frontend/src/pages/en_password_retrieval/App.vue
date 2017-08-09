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
            <input type="password" v-model="newPassword" name="newPassword" class="text" @blur="checkNewPassword" @focus="newPasswordInput">
            <i-label v-if="passwordNonStandard">
              <p>密码只能且必须包含大小写字母和数字，长度6-20位！</p>
            </i-label>
          </div>
          <div class="div">
            <label class="label">确认密码：</label>
            <input type="password" v-model="newPasswordConfirm" name="newPasswordConfirm" class="text" @blur="checkNewPassword" @focus="newPasswordInput">
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
      adminFindPssword: {},
      apiAdminFindPasswordCheckVid: '../api/admin_find_password_check_vid/',
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
    },
    finish () {
      if (this.newPassword === '' || this.newPasswordConfirm === '') {
        this.$Message.info('您的信息不完善！')
      } else {
        if (this.passwordInConsistent === false) {
          // 与后端链接进行信息传输和验证
        }
      }
    },
    verify () {
      this.$http.post(this.apiAdminFindPasswordCheckVid, this.adminFindPssword)
        .then((response) => {
          if (response.data === 'ERROR, incomplete information.') {
            window.location.href = '../main'
          } else if (response.data === 'ERROR, wrong information.') {
            window.location.href = '../main'
          } else if (response.data === 'ERROR, wrong vid.') {
            window.location.href = '../main'
          } else {
            return
          }
        }, (response) => {
          window.location.href = '../main'
        })
    }
  },
  created () {
    this.adminFindPssword = {
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

