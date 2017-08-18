<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>Essential Links</h2>
    <ul>
      <li>
        <a href="https://vuejs.org" target="_blank">Core Docs</a>
      </li>
      <li>
        <a href="https://forum.vuejs.org" target="_blank">Forum</a>
      </li>
      <li>
        <a href="https://gitter.im/vuejs/vue" target="_blank">Gitter Chat</a>
      </li>
      <li>
        <a href="https://twitter.com/vuejs" target="_blank">Twitter</a>
      </li>
      <br>
      <li>
        <a href="http://vuejs-templates.github.io/webpack/" target="_blank">Docs for This Template</a>
      </li>
    </ul>
    <h2>Ecosystem</h2>
    <ul>
      <li>
        <a href="http://router.vuejs.org/" target="_blank">vue-router</a>
      </li>
      <li>
        <a href="http://vuex.vuejs.org/" target="_blank">vuex</a>
      </li>
      <li>
        <a href="http://vue-loader.vuejs.org/" target="_blank">vue-loader</a>
      </li>
      <li>
        <a href="https://github.com/vuejs/awesome-vue" target="_blank">awesome-vue</a>
      </li>
    </ul>
    <div>
      <div class="functions">
        <div @click="imgupload">发送图片</div>
      </div>
      <input id="inputFile" name='inputFile' type='file' accept="image/png, image/jpeg, image/gif, image/jpg" style="display: none" @change="fileup">
    </div>
  </div>
</template>

<script>
export default {
  name: 'hello',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      // for test, do not delete it.
      api_admin_create: './api/admin_create/',
      api_admin_login: './api/admin_login/',
      api_admin_reset_password: './api/admin_reset_password/',
      api_admin_show_communication_key: './api/admin_show_communication_key/',
      api_admin_reset_communication_key: './api/admin_reset_communication_key/',
      api_admin_find_password_email_request: './api/admin_find_password_email_request/',
      api_admin_find_password_check_vid: './api/admin_find_password_check_vid/',

      api_admin_delete_cs: './api/admin_delete_cs/',

      api_customerservice_create: './api/customerservice_create/',
      api_customerservice_set_profile: './api/customerservice_set_profile/',
      api_customerservice_login: './api/customerservice_login/',

      api_chattinglog_send_message: './api/chattinglog_send_message/',
      api_chattinglog_delete_record: './api/chattinglog_delete_record/',
      api_chattinglog_get_data: './api/chattinglog_get_data/',
      api_chattinglog_delete_record_ontime: './api/chattinglog_delete_record_ontime/',
      api_chattinglog_status_change: './api/chattinglog_status_change/',
      api_chattinglog_show_history: './api/chattinglog_show_history/',

      api_smallimagelog_send_image: './api/smallimagelog_send_image/',
      api_smallimagelog_show_history: './api/smallimagelog_show_history/',

      api_log_show_history: './api/log_show_history/',

      api_test_file: './api/test_file/',

      item: {},
      gridData: '',
      test: {},
      text: '',
      isText: false
    }
  },

  // FOR TEST, DO NOT DELETE IT!
  methods: {
    fileup () {
      var that = this
      var file = document.getElementById('inputFile').files[0]
      console.log('准备发送')
      if (file) {
        console.log('开始发送')
        let self = this
        if (/^image/.test(file.type)) {
          // 创建一个reader
          var reader = new FileReader()
          // 将图片将转成 base64 格式
          reader.readAsDataURL(file)
          // 读取成功后的回调
          reader.onloadend = function () {
            self.text = this.result
            self.isText = false
            console.log(self.text)
          }
          console.log(self.text)
        }
      } else {
        this.$Message.info('必须有文件')
      }
    },
    imgupload () {
      var file = document.getElementById('inputFile')
      console.log('点击发送')
      file.click()
      this.fileup()
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
