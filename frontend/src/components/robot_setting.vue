<template>
  <Table border stripe :height="400" :columns="columns" :data="data"></Table>
</template>
<script>
import 'iview/dist/styles/iview.css'
export default {
  data () {
    return {
      columns: [
        {
          title: '问题',
          key: 'question',
          ellipsis: 'true',
          render: (h, params) => {
            return h('div', [
              h('strong', params.row.question)
            ])
          }
        },
        {
          title: '回答',
          key: 'answer',
          ellipsis: 'true'
        },
        {
          title: '关键词',
          key: 'keyword',
          ellipsis: 'true'
        },
        {
          title: '权重',
          key: 'weight',
          ellipsis: 'true'
        },
        {
          title: '操作',
          key: 'action',
          width: 150,
          align: 'center',
          render: (h, params) => {
            return h('div', [
              h('Button', {
                props: {
                  type: 'primary',
                  size: 'small'
                },
                style: {
                  marginRight: '5px'
                },
                on: {
                  click: () => {
                    this.show(params.index)
                  }
                }
              }, '查看'),
              h('Button', {
                props: {
                  type: 'error',
                  size: 'small'
                },
                on: {
                  click: () => {
                    this.delete_robot(params.index)
                  }
                }
              }, '删除')
            ])
          }
        }
      ],
      data: [],
      index: 0,
      question: '',
      answer: '',
      apiCustomerserviceSetrobotinfoDelete: '../api/customerservice_setrobotinfo_delete/',
      apiCustomerserviceSetrobotinfoShow: '../api/customerservice_setrobotinfo_show/',
      robot_question_delete: {},
      robot_question: {}
    }
  },
  methods: {
    /**
      * @description 点击查看显示某条智能机器人语料的详细信息
      */
    show (index) {
      this.$Modal.info({
        title: '机器人语料库',
        content: `问题：${this.data[index].question}<br>回答：${this.data[index].answer}<br>关键词：${this.data[index].keyword}<br>权重：${this.data[index].weight}`
      })
    },
    /**
      * @description 删除智能机器人语料库语料调用后端接口
      */
    delete_robot_api () {
      this.$http.post(this.apiCustomerserviceSetrobotinfoDelete, this.robot_question_delete)
        .then((response) => {
          if (response.data === 'ERROR, wrong information.') {
            window.location.href = '../se_login'
          } else if (response.data === 'ERROR, incomplete information.') {
            this.$Message.info('您所填的信息不完整')
          } else if (response.data === 'ERROR, session is broken.') {
            window.location.href = '../se_login'
          } else if (response.data === 'ERROR, wrong email.') {
            window.location.href = '../se_login'
          } else if (response.data === 'ERROR, info is not exist.') {
            this.$Message.info('该问题不存在')
          } else {
            this.$Message.info('删除成功')
            this.show_robot_question_api()
          }
        }, (response) => {
          window.location.href = '../se_login'
        })
    },
    /**
      * @description 显示机器人语料库调用后端接口
      */
    show_robot_question_api () {
      this.$http.post(this.apiCustomerserviceSetrobotinfoShow, this.robot_question)
        .then((response) => {
          if (response.data === 'ERROR, session is broken.') {
            window.location.href = '../se_login'
          } else if (response.data === 'ERROR, wrong email.') {
            window.location.href = '../se_login'
          } else {
            this.data = response.data
            for (var i = 0; i < this.data.length; i++) {
              if (this.data[i].weight === 1) {
                this.data[i].weight = '低'
              } else if (this.data[i].weight === 2) {
                this.data[i].weight = '中'
              } else if (this.data[i].weight === 3) {
                this.data[i].weight = '高'
              }
            }
          }
        }, (response) => {
          window.location.href = '../se_login'
        })
    },
    /**
      * @description 删除智能机器人语料库中语料
      */
    delete_robot (index) {
      this.robot_question_delete = {
        'question': this.data[index].question
      }
      this.delete_robot_api()
    }
  },
  created () {
    this.show_robot_question_api()
  }
}
</script>
