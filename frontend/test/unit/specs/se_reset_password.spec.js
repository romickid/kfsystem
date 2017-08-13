import Vue from 'vue'
import reset from '../../../src/components/se_reset_password.vue'

describe('se_reset_password.vue', () => {
  it('对点击忘记密码窗口弹出功能的检查', () => {
    const Constructor = Vue.extend(reset)
    const vm = new Constructor().$mount()
    const button = vm.$el.querySelector('Button')
    vm.find = false
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    vm._watcher.run()
    expect(vm.find)
      .to.be.ok
  })
  it('判断正确的密码格式', () => {
    const Constructor = Vue.extend(reset)
    const vm = new Constructor().$mount()
    vm.newPassword = 'QWEqwe123'
    vm.checkNewPassword()
    expect(vm.passwordNonstandard)
      .to.not.be.ok
  })
  it('判断缺少大写字母的错误密码格式', () => {
    const Constructor = Vue.extend(reset)
    const vm = new Constructor().$mount()
    vm.newPassword = 'qweqwe123'
    vm.checkNewPassword()
    expect(vm.passwordNonstandard)
      .to.be.ok
  })
  it('判断缺少小写字母的错误密码格式', () => {
    const Constructor = Vue.extend(reset)
    const vm = new Constructor().$mount()
    vm.newPassword = 'QWEQWE123'
    vm.checkNewPassword()
    expect(vm.passwordNonstandard)
      .to.be.ok
  })
  it('判断缺少数字的错误密码格式', () => {
    const Constructor = Vue.extend(reset)
    const vm = new Constructor().$mount()
    vm.newPassword = '123123123'
    vm.checkNewPassword()
    expect(vm.passwordNonstandard)
      .to.be.ok
  })
  it('判断密码长度不足6位的错误密码格式', () => {
    const Constructor = Vue.extend(reset)
    const vm = new Constructor().$mount()
    vm.newPassword = 'Q12we'
    vm.checkNewPassword()
    expect(vm.passwordNonstandard)
      .to.be.ok
  })
  it('判断密码超过20位的错误密码格式', () => {
    const Constructor = Vue.extend(reset)
    const vm = new Constructor().$mount()
    vm.newPassword = 'Q12we111111111111111111'
    vm.checkNewPassword()
    expect(vm.passwordNonstandard)
      .to.be.ok
  })
  it('判断关闭函数对变量的修改', () => {
    const Constructor = Vue.extend(reset)
    const vm = new Constructor().$mount()
    vm.oldPassword = '123QWEqwe'
    vm.newPassword = 'QWE123qwe'
    vm.passwordNonstandard = true
    vm.cancel()
    expect(vm.oldPassword)
      .to.equal('')
    expect(vm.newPassword)
      .to.equal('')
    expect(vm.passwordNonstandard)
      .to.not.be.ok
  })
})
