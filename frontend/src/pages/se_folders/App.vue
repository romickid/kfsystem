<template>
  <div>
    <form>
      <div class="all">
        <div class="container">
          <div class="div">
            <label id="title">客服信息完善</label>
          </div>
          <div class="div">
            <label class="label">登录密码：</label>
            <input type="password" v-model="password" name="password" class="text" @blur="checkPassword" @focus="passwordInput">
            <i-label v-if="passwordNonStandard">
              <p>密码只能且必须包含大小写字母和数字，长度6-20位！</p>
            </i-label>
          </div>
          <div class="div">
            <label class="label">确认密码：</label>
            <input type="password" v-model="passwordConfirm" name="passwordConfirm" class="text" @blur="checkPassword" @focus="passwordInput">
            <i-label v-if="passwordInConsistent">
              <p>两次密码输入不一致！</p>
            </i-label>
          </div>
          <div class="div">
            <label class="label">使用昵称：</label>
            <input type="text" v-model="nickname" name="nickname" class="text">
          </div>
          <div class="div">
            <Button type="primary" shape="circle" size="large" id="finish" @click="finish">完成</Button>
          </div>
          <div class="div">
            <label id="la">已有账号，直接</label>
            <a href="../se_login" target="_blank" id="login">登录</a>
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
      password: '',
      passwordConfirm: '',
      nickname: '',
      passwordNonStandard: false,
      passwordInConsistent: false,
      api_set_profile: '../api/customerservice_set_profile/',
      api_customerservice_set_profile_check_vid: '../api/customerservice_set_profile_check_vid/',
      customerserviceVerify: {},
      item: {}
    }
  },
  methods: {
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
    passwordInput () {
      this.passwordInConsistent = false
    },
    communicate () {
      this.$http.post(this.set_profile, this.item)
        .then((response) => {
          if (response.data === 'ERROR, invalid data in serializer.') {
            window.location.href = '../notfound'
          } else if (response.data === 'ERROR, incomplete information.' || response.data === 'ERROR, wrong information.') {
            window.location.href = '../notfound'
          } else if (response.data === 'ERROR, admin_email is wrong.') {
            window.location.href = '../notfound'
          } else if (response.data === 'ERROR, email has not been registered.') {
            this.$Message.info('该邮箱未被注册！')
          } else if (response.data === 'ERROR, nickname has been used.') {
            this.$Message.info('该昵称已被注册！')
          } else {
            window.location.href = '../se_login'
          }
        }, (response) => {
          window.location.href = '../notfound'
        })
    },
    finish () {
      if (this.password === '' || this.passwordConfirm === '' || this.nickname === '') {
        this.$Message.info('您的信息不完善！')
      } else if (this.passwordNonstandard === true) {
        this.$Message.info('您的输入的密码格式不正确！')
      } else if (this.passwordInconsistent === true) {
        this.$Message.info('您两次输入的密码不一致！')
      } else {
        // 与后端链接进行信息传输和验证
        this.item = {
          'email': this.customerserviceVerify.email,
          'password': this.password,
          'nickname': this.nickname
        }
        this.communicate()
      }
    },
    verify () {
      this.$http.post(this.api_customerservice_set_profile_check_vid, this.customerserviceVerify)
        .then((response) => {
          if (response.data === 'ERROR, incomplete information.') {
            window.location.href = '../notfound'
          } else if (response.data === 'ERROR, wrong information.') {
            window.location.href = '../notfound'
          } else if (response.data === 'ERROR, wrong email or vid.') {
            window.location.href = '../notfound'
          }
        }, (response) => {
          window.location.href = '../notfound'
        })
    }
  },
  created () {
    this.customerserviceVerify = {
      'email': this.$utils.getUrlKey('email'),
      'vid': this.$utils.getUrlKey('key')
    }
    this.verify()
  }
}
</script>

<style>
body {
  background: url(../../../static/center.jpg) no-repeat;
  height: 100%;
  width: 100%;
  overflow: hidden;
  background-size: cover;
}

.all {
  width: 40%;
  height: 530px;
  margin: 3.2% 0 0 40%;
  border-radius: 10px;
  background: rgba(154, 192, 205, 0.5);
}

.container {
  display: flex;
  width: 100%;
  height: 85%;
  padding: 5.67% 14.16%;
  flex-wrap: wrap;
}

.div {
  margin-top: 1.78%;
  flex: 1 1 100%;
}

.label {
  font-weight: bold;
  font-size: 15px;
  padding-top: 30px;
  padding-bottom: 40px;
  flex: 1 1 100%;
}

#title {
  font-size: 15pt;
  font-weight: bold;
  margin-bottom: 25px;
  padding-left: 34%;
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
