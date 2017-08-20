var express = require('express');
var path = require('path');
var IO = require('socket.io');
var router = express.Router();

var app = express();
var server = require('http').Server(app);
app.use(express.static(path.join(__dirname, 'public')));
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'hbs');


// 创建socket服务
var socketIO = IO(server);

// 企业的已登录客服Socket  socket = cs_socket_list[enterprise_id][cs_id]
var cs_socket_list = {};


function sortByCustomerNumberInCs (arr) {
  // 从小到大排序 返回数组
  arr.sort(function (a, b) {
    return a.customer_num - b.customer_num
  })
}


function findByCsId (arr, cs_id) {
  console.log('[function: findByCsId]')
  for (let i = 0; i < arr.length; i++) {
    console.log(arr[i].cs_id)
    console.log(cs_id)
    if (arr[i].cs_id == cs_id) {
      return arr[i]
    }
  }
  return -1
}


function findByCustomerId (arr, customer_id) {
  console.log('[function: findByCustomerId]')
  for (let i = 0; i < arr.length; i++) {
    console.log(arr[i].customer_id)
    console.log(customer_id)
    if (arr[i].customer_id == customer_id) {
      return arr[i]
    }
  }
  return -1
}


function csaddCustomerSocket (cs_socket, customer_socket) {
  console.log('[function: csaddCustomerSocket]')
  cs_socket.list_customer_socket.push(customer_socket)
  cs_socket.customer_num++
  console.log('After add customer ' + customer_socket.customer_id)
  console.log('      Cs ' + cs_socket.cs_id + ' have customer：' + cs_socket.customer_num)
}

function csdeleteCustomerSocket (cs_socket, customer_socket) {
  console.log('[function: csdeleteCustomerSocket]')
  cs_socket_list_lenght = cs_socket.list_customer_socket.length
  for (let i = 0; i < length; i++) {
    if (cs_socket.list_customer_socket[i].customer_id == customer_socket.customer_id) {
      cs_socket.list_customer_socket.splice(i, 1);
      break;
    }
  }

}


function removeByCustomerId (arr, customer_id) {
  for(let i = 0; i < arr.length; i++) {
    if (arr[i].customer_id === customer_id) {
      arr.splice(i, 1);
      break;
    }
  }
}


function removeByCsId (arr, cs_id) {
  for(let i = 0; i < arr.length; i++) {
    if (arr[i].cs_id === cs_id) {
      arr.splice(i, 1);
      break;
    }
  }
}


function distributeCustomer (cs_socket) {
  for (let i = 0; i < cs_socket.list_customer_socket.length; i++) {
    cs_socket.list_customer_socket[i].emit('switch cs', cs_socket.enterprise_id, cs_socket.cs_id)
  }
}


socketIO.on('connection', function (socket) {
  console.log('connection')
  
  // 客服登录 cs_socket
  socket.on('cs login', function (enterprise_id, cs_id) {
    console.log("[cs login]")
    
    let cs_socket = socket
    cs_socket.is_cs = true
    cs_socket.enterprise_id = enterprise_id
    cs_socket.cs_id = cs_id
    cs_socket.list_customer_socket = []
    cs_socket.customer_num = 0
    
    // 如果企业的客服列表没有创建
    if (!cs_socket_list[enterprise_id]) {
      cs_socket_list[enterprise_id] = [];
    }
    cs_socket_list[enterprise_id].push(cs_socket);

    console.log('企业 ' +  cs_socket.enterprise_id + ' 的客服 ' + cs_socket.cs_id + '成功登录')
  })

  // 为用户分配客服 customer_socket
  socket.on('assigned to cs', function (enterprise_id, customer_id) {
    console.log("[assigned to cs]")
    let customer_socket = socket

    if (!cs_socket_list[enterprise_id] || cs_socket_list[enterprise_id].length === 0) {
      console.log("[no cs available]")
      customer_socket.emit('no cs available')
    } else {
      console.log("[else]")
      sortByCustomerNumberInCs(cs_socket_list[enterprise_id])
      let cs_socket = cs_socket_list[enterprise_id][0]
      let cs_id = cs_socket.cs_id
      customer_socket.is_cs = false
      customer_socket.customer_id = customer_id
      customer_socket.cs_id = cs_id

      cs_socket.emit('add customer', enterprise_id, customer_id)
      console.log('Cs ' + cs_id + ' add customer ' + customer_id)
      customer_socket.emit('connect to cs', cs_id)
      console.log('Customer ' + customer_id + ' connect to cs ' + cs_id)
      csaddCustomerSocket(cs_socket, customer_socket)
    }
  })

  // 客服向用户发送消息 cs_socket
  socket.on('cs send message', function (msg, enterprise_id, cs_id, customer_id) {
    console.log("[cs send message]")
    let cs_socket = socket
    let customer_socket = findByCustomerId(cs_socket.list_customer_socket, customer_id)
    customer_socket.emit('cs send message', msg, enterprise_id, cs_id, customer_id)
    console.log('cs ' +  cs_id + ' send message to customer ' + customer_id)
  })

  
  // 客服向用户发送图片 cs_socket
  socket.on('cs send picture', function (bpic, spic, enterprise_id, cs_id, customer_id) {
    console.log("[cs send picture]")
    let cs_socket = socket
    let customer_socket = findByCustomerId(cs_socket.list_customer_socket, customer_id)
    customer_socket.emit('cs send picture', bpic, spic, enterprise_id, cs_id, customer_id)
    console.log('cs ' +  cs_id + ' send picture to customer ' + customer_id)  
  })
  
  
  // 用户向客服发送消息 customer_socket
  socket.on('customer send message', function (msg, enterprise_id, cs_id, customer_id) {
    console.log("[customer send message]")
    let customer_socket = socket
    let cs_socket = findByCsId(cs_socket_list[enterprise_id], cs_id)
    cs_socket.emit('customer send message', msg, enterprise_id, cs_id, customer_id)
    console.log('customer ' + customer_id + ' send message to server ' + cs_id)
  })

  
  // 用户向客服发送图片 customer_socket
  socket.on('customer send picture', function (bpic, spic, enterprise_id, cs_id, customer_id) {
    console.log("[customer send picture]")
    let customer_socket = socket
    let cs_socket = findByCsId(cs_socket_list[enterprise_id], cs_id)
    cs_socket.emit('customer send picture', bpic, spic, enterprise_id, cs_id, customer_id)
    console.log('customer ' +  customer_id + ' send picture to server ' + cs_id)  
  })
  

  // 为用户转接客服 customer_socket
  socket.on('switch cs', function (enterprise_id, former_cs_id, customer_id) {
    console.log("[switch cs]")
    let customer_socket = socket

    if (cs_socket_list[enterprise_id].length === 0 || cs_socket_list[enterprise_id].length === 1) {
      cs_socket.emit('no server available') // 无法转接
    } else {
      sortByCustomerNumberInCs(cs_socket_list[enterprise_id])
      let former_count = 0
      while (cs_socket_list[enterprise_id][former_count].cs_id === former_cs_id) {
        former_count++
      }
      former_cs_socket = findByCsId(cs_socket_list[enterprise_id], former_cs_id)

      let cs_socket = cs_socket_list[enterprise_id][former_count]
      cs_id = cs_socket.cs_id
      console.log('Transfer customer ' + customer_socket.customer_id + ' to cs ' + cs_id + ': ')
      cs_socket.emit('add customer', enterprise_id, customer_id)
      console.log('    Cs ' + cs_id + ' add customer ' + customer_id)
      customer_socket.emit('connect to Cs', cs_id)
      customer_socket.cs_id = cs_id
      console.log('    Customer ' + customer_socket.customer_id + ' connect to cs ' + cs_id)
      csaddCustomerSocket(cs_socket, customer_socket)
    }
  })
 
  // 客服申请为用户转接客服 cs_socket
  socket.on('cs apply to transfer for customer', function (enterprise_id, customer_id) {
    console.log("[cs apply to transfer for customer]")
    console.log('cs ' + socket.cs_id + ' apply to transfer for customer ' + customer_id)
    let cs_socket = socket
    if (cs_socket_list[enterprise_id].length === 1) {
      cs_socket.emit('switch failed')
      console.log('switch failed')
      return
    } else {
      cs_socket.emit('switch succeeded')
      console.log('switch succeeded')
      let customer_socket = findByCustomerId(cs_socket.list_customer_socket, customer_id)
      customer_socket.emit('switch cs', cs_socket.cs_id)
      cs_socket.customer_num--
      csdeleteCustomerSocket(cs_socket, customer_socket)
      console.log('After switch a customer out, cs ' + socket.id + socket.customer_num + ' customer.')
    }
  })


  // 用户刷新 customer_socket
  socket.on('customer come back', function (enterprise_id, cs_id, customer_id) {
    console.log('[customer come back]')
    let customer_socket = socket
    customer_socket.customer_id = customer_id
    customer_socket.cs_id = cs_id
    let cs_socket = findByCsId(cs_socket_list[enterprise_id], cs_id)
    console.log('findByCsId server: ' + cs_socket.cs_id)
    removeByCustomerId(cs_socket.list_customer_socket, customer_id)
    console.log('After removing, cs.customer_num: ' + cs_socket.customer_num)
    cs_socket.list_customer_socket.push(socket)
  })


  // 客服刷新 cs_socket
  socket.on('cs come back', function (enterprise_id, cs_id) {
    console.log("[cs come back]")
    console.log('cs come back: ' + cs_id)
    let cs_socket = socket
    let former_cs_socket = findByCsId(cs_socket_list[enterprise_id], cs_id)
    removeByCsId(cs_socket_list[enterprise_id], cs_id)
    cs_socket.is_cs = true
    cs_socket.cs_id = cs_id
    cs_socket.enterprise_id = enterprise_id
    cs_socket.customer_num = 0
    cs_socket.list_customer_socket = []
    
    for (let i = 0; i < former_cs_socket.list_customer_socket.length; i++) {
      socket.list_customer_socket.push(former_cs_socket.list_customer_socket[i])
      socket.customer_num++
    }
    cs_socket_list[enterprise_id].push(socket)
  })


  // 离开 
  socket.on('log out', function () {
    console.log('[log out]')
    if (!socket.is_cs) {
      // 用户5分钟未说话自动断开
      let customer_socket = socket
      console.log('Customer ' + customer_socket.customer_id + ' is left')
      let cs_socket = findByCsId(cs_socket_list[socket.enterprise_id], customer_socket.cs_id)
      removeByCustomerId(cs_socket.list_customer_socket, customer_socket.customer_id)
      cs_socket.customer_num--
      console.log('After one customer left, cs ' + cs_socket.cs_id + 'has customers: ' + cs_socket.list_customer_socket.length)
      cs_socket.emit('customer hang off', customer_socket.enterprise_id, customer_socket.customer_id)
    } else {
      // 客服登出
      let cs_socket = socket
      console.log('Cs ' + cs_socket.cs_id + ' is left')
      removeByCsId(cs_socket_list[socket.enterprise_id], cs_socket.cs_id)
      distributeCustomer(cs_socket) // 转接所有客户至其他客服
    }
  })
  
  // 客户关闭页面：从客服端发出断开客户的信息 cs_socket
  socket.on('customer out', function (customer_id) {
    let cs_socket = socket
    console.log('[customer out]')
    console.log('Customer out: ' + customer_id)
    let customer_socket = findByCustomerId(cs_socket.list_customer_socket, customer_id)
    customer_socket.emit('no server available')
    removeByCustomerId(cs_socket.list_customer_socket, customer_id)
    cs_socket.customer_num--
    cs_socket.emit('customer hang off', cs_socket.enterprise_id, customer_id)
    console.log('After one customer left, cs ' + cs_socket.cs_id + ' has customers: ' + cs_socket.list_customer_socket.length)
  })
});


// room page
router.get('/room/*/*', function (req, res) {
  var roomID = req.params[0];
  
  // 渲染页面数据(见views/room.hbs)
  res.render('room', {
    roomID: roomID,
    users: roomInfo[roomID]
  });
});


app.use('/', router);

server.listen(3000, function () {
  console.log('server listening on port 3000');
});
