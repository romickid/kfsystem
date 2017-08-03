<template>
  <div id="app">
    <div class="chatbox">
      <div class="chat_top fn-clear">
        <div class="logo"><img src="../index/assets/logo.png" width="190" height="60"  alt=""/></div>
        <div class="uinfo fn-clear">
          <div class="uface"><img src="../index/assets/hetu.jpg" width="40" height="40"  alt=""/></div>
          <div class="uname">
            河图<i class="fontico down"></i>
            <ul class="managerbox">
              <li><a href="#"><i class="fontico lock"></i>修改密码</a></li>
              <li><a href="#"><i class="fontico logout"></i>退出登录</a></li>
            </ul>
          </div>
        </div>
      </div>
      <div class="chat_message fn-clear">
        <div class="chat_left">
          <div class="information_box" id="information_box">此处显示用户信息</div>
          <div class="message_box" id="message_box">
            <div class="msg_item fn-clear">
              <div class="uface"><img src="../index/assets/53f44283a4347.jpg" width="40" height="40"  alt=""/></div>
              <div class="item_right">
                <div class="msg">hello!!!!</div>
                <div class="name_time">猫猫 · 3分钟前</div>
              </div>
            </div>

            <div class="msg_item fn-clear">
              <div class="uface"><img src="../index/assets/53f442834079a.jpg" width="40" height="40"  alt=""/></div>
              <div class="item_right">
                <div class="msg">Hi~</div>
                <div class="name_time">白猫 · 1分钟前</div>
              </div>
            </div>

            <div class="msg_item fn-clear">
              <div class="u_ownface"><img src="../index/assets/hetu.jpg" width="40" height="40"  alt=""/></div>
              <div class="item_left">
                <div class="msg own">那个统计表也不能说明一切</div>
                <div class="name_time">河图 · 30秒前</div>
              </div>
            </div>
          </div>
          <div class="write_box">
            <textarea id="message" name="message" class="write_area" placeholder="说点啥吧..."></textarea>
            <input type="hidden" name="fromname" id="fromname" value="河图" />
            <input type="hidden" name="to_uid" id="to_uid" value="0">
            <div class="facebox fn-clear">
              <div class="expression"></div>
              <div class="chat_type" id="chat_type">群聊</div>
              <button name="" class="sub_but">提交</button>
            </div>
          </div>
        </div>
        <div class="chat_right">
          <ul class="user_list" title="双击用户私聊">
            <li class="fn-clear selected"><em>所有用户</em></li>
            <li class="fn-clear" data-id="1"><span><img src="../index/assets/hetu.jpg" width="30" height="30"  alt=""/></span><em>河图</em><small class="online" title="在线"></small></li>
            <li class="fn-clear" data-id="2"><span><img src="../index/assets/53f44283a4347.jpg" width="30" height="30"  alt=""/></span><em>猫猫</em><small class="online" title="在线"></small></li>
            <li class="fn-clear" data-id="3"><span><img src="../index/assets/53f442834079a.jpg" width="30" height="30"  alt=""/></span><em>白猫</em><small class="offline" title="离线"></small></li>
          </ul>
        </div>
      </div>
    </div>
    <!-- <script type="text/javascript">
    $(document).ready(function(e) {
    	$('#message_box').scrollTop($("#message_box")[0].scrollHeight + 20);
    	$('.uname').hover(
    	    function(){
    		    $('.managerbox').stop(true, true).slideDown(100);
    	    },
    		function(){
    		    $('.managerbox').stop(true, true).slideUp(100);
    		}
    	);

    	var fromname = $('#fromname').val();
    	var to_uid   = 0; // 默认为0,表示发送给所有用户
    	var to_uname = '';
    	$('.user_list > li').dblclick(function(){
    		to_uname = $(this).find('em').text();
    		to_uid   = $(this).attr('data-id');
    		if(to_uname == fromname){
    		    alert('您不能和自己聊天!');
    			return false;
    		}
    		if(to_uname == '所有用户'){
    		    $("#toname").val('');
    			$('#chat_type').text('群聊');
    		}else{
    		    $("#toname").val(to_uid);
    			$('#chat_type').text('您正和 ' + to_uname + ' 聊天');
    		}
    		$(this).addClass('selected').siblings().removeClass('selected');
    	    $('#message').focus().attr("placeholder", "您对"+to_uname+"说：");
    	});

    	$('.sub_but').click(function(event){
    	    sendMessage(event, fromname, to_uid, to_uname);
    	});

    	/*按下按钮或键盘按键*/
    	$("#message").keydown(function(event){
    		var e = window.event || event;
            var k = e.keyCode || e.which || e.charCode;
    		//按下ctrl+enter发送消息
    		if((event.ctrlKey && (k == 13 || k == 10) )){
    			sendMessage(event, fromname, to_uid, to_uname);
    		}
    	});
    });
    function sendMessage(event, from_name, to_uid, to_uname){
        var msg = $("#message").val();
    	if(to_uname != ''){
    	    msg = '您对 ' + to_uname + ' 说： ' + msg;
    	}
    	var htmlData =   '<div class="msg_item fn-clear">'
                       + '   <div class="uface"><img src="images/hetu.jpg" width="40" height="40"  alt=""/></div>'
    			       + '   <div class="item_right">'
    			       + '     <div class="msg own">' + msg + '</div>'
    			       + '     <div class="name_time">' + from_name + ' · 30秒前</div>'
    			       + '   </div>'
    			       + '</div>';
    	$("#message_box").append(htmlData);
    	$('#message_box').scrollTop($("#message_box")[0].scrollHeight + 20);
    	$("#message").val('');
    }
    </script> -->

  </div>
</template>

<script>
export default {
  name: 'app'
}
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
/*
 * author yinq
 */
/* 防止用户自定义背景颜色对网页的影响，添加让用户可以自定义字体 */
html {
  color:#000;
  height:100%;}
/* 内外边距通常让各个浏览器样式的表现位置不同 */
body,div,dl,dt,
dd,ul,ol,li,h1,
h2,h3,h4,h5,h6,
pre,code,form,fieldset,
legend,input,textarea,p,
blockquote,th,td,hr,
button,article,aside,details,
figcaption,figure,footer,header,
hgroup,menu,nav,section {
  margin:0;
  padding:0;}
/* 重设 HTML5 标签, IE 需要在 js 中 createElement(TAG) */
article,aside,details,figcaption,
figure,footer,header,hgroup,menu,
nav,section { display:block;}
/* HTML5 媒体文件跟 img 保持一致 */
audio,canvas,video {
  display: inline-block;
  *display: inline;
  *zoom: 1;}
/* 要注意表单元素并不继承父级 font 的问题 */
body,button,input,select,textarea{
  font:14px/1.5 "微软雅黑",tahoma,arial,\5b8b\4f53;}
input,select,textarea{font-size:100%;}
/* 去掉各Table  cell 的边距并让其边重合 */
table{border-collapse:collapse;border-spacing:0;}
/* IE bug fixed: th 不继承 text-align*/
th{text-align:inherit;}
/* 去除默认边框 */
fieldset,img{border:0;}
/* ie6 7 8(q) bug 显示为行内表现 */
iframe{display:block;}
/* 去掉 firefox 下此元素的边框 */
abbr,acronym{border:0;font-variant:normal;}
/* 一致的 del 样式 */
del {text-decoration:line-through;}
address,caption,cite,code,dfn,em,th,var {font-style:normal;font-weight:500;}
/* 去掉列表前的标识, li 会继承 */
ol,ul {list-style:none;}
/* 对齐是排版最重要的因素, 别让什么都居中 */
caption,th {text-align:left;}
/* 来自yahoo, 让标题都自定义, 适应多个系统应用 */
h1,h2,h3,h4,h5,h6 {font-size:100%;font-weight:500;}
q:before,q:after {content:'';}
/* 统一上标和下标 */
sub, sup {font-size: 75%; line-height: 0; position: relative; vertical-align: baseline;}
sup {top: -0.5em;}
sub {bottom: -0.25em;}

/* 让链接在 hover 状态下显示下划线 */
a:hover {text-decoration:underline;}
/* 默认不显示下划线，保持页面简洁 */
ins,a {text-decoration:none;}
/* 清理浮动 */
.fn-clear:after {visibility:hidden;display:block;font-size:0;content:" ";clear:both;height:0;}
.fn-clear {zoom:1; /* for IE6 IE7 */}
/* 隐藏, 通常用来与 JS 配合 */
body .fn-hide {display:none;}
/* 设置内联, 减少浮动带来的bug */
.fn-left,.fn-right {display:inline;}
.fn-left {float:left;}
.fn-right {float:right;}
/*webkit内核浏览器滚动条*/
::-webkit-scrollbar-track-piece{background:#e9e9e9;}
::-webkit-scrollbar{width:8px;height:8px;}
::-webkit-scrollbar-button{display:none;}
::-webkit-scrollbar-track,::-webkit-scrollbar-track-piece{background:-webkit-gradient(linear,left);}
::-webkit-scrollbar-thumb,::-webkit-scrollbar-thumb:horizontal{border-radius:6px;background:#bdbdbd;}
::-webkit-scrollbar-thumb:hover{background:#8e8e8e;}
::-webkit-scrollbar-thumb:active{background:#828181;}
@font-face {
  font-family: 'fontello';
  src: url('../index/assets/font/fontello.eot?68245288');
  src: url('../index/assets/font/fontello.eot?68245288#iefix') format('embedded-opentype'),
       url('../index/assets/font/fontello.woff?68245288') format('woff'),
       url('../index/assets/font/fontello.ttf?68245288') format('truetype'),
       url('../index/assets/font/fontello.svg?68245288#fontello') format('svg');
  font-weight: normal;
  font-style: normal;
}

/*common*/
body{
  background:#176994 url(../index/assets/bg.jpg);
  height:-moz-calc(100% - 100px);
  height:-webkit-calc(100% - 100px);
  height:calc(100% - 100px);
  padding:40px;}
.fontico:before{
  font-family: "fontello";
  font-style: normal;
  font-weight: normal;
  speak: none;
  display: inline-block;
  text-decoration: inherit;
  text-align: center;
}
i.down:before{ content:'\e800';}
i.lock:before{ content:'\e806';}
i.logout:before{ content:'\e804';}

/*chatbox*/
.chatbox{
  overflow:hidden;
  height:100%;
  width:100%;
  -moz-border-radius:5px;
  -webkit-border-radius:5px;
  border-radius:5px;
  background-color:rgba(244,255,255,1);}

/*chat_top*/
.chat_top{
   height:60px;
   border-bottom:1px solid #eee;}
.logo{ float:left;}
.logo img{ vertical-align:bottom;}
.uinfo{
   margin:10px 0;
   float:right;
   padding-right:20px;}
.uface{ float:left; height: 40px;}
.u_ownface{ float:right; height: 40px;}
.uface img{
   -moz-border-radius:50%;
   -webkit-border-radius:50%;
   border-radius:50%;}
.u_ownface img{
   -moz-border-radius:50%;
   -webkit-border-radius:50%;
   border-radius:50%;}
.uinfo .uname{
   float:left;
   line-height:40px;
   margin-left:10px;
   color:#2E4059;
   position:relative;}
.uinfo .uname i.down{ margin-left:50px;}
.managerbox{
  display:none;
  width:100px;
  border:1px solid #eee;
  background-color:#FFF;
  padding:10px 0;
  position:absolute;
  top:40px;
  right:-10px;}
.managerbox a{
  display:block;
  color:#2E4059;
  padding:0px 10px;}
.managerbox a i{ margin-right:10px;}
.managerbox a:hover{ background-color:#f9f9f9; text-decoration:none;}

/*chat_message*/
.chat_message{ height:-moz-calc(100% - 61px); height:-webkit-calc(100% - 61px); height:calc(100% - 61px);}

/*chat_left*/
.chat_left{
  padding:20px;
  width:-moz-calc(100% - 240px);
  width:-webkit-calc(100% - 240px);
  width:calc(100% - 240px);
  height:-moz-calc(100% - 40px);
  height:-webkit-calc(100% - 40px);
  height:calc(100% - 40px);
  float:right;}
.message_box{
  background-color:#FFF;
  margin-bottom:20px;
  height:-moz-calc(100% - 120px);
  height:-webkit-calc(100% - 120px);
  height:calc(100% - 120px);
  overflow:auto;}
.msg_item{
  margin-bottom:20px;
  position:relative;}
.msg_item .uface{
  position:absolute;
  bottom:0px;}
.msg_item .u_ownface{
  /*position:absolute;*/
  bottom:0px;}
.msg_item .item_left{
  margin-left:45px;
  float:right;
  margin-right:15px;}
.msg_item .item_right{
  margin-left:45px;
  float:left;
  margin-right:15px;}
.msg_item .msg{
  background-color:#F4F6F8;
  padding:10px 15px;
  line-height:24px;
  -moz-border-radius:10px;
  -webkit-border-radius:10px;
  border-radius:10px;
  color:#2E4059;
  position: relative;
  margin-bottom:5px;}
.msg.own{ background-color:#E0F1FC;}/*自己的聊天记录显示为蓝色*/
.msg_item .msg:before {
  content: "";
  position: absolute;
  bottom: -12px;
  left: 10px;
  border-width: 12px 12px 0 0 ;
  border-style: solid;
  border-color: #F4F6F8 transparent;
  display: block;
  width: 0;
}
.msg_item .msg.own:before{
  border-color: #E0F1FC transparent;}
.msg_item .name_time{
  font-size: 12px;
  color: #7E90A5;
  line-height: 30px;
  padding-left: 10px;}

.write_box{
  height: 100px;
  overflow: hidden;
  -moz-border-radius: 5px;
  -webkit-border-radius: 5px;
  border-radius: 5px;
  overflow:hidden;}
.write_area{
  border: 2px solid #E3E8ED;
  border-bottom: none;
  padding: 5px;
  outline: none;
  color: #B4C0CE;
  margin: 0;
  vertical-align: bottom;
  width: -moz-calc(100% - 14px);
  width: -webkit-calc(100% - 14px);
  width: calc(100% - 14px);
  height: 56px;}
.facebox{
  height: 32px;
  width: 100%;
  background-color: #E3E8ED;}
.sub_but{
  float: right;
  padding: 0 25px;
  background-color: #7E90A5;
  outline: none;
  border: none;
  height: 32px;
  cursor: pointer;
  line-height: 30px;
  color: #FFF;}
.information_box{
  width: 199px;
  height: 100%;
  float: right;
  border-left: 1px solid #eee;}
/*chat_right*/
.chat_right{
  width: 199px;
  height: 100%;
  float: left;
  border-left: 1px solid #eee;}
.user_list{
  padding:0;
  overflow:auto;
  height:100%;}
.user_list li{
  padding:10px 20px;
  color:#2E4059;
  cursor:pointer;}
.user_list li:hover,
.user_list li.selected{ background-color:#F4F6F8;}
.user_list li span{
  display:block;
  float:left;
  width:30px;
  height:30px;
  margin-right:10px;}
.user_list li em{
  display:block;
  float:left;
  height:30px;
  line-height:30px;}
.user_list li small{
  width:10px;
  height:10px;
  margin:10px;
  float:left;
  -moz-border-radius:50%;
  -webkit-border-radius:50%;
  border-radius:50%;}
small.online{ background-color:#57B869;}
small.offline{ background-color:#EB3E3E;}
.user_list li img{
  -moz-border-radius:50%;
  -webkit-border-radius:50%;
  border-radius:50%;
  vertical-align:middle;}


/*expression - 表情,有待增加*/
.expression{ float:left;}

/*chat_type - 聊天性质,私聊|群聊*/
.chat_type{
  float:left;
  line-height:30px;
  padding-left:10px;}

</style>
