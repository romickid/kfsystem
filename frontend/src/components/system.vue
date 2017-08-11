<template>
  <div class='system'>
    <div class='key'>
      <div class='key-title'>
        <h2>用户信息对接设置</h2>
      </div>
      <div class='key-content'>
        <div class='introduction'>
          <p>您可以通过信息接口将用户名和用户ID与夜莺系统对接,从而在会话界面和历史记录中查看用户信息。</p>
          <a>点击查看客户用户信息对接流程</a>
        </div>
        <h3>通讯密钥:</h3>
        <p class='key-number'>{{ communicationKey }}</p>
        <p class='remind'>字符串密钥为平台的API通讯密钥，请妥善保管，如果发现通讯密钥泄露请重设。</p>
        <i-button type='ghost' @click='reset_key'>重新生成密钥</i-button>
      </div>
    </div>
    <div class='info'>
      <div class='info-title'>
        <h2>客服可获取用户信息种类设置</h2>
        <div class='add'>
          <Icon type='person-ad'></Icon>
          <i-button type='text' @click='modal = true' id='add-info-button'>添加用户信息</i-button>
          <Modal v-model='modal' title='添加用户信息' @on-ok='ok' @on-cancel='cancel' id='add-info-modal'>
            <Form :model='formItem' :label-width='80' class='input'>
              <Form-item label='名称'>
                <Input v-model='formItem.name' placeholder='请输入' @on-blur='check_name' @on-focus='name_inputing' id='input-name'></Input>
                <i-label v-if='nameIsNull'>
                  <p>名称不能为空</p>
                </i-label>
              </Form-item>
              <Form-item label='自定义说明'>
                <Input v-model='formItem.comment' placeholder='请输入'
                @on-blur='check_comment' @on-focus='comment_inputing' id='input-comment'></Input>
                <i-label v-if='commentIsNull'>
                  <p>自定义信息不能为空</p>
                </i-label>
              </Form-item>
            </Form>
          </Modal>
        </div>
      </div>
      <div class='info-list'>
        <table cellspacing='0'>
          <tr>
            <th>名称</th>
            <th>说明</th>
            <th>操作</th>
          </tr>
          <tr class='list-item'>
            <td>Id</td>
            <td></td>
            <td>
              <i-button type='text' disabled>删除</i-button>
            </td>
          </tr>
          <tr class='list-item'>
            <td>用户名</td>
            <td></td>
            <td>
              <i-button type='text' disabled>删除</i-button>
            </td>
          </tr>
          <tr class='list-item' v-for='(infomation, id) in infomations'>
            <td>{{ infomation.name }}</td>
            <td>{{ infomation.comment }}</td>
            <td>
              <i-button type='text' @click='delete_info(id)'>删除</i-button>
            </td>
          </tr>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'system',
  data () {
    return {
      modal: false,
      formItem: {
        name: '',
        comment: ''
      },
      nameIsNull: false,
      commentIsNull: false,
      apiShowCommunicationKey: '../api/admin_show_communication_key/',
      apiResetCommunicationKey: '../api/admin_reset_communication_key/',
      apiAdminDisplayInfoCreate: '../api/admin_display_info_create/',
      apiAdminDisplayInfoDelete: '../api/admin_display_info_delete/',
      apiAdminDisplayInfoShow: '../api/admin_display_info_show/',
      communicationKey: '',
      infomationItem: {},
      deleteName: {},
      infomations: []
    }
  },
  methods: {
    check_name () {
      if (this.formItem.name === '') {
        this.nameIsNull = true
      }
    },
    name_inputing () {
      this.nameIsNull = false
    },
    check_comment () {
      if (this.formItem.comment === '') {
        this.commentIsNull = true
      }
    },
    comment_inputing () {
      this.commentIsNull = false
    },
    ok () {
      if (this.formItem.name === '' || this.formItem.comment === '') {
        this.$Message.info('您的信息不完善')
      } else {
        this.infomationItem = {
          'name': this.formItem.name,
          'comment': this.formItem.comment
        }
        this.add_api()
        this.show_info()
      }
      this.cancel()
    },
    add_api () {
      this.$http.post(this.apiAdminDisplayInfoCreate, this.infomationItem)
        .then((response) => {
          if (response.data === 'ERROR, session is broken.') {
            window.location.href = '../en_login'
          } else if (response.data === 'ERROR, wrong email.') {
            window.location.href = '../en_login'
          } else if (response.data === 'ERROR, attribute name has been used.') {
            this.$Message.info('该名称已存在')
          } else if (response.data === 'ERROR, invalid data in serializer.') {
            window.location.href = '../en_login'
          } else {
            this.$Message.info('添加成功')
          }
        }, (response) => {
          window.location.href = '../en_login'
        })
    },
    cancel () {
      this.formItem.name = ''
      this.formItem.comment = ''
      this.nameIsNull = false
      this.commentIsNull = false
    },
    delete_info (index) {
      this.deleteName = {
        'name': this.infomations[index].name
      }
      this.delete_api()
      this.show_info()
    },
    delete_api () {
      this.$http.post(this.apiAdminDisplayInfoDelete, this.deleteName)
        .then((response) => {
          if (response.data === 'ERROR, session is broken.') {
            window.location.href = '../en_login'
          } else if (response.data === 'ERROR, wrong email.') {
            window.location.href = '../en_login'
          } else if (response.data === 'ERROR, attribute is not existent.') {
            this.$Message.info('该名称不存在')
          } else {
            this.$Message.info('删除成功')
          }
        }, (response) => {
          window.location.href = '../en_login'
        })
    },
    reset_key () {
      this.$http.post(this.apiResetCommunicationKey)
        .then((response) => {
          if (response.data === 'ERROR, session is broken.') {
            window.location.href = '../en_login'
          } else if (response.data === 'ERROR, wrong email.') {
            window.location.href = '../en_login'
          } else if (response.data === 'ERROR, invalid data in serializer.') {
            window.location.href = '../en_login'
          } else {
            this.communicationKey = response.data.communication_key
          }
        }, (response) => {
          window.location.href = '../en_login'
        })
    },
    show_info () {
      this.$http.post(this.apiAdminDisplayInfoShow)
        .then((response) => {
          if (response.data === 'ERROR, session is broken.') {
            window.location.href = '../en_login'
          } else if (response.data === 'ERROR, wrong email.') {
            window.location.href = '../en_login'
          } else if (response.data === 'ERROR, display info is empty.') {
            this.infomations = []
          } else {
            this.infomations = response.data
          }
        }, (response) => {
          window.location.href = '../en_login'
        })
      },
      show_key () {
        this.$http.post(this.apiShowCommunicationKey)
          .then((response) => {
            if (response.data === 'ERROR, session is broken.') {
              window.location.href = '../en_login'
            } else if (response.data === 'ERROR, wrong email.') {
              window.location.href = '../en_login'
            } else {
              this.communicationKey = response.data.communication_key
            }
          }, (response) => {
            window.location.href = '../en_login'
          })
      }
  },
  created () {
    this.show_key()
    this.show_info()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.system {
  padding: 0em 3em;
}

.key {
  margin: 4em 0em;
  border: 1px solid #d7dde4;
}

.key-title {
  border-bottom: 1px solid #d7dde4;
  padding: 0.5em 2em;
}

.key-content {
  background-color: #f5f7f9;
  padding: 2em 2em;
}

.introduction {
  padding-bottom: 1em;
}

.introduction p {
  display: inline;
}

.key-content h3 {
  padding-right: 2em
}

.key-number {
  display: inline;
  padding: 0.5em 0.5em;
  background-color: #dddee1;
}

.remind {
  padding: 1em 0em;
}


.key-content h3 {
  display: inline;
}

.info {
  margin: 4em 0em;
  border: 1px solid #d7dde4;
}

.info-title {
  border-bottom: 1px solid #d7dde4;
  padding: 0.5em 2em;
}

.info-title h2 {
  display: inline;
}

.add {
  float: right;
}

.info-title button {
  padding-left: 0.5em;
}

.info-list {
  background-color: #f5f7f9;
}

.info-list table {
  width: 100%;
  text-align: center;
}

.info-list td {
  width: 33%;
  border: 1px solid #bbbec4;
  border-bottom: 0;
  border-left: 0;
  padding: 0.5em 0;
}

.info-list th {
  width: 33%;
  border: 1px solid #bbbec4;
  border-bottom: 0;
  border-left: 0;
  padding: 0.5em 0;
}

.input p {
  color: red;
}
</style>
