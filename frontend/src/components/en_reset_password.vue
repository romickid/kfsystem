<template>
  <div>
    <Button type="text" @click="find = true">修改密码</Button>
    <Modal v-model="find" title="修改密码页" @on-ok="ok" @on-cancel="cancel">
      <div class="div">
        <p>登录邮箱：</p>
        <i-input v-model="email" class="input" @on-blur="checkEmail" @on-focus="emailInput"></i-input>
        <i-label v-if="emailIllegal">
          <p class="p">请输入正确的邮箱！</p>
        </i-label>
      </div>
      <div class="div">
        <p>旧密码：</p>
        <i-input type="password" class="input" v-model="oldPassword"></i-input>
      </div>
      <div class="div">
        <p>新密码：</p>
        <i-input type="password" class="input" v-model="newPassword" @on-blur="checkNewPassword"></i-input>
        <i-label v-if="passwordNonstandard">
          <p class="p">密码只能且必须包含大小写字母和数字，长度6-20位！</p>
        </i-label>
      </div>
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
      oldPassword: '',
      newPassword: '',
      passwordNonstandard: false,
      emailIllegal: false
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
    checkNewPassword () {
      let reg = /^(?![a-z]+$)(?!\d+$)(?![A-Z]+$)(?![a-z\d]+$)(?![a-zA-Z]+$)(?![\dA-Z]+$)[a-zA-Z\d]{6,20}$/
      let standardContent = reg.test(this.newPassword)
      if (standardContent === false && this.newPassword !== '') {
        this.passwordNonstandard = true
      } else {
        this.passwordNonstandard = false
      }
    },
    ok () {
      if (this.email === '' || this.oldPassword === '' || this.newPassword === '') {
        this.$Message.info('您的信息不完善！')
      } else if (this.emailIllegal === true) {
        this.$Message.info('您的输入的邮箱格式不正确！')
      } else if (this.passwordNonstandard === true) {
        this.$Message.info('您的输入的密码格式不正确！')
      } else {
        // 与后端链接进行信息传输和验证
        this.$Message.info('与后端链接进行信息传输和验证！')
      }
      this.email = ''
      this.oldPassword = ''
      this.newPassword = ''
      this.emailIllegal = false
      this.passwordNonstandard = false
    },
    cancel () {
      this.email = ''
      this.oldPassword = ''
      this.newPassword = ''
      this.emailIllegal = false
      this.passwordNonstandard = false
    }
  }
}
</script>

<style>
.p {
  color: red;
}

.input {
  width: 300px;
}

.div {
  margin-bottom: 10px;
}
</style>