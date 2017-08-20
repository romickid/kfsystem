<template>
  <div class="outline">
    <p></p>
    <Row>
      <Col span="11">
        <Card>
          <p slot="title">在线客服数</p>
          <h1>{{ online_cs_count }}</h1>
        </Card>
      </Col>
      <Col span="11" offset="2">
        <Card>
          <p slot="title">当前会话数</p>
          <h1>{{ connect_number }}</h1>
        </Card>
      </Col>
    </Row>
  </div>
</template>

<script>
export default {
  name: 'outline',
  data () {
    return {
      connect_number: 0,
      online_cs_count: 0,
      apiAdminShowCsStatus: '../api/admin_show_cs_status/'
    }
  },
  methods: {
    get_information_api () {
      this.$http.post(this.apiAdminShowCsStatus)
        .then((response) => {
          if (response.data === 'ERROR, session is broken.') {
            window.location.href = '../en_login'
          } else if (response.data === 'ERROR, wrong email.') {
            window.location.href = '../en_login'
          } else {
            console.log(response.data)
            for (var p in response.data) {
              this.connect_number += response.data[p].connection_num
              this.online_cs_count += response.data[p].is_online
            }
          }
        }, (response) => {
          window.location.href = '../en_login'
        })
    }
  },
  created () {
    this.get_information_api()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.outline {
  padding: 0em 3em;
}
</style>
