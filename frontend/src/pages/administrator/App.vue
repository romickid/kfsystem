<template>
  <div id='app'>
    <!-- Header -->
    <div class='layout'>
      <div class='layout-ceiling'>
        <div class='layout-logo'>logo</div>
        <div class='layout-ceiling-main'>
          <a href='../main'>首页</a> |
          <a href='../documentation'>帮助中心</a>
        </div>
      </div>
    </div>
    <!-- Main -->
    <div class='main' :class="{'main-hide-text': spanLeft < 5}">
      <Row type='flex'>
        <i-col :span="spanLeft" class='main-menu-left'>
          <Menu active-name='1' theme='dark' width='auto' @on-select='select'>
            <div class='main-logo-left'>
              <span>logo</span>
              <p class='main-text'>{{ adminName }}</p>
            </div>
            <Menu-item name=''>
              <Icon type='ios-navigate' :size='iconSize'></Icon>
              <span class='main-text'>概览</span>
            </Menu-item>
            <Menu-item name='team'>
              <Icon type='ios-keypad' :size='iconSize'></Icon>
              <span class='main-text'>团队管理</span>
            </Menu-item>
            <Menu-item name='system'>
              <Icon type='ios-analytics' :size='iconSize'></Icon>
              <span class='main-text'>系统设置</span>
            </Menu-item>
            <Submenu name='1'>
              <template slot='title'>
                <Icon type='android-locate' :size='iconSize'></Icon>
                <span class='main-text'>多渠道设置</span>
              </template>
              <Menu-item name='web'>web</Menu-item>
              <Menu-item name='widget'>widget</Menu-item>
              <Menu-item name='mobile'>mobile</Menu-item>
            </Submenu>
          </Menu>
        </i-col>
        <i-col :span='spanRight' class='content'>
          <div class='main-header'>
            <i-button type='text' @click='toggleClick'>
              <Icon type='navicon' size='32'></Icon>
            </i-button>
            <div class='components'>
              <en-reset-password ref="enResetPassword"></en-reset-password>
            </div>
            <div>
              <p>{{ adminEmail }}</p>
            </div>
          </div>
          <div class='main-content'>
            <router-view></router-view>
          </div>
          <div class='main-copy'>
            2011-2016 &copy; TalkingData
          </div>
        </i-col>
      </Row>
    </div>
  </div>
</template>

<script>
import enResetPassword from '../../components/en_reset_password'
export default {
  name: 'app',
  components: {
    enResetPassword
  },
  data () {
    return {
      spanLeft: 5,
      spanRight: 19,
      apiAdminShowUserStatus: '../api/admin_show_user_status/',
      adminEmail: '',
      adminName: ''
    }
  },
  computed: {
    iconSize () {
      return this.spanLeft === 5 ? 14 : 24
    }
  },
  methods: {
    toggleClick () {
      if (this.spanLeft === 5) {
        this.spanLeft = 2
        this.spanRight = 22
      } else {
        this.spanLeft = 5
        this.spanRight = 19
      }
    },
    select (name) {
      this.$router.push('/' + name)
    },
    getAdminInfomation () {
      this.$http.post(this.apiAdminShowUserStatus)
        .then((response) => {
          if (response.data === 'ERROR, session is broken.') {
            window.location.href = '../en_login'
          } else if (response.data === 'ERROR, wrong email.') {
            window.location.href = '../en_login'
          } else {
            adminEmail = response.data.email
            adminName = response.data.nickname
          }
        })
    }
  },
  create () {
    this.getAdminInfomation()
  }
}
</script>

 <style scoped>
.layout {
  border: 1px solid #d7dde4;
  border-bottom: 0;
  background: #f5f7f9;
  position: relative;
  border-radius: 4px;
  overflow: hidden;
}

.layout-logo {
  color: #9ba7b5;
  font-size: 2em;
  float: left;
  position: relative;
}

.layout-ceiling {
  background: #464c5b;
  padding: 1em 0em;
  overflow: hidden;
}

.layout-ceiling-main {
  float: right;
  padding-top: 1em;
  margin-right: 3em;
}

.layout-ceiling-main a {
  color: #9ba7b5;
}

.main {
  border: 1px solid #d7dde4;
  background: #f5f7f9;
  position: relative;
  border-radius: 4px;
  overflow: hidden;
}

.main-content {
  min-height: 424px;
  margin: 15px;
  overflow: hidden;
  background: #fff;
  border-radius: 4px;
}

.main-content-body {
  padding: 10px;
}

.main-copy {
  text-align: center;
  padding: 10px 0 20px;
  color: #9ea7b4;
}

.main-menu-left {
  background: #464c5b;
}

.main-header {
  height: 60px;
  background: #fff;
  box-shadow: 0 1px 1px rgba(0, 0, 0, .1);
}

.main-logo-left {
  width: 90%;
  height: 30px;
  background: #5b6270;
  border-radius: 3px;
  margin: 15px auto;
  text-align: center;
}

.main-logo-left p {
  padding-left: 1em;
  display: inline;
}

.main-hide-text .main-text {
  display: none;
}

.components {
  display: inline;
}

.ivu-col {
  transition: width .2s ease-in-out;
}
</style>