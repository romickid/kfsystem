import Vue from 'vue'
import en_login from '@/components/en_login'

describe('test en_login.vue', () => {
	it('测试输入邮箱格式不合法时能否进行标记', () => {
		const Constructor = Vue.extend(en_login)
    const vm = new Constructor().$mount()
    const button = vm.$el.querySelector('#input-email')
    const clickEvent = new window.Event('blur')
    button.dispatchEvent(clickEvent)
    vm.email = '1'
    vm._watcher.run()
    expect(vm.emailIllegal)
      .to.be.ok
	})
	it('测试正在输入邮箱时能否取消标记', () => {
		const Constructor = Vue.extend(en_login)
    const vm = new Constructor().$mount()
    const input = vm.$el.querySelector('#input-email')
    const clickEvent = new window.Event('focus')
    input.dispatchEvent(clickEvent)
    vm.email = '1'
    vm.checkEmail()
    vm._watcher.run()
    expect(vm.emailIllegal)
      .to.not.be.ok
	})
	it('测试输入正确时点击登录能否正确赋值', () => {
		const Constructor = Vue.extend(en_login)
    const vm = new Constructor().$mount()
    const button = vm.$el.querySelector('#login')
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    vm.email = '1@1.com'
    vm.password = '1'
    vm.checkEmail()
    vm._watcher.run()
    expect(vm.item.email)
      .to.be.equal('1@1.com')
	})
	it('测试输入为空时点击登录能否不赋值', () => {
		const Constructor = Vue.extend(en_login)
    const vm = new Constructor().$mount()
    const button = vm.$el.querySelector('#login')
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    vm.email = ''
    vm.password = '1'
    vm.checkEmail()
    vm._watcher.run()
    expect(vm.item)
      .to.be.empty
	})
	it('测试邮箱格式不正确时点击登录能否不赋值', () => {
		const Constructor = Vue.extend(en_login)
    const vm = new Constructor().$mount()
    const button = vm.$el.querySelector('#login')
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    vm.email = '1'
    vm.password = '1'
    vm.checkEmail()
    vm._watcher.run()
    expect(vm.item)
      .to.be.empty
	})
})