<template>
  <div>
    <form>
      <div class="all">
        <div class="container">
          <label id="title">客服完善信息</label>
          <div>
            <label class="label">登录邮箱：</label>
            <input type="text" name="email" class="text" id="email">
          </div>
          <div>
            <label class="label">登录密码：</label>
            <input type="text" name="password" class="text" id="password">
          </div>
          <div>
            <label class="label">确认密码：</label>
            <input type="text" name="password_confirm" class="text" id="password_confirm">
          </div>
          <div>
            <label class="label">使用昵称：</label>
            <input type="text" name="nickname" class="text" id="nickname">
          </div>
          <div>
            <input type="button" name="apply" id="apply" class="button" value="完成">
          </div>
          <label id="la">已有账号，直接</label>
          <a href="../se_login" target="_blank" id="login">登录</a>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
body {
  background: url(../../../static/center.jpg) no-repeat;
  height: 100%;
  width: 100%;
  overflow: hidden;
  background-size: cover;
}

.all {
  width: 500px;
  height: 530px;
  margin: 30px 350px 0 100px;
  border-radius: 10px;
  background: rgba(230, 230, 250, 0.8);
}

.container {
  display: flex;
  width: 400px;
  height: 450px;
  padding: 30px 75px;
  flex-wrap: wrap;
}

#title {
  font-size: 20pt;
  font-weight: bold;
  text-align: center;
  width: 350px;
}

.label {
  font-weight: bold;
  flex: 1 1 500px;
}

.text {
  border: 2px solid #E3E3E3;
  border-radius: 5px;
  font-size: 11pt;
  height: 38px;
  color: #808080;
  font-weight: bold;
  text-align: center;
  width: 340px;
  height: 38px;
  flex: 1 1 500px;
}

.explain {
  font-weight: bold;
  font-size: 9pt;
  color: #808080;
  flex: 1 1 500px;
}

#apply {
  font-weight: bold;
  color: white;
  font-size: 15pt;
  background-color: #228B22;
  border-radius: 20px;
  width: 350px;
  height: 40px;
  flex: 1 1 500px;
}

a {
  font-weight: bold;
  font-size: 9pt;
  color: #4876FF;
}

#login {
  font-size: 12pt;
}

#la {
  width: 310px;
  text-align: right;
}
</style>
