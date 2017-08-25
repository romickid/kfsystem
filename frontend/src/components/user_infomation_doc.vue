<template>
  <div id='app'>
    <div class='main-content-head'>
      <h1>客户账户体系对接流程</h1>
      <p>企业可以将自己的用户体系和BIG5打通，当企业用户通过BIG5咨询问题的时候，企业客服能够识别当前用户是谁。</p>
    </div>
    <div class='main-content-body'>
      <div class='guide'>
        <h2>获取用户信息对接通讯密钥</h2>
        <ul>
          <li>1. 登录BIG5智能客服，进入系统设置，在页面中找到通讯秘钥。
            <img src='./docPic/doc13.png'>
          </li>
          <li>2. 该通讯密钥（后面提到的secureKey参数）用来对用户信息做签名。你也可以点击“重新生成通讯密钥”更新它。</li>
          <li>提示：只有管理员才有此权限。</li>
        </ul>
      </div>
      <div class='line'></div>
      <div class='guide'>
        <h2>桌面网站、移动网站用户信息对接</h2>
        <ul>
          <li>1. 进入BIG5多渠道设置，找到相应的咨询页面地址：</li>
          <li>2. 访问BIG5客服url时，带入用户信息</li>
          <li>例如：http://192.168.55.33:8000/customer_newlabel/customer_newlabel.html?userId=123@qq.com&userName=aaa&adminName＝lalala&signature=2f3b3bc0e8b51e17ff2b2440005dd5fa</li>
          <li>请求参数请参考参数说明</li>
          <li>提示：这样的url暴露给用户不太美观，建议企业自己创建一个独立页面，用iframe标签嵌入该地址，如：</li>
          <li>请求参数请参考参数说明</li>
        </ul>
      </div>
      <div class='line'></div>
      <div class='guide'>
        <h2>请求参数说明</h2>
        <Table stripe :columns='columns' :data='data'></Table>
        <ul>
          <li>signature生成算法：</li>
          <li>1. 用户ID、用户名、企业名和通讯密钥按参数名自然排序（即升序）</li>
          <li>2. 把他们的参数值拼接成一个字符串</li>
          <li>3. 对拼接后的字符串做sha512加密，得到的加密结果即为signature</li>
          <li>例如：</li>
          <li>userId=123</li>
          <li>userName=张三</li>
          <li>adminName=jisuanke</li>
          <li>secureKey=eb19db3df22644e18d11a6994e89934f</li>
          <li>按自然排序后的顺序为：adminName,secureKey,userId,userName</li>
          <li>拼接后的参数值为：eb19db3df22644e18d11a6994e89934fjisuanke123张三</li>
          <li>sha512后生成的signtaure为：c119ad4929bc44a1d52b9febb6ca78eb</li>
          <li>原理：</li>
          <li>用户信息对接验证是基于通讯密匙来完成的，通讯密匙是一个随机生成的唯一的字符串，我们借助它来建立双方的信任关系，保证企业传递的用户信息是合法且有效的。</li>
        </ul>
      </div>
      <div class='line'></div>
      <div class='guide'>
        <h2>附：常见问题</h2>
        <ul>
          <li>对接的用户信息，在哪里体现？</li>
          <li>在客服界面的右边栏中显示用户信息</li>
        </ul>
      </div>
      <div class='line'></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'web',
  data () {
    return {
      columns: [
        {
          title: '参数名称',
          key: 'parameterName'
        },
        {
          title: '是否必须',
          key: 'isEssential'
        },
        {
          title: '类型',
          key: 'parameterType'
        },
        {
          title: '描述',
          key: 'parameterDescribe'
        }
      ],
      data: [
        {
          parameterName: 'userId',
          isEssential: '是',
          parameterType: 'string',
          parameterDescribe: '用户唯一标识'
        },
        {
          parameterName: 'userName',
          isEssential: '是',
          parameterType: 'string',
          parameterDescribe: '用户名'
        },
        {
          parameterName: 'adminName',
          isEssential: '是',
          parameterType: 'string',
          parameterDescribe: '公司名'
        },
        {
          parameterName: 'signature',
          isEssential: '是',
          parameterType: 'string',
          parameterDescribe: 'sha512签名串'
        }
      ]
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#app {
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  color: #2c3e50;
}
/*= font-size
-----------------------------------------------------------------*/

h1 {
  font-size: 3em;
  font-weight: normal;
}

h2 {
  font-size: 2.1em;
  font-weight: normal;
}

h3 {
  font-size: 1.8em;
  font-weight: normal;
}

h4 {
  font-size: 1em;
  font-weight: normal;
}

h5 {
  font-size: 0.5em;
  font-weight: normal;
}

p {
  font-size: 1.1em;
  padding: 1em 0em;
}

.guide li {
  font-size: 1.3em;
}
/*= main
-----------------------------------------------------------------*/

.main-content-head h1 {
  margin-bottom: 0;
}

.main-content-head {
  padding-bottom: 2em;
}

.main-content-body ul {
  padding: 0.7em 1.3em;
}

.line {
  margin: 2em 0em;
  border: 1px solid #2a333b;
  border-top: 0px;
}

.guide a {
  color: #9d2933;
}

img {
  width: 600px;
  margin: 2em 0em;
}
</style>
