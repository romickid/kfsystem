import Vue from 'vue'
import team from '../../../src/components/team.vue'

describe('test team.vue', () => {
  it('测试添加客服按钮', () => {
    const Constructor = Vue.extend(team)
    const vm = new Constructor().$mount()
    const button = vm.$el.querySelector('#add-cs-button')
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    vm._watcher.run()
    expect(vm.addModal)
      .to.be.ok
  })
  it('测试输入邮箱为空时能否标记', () => {
    const Constructor = Vue.extend(team)
    const vm = new Constructor().$mount()
    const button = vm.$el.querySelector('#input-email')
    const clickEvent = new window.Event('on-blur')
    button.dispatchEvent(clickEvent)
    vm._watcher.run()
    expect(vm.emailIsNull)
      .to.be.ok
  })
  it('测试输入邮箱格式不正确时能否标记', () => {
    const Constructor = Vue.extend(team)
    const vm = new Constructor().$mount()
    const button = vm.$el.querySelector('#input-email')
    vm.kf = '1'
    const clickEvent = new window.Event('on-blur')
    button.dispatchEvent(clickEvent)
    vm._watcher.run()
    expect(vm.emailIsNotStandard)
      .to.be.ok
  })
  it('测试输入邮箱时能否取消空标记', () => {
    const Constructor = Vue.extend(team)
    const vm = new Constructor().$mount()
    const button = vm.$el.querySelector('#input-email')
    vm.kf = ''
    vm.check_email()
    const clickEvent = new window.Event('on-focus')
    button.dispatchEvent(clickEvent)
    vm._watcher.run()
    expect(vm.emailIsNull)
      .to.not.be.ok
  })
  it('测试输入邮箱时能否取消格式不正确标记', () => {
    const Constructor = Vue.extend(team)
    const vm = new Constructor().$mount()
    const button = vm.$el.querySelector('#input-email')
    vm.kf = '1'
    vm.check_email()
    const clickEvent = new window.Event('on-focus')
    button.dispatchEvent(clickEvent)
    vm._watcher.run()
    expect(vm.emailIsNotStandard)
      .to.not.be.ok
  })
  // it('测试正确输入客服邮箱时点击ok时能否正确赋值', () => {
  //   const Constructor = Vue.extend(team)
  //   const vm = new Constructor().$mount()
  //   const button = vm.$el.querySelector('#add-cs-modal')
  //   vm.kf = '1@1.com'
  //   vm.check_email()
  //   const clickEvent = new window.Event('on-ok')
  //   button.dispatchEvent(clickEvent)
  //   vm._watcher.run()
  //   expect(vm.customerService.email)
  //     .to.be.equal('1@1.com')
  // })
  // it('测试输入客服邮箱为空时点击ok时能否不赋值', () => {
  //   const Constructor = Vue.extend(team)
  //   const vm = new Constructor().$mount()
  //   const button = vm.$el.querySelector('#add-cs-modal')
  //   vm.kf = ''
  //   vm.check_email()
  //   const clickEvent = new window.Event('on-ok')
  //   button.dispatchEvent(clickEvent)
  //   vm._watcher.run()
  //   expect(vm.customerService)
  //     .to.be.empty
  // })
  // it('测试输入客服邮箱为格式不正确时点击ok时能否不赋值', () => {
  //   const Constructor = Vue.extend(team)
  //   const vm = new Constructor().$mount()
  //   const button = vm.$el.querySelector('#add-cs-modal')
  //   vm.kf = '1'
  //   vm.check_email()
  //   const clickEvent = new window.Event('on-ok')
  //   button.dispatchEvent(clickEvent)
  //   vm._watcher.run()
  //   expect(vm.customerService)
  //     .to.be.empty
  // })
  it('测试输入客服邮箱点击cancel时能否还原变量', () => {
    const Constructor = Vue.extend(team)
    const vm = new Constructor().$mount()
    const button = vm.$el.querySelector('#add-cs-modal')
    vm.kf = '1'
    vm.check_email()
    const clickEvent = new window.Event('on-cancel')
    button.dispatchEvent(clickEvent)
    vm._watcher.run()
    expect(vm.kf)
      .to.be.empty
    expect(vm.emailIsNotStandard)
      .to.not.be.ok
  })
  it('测试删除客服函数能否正确执行', () => {
    const Constructor = Vue.extend(team)
    const vm = new Constructor().$mount()
    vm.kfstaff = [{
      'email': '1'
    }]
    vm.deleteKf(0)
    expect(vm.kfstaff)
      .to.be.empty
  })
})
