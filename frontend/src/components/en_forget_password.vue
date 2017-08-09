<template>
  <div>
    <Button type="text" @click="find = true">忘记密码</Button>
    <Modal v-model="find" title="找回密码页" @on-ok="ok" @on-cancel="cancel">
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
      api_find_password_email_request: '../api/admin_find_password_email_request/',
      vm: this,
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
      if (this.email === '') {
        this.emailIllegal = false
        this.$Message.info('您的信息不完善！')
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
      this.vm.$http.post(this.vm.api_find_password_email_request, this.item)
        .then((response) => {
          if (response.data === 'ERROR, wrong email.') {
            this.$Message.info('错误的账号！')
          } else if (response.data === 'ERROR, invalid data in serializer.') {
            this.$Message.info('未知错误！')
          } else if (response.data === 'ERROR, incomplete information.') {
            this.$Message.info('信息不完善！')
          } else if (response.data === 'ERROR, wrong information.') {
            this.$Message.info('信息错误！')
          } else {
            this.$Message.info(response.data)
            // window.location.href = '../en_login'
          }
        }, (response) => {
          this.$Message.info('未知错误2！')
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