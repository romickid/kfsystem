<template>
  <div>
    <form>
      <div class="all">
        <div class="container">
          <div>
            <label id="title">客服完善信息</label>
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
          <div>
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
      email: '',
      password: '',
      passwordConfirm: '',
      nickname: '',
      emailIllegal: false,
      passwordInConsistent: false
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
    checkPassword () {
      if (this.password !== this.passwordConfirm && this.password !== '' && this.passwordConfirm !== '') {
        this.passwordInConsistent = true
      }
    },
    passwordInput () {
      this.passwordInConsistent = false
    },
    finish () {
      if (this.email === '' || this.password === '' || this.passwordConfirm === '' || this.nickname === '') {
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
  background: url(../../../static/center.jpg) no-repeat;
  height: 100%;
  width: 100%;
  overflow: hidden;
  background-size: cover;
}

.all {
  width: 500px;
  height: 530px;
  margin: 40px 0 0 500px;
  border-radius: 10px;
  background: rgba(154, 192, 205, 0.5);
}

.container {
  display: flex;
  width: 400px;
  height: 450px;
  padding: 30px 75px;
  flex-wrap: wrap;
}

.div {
  margin-top: 8px;
}

#title {
  font-size: 20pt;
  font-weight: bold;
  text-align: center;
  margin-left: 90px;
  width: 350px;
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
