<template>
  <div>
    <Button type="text" @click="find = true">忘记密码</Button>
    <Modal v-model="find" title="找回密码" @on-ok="ok" @on-cancel="cancel">
      <p>登录邮箱：</p>
      <br>
      <i-input v-model="email" id="input" @on-blur="checkEmail" @on-focus="emailInput"></i-input>
      <i-label v-if="emailIllegal">
        <p class="p">请输入正确的邮箱！</p>
      </i-label>
    </Modal>
  </div>
</template>
<script>
import 'iview/dist/styles/iview.css'
export default {
  data () {
    return {
      find: false,
      email: '',
      emailIllegal: false,
      api_forget_password_email_request: '../api/admin_forget_password_email_request/',
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
    ok () {
      if (this.email === '' || this.emailIllegal === true) {
        this.$Message.info('您的邮箱不正确！')
      } else {
        // 与后端链接进行信息传输和验证
        this.item = {
          'email': this.email
        }
        this.communicate()
      }
      this.cancel()
    },
    communicate () {
      this.$http.post(this.api_forget_password_email_request, this.item)
        .then((response) => {
          if (response.data === 'ERROR, wrong email.') {
            this.$Message.info('您的邮箱不正确！')
          } else if (response.data === 'ERROR, invalid data in serializer.') {
            window.location.href = '../notfound'
          } else if (response.data === 'ERROR, incomplete information.') {
            window.location.href = '../notfound'
          } else if (response.data === 'ERROR, wrong information.') {
            window.location.href = '../notfound'
          } else {
            this.$Message.info('验证邮件已发送至您的邮箱')
          }
        }, (response) => {
          window.location.href = '../notfound'
        })
    },
    cancel () {
      this.email = ''
      this.emailIllegal = false
    }
  }
}
</script>

<style>
.p {
  color: red;
}

#input {
  width: 300px;
}
</style>