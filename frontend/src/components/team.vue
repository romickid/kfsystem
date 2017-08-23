<template>
  <div class='team'>
    <div class='team-content'>
      <div class='title'>
        <h2>客服人员列表</h2>
        <i-button type='text' @click='refresh' class='title-button'>刷新</i-button>
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
            <th style='border-right: 0;'>操作</th>
          </tr>
          <tr v-for='(kf, id) in kfstaff'>
            <td>{{ kf.email }}</td>
            <td>{{ kf.nickname }}</td>
            <td>{{ kf.is_register ? '已验证' : '未验证'}}</td>
            <td>{{ kf.is_online ? '在线' : '离线'}}</td>
            <th>{{ kf.connection_num }}</th>
            <th style='border-right: 0;'>
              <i-button type='text' @click='delete_cs(id)'>删除</i-button>
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
      apiAdminDeleteCs: '../api/admin_delete_cs/',
      customerService: {},
      deleteCSItem: {}
    }
  },
  methods: {
    /**
      * @description 添加客服时点击确定
      */
    ok () {
      if (this.kf === '') {
        this.$Message.info('邮箱不能为空')
      } else if (this.emailIsNotStandard === true) {
        this.$Message.info('您输入的邮箱格式不正确')
      } else {
        this.customerService = {
          'email': this.kf
        }
        this.add_cs_api()
      }
      this.cancel()
    },
    /**
      * @description 检查邮箱输入格式
      */
    check_email () {
      let reg = /^[a-z0-9]([a-z0-9]*[-_]?[a-z0-9]+)*@([a-z0-9]*[-_]?[a-z0-9]+)+[\.][a-z]{2,3}([\.][a-z]{2})?$/i
      let legal = reg.test(this.kf)
      if (this.kf === '') {
        this.emailIsNull = true
      } else if (legal === false) {
        this.emailIsNotStandard = true
      }
    },
    /**
      * @description 正在输入邮箱时取消邮箱格式检查标记
      */
    email_inputing () {
      this.emailIsNull = false
      this.emailIsNotStandard = false
    },
    /**
      * @description 添加客服调用后端接口
      */
    add_cs_api () {
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
            this.refresh()
          }
        }, (response) => {
          window.location.href = '../en_login'
        })
    },
    /**
      * @description 添加客服时点击取消，清空变量
      */
    cancel () {
      this.kf = ''
      this.emailIsNull = false
      this.emailIsNotStandard = false
    },
    /**
      * @description 删除客服调用后端接口
      */
    delete_cs_api () {
      this.$http.post(this.apiAdminDeleteCs, this.deleteCSItem)
        .then((response) => {
          if (response.data === 'ERROR, incomplete information.') {
            window.location.href = '../en_login'
          } else if (response.data === 'ERROR, wrong information.') {
            window.location.href = '../en_login'
          } else if (response.data === 'ERROR, session is broken.') {
            window.location.href = '../en_login'
          } else if (response.data === 'ERROR, wrong admin email.') {
            window.location.href = '../en_login'
          } else if (response.data === 'ERROR, wrong customerservice email.') {
            window.location.href = '../en_login'
          } else if (response.data === 'ERROR, customerservice is not belong to admin.') {
            window.location.href = '../en_login'
          } else {
            this.$Message.info('删除成功')
            this.refresh()
          }
        }, (response) => {
          window.location.href = '../en_login'
        })
    },
    /**
      * @description 删除客服
      */
    delete_cs (index) {
      this.deleteCSItem = {
        'email': this.kfstaff[index].email
      }
      this.delete_cs_api()
    },
    /**
      * @description 刷新客服详细信息
      */
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
  border-radius: 4px;
  margin: 4em 3em;
}

.title {
  padding: 1em 2em;
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
  width: 16.66%;
  border: 1px solid #d7dde4;
  border-bottom: 0;
  border-left: 0;
  padding: 0.5em 0;
}

.list td {
  width: 16.66%;
  border: 1px solid #d7dde4;
  border-bottom: 0;
  border-left: 0;
  padding: 0.5em 0;
}

.input p{
  color: red;
}

.title-button {
  padding: 0;
}
</style>
