var app = require('express')()
var http = require('http').Server(app)
var io = require('socket.io')(http)
var port = process.env.PORT || 3000

var customerSocket = []
var serverSocket = []

// 客服向用户发送消息
io.on('connection', function (socket) {
  socket.on('server message', function (msg, toId) {
    let to = customerSocket.filter(function (item) {
      return item && item.id == toId
    })
    to[0].emit('server message', msg, toId)
  })
})

// 用户向客服发送消息
io.on('connection', function (socket) {
  socket.on('customer message', function (msg, toId) {
    let to = serverSocket.filter(function (item) {
      return item && item.id == toId
    })
    to[0].emit('customer message', msg, toId)
  })
})

// 登陆设置id
io.on('connection', function (socket) {
  socket.on('customer set id', function (msg) {
    socket.broadcast.emit('customer message', msg)
    socket.id = msg
    customerSocket.push(socket)
  })
})

io.on('connection', function (socket) {
  socket.on('server set id', function (msg) {
    socket.broadcast.emit('server message', msg)
    socket.id = msg
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
