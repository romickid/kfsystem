<template>
  <div>
    <li type="text" @click="find = !find">忘记密码</li>
    <Modal v-if="find" title="找回密码页" @on-ok="ok" @on-cancel="cancel">
      <p>登录邮箱：</p>
      <br>
      <i-input v-model="value" placeholder="请输入邮箱" style="width: 300px"></i-input>
    </Modal>
  </div>
</template>
<script>
export default {
  data () {
    return {
      find: false,
      value: ''
    }
  },
  methods: {
    ok () {
      this.$Message.info('成功向您的邮箱发送邮件')
      this.value = ''
    },
    cancel () {
      this.value = ''
    }
  }
}
</script>
