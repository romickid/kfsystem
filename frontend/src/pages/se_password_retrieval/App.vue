<template>
  <div>
    <form>
      <div class="all">
        <div class="container">
          <label id="title">找回密码</label>
          <div>
            <label class="label">新密码：</label>
            <input type="text" name="newPassword" class="text" id="newPassword">
          </div>
          <div>
            <label class="label">确认密码：</label>
            <input type="text" name="repeat" class="text" id="repeat">
          </div>
          <div>
            <Button type="primary" shape="circle" size="large" id="finish">完成</Button>
          </div>
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
  background: url(../../../static/password.jpg) no-repeat;
  height: 100%;
  width: 100%;
  overflow: hidden;
  background-size: cover;
}

.all {
  width: 400px;
  height: 350px;
  margin: 170px 0 0 703px;
  border-radius: 10px;
  background: rgba(127, 255, 170, 0.3);
}

.container {
  display: flex;
  width: 370px;
  height: 280px;
  padding: 20px 50px;
  flex-wrap: wrap;
}

#title {
  font-size: 20pt;
  font-weight: bold;
  text-align: center;
  padding-left: 95px;
  margin-bottom: 15px;
}

.label {
  font-weight: bold;
  font-size: 15px;
  padding-top: 20px;
  padding-bottom: 40px;
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
  width: 300px;
  height: 38px;
  margin-bottom: 20px;
  margin-top: 5px;
  flex: 1 1 500px;
}

#finish {
  width: 300px;
}

a {
  font-weight: bold;
  font-size: 9pt;
  color: #4876FF;
}
</style>

