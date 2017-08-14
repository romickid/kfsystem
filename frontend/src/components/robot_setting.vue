<template>
  <Table border :height="400":columns="columns7" :data="data6"></Table>
</template>
<script>
import 'iview/dist/styles/iview.css'
import editrobot from './edit_robot'
export default {
  data () {
    return {
      columns7: [
        {
          title: '问题',
          key: 'question',
          ellipsis: 'true',
          render: (h, params) => {
            return h('div', [
              h('strong', params.row.question)
            ]);
          }
        },
        {
          title: '回答',
          key: 'answer',
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
              }, '编辑'),
              h('Button', {
                props: {
                  type: 'error',
                  size: 'small'
                },
                on: {
                  click: () => {
                    this.remove(params.index)
                  }
                }
              }, '删除')
            ]);
          }
        }
      ],
      data6: [
        {
          question: '问题一',
          answer: '回答一'
        },
        {
          question: '问题二',
          answer: '回答二'
        }
      ],
      index: 0,
      question: '',
      answer: ''
    }
  },
  methods: {
    show (index) {
      this.$Modal.confirm({
        render: (h) => {
          return h('div', [
            h('Input', {
              props: {
                value: this.data6[index].question,
                autofocus: true,
                placeholder: this.data6[index].question
              },
              on: {
                input: (val) => {
                  this.data6[index].question = val;
                }
              }
            }),
            h('Input', {
              props: {
                value: this.data6[index].answer,
                autofocus: true,
                placeholder: this.data6[index].answer
              },
              on: {
                input: (val) => {
                  this.data6[index].answer = val;
                }
              }
            })
          ])
        }
      })
    },
    remove (index) {
      this.data6.splice(index, 1);
    }
  },
  components: {
    editrobot
  }
}
</script>
