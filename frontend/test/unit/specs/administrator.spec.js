import Vue from 'vue'
import administrator from '../../../src/pages/administrator/administrator.vue'

describe('test administrator.vue', () => {
  it('测试点击toggle能否进行布局调整', () => {
    const Constructor = Vue.extend(administrator)
    const vm = new Constructor().$mount()
    const button = vm.$el.querySelector('#toggle-click')
    vm.spanLeft = 5
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    vm._watcher.run()
    expect(vm.spanLeft)
      .to.be.equal(2)
    expect(vm.spanRight)
      .to.be.equal(22)
  })
  it('测试点击toggle能否进行布局调整', () => {
    const Constructor = Vue.extend(administrator)
    const vm = new Constructor().$mount()
    const button = vm.$el.querySelector('#toggle-click')
    vm.spanLeft = 2
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    vm._watcher.run()
    expect(vm.spanLeft)
      .to.be.equal(5)
    expect(vm.spanRight)
      .to.be.equal(19)
  })
  it('测试iconsize能否根据spanleft的值进行变化', () => {
    const Constructor = Vue.extend(administrator)
    const vm = new Constructor().$mount()
    vm.spanLeft = 2
    expect(vm.iconSize)
      .to.be.equal(24)
  })
  it('测试iconsize能否根据spanleft的值进行变化', () => {
    const Constructor = Vue.extend(administrator)
    const vm = new Constructor().$mount()
    vm.spanLeft = 5
    expect(vm.iconSize)
      .to.be.equal(14)
  })
})
