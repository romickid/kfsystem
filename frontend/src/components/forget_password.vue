<template>
  <div>
    <Button type="text" @click="find = true">忘记密码</Button>
    <Modal v-model="find" title="找回密码页" @on-ok="ok" @on-cancel="cancel">
      <p>登录邮箱：</p>
      <br>
      <i-input v-model="email" id="input" @on-blur="checkEmail" @on-focus="emailInput"></i-input>
      <i-label v-if="isEmpty">
        <p class="p">请输入邮箱！</p>
      </i-label>
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
      isEmpty: false,
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
    ok () {
      if (this.email === '') {
        this.isEmpty = false
        this.emailIllegal = false
      } else {
        if (this.emailIllegal === false) {
          this.$Message.info('成功向您的邮箱发送邮件!')
        } else {
          this.$Message.info('您的邮箱不正确，请重新填写申请！')
        }
        this.email = ''
        this.isEmpty = false
        this.emailIllegal = false
      }
    },
    cancel () {
      this.email = ''
      this.isEmpty = false
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