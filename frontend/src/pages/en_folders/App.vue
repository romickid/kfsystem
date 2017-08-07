<template>
  <div>
    <form>
      <div class="all">
        <div class="container">
          <div>
            <label id="title">账号注册</label>
          </div>
          <div class="div">
            <label class="label">登录邮箱：</label>
            <input type="text" v-model="email" name="email" class="text" @blur="checkEmail" @focus="emailInput">
            <i-label v-if="emailIllegal">
              <p>请输入正确的邮箱！</p>
            </i-label>
          </div>
          <div class="div">
            <label class="label">登录密码：</label>
            <input type="password" v-model="password" name="password" class="text" @blur="checkPassword" @focus="passwordInput">
            <i-label v-if="passwordNonStandard">
              <p>密码要包含字母、数字和特殊字符，不包含空格，长度6-20位！</p>
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
            <label class="label">产品序列号：</label>
            <input type="text" v-model="serialNumber" name="serialNumber" class="text">
          </div>
          <div class="div">
            <Button type="primary" shape="circle" size="large" id="finish" @click="register">注册</Button>
          </div>
          <div>
            <label id="la">已有账号，直接</label>
            <a href="../en_login" target="_blank" id="login">登录</a>
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
      api_create1: '../api/admin_create/',
      item: {}
    }
  },
  methods: {
    checkEmail () {
      let reg = /^[a-z0-9]([a-z0-9]*[-_]?[a-z0-9]+)*@([a-z0-9]*[-_]?[a-z0-9]+)+[\.][a-z]{2,3}([\.][a-z]{2})?$/i
      let legal = reg.test(this.email)
      if (legal === false && this.email !== '') {
        this.emailIllegal = true
      } else {
        this.emailIllegal = false
      }
    },
    emailInput () {
      this.emailIllegal = false
    },
    checkPassword () {
      if (this.password !== this.passwordConfirm && this.password !== '' && this.passwordConfirm !== '') {
        this.passwordInConsistent = true
      }
      let reg = /^(?![a-zA-z]+$)(?!\d+$)(?![!@#$%^&*]+$)(?![a-zA-z\d]+$)(?![a-zA-z!@#$%^&*]+$)(?![\d!@#$%^&*]+$)[a-zA-Z\d!@#$%^&*]+$/
      let standardContent = reg.test(this.password)
      let standardLength = true
      if ((this.password.length >= 1 && this.password.length < 6) || this.password.length > 20) {
        standardLength = false
      }
      if ((standardContent === false || standardLength === false) && this.password !== '') {
        this.passwordNonStandard = true
      } else {
        this.passwordNonStandard = false
      }
    },
    passwordInput () {
      this.passwordInConsistent = false
    },
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
        var vm = this
        this.item = {
          'email': this.email,
          'nickname': this.nickname,
          'password': this.password,
          'serials': this.serialNumber
        }
        vm.$http.post(vm.api_create1, this.item)
          .then((response) => {
            if (response.data === 'ERROR, invalid data in serializer.') {
              this.$Message.info('未知错误')
            } else if (response.data === 'ERROR, serials is invalid.') {
              this.$Message.info('请输入正确的产品序列号！')
            } else if (response.data === 'ERROR, email has been registered.') {
              this.$Message.info('该邮箱已被注册！')
            } else if (response.data === 'ERROR, nickname has been used.') {
              this.$Message.info('该昵称已被注册')
            } else {
              window.location.href = '../en_login'
            }
          }, (response) => {
            this.$Message.info('未知错误')
          })
      }
    }
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
  width: 500px;
  height: 600px;
  margin: 10px 0 0 500px;
  border-radius: 10px;
  background: rgba(154, 192, 205, 0.5);
}

.container {
  display: flex;
  width: 400px;
  height: 500px;
  padding: 30px 75px;
  flex-wrap: wrap;
}

.div {
  margin-top: 8px;
}

#title {
  font-size: 20pt;
  font-weight: bold;
  margin-bottom: 25px;
  padding-left: 120px;
}

.label {
  font-weight: bold;
  font-size: 15px;
  padding-top: 30px;
  padding-bottom: 40px;
  flex: 1 1 500px;
}

.text {
  border: 2px solid #E3E3E3;
  border-radius: 5px;
  font-size: 11pt;
  height: 38px;
  color: #808080;
  font-weight: bold;
  text-align: center;
  margin-bottom: 5px;
  margin-top: 5px;
  width: 340px;
  height: 38px;
  flex: 1 1 500px;
}

.explain {
  font-weight: bold;
  font-size: 9pt;
  color: #808080;
  flex: 1 1 500px;
}

#apply {
  font-weight: bold;
  color: white;
  font-size: 15pt;
  background-color: #228B22;
  border-radius: 20px;
  width: 350px;
  height: 40px;
  flex: 1 1 500px;
}

a {
  font-weight: bold;
  font-size: 9pt;
  color: #4876FF;
}

#finish {
  width: 340px;
  margin-bottom: 10px;
}

#la {
  margin-left: 115px;
}

p {
  color: red;
}
</style>
