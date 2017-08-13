import Vue from 'vue'
import kf from '../../../src/pages/kf_working/kf_working.vue'

describe('kf_working.vue', () => {
  // it('添加用户到活跃用户列表', () => {
  //   const Constructor = Vue.extend(kf)
  //   const vm = new Constructor().$mount()
  //   let customer = vm.createUser('4', 'lala')
  //   vm.addCustomer(vm.userList, vm.sessionList, vm.historySessionList, customer)
  //   expect(vm.userList[0].id).to.equal('4')
  // })
  // it('添加用户到已挂断用户列表', () => {
  //   const Constructor = Vue.extend(kf)
  //   const vm = new Constructor().$mount()
  //   let customer = vm.createUser('4', 'lala')
  //   vm.addCustomer(vm.userList, vm.sessionList, vm.historySessionList, customer)
  //   vm.customerHangoff(vm.userList, vm.hangoffUserList,
  //     vm.sessionList, vm.hangoffSessionList,
  //       vm.historySessionList, customer.id)
  //   expect(vm.hangoffUserList[0].id).to.equal('4')
  // })
  // it('用户消息上浮', () => {
  //   const Constructor = Vue.extend(kf)
  //   const vm = new Constructor().$mount()
  //   let customer = vm.createUser('4', 'lala')
  //   vm.addCustomer(vm.userList, vm.sessionList, vm.historySessionList, customer)
  //   let customer1 = vm.createUser('5', 'lala')
  //   vm.addCustomer(vm.userList, vm.sessionList, vm.historySessionList, customer1)
  //   vm.popUp(vm.userList, 1)
  //   expect(vm.userList[0].id).to.equal('5')
  // })
  // it('从活跃消息列表中删除最后一个用户(同时列表中仅有一个用户)', () => {
  //   const Constructor = Vue.extend(kf)
  //   const vm = new Constructor().$mount()
  //   let customer = vm.createUser('4', 'lala')
  //   vm.addCustomer(vm.userList, vm.sessionList, vm.historySessionList, customer)
  //   vm.sessionIndex--
  //   vm.deleteCustomer(vm.userList, vm.sessionList, vm.historySessionList, '4')
  //   expect(vm.session.userId).to.equal(-1)
  // })
  // it('从活跃消息列表中删除非最后一个用户(列表中有多个用户，删除非最后一个用户)', () => {
  //   const Constructor = Vue.extend(kf)
  //   const vm = new Constructor().$mount()
  //   let customer = vm.createUser('4', 'lala')
  //   vm.addCustomer(vm.userList, vm.sessionList, vm.historySessionList, customer)
  //   let customer1 = vm.createUser('5', 'lala')
  //   vm.addCustomer(vm.userList, vm.sessionList, vm.historySessionList, customer1)
  //   vm.deleteCustomer(vm.userList, vm.sessionList, vm.historySessionList, '4')
  //   expect(vm.session.userId).to.equal('5')
  // })
  // it('用文本框发用消息，添加到对应的消息列表（当前为活跃状态）', () => {
  //   const Constructor = Vue.extend(kf)
  //   const vm = new Constructor().$mount()
  //   const button = vm.$el.querySelector('.submit-button')
  //   vm.text = 'hello'
  //   let customer = vm.createUser('4', 'lala')
  //   vm.addCustomer(vm.userList, vm.sessionList, vm.historySessionList, customer)
  //   const clickEvent = new window.Event('click')
  //   button.dispatchEvent(clickEvent)
  //   vm._watcher.run()
  //   expect(vm.sessionList[0].messages[0].text).to.equal('hello')
  // })
  // it('用文本框发用消息，添加到对应的消息列表（当前为已挂断状态）', () => {
  //   const Constructor = Vue.extend(kf)
  //   const vm = new Constructor().$mount()
  //   const button = vm.$el.querySelector('.submit-button')
  //   vm.hangon = false
  //   vm.text = 'hello'
  //   let customer = vm.createUser('4', 'lala')
  //   vm.addCustomer(vm.userList, vm.sessionList, vm.historySessionList, customer)
  //   vm.customerHangoff(vm.userList, vm.hangoffUserList,
  //     vm.sessionList, vm.hangoffSessionList,
  //       vm.historySessionList, customer.id)
  //   const clickEvent = new window.Event('click')
  //   button.dispatchEvent(clickEvent)
  //   vm._watcher.run()
  //   expect(vm.text).to.equal('')
  // })
  // it('在活跃状态，点击按钮切换到挂断列表', () => {
  //   const Constructor = Vue.extend(kf)
  //   const vm = new Constructor().$mount()
  //   const button = vm.$el.querySelector('.switchoff')
  //   const clickEvent = new window.Event('click')
  //   button.dispatchEvent(clickEvent)
  //   vm._watcher.run()
  //   expect(vm.hangon).to.equal(false)
  // })
  // it('在挂断状态，点击按钮切换到活跃列表', () => {
  //   const Constructor = Vue.extend(kf)
  //   const vm = new Constructor().$mount()
  //   const button = vm.$el.querySelector('.switchoff')
  //   const clickEvent = new window.Event('click')
  //   button.dispatchEvent(clickEvent)
  //   vm._watcher.run()
  //   expect(vm.hangon).to.equal(false)
  // })
  it('在活跃状态，点击按钮显示历史消息', () => {
    const Constructor = Vue.extend(kf)
    const vm = new Constructor().$mount()
    const button = vm.$el.querySelector('.history-message')
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    vm._watcher.run()
    expect(vm.history).to.equal(true)
  })
  it('在活跃状态，点击按钮隐藏历史消息', () => {
    const Constructor = Vue.extend(kf)
    const vm = new Constructor().$mount()
    vm.history = true
    const button = vm.$el.querySelector('.history-message')
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    vm._watcher.run()
    expect(vm.history).to.equal(false)
  })
  it('在挂断状态，点击按钮查看历史消息', () => {
    const Constructor = Vue.extend(kf)
    const vm = new Constructor().$mount()
    vm.hangon = false
    const button = vm.$el.querySelector('.history-message')
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    vm._watcher.run()
    expect(vm.history).to.equal(false)
  })
})
