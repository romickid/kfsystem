import Vue from 'vue'
import system from '@/components/system'

describe('test system.vue', () => {
	it('对弹出添加用户信息对话框的测试', () => {
		const Constructor = Vue.extend(system)
    const vm = new Constructor().$mount()
    const button = vm.$el.querySelector('#add-info-button')
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    vm._watcher.run()
    expect(vm.modal)
      .to.be.ok
	})
	it('测试用户输入名称为空时能否标记为空', () => {
		const Constructor = Vue.extend(system)
    const vm = new Constructor().$mount()
    const input = vm.$el.querySelector('#input-name')
    const clickEvent = new window.Event('on-blur')
    input.dispatchEvent(clickEvent)
    vm._watcher.run()
    expect(vm.nameIsNull)
      .to.be.ok
	})
	it('测试用户正在输入名称时能否取消为空标记', () => {
		const Constructor = Vue.extend(system)
    const vm = new Constructor().$mount()
    const input = vm.$el.querySelector('#input-name')
    const clickEvent = new window.Event('on-focus')
    input.dispatchEvent(clickEvent)
    vm._watcher.run()
    expect(vm.nameIsNull)
      .to.not.be.ok
	})
	it('测试用户输入说明为空时能否标记为空', () => {
		const Constructor = Vue.extend(system)
    const vm = new Constructor().$mount()
    const input = vm.$el.querySelector('#input-comment')
    const clickEvent = new window.Event('on-blur')
    input.dispatchEvent(clickEvent)
    vm._watcher.run()
    expect(vm.commentIsNull)
      .to.be.ok
	})
	it('测试用户正在输入名称时能否取消为空标记', () => {
		const Constructor = Vue.extend(system)
    const vm = new Constructor().$mount()
    const input = vm.$el.querySelector('#input-comment')
    const clickEvent = new window.Event('on-focus')
    input.dispatchEvent(clickEvent)
    vm._watcher.run()
    expect(vm.commentIsNull)
      .to.not.be.ok
	})
	it('测试用户正确输入名称和说明时点击ok能否正确赋值', () => {
		const Constructor = Vue.extend(system)
    const vm = new Constructor().$mount()
    const modal = vm.$el.querySelector('#add-info-modal')
    const clickEvent = new window.Event('on-ok')
    modal.dispatchEvent(clickEvent)
    vm.formItem.name = '1'
    vm.formItem.comment = '2'
    vm._watcher.run()
    expect(vm.infomationItem.name)
      .to.be.equal('1')
    expect(vm.infomationItem.comment)
      .to.be.equal('2')
	})
	it('测试用户输入的名称为空，说明不为空时点击ok能否不赋值', () => {
		const Constructor = Vue.extend(system)
    const vm = new Constructor().$mount()
    const modal = vm.$el.querySelector('#add-info-modal')
    const clickEvent = new window.Event('on-ok')
    modal.dispatchEvent(clickEvent)
    vm.formItem.name = ''
    vm.formItem.comment = '1'
    vm._watcher.run()
    expect(vm.infomationItem.name)
      .to.be.empty
    expect(vm.infomationItem.comment)
      .to.be.empty
	})
	it('测试用户输入的名称为不空，说明为空时点击ok能否不赋值', () => {
		const Constructor = Vue.extend(system)
    const vm = new Constructor().$mount()
    const modal = vm.$el.querySelector('#add-info-modal')
    const clickEvent = new window.Event('on-ok')
    modal.dispatchEvent(clickEvent)
    vm.formItem.name = '1'
    vm.formItem.comment = ''
    vm._watcher.run()
    expect(vm.infomationItem.name)
      .to.be.empty
    expect(vm.infomationItem.comment)
      .to.be.empty
	})
	it('测试用户点击cancel后，能否将变量恢复', () => {
		const Constructor = Vue.extend(system)
    const vm = new Constructor().$mount()
    const modal = vm.$el.querySelector('#add-info-modal')
    const clickEvent = new window.Event('on-cancel')
    modal.dispatchEvent(clickEvent)
    vm.formItem.name = '1'
    vm.formItem.comment = '2'
    vm._watcher.run()
    expect(vm.formItem.name)
      .to.be.empty
    expect(vm.formItem.comment)
      .to.be.empty
    expect(vm.nameIsNull)
      .to.not.be.ok
    expect(vm.commentIsNull)
      .to.not.be.ok
	})
	it('测试用户点击ok后，能否将变量恢复', () => {
		const Constructor = Vue.extend(system)
    const vm = new Constructor().$mount()
    const modal = vm.$el.querySelector('#add-info-modal')
    const clickEvent = new window.Event('on-ok')
    modal.dispatchEvent(clickEvent)
    vm.formItem.name = '1'
    vm.formItem.comment = '2'
    vm._watcher.run()
    expect(vm.formItem.name)
      .to.be.empty
    expect(vm.formItem.comment)
      .to.be.empty
    expect(vm.nameIsNull)
      .to.not.be.ok
    expect(vm.commentIsNull)
      .to.not.be.ok
	})
	it('测试删除信息函数', () => {
		const Constructor = Vue.extend(system)
    const vm = new Constructor().$mount()
    vm.infomations = [{'name': '1'}]
    vm.delete_info(0)
    expect(vm.deleteName.name)
      .to.be.equal('1')
	})
})