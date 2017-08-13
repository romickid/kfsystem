// import Vue from 'vue'
// import customer from '../../../src/pages/customer_newlabel/customer_newlabel.vue'
// describe('customer_newlabel.vue', () => {
//   it('用文本框发用消息，添加到对应的消息列表', () => {
//     const Constructor = Vue.extend(customer)
//     const vm = new Constructor().$mount()
//     const button = vm.$el.querySelector('.submit-button')
//     vm.text = 'hello'
//     const clickEvent = new window.Event('click')
//     button.dispatchEvent(clickEvent)
//     vm._watcher.run()
//     expect(vm.sessionList[0].messages[0].text).to.equal('hello')
//   })
//   it('在机器人的情况下选择切换客服', () => {
//     const Constructor = Vue.extend(customer)
//     const vm = new Constructor().$mount()
//     const button = vm.$el.querySelector('.switch-button')
//     const clickEvent = new window.Event('click')
//     button.dispatchEvent(clickEvent)
//     vm._watcher.run()
//     expect(vm.userList[0].id).to.not.equal(-1)
//   })
//   it('已为人工的情况下选择切换客服', () => {
//     const Constructor = Vue.extend(customer)
//     const vm = new Constructor().$mount()
//     vm.vm.userList[0].id = 'lalala'
//     const button = vm.$el.querySelector('.switch-button')
//     const clickEvent = new window.Event('click')
//     button.dispatchEvent(clickEvent)
//     vm._watcher.run()
//     expect(vm.userList[0].id).to.equal('lalala')
//   })
// })
