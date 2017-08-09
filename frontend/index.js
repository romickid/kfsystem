var app = require('express')()
var http = require('http').Server(app)
var io = require('socket.io')(http)
var port = process.env.PORT || 3000

io.on('connection', function (socket) {
  io.emit('chat2 message', 'one connection')
  socket.on('chat2 message', function (msg) {
    socket.broadcast.emit('chat2 message', msg)
  })
})

io.on('connection', function (socket) {
  socket.on('disconnect', function () {
  console.log('user disconnected')
})
})

http.listen(port, function () {
  console.log('listening on *:' + port);
})
