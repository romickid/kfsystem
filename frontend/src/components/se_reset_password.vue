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
      api_reset_password: '../api/customerservice_reset_password/',
      item: {}
    }
  },
  methods: {
    /**
      * @description 用来判断新密码的安全性，格式需要符合：长度在6-20位且必须包含大写字母、小写字母和数字
      */
    checkNewPassword () {
      let reg = /^(?![a-z]+$)(?!\d+$)(?![A-Z]+$)(?![a-z\d]+$)(?![a-zA-Z]+$)(?![\dA-Z]+$)[a-zA-Z\d]{6,20}$/
      let standardContent = reg.test(this.newPassword)
      if (standardContent === false && this.newPassword !== '') {
        this.passwordNonstandard = true
      } else {
        this.passwordNonstandard = false
      }
    },
    /**
      * @description 在新密码格式正确的前提下，调用communicate函数与后端进行交互
      */
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
    /**
      * @description 向后端传输没有格式问题的新密码和需要修改的旧密码，取回验证结果并给出反馈
      */
    communicate () {
      this.$http.post(this.api_reset_password, this.item)
        .then((response) => {
          if (response.data === 'ERROR, wrong email.') {
            window.location.href = '../se_login/'
          } else if (response.data === 'ERROR, invalid data in serializer.') {
            window.location.href = '../se_login/'
          } else if (response.data === 'ERROR, session is broken.') {
            window.location.href = '../se_login/'
          } else if (response.data === 'ERROR, incomplete information.') {
            window.location.href = '../se_login/'
          } else if (response.data === 'ERROR, wrong information.') {
            window.location.href = '../se_login/'
          } else if (response.data === 'ERROR, wrong email or password.') {
            this.$Message.info('您的输入的旧密码不正确')
          } else {
            this.$Message.info('密码修改成功！')
          }
        }, (response) => {
          window.location.href = '../se_login/'
        })
    },
    /**
      * @description 关闭对话框时清除所有信息
      */
    cancel () {
      this.oldPassword = ''
      this.newPassword = ''
      this.passwordNonstandard = false
    },
    /**
      * @description 对密码进行hash操作，提高传输的安全性
      * @param {String} str 为传输的密码
      */
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