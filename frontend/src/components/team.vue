<template>
  <div class='team'>
    <div class='team-content'>
      <div class='title'>
        <h2>客服人员列表</h2>
        <i-button type='text' @click='refresh'>刷新</i-button>
        <div class='add'>
          <Icon type='person-add' class='add-icon'></Icon>
          <i-button type='text' @click='addModal = true' id='add-cs-button'>添加客服
          </i-button>
          <Modal v-model='addModal' title='添加客服' @on-ok='ok' @on-cancel='cancel' id='add-cs-modal'>
            <Form class='input'>
              <Form-item>
                <i-input placeholder='在此输入您要添加的客服邮箱' size=large v-model='kf' @on-blur='check_email' @on-focus='email_inputing' id='input-email'></i-input>
                <i-label v-if='emailIsNull'>
                  <p>邮箱不能为空</p>
                </i-label>
                <i-label v-if='emailIsNotStandard'>
                  <p>邮箱格式不正确</p>
                </i-label>
              </Form-item>
            </Form>
          </Modal>
        </div>
      </div>
      <div class='list'>
        <table cellspacing='0'>
          <tr>
            <th>帐号</th>
            <th>昵称</th>
            <th>验证状态</th>
            <th>在线状态</th>
            <th>连接人数</th>
            <th>操作</th>
          </tr>
          <tr v-for='(kf, id) in kfstaff'>
            <td>{{ kf.email }}</td>
            <td>{{ kf.nickname }}</td>
            <td>{{ kf.is_register ? '已验证' : '未验证'}}</td>
            <td>{{ kf.is_online ? '在线' : '离线'}}</td>
            <th>{{ kf.connection_num }}</th>
            <th>
              <i-button type='text' @click='deleteKf(id)'>删除</i-button>
            </th>
          </tr>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import 'iview/dist/styles/iview.css'
export default {
  name: 'team',
  data () {
    return {
      addModal: false,
      kf: '',
      kfstaff: [],
      emailIsNotStandard: false,
      emailIsNull: false,
      apiCustomerserviceCreate: '../api/customerservice_create/',
      apiAdminShowCsStatus: '../api/admin_show_cs_status/',
      customerService: {}
    }
  },
  methods: {
    ok () {
      if (this.kf === '') {
        this.$Message.info('邮箱不能为空')
      } else if (this.emailIsNotStandard === true) {
        this.$Message.info('您输入的邮箱格式不正确')
      } else {
        this.customerService = {
          'email': this.kf
        }
        this.communicate()
      }
      this.cancel()
    },
    check_email () {
      let reg = /^[a-z0-9]([a-z0-9]*[-_]?[a-z0-9]+)*@([a-z0-9]*[-_]?[a-z0-9]+)+[\.][a-z]{2,3}([\.][a-z]{2})?$/i
      let legal = reg.test(this.kf)
      if (this.kf === '') {
        this.emailIsNull = true
      } else if (legal === false) {
        this.emailIsNotStandard = true
      }
    },
    email_inputing () {
      this.emailIsNull = false
      this.emailIsNotStandard = false
    },
    communicate () {
      this.$http.post(this.apiCustomerserviceCreate, this.customerService)
        .then((response) => {
          if (response.data === 'ERROR, incomplete information.') {
            window.location.href = '../en_login'
          } else if (response.data === 'ERROR, wrong information.') {
            window.location.href = '../en_login'
          } else if (response.data === 'ERROR, session is broken.') {
            window.location.href = '../en_login'
          } else if (response.data === 'ERROR, admin_email is wrong.') {
            window.location.href = '../en_login'
          } else if (response.data === 'ERROR, email has been registered.') {
            this.$Message.info('该客服邮箱已被注册')
            this.kf = ''
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
      this.kf = ''
      this.emailIsNull = false
      this.emailIsNotStandard = false
    },
    deleteKf (index) {
      this.kfstaff.splice(index, 1)
    },
    refresh () {
      this.$http.post(this.apiAdminShowCsStatus)
        .then((response) => {
          if (response.data === 'ERROR, session is broken.') {
            window.location.href = '../en_login'
          } else if (response.data === 'ERROR, wrong email.') {
            window.location.href = '../en_login'
          } else {
            this.kfstaff = response.data
          }
        }, (response) => {
          window.location.href = '../en_login'
        })
    }
  },
  created () {
    this.refresh()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.team-content {
  border: 1px solid #d7dde4;
  border-bottom: 1px solid #d7dde4;
}

.title {
  padding: 0.5em 2em;
}

.title h2 {
  display: inline;
}

.add {
  float: right;
}

.add button {
  padding-left: 0.5em;
}

.list {
  background-color: #f5f7f9;
}

.list table {
  width: 100%;
  text-align: center;
}

.list th {
  width: 16.65%;
  border: 1px solid #bbbec4;
  border-bottom: 0;
  border-left: 0;
  padding: 0.5em 0;
}

.list td {
  width: 16.65%;
  border: 1px solid #bbbec4;
  border-bottom: 0;
  border-left: 0;
  padding: 0.5em 0;
}

.input p{
  color: red;
}
</style>
