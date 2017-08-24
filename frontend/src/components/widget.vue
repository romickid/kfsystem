<template>
  <div class="widget">
    <div class='method'>
      <div class='method-title'>
        <h2>在网站中嵌入widget咨询页面地址</h2>
      </div>
      <div class='method-background'>
        <div class='method-content'>
          <a>{{ script }}</a>
        </div>
        <div class='method-foot'>
          <ul>
            <li>企业配置桌面widget客服页面接入，可参考<a href='http://192.168.55.33:8000/documentation/#/widget'>《桌面网站widget页面接入》</a></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'widget',
  computed: {
    script () {
      return '<scrip' + 't src="http://192.168.55.33:8000/static/js/jquery-2.1.1.min.js"></scrip' + 't><scrip' + 't src="http://192.168.55.33:8000/static/js/html2canvas.js"></scrip' + 't><scrip' + 't src="http://192.168.55.33:8000/static/js/embeddedwindow.js"></scrip' + 't>'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.widget {
  padding: 0em 3em;
}

.method {
  margin: 4em 0em;
  border: 1px solid #d7dde4;
  border-radius: 4px;
}

.method-title {
  padding: 0.5em 2em;
  border-bottom: 1px solid #d7dde4;
}

.method-content {
  margin: 0.5em 2em;
  margin-top: 0em;
  padding: 1em 1em;
  background-color: #dddee1;
}

.method-foot {
  padding: 0.5em 2em;
  padding-bottom: 1em;
}

.method-background {
  padding-top: 1em;
  background-color: #f5f7f9;
}
</style>