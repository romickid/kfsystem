import Vue from 'vue'
import forget from '../../../src/components/en_forget_password.vue'

describe('en_forget_password.vue', () => {
  it('对点击忘记密码窗口弹出功能的检查', () => {
    const Constructor = Vue.extend(forget)
    const vm = new Constructor().$mount()
    const button = vm.$el.querySelector('Button')
    vm.find = false
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    vm._watcher.run()
    expect(vm.find)
      .to.be.ok
  })
  it('判断含有-和_的正确邮箱格式，@后有两个.', () => {
    const Constructor = Vue.extend(forget)
    const vm = new Constructor().$mount()
    vm.email = 'w123-45_6@nankai.edu.cn'
    vm.checkEmail()
    expect(vm.emailIllegal)
      .to.not.be.ok
  })
  it('判断含有-和_的正确邮箱格式,@后有一个.', () => {
    const Constructor = Vue.extend(forget)
    const vm = new Constructor().$mount()
    vm.email = 'w12_34-56@qq.com'
    vm.checkEmail()
    expect(vm.emailIllegal)
      .to.not.be.ok
  })
  it('判断-和_在开头或结尾的错误格式', () => {
    const Constructor = Vue.extend(forget)
    const vm = new Constructor().$mount()
    vm.email = 'w123_@nankai.edu.cn'
    vm.checkEmail()
    expect(vm.emailIllegal)
      .to.be.ok
  })
  it('判断含有不允许的特殊符号的错误格式', () => {
    const Constructor = Vue.extend(forget)
    const vm = new Constructor().$mount()
    vm.email = 'w1.234$56@nankai.edu.cn'
    vm.checkEmail()
    expect(vm.emailIllegal)
      .to.be.ok
  })
  it('判断含有三个.的错误格式', () => {
    const Constructor = Vue.extend(forget)
    const vm = new Constructor().$mount()
    vm.email = 'w123456@nan.kai.edu.cn'
    vm.checkEmail()
    expect(vm.emailIllegal)
      .to.be.ok
  })
  it('判断域名缺失的错误格式', () => {
    const Constructor = Vue.extend(forget)
    const vm = new Constructor().$mount()
    vm.email = 'w123456@nankai'
    vm.checkEmail()
    expect(vm.emailIllegal)
      .to.be.ok
  })
  it('判断聚焦函数对变量的修改', () => {
    const Constructor = Vue.extend(forget)
    const vm = new Constructor().$mount()
    vm.emailIllegal = true
    vm.emailInput()
    expect(vm.emailIllegal)
      .to.not.be.ok
  })
  it('判断关闭函数对变量的修改', () => {
    const Constructor = Vue.extend(forget)
    const vm = new Constructor().$mount()
    vm.email = '123'
    vm.emailIllegal = true
    vm.cancel()
    expect(vm.email)
      .to.equal('')
    expect(vm.emailIllegal)
      .to.not.be.ok
  })
})
