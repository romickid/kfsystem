<template>
  <div>
    <form>
      <div class="all">
        <div class="container">
          <div class="div">
            <label id="title">用户登录</label>
          </div>
          <div class="div">
            <label class="label">登录邮箱：</label>
            <input type="text" v-model="email" name="email" class="text" @blur="checkEmail" @focus="emailInput">
            <i-label v-if="emailIllegal">
              <p id="p">请输入正确的邮箱！</p>
            </i-label>
          </div>
          <div class="div">
            <label class="label">登录密码：</label>
            <input type="password" v-model="password" name="password" class="text" id="password">
          </div>
          <div class="div">
            <Button type="primary" shape="circle" size="large" id="login" @click="login">登录</Button>
          </div>
          <!-- test -->
          <a href='' id='links'>联系客服</a>
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
      api_login: '../api/customer_login/',
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
    communicate () {
      this.$http.post(this.api_login, this.item)
        .then((response) => {
          if (response.data === 'ERROR, wrong email or password.') {
            this.$Message.info('错误的账号或密码！')
          } else if (response.data === 'ERROR, wrong information.') {
            alert('ERROR, wrong information.')
            window.location.href = '../notfound'
          } else if (response.data === 'ERROR, incomplete information.') {
            alert('incomplete information.')
            window.location.href = '../notfound'
          } else {
            window.location.href = '../index'
          }
        }, (response) => {
          alert('太搞笑了')
          window.location.href = '../notfound'
        })
    },
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
body {
  background: url(../../../static/back.jpg) no-repeat;
  height: 100%;
  width: 100%;
  overflow: hidden;
  background-size: cover;
}

.all {
  width: 40%;
  height: 350px;
  margin: 40px 250px 0 58.4%;
  border-radius: 10px;
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
