<template>
  <div class="team">
   <div class='team-content'>
    <div class='title'>
      <h2>客服人员列表</h2>
      <button>添加客服</button>
    </div>
    <div class='list'>
      <table cellspacing='0'>
        <tr>
          <th>帐号</th>
          <th>姓名</th>
          <th>操作</th>
        </tr>
        <tr>
          <td>xiaochen.gao@icloud.com</td>
          <td>高小宸</td>
          <td><button>删除</button></td>
        </tr>
      </table>
    </div>
   </div>
  </div>
</template>

<script>
export default {
  name: 'team'

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

.title h2{
  display: inline;
}

.title button {
  float: right;
}

.list {
  background-color: #f5f7f9;
}
.list table {
  width: 100%;
  text-align: center;
}
.list th{
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
