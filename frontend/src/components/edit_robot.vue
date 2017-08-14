<template>
  <Button @click="editable=true">
  <Modal v-model="editable" title="编辑语料" @on-ok="ok" @on-cancel="cancel" z-index=20>
    <div>
      <p>问题：</p>
      <i-input v-model="question" placeholder=""></i-input>
    </div>
    <div class="div">
      <p>回答：</p>
      <i-input v-model="answer" placeholder=""></i-input>
    </div>
  </Modal>
</template>
<script>
import 'iview/dist/styles/iview.css'
export default {
  name: 'editrobot',
  data () {
    return {
      question: '',
      answer: '',
      editable: false
    }
  }
}
</script>
