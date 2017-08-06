<template>
  <div>
    <p type="text" @click="showModal" class="show-modal"><a>机器人设置</a></p>
    <ul class="robot-setting">
      <li class="robot-modal" v-if="find" @on-ok="ok" @on-cancel="cancel">
        <a><p>增添语料</p>
        <input v-model="value" placeholder="请输入语料"></input>
        <button @click="ok">确定</button></a>
      </li>
      <li class="robot-modal" v-if="find" @on-ok="ok" @on-cancel="cancel">
        <a><p>更改语料</p></a>
      </li>
      <li class="robot-modal" v-if="find" @on-ok="ok" @on-cancel="cancel">
        <a><p>删除语料</p></a>
      </li>
    </ul>
  </div>
</template>
<script>
export default {
  data () {
    return {
      find: false,
      value: ''
    }
  },
  methods: {
    ok () {
      this.$Message.info('成功添加')
      this.value = ''
    },
    cancel () {
      this.value = ''
    },
    showModal () {
      this.find = !this.find
      // let modal = document.getElementById('robot-modal')
      // robot = document.createElemnt()
      // modal.style.position = "absolute"
      // modal.style.height = "100px"
      // model.style.left = "100px"
      // console.log(typeof(modal))
      // document.body.appendChild(modal)
    }
  }
}
</script>
<style>
  .show-modal a:hover{
    cursor: pointer;
  }
  .robot-setting {
    background: white;
    color: black;
    width: 132px;
    position: fixed;
    left: 40px;
    background-color: #FFF;
    border-radius: 4px;
    cursor: pointer;
    overflow: visible;
  }
  .robot-setting li {
    height: auto;
    font-size: small;
    text-align: center;
    color: grey;
    border: 1px solid #eee;
  }
  .robot-setting li a:hover {
    background-color: rgba(255, 255, 0, 0.1);
    display: block;
  }
</style>
