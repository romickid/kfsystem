import Vue from 'vue'
import SePasswordRetrieval from '../../../src/pages/se_password_retrieval/se_password_retrieval.vue'

describe('test SePasswordRetrieval.vue', () => {
  it('测试密码输入不合法时是否能够标记', () => {
    const Constructor = Vue.extend(SePasswordRetrieval)
    const vm = new Constructor().$mount()
    const input = vm.$el.querySelector('#input-password')
    vm.newPassword = '1'
    const clickEvent = new window.Event('blur')
    input.dispatchEvent(clickEvent)
    vm._watcher.run()
    expect(vm.passwordNonStandard)
      .to.be.ok
  })
  it('测试密码输入不一致时是否能够标记', () => {
    const Constructor = Vue.extend(SePasswordRetrieval)
    const vm = new Constructor().$mount()
    const input = vm.$el.querySelector('#input-password-confirm')
    vm.newPassword = '123Abc'
    vm.newPasswordConfirm = '223Abc'
    const clickEvent = new window.Event('blur')
    input.dispatchEvent(clickEvent)
    vm._watcher.run()
    expect(vm.passwordInConsistent)
      .to.be.ok
  })
  it('测试正在输入密码时是否能取消不一致标记', () => {
    const Constructor = Vue.extend(SePasswordRetrieval)
    const vm = new Constructor().$mount()
    const input = vm.$el.querySelector('#input-password-confirm')
    vm.newPassword = '123Abc'
    vm.passwordConfirm = '223Abc'
    vm.checkNewPassword()
    const clickEvent = new window.Event('focus')
    input.dispatchEvent(clickEvent)
    vm._watcher.run()
    expect(vm.passwordInConsistent)
      .to.not.be.ok
  })
  it('测试正在输入密码时是否能取消不合法标记', () => {
    const Constructor = Vue.extend(SePasswordRetrieval)
    const vm = new Constructor().$mount()
    const input = vm.$el.querySelector('#input-password')
    vm.newPassword = '123abc'
    vm.checkNewPassword()
    const clickEvent = new window.Event('focus')
    input.dispatchEvent(clickEvent)
    vm._watcher.run()
    expect(vm.passwordNonStandard)
      .to.not.be.ok
  })
  // it('测试正在输入正确时是否能正确赋值', () => {
  //   const Constructor = Vue.extend(SePasswordRetrieval)
  //   const vm = new Constructor().$mount()
  //   const button = vm.$el.querySelector('#finish')
  //   vm.newPassword = '123Abc'
  //   vm.newPasswordConfirm = '123Abc'
  //   vm.checkNewPassword()
  //   const clickEvent = new window.Event('click')
  //   button.dispatchEvent(clickEvent)
  //   vm._watcher.run()
  //   expect(vm.customerserviceResetPassword.newpassword)
  //     .to.be.equal(vm.hashPassword())
  // })
  // it('测试正在输入有空时是否能不赋值', () => {
  //   const Constructor = Vue.extend(SePasswordRetrieval)
  //   const vm = new Constructor().$mount()
  //   const button = vm.$el.querySelector('#finish')
  //   vm.newPassword = ''
  //   vm.newPasswordConfirm = '123Abc'
  //   vm.checkNewPassword()
  //   const clickEvent = new window.Event('click')
  //   button.dispatchEvent(clickEvent)
  //   vm._watcher.run()
  //   expect(vm.customerserviceResetPassword)
  //     .to.be.empty
  // })
  // it('测试正在密码输入不合法时是否能不赋值', () => {
  //   const Constructor = Vue.extend(SePasswordRetrieval)
  //   const vm = new Constructor().$mount()
  //   const button = vm.$el.querySelector('#finish')
  //   vm.newPassword = '123abc'
  //   vm.newPasswordConfirm = '123abc'
  //   vm.nickname = 'abc'
  //   vm.checkNewPassword()
  //   const clickEvent = new window.Event('click')
  //   button.dispatchEvent(clickEvent)
  //   vm._watcher.run()
  //   expect(vm.customerserviceResetPassword)
  //     .to.be.empty
  // })
  // it('测试正在密码输入不一致时是否能不赋值', () => {
  //   const Constructor = Vue.extend(SePasswordRetrieval)
  //   const vm = new Constructor().$mount()
  //   const button = vm.$el.querySelector('#finish')
  //   vm.newPassword = '123Abc'
  //   vm.newPasswordConfirm = '123ABc'
  //   vm.checkNewPassword()
  //   const clickEvent = new window.Event('click')
  //   button.dispatchEvent(clickEvent)
  //   vm._watcher.run()
  //   expect(vm.customerserviceResetPassword)
  //     .to.be.empty
  // })
})
