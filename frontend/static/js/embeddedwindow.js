window.onload = function () {
  var mydiv = document.body
  var btn = document.createElement('input')
  btn.type = 'button'
  btn.id = 'btn'
  btn.style = 'position: fixed;background: url(http://192.168.55.33:8000/static/photo.png) no-repeat;height: 80px;width: 80px;margin-left: 90%;margin-top: 35%;border: 0'
  mydiv.insertBefore(btn, mydiv.childNodes[0])
  document.getElementById('btn').onclick = show
  var div1 = document.createElement('div')
  div1.style = 'display: none;margin-left: 20%'
  div1.className = 'insertf'
  mydiv.insertBefore(div1, mydiv.childNodes[1])
  document.getElementsByClassName('insertf')[0].innerHTML = '<iframe class="insertframe" id="links" src=""></iframe>'
  document.getElementsByClassName('insertframe')[0].style = 'position: fixed;width: 35%;height: 60%;z-index: 9999;margin-left: 45%'
}

window.addEventListener('message', function (e) {
  if (e.data.toString() === 'End session') {
    document.getElementsByClassName('insertf')[0].style.display = 'none'
  } else if (e.data.toString() === 'Screen shot') {
    document.getElementsByClassName('insertf')[0].style.display = 'none'
    html2canvas(document.body, {
      onrendered: function (canvas) {
        var canvasData = canvas.toDataURL()
        window.frames[0].postMessage(canvasData, 'http://192.168.55.33:8000/customer_iframe/')
      }
    })
    document.getElementsByClassName('insertf')[0].style.display = 'block'
  }
}, false)

function show () {
  getInfo()
  if (document.getElementsByClassName('insertf')[0].style.display === 'block') {
    document.getElementsByClassName('insertf')[0].style.display = 'none'
  } else {
    document.getElementsByClassName('insertf')[0].style.display = 'block'
  }
}

function getInfo () {
  $(function () {
    $.ajax({
      type: 'POST',
      url: 'http://192.168.55.33:7000/api/admin_get_info_iframe/',
      success: function (data) {
        console.log(data)
        document.getElementById('links').setAttribute('src', data)
      },
      error: function () {
        console.log('error')
      }
    })
  })
}
