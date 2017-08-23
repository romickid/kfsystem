<template>
  <div id="app">
    <img src="./assets/logo.png">
    <div>
      <h2>
        <a href="./en_login">跳转至用户登录页面</a>
        <a href="./en_folders">跳转至用户注册页面</a>
        <br>
      </h2>
    </div>  
    <router-view></router-view>
    <!-- <div class="insertf" id="div1" style="display:none;">
      <iframe class="insertframe" id="links" src=""></iframe>
    </div>
    <button class="pic" @click="show"></button> -->
  </div>
</template>

<script>
// window.addEventListener('message', function (e) {
//   if (e.data.toString() === 'End session') {
//     document.getElementsByClassName('insertf')[0].style.display = 'none'
//   } else if (e.data.toString() === 'Screen shot') {
//     document.getElementsByClassName('insertf')[0].style.display = 'none'
//     html2canvas(document.body, {
//       onrendered: function (canvas) {
//         var canvasData = canvas.toDataURL()
//         window.frames[0].postMessage(canvasData, 'http://192.168.55.33:8000/customer_iframe/')
//       }
//     })
//     document.getElementsByClassName('insertf')[0].style.display = 'block'
//   }
// }, false)
// export default {
//   name: 'app',
//   data () {
//     return {
//       admin_get_info_iframe: '../api/admin_get_info_iframe/',
//       item: ''
//     }
//   },
//   created () {
//   },
//   methods: {
//     show () {
//       this.getInfo()
//       if (document.getElementsByClassName('insertf')[0].style.display === 'block') {
//         document.getElementsByClassName('insertf')[0].style.display = 'none'
//       } else {
//         document.getElementsByClassName('insertf')[0].style.display = 'block'
//       }
//     },
//     getInfo () {
//       let vm = this
//       this.$http.post(this.admin_get_info_iframe)
//         .then((response) => {
//           // alert(response.data)
//           vm.$set(this, 'item', response.data)
//           document.getElementById('links').setAttribute('src', this.item)
//         }, (response) => {
//           // window.location.href = '../not_found'
//         })
//     }
//   }
// }
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

body {
  overflow-y: scroll;
}

/* .insertframe {
  position: fixed;
  width: 40%;
  height: 60%;
  z-index: 9999;
}

.insertf {
  margin-left: 20%
}

.pic {
  position: fixed;
  background: url(./assets/photo.png) no-repeat;
  height: 80px;
  width: 80px;
  margin-top: 8%;
  margin-left: 38%;
  border: 0;
} */
</style>
