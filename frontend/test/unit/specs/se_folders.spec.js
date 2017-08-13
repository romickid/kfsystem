import Vue from 'vue'
import SeFolders from '../../../src/pages/se_folders/se_folders.vue'

describe('test SeFolders.vue', () => {
  it('测试密码输入不合法时是否能够标记', () => {
    const Constructor = Vue.extend(SeFolders)
    const vm = new Constructor().$mount()
    const input = vm.$el.querySelector('#input-password')
    vm.password = '1'
    const clickEvent = new window.Event('blur')
    input.dispatchEvent(clickEvent)
    vm._watcher.run()
    expect(vm.passwordNonStandard)
      .to.be.ok
  })
  it('测试密码输入不一致时是否能够标记', () => {
    const Constructor = Vue.extend(SeFolders)
    const vm = new Constructor().$mount()
    const input = vm.$el.querySelector('#input-password-confirm')
    vm.password = '123Abc'
    vm.passwordConfirm = '223Abc'
    const clickEvent = new window.Event('blur')
    input.dispatchEvent(clickEvent)
    vm._watcher.run()
    expect(vm.passwordInConsistent)
      .to.be.ok
  })
  it('测试正在输入密码时是否能取消不一致标记', () => {
    const Constructor = Vue.extend(SeFolders)
    const vm = new Constructor().$mount()
    const input = vm.$el.querySelector('#input-password-confirm')
    vm.password = '123Abc'
    vm.passwordConfirm = '223Abc'
    vm.checkPassword()
    const clickEvent = new window.Event('focus')
    input.dispatchEvent(clickEvent)
    vm._watcher.run()
    expect(vm.passwordInConsistent)
      .to.not.be.ok
  })
  it('测试正在输入密码时是否能取消不合法标记', () => {
    const Constructor = Vue.extend(SeFolders)
    const vm = new Constructor().$mount()
    const input = vm.$el.querySelector('#input-password')
    vm.password = '123abc'
    vm.checkPassword()
    const clickEvent = new window.Event('focus')
    input.dispatchEvent(clickEvent)
    vm._watcher.run()
    expect(vm.passwordNonStandard)
      .to.not.be.ok
  })
  // it('测试正在输入正确时是否能正确赋值', () => {
  //   const Constructor = Vue.extend(SeFolders)
  //   const vm = new Constructor().$mount()
  //   const button = vm.$el.querySelector('#finish')
  //   vm.password = '123Abc'
  //   vm.passwordConfirm = '123Abc'
  //   vm.nickname = 'abc'
  //   vm.checkPassword()
  //   const clickEvent = new window.Event('click')
  //   button.dispatchEvent(clickEvent)
  //   vm._watcher.run()
  //   expect(vm.item.nickname)
  //     .to.be.equal('abc')
  // })
  // it('测试正在输入有空时是否能不赋值', () => {
  //   const Constructor = Vue.extend(SeFolders)
  //   const vm = new Constructor().$mount()
  //   const button = vm.$el.querySelector('#finish')
  //   vm.password = ''
  //   vm.passwordConfirm = '123Abc'
  //   vm.nickname = 'abc'
  //   vm.checkPassword()
  //   const clickEvent = new window.Event('click')
  //   button.dispatchEvent(clickEvent)
  //   vm._watcher.run()
  //   expect(vm.item)
  //     .to.be.empty
  // })
  // it('测试正在密码输入不合法时是否能不赋值', () => {
  //   const Constructor = Vue.extend(SeFolders)
  //   const vm = new Constructor().$mount()
  //   const button = vm.$el.querySelector('#finish')
  //   vm.password = '123abc'
  //   vm.passwordConfirm = '123abc'
  //   vm.nickname = 'abc'
  //   vm.checkPassword()
  //   const clickEvent = new window.Event('click')
  //   button.dispatchEvent(clickEvent)
  //   vm._watcher.run()
  //   expect(vm.item)
  //     .to.be.empty
  // })
  // it('测试正在密码输入不一致时是否能不赋值', () => {
  //   const Constructor = Vue.extend(SeFolders)
  //   const vm = new Constructor().$mount()
  //   const button = vm.$el.querySelector('#finish')
  //   vm.password = '123Abc'
  //   vm.passwordConfirm = '123ABc'
  //   vm.nickname = 'abc'
  //   vm.checkPassword()
  //   const clickEvent = new window.Event('click')
  //   button.dispatchEvent(clickEvent)
  //   vm._watcher.run()
  //   expect(vm.item)
  //     .to.be.empty
  // })
})
