<template>
  <div class="system">
   <div class='key'>
    <div class='key-title'><h2>用户信息对接设置</h2></div>
    <div class='key-content'>
      <div class='introduction'>
        <p>您可以通过信息接口将用户名和用户ID与夜莺系统对接,从而在会话界面和历史记录中查看用户信息。</p>
        <a>点击查看客户用户信息对接流程</a>
      </div>
      <h3>通讯密钥:</h3><input readonly>
      <p class='remind'>字符串密钥为平台的API通讯密钥，请妥善保管，如果发现通讯密钥泄露请重设。</p><button>重新生成密钥</button>
    </div>
   </div>
   <div class='info'>
    <div class='info-title'>
      <h2>客服可获取用户信息种类设置</h2>
      <button>添加用户信息</button>
    </div>
    <div class='info-list'>
      <table cellspacing='0'>
        <tr>
          <th>种类</th>
          <th>例子</th>
          <th>操作</th>
        </tr>
        <tr class='list-item'>
          <td>Id</td>
          <td>例：</td>
          <td>无</td>
        </tr>
        <tr class='list-item'>
          <td>Username</td>
          <td>例：</td>
          <td>无</td>
        </tr>
        <tr class='list-item'>
          <td>Email</td>
          <td>例：</td>
          <td><button>删除</button></td>
        </tr>
      </table>
    </div>
   </div>
  </div>
</template>

<script>
export default {
  name: 'system'

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

.introduction p{
  display: inline;
}

.key-content h3 {
  padding-right: 2em
}

.key-content input {
  height: 3em;
}

.remind {
  padding: 1em 0em;
}


.key-content h3{
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

.info-title button {
  float: right;
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
</style>
