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
function findById (arr, id) {
  let result = arr.filter(function (item) {
    return item && item.id == id
  })
  return result
}
function sortByCustomerNumber (arr) {
  arr.sort(function (a, b) {
    return a.customerNumber - b.customerNumber
  })
}
function addCustomer (server, customer) {
  server.customers.push(customer)
  server.customerNumber++
  console.log('After add customer ' + customer.id)
  console.log('      Server ' + server.id + ' have customer：' + server.customerNumber)
}
function distributeCustomer (server) {
  for (let s = 0; s < server.customers.length; s++) {
    server.customers[s].emit('switch server', server.id)
  }
}
io.on('connection', function (socket) {

  // 登陆设置id
  socket.on('server set id', function (msg) {
    socket.isServer = true
    socket.id = msg
    socket.customerNumber = 0
    socket.customers = []
    console.log('server set id: ' + socket.id)
    serverSocket.push(socket)
  })

  // 客服向用户发送消息
  socket.on('server message', function (msg, fromId, toId) {
    let server = findById(serverSocket, fromId)
    let to = findById(server[0].customers, toId)
    to[0].emit('server message', msg, fromId, toId)
    console.log('Server ' +  fromId + ' send message to customer ' + toId)
  })

  // 用户向客服发送消息
  socket.on('customer message', function (msg, fromId, toId) {
    let to = findById(serverSocket, toId)
    to[0].emit('customer message', msg, fromId, toId)
    console.log('customer ' + fromId + ' send Messages to server ' + toId)
  })

  // 为用户分配客服
  socket.on('assigned to server', function (fromId, information) {
    if (serverSocket.length === 0) {
      socket.emit('no server available')
    } else {
      sortByCustomerNumber(serverSocket)
      let to = serverSocket[0]
      toId = to.id
      socket.id = fromId
      socket.serverId = toId
      to.emit('add client', fromId, information)
      console.log('Server ' + toId + ' add client ' + fromId)
      socket.emit('connect to server', toId)
      console.log('Customer ' + fromId + ' connect to server ' + toId)
      addCustomer(to, socket)
      customerSocket.push(socket)
    }
  })

  // 为用户转接客服
  socket.on('switch server', function (formerId, information) {
    if (serverSocket.length === 0) {
      socket.emit('no server available')
    } else {
      sortByCustomerNumber(serverSocket)
      let i = 0
      while (serverSocket[i].id === formerId) {
        i++
      }
      let to = serverSocket[i]
      toId = to.id
      console.log('Transfer customer ' + socket.id + ' to server ' + to.id + ': ')
      to.emit('add client', socket.id, information)
      console.log('    Server ' + toId + ' add client ' + socket.id)
      socket.emit('connect to server', toId)
      socket.serverId = toId
      console.log('    Client ' + socket.id + ' connect to server ' + toId)
      addCustomer(to, socket)
    }
  })

  // 客服申请为用户转接客服
  socket.on('switch server from server', function (id) {
    console.log('Server ' + socket.id + ' switch server for customer ' + id)
    if (serverSocket.length === 1) {
      socket.emit('switch failed')
      console.log('switch failed!')
      return
    }
    let customer = findById(socket.customers, id)
    customer[0].emit('switch server', socket.id)
    socket.customerNumber--
    console.log('After switch a customer out, server ' + socket.id + 'have customer: ' + socket.customerNumber)
  })

  // 用户刷新
  socket.on('customer come back', function (customerId, serverId) {
    console.log('customer come back')
    socket.id = customerId
    socket.serverId = serverId
    let server = findById(serverSocket, serverId)
    console.log('findById server: ' + server[0].id)
    removeById(server[0].customers, customerId)
    console.log('After remove server.costomers.length: ' + server[0].customers.length)
    server[0].customers.push(socket)
  })

  // 客服刷新
  socket.on('server come back', function (serverId) {
    console.log('server come back: ' + serverId)
    let oldserver = findById(serverSocket, serverId)
    removeById(serverSocket, serverId)
    socket.isServer = true
    socket.id = serverId
    socket.customerNumber = 0
    socket.customers = []
    for (let i = 0; i < oldserver[0].customers.length; i++) {
      socket.customers.push(oldserver[0].customers[i])
      socket.customerNumber++
    }
    serverSocket.push(socket)
  })

  // 离开
  socket.on('log out', function () {
    // 用户5分钟未说话自动断开
    if (!socket.isServer) {
      console.log('Customer ' + socket.id + ' is left')
      let server = findById(serverSocket, socket.serverId)
      removeById(server[0].customers, socket.id)
      server[0].customerNumber--
      console.log('After one customer left,server ' + server[0].id + 'has customers: ' + server[0].customers.length)
      server[0].emit('customer hang off', socket.id)
    } else {
      // 客服登出
      console.log('Server ' + socket.id + ' is left')
      removeById(serverSocket, socket.id)
      distributeCustomer(socket)
    }
  })
  // 客户关闭页面：从客服端发出断开客户的信息
  socket.on('customer out', function (customerId) {
    console.log('Customer out: ' + customerId)
    let server = findById(serverSocket, socket.id)
    let customer = findById(server[0].customers, customerId)
    customer[0].emit('no server available')
    removeById(server[0].customers, customerId)
    server[0].customerNumber--
    server[0].emit('customer hang off', customerId)
    console.log('After one customer left,server ' + server[0].id + 'has customers: ' + server[0].customers.length)
  })
})

http.listen(port, function () {
  console.log('listening on *:' + port);
})
