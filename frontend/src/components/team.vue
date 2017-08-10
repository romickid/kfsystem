<template>
  <div class='team'>
    <div class='team-content'>
      <div class='title'>
        <h2>客服人员列表</h2>
        <i-button type='text' @click='refresh'>刷新</i-button>
        <div class='add'>
          <Icon type='person-add' class='add-icon'></Icon>
          <i-button type='text' @click='addModal = true'>添加客服
          </i-button>
          <Modal v-model='addModal' title='添加客服' @on-ok='ok' @on-cancel='cancel'>
            <form>
              <i-input placeholder='在此输入您要添加的客服邮箱' size=large v-model='kf'></i-input>
            </form>
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
      apiCustomerserviceCreate: '../api/customerservice_create/',
      apiCustomerserviceShowStatus: '../api/admin_show_cs_status/',
      adminEmail: {},
      customerService: {}
    }
  },
  methods: {
    ok () {
      if (this.kf === '') {
        return
      }
      this.customerService = {
        'email': this.kf,
        'admin_email': this.adminEmail.admin_email
      }
      this.communicate()
    },
    communicate () {
      this.$http.post(this.apiCustomerserviceCreate, this.customerService)
        .then((response) => {
          if (response.data === 'ERROR, incomplete information.') {
            // window.location.href = '../en_login'
            console.log(1)
          } else if (response.data === 'ERROR, email has been registered.') {
            this.$Message.info('该客服邮箱已被注册')
            this.kf = ''
          } else if (response.data === 'ERROR, admin_email is wrong.') {
            // window.location.href = '../en_login'
            console.log(2)
          } else if (response.data === 'ERROR, wrong information.') {
            // window.location.href = '../en_login'
            console.log(3)
          } else if (response.data === 'ERROR, invalid data in serializer.') {
            // window.location.href = '../en_login'
            console.log(4)
          } else {
            this.$Message.info('添加成功')
          }
        }, (response) => {
          // window.location.href = '../en_login'
          console.log(5)
        })
    },
    cancel () {
      this.kf = ''
    },
    deleteKf (index) {
      this.kfstaff.splice(index, 1)
    },
    refresh () {
      this.$http.post(this.apiCustomerserviceShowStatus)
        .then((response) => {
          if (response.data === 'ERROR, session is broken.') {
            // window.location.href = '../en_login'
            console.log(6)
          } else if (response.data === 'ERROR, wrong email.') {
            // window.location.href = '../en_login'
            console.log(7)
          } else {
            this.kfstaff = response.data
          }
        }, (response) => {
          // window.location.href = '../en_login'
          console.log(8)
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
</style>
