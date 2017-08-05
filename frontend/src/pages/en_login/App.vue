<template>
  <div>
    <form>
      <div class="all">
        <div class="container">
          <label id="title">用户登录</label>
          <div class="div">
            <label class="label">登录邮箱：</label>
            <input type="text" v-model="email" name="email" class="text" @blur="checkEmail" @focus="emailInput">
            <i-label v-if="emailIllegal">
              <p id="p">请输入正确的邮箱！</p>
            </i-label>
          </div>
          <div class="div">
            <label class="label">登录密码：</label>
            <input type="text" v-model="password" name="password" class="text" id="password">
          </div>
          <div class="div">
            <Button type="primary" shape="circle" size="large" id="login" @click="login">登录</Button>
          </div>
          <div id="butt">
            <forget-password ref="forgetPassword"></forget-password>
          </div>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import ForgetPassword from '../../components/ForgetPassword'
export default {
  name: 'app',
  components: {
    ForgetPassword
  },
  data () {
    return {
      email: '',
      password: '',
      emailIllegal: false
    }
  },
  methods: {
    checkEmail () {
      let reg = /^([a-zA-Z0-9]+[_|]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/
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
    login () {
      if (this.email === '' || this.password === '') {
        this.$Message.info('您的信息不完善！')
      } else {
        // 与后端链接进行信息传输和验证
      }
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
  width: 500px;
  height: 350px;
  margin: 40px 250px 0 730px;
  border-radius: 10px;
  background: rgba(230, 230, 250, 0.5);
}

.container {
  display: flex;
  width: 400px;
  height: 280px;
  padding: 20px 75px;
  flex-wrap: wrap;
}

.div {
  margin-top: 8px;
}

#title {
  font-size: 20pt;
  font-weight: bold;
  text-align: center;
  padding-left: 120px;
  margin-bottom: 15px;
}

.label {
  font-weight: bold;
  font-size: 15px;
  padding-top: 20px;
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
  width: 340px;
  height: 38px;
  margin-bottom: 5px;
  margin-top: 5px;
  flex: 1 1 500px;
}

#login {
  width: 340px;
}

#butt {
  padding-left: 270px;
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

#p {
  color: red;
}
</style>
