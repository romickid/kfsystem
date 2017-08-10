var app = require('express')()
var http = require('http').Server(app)
var io = require('socket.io')(http)
var port = process.env.PORT || 3000

var customerSocket = []
var serverSocket = []

// 客服向用户发送消息
io.on('connection', function (socket) {
  socket.on('server message', function (msg, fromId, toId) {
    let to = customerSocket.filter(function (item) {
      return item && item.id == toId
    })
    to[0].emit('server message', msg, fromId, toId)
    console.log('server message from ' + fromId + ' to ' + toId)
  })
})

// 用户向客服发送消息
io.on('connection', function (socket) {
  socket.on('customer message', function (msg, fromId, toId) {
    let to = serverSocket.filter(function (item) {
      return item && item.id == toId
    })
    to[0].emit('customer message', msg, fromId, toId)
    console.log('customer message from ' + fromId + ' to ' + toId)
  })
})
// 为用户分配客服
io.on('connection', function(socket) {
  socket.on('assigned to server', function (fromId) {
    let to = serverSocket[0]
    toId = to.id
    to.emit('add client', fromId)
    console.log(toId + 'add client' + fromId)
    socket.emit('connect to server', toId)
    console.log(fromId + 'connect to server' + toId)

  })
})
// 登陆设置id
io.on('connection', function (socket) {
  socket.on('customer set id', function (msg) {
    // socket.broadcast.emit('customer message', msg)
    socket.id = msg
    console.log('customer set id:' + socket.id)
    customerSocket.push(socket)
  })
})

io.on('connection', function (socket) {
  socket.on('server set id', function (msg) {
    socket.id = msg
    socket.customerNumber = 0
    console.log('server set id:' + socket.id)
    serverSocket.push(socket)
  })
})

io.on('connection', function (socket) {
  socket.on('disconnect', function () {
})
})

http.listen(port, function () {
  console.log('listening on *:' + port);
})
