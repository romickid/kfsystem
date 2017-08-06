<template>
  <div class="team">
   <div class='team-content'>
    <div class='title'>
      <h2>客服人员列表</h2>
      <div class='add'>
      <Icon type="person-add" class='add-icon'></Icon>
      <i-button type='text' @click='addModal = true'>添加客服
      </i-button>
      <Modal
        v-model="addModal"
        title="添加客服"
        @on-ok="ok"
        @on-cancel="cancel">
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
          <th>姓名</th>
          <th>操作</th>
        </tr>
        <tr v-for='(kf, id) in kfstaff'>
          <td>{{ kf }}</td>
          <td>高小宸</td>
          <td>
            <i-button type='text' @click='deleteKf(id)'>删除
            </i-button>
          </td>
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
      kfstaff: []
    }
  },
  methods: {
    ok () {
      if (this.kf === '')
        return
      this.kfstaff.push(this.kf)
      this.kf = ''
    },
    cancel () {
      this.kf = ''
    },
    deleteKf (index) {
      this.kfstaff.splice(index, 1)
    }
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
  width: 33%;
  border: 1px solid #bbbec4;
  border-bottom: 0;
  border-left: 0;
  padding: 0.5em 0;
}

.list td {
  width: 33%;
  border: 1px solid #bbbec4;
  border-bottom: 0;
  border-left: 0;
  padding: 0.5em 0;
}
</style>
