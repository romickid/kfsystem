var app = require('express')()
var http = require('http').Server(app)
var io = require('socket.io')(http)
var port = process.env.PORT || 3000

var customerSocket = []
var serverSocket = []

function removeById (arr, val) {
  for(let i = 0; i < arr.length; i++) {
    if (arr[i].id === val) {
      arr.splice(i, 1);
      break;
    }
  }
}

io.on('connection', function (socket) {

  // 登陆设置id
  socket.on('customer set id', function (msg) {
    socket.isConnect = true
    socket.isCustomer = true
    socket.id = msg
    console.log('customer set id:' + socket.id)
    customerSocket.push(socket)
  })
  socket.on('server set id', function (msg) {
    socket.isConnect = true
    socket.isCustomer = false
    socket.id = msg
    socket.customerNumber = 0
    socket.customers = []
    console.log('server set id:' + socket.id)
    serverSocket.push(socket)
  })

  // 客服向用户发送消息
  socket.on('server message', function (msg, fromId, toId) {
    let to = customerSocket.filter(function (item) {
      return item && item.id === toId
    })
    to[0].emit('server message', msg, fromId, toId)
    console.log('server message from ' + fromId + ' to ' + toId)
  })

  // 用户向客服发送消息
  socket.on('customer message', function (msg, fromId, toId) {
    let to = serverSocket.filter(function (item) {
      return item && item.id === toId
    })
    to[0].emit('customer message', msg, fromId, toId)
    console.log('customer message from ' + fromId + ' to ' + toId)
  })

  // 为用户分配客服
  socket.on('assigned to server', function (fromId) {
    if (serverSocket.length === 0) {
      socket.emit('no server available')
    } else {
      serverSocket.sort(function (a, b) {
        return a.customerNumber - b.customerNumber
      })
      let to = serverSocket[0]
      to.customers.push(socket)
      to.customerNumber ++
      console.log(to.id + 'have customer：' + to.customerNumber)
      toId = to.id
      to.emit('add client', fromId)
      console.log(toId + 'add client' + fromId)
      socket.emit('connect to server', toId)
      socket.serverId = toId
      console.log(fromId + 'connect to server' + toId)
    }
  })
  // 为用户转接客服
  socket.on('switch server', function (formerId) {
    if (serverSocket.length === 0) {
      socket.emit('no server available')
    } else {
      serverSocket.sort(function (a, b) {
        return a.customerNumber - b.customerNumber
      })
      let i = 0
      while (serverSocket[i].id === formerId) {
        i++
      }
      let to = serverSocket[i]
      to.customers.push(socket)
      to.customerNumber ++
      console.log('After add transfer,' + to.id + 'have customer：' + to.customerNumber)
      toId = to.id
      to.emit('add client', socket.id)
      console.log(toId + 'add client' + socket.id)
      socket.emit('connect to server', toId)
      socket.serverId = toId
      console.log(socket.id + 'connect to server' + toId)
    }
  })

  // 离开
  socket.on('disconnect', function () {
    if (socket.isConnect) {
      if (socket.isCustomer) {
        if (socket.serverId) {
          console.log('This Customer is connected before')
          console.log('Customer ' + socket.id + 'is left')
          let server = serverSocket.filter(function (item) {
            return item && item.id === socket.serverId
          })
          removeById(server[0].customers, socket.id)
          server.customerNumber --
          console.log(server[0].customers.length)
          server[0].emit('customer hang off', socket.id)
        }
      } else {
        console.log('Server ' + socket.id + 'is left')
        removeById(serverSocket, socket.id)
        for (let s = 0; s < socket.customers.length; s++) {
          socket.customers[s].emit('switch server', socket.id)
        }
      }
    }
  })
})

http.listen(port, function () {
  console.log('listening on *:' + port);
})
