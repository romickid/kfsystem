<template>
  <div>
    <Button type="text" @click="find = true">修改密码</Button>
    <Modal v-model="find" title="修改密码" @on-ok="ok" @on-cancel="cancel">
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
      oldPassword: '',
      newPassword: '',
      passwordNonstandard: false,
      api_reset_password: '../api/admin_reset_password/',
      item: {}

    }
  },
  methods: {
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
      if (this.oldPassword === '' || this.newPassword === '') {
        this.$Message.info('您的信息不完善！')
      } else if (this.passwordNonstandard === true) {
        this.$Message.info('您的输入的密码格式不正确！')
      } else {
        // 与后端链接进行信息传输和验证
        this.item = {
          'password': this.hashPassword(this.oldPassword),
          'newpassword': this.hashPassword(this.newPassword)
        }
        this.communicate()
      }
      this.cancel()
    },
    communicate () {
      this.$http.post(this.api_reset_password, this.item)
        .then((response) => {
          if (response.data === 'ERROR, session is broken.') {
            window.location.href = '../en_login'
          } else if (response.data === 'ERROR, invalid data in serializer.') {
            window.location.href = '../en_login'
          } else if (response.data === 'ERROR, incomplete information.') {
            window.location.href = '../en_login'
          } else if (response.data === 'ERROR, wrong information.') {
            window.location.href = '../en_login'
          } else if (response.data === 'ERROR, wrong email or password.') {
            this.$Message.info('您输入的旧密码不正确')
          } else if (response.data === 'ERROR, wrong email.') {
            window.location.href = '../en_login'
          } else {
            this.$Message.info('密码修改成功！')
          }
        }, (response) => {
          window.location.href = '../en_login'
        })
    },
    cancel () {
      this.oldPassword = ''
      this.newPassword = ''
      this.passwordNonstandard = false
    },
    hashPassword (str) {
      var sha512 = require('js-sha512').sha512
      var hash = sha512.create()
      hash.update(str)
      str = hash.hex()
      return str
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