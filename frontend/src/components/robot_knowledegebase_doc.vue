<template>
  <div id='app'>
    <div class='main-content-head'>
      <h1>知识库语料标准</h1>
      <p>根据数据分析的结果，在机器人回答不正确的问题中，语料库的质量是占比最大的部分。因此保证语料库的质量是提高机器人的准确率至关重要的一环。</p>
    </div>
    <div class='main-content-body'>
      <div class='guide'>
        <h2>机器人工作原理</h2>
        <p>机器人是通过对用户的问题进行词粒度的拆分，按照中文语义分析技术，找到问句的关键元素；和语料库中的问题进行匹配。当规则问句越完整，拆解的关键词越多越具体，则匹配到的概率越高。</p>
      <div class='guide'>
        <h2>如何让知识库发挥作用</h2>
        <div class='line'></div>
        <h2>原则一 提高知识库更新频率</h2>
        <ul>
          <li>根据业务的发展，用户会不断产生新的问题。因此定期通过数据回顾将用户新的问题补充到语料中，将会对准确率有很大帮助。</li>
        </ul>
      </div>
      <div class='line'></div>
      <div class='guide'>
        <h2>原则二 提高知识库质量</h2>
        <ul>
          <li>1. 设置一个完整的问句，包含主谓宾语，按照问题类型大致分为：</li>
          <li>What: 【什么是女生节特惠？】 【什么是储值卡？】</li>
          <li>How： 【如何修改外卖订餐地址】【返现金额怎么使用】</li>
          <li>Why： 【为什么不能用支付宝付款】</li>
          <li>YesNo: 【棉被可以洗吗】</li>
          <li>Suggest: 【订单地址写错了怎么办？】【火车票买重复了，怎么办】</li>
          <li>2. 精简语料问题，去掉多余无意义的语气词、虚词等。例如：亲、到现在、这个、那个等。</li>
          <li>BAD： 亲，请问以下，可不可以注明衣物一定要干洗？</li>
          <li>GOOD：是否可以注明衣物要干洗？</li>
          <li>3 尽量避免口语化表达，使用书面用语准确表达意思。】</li>
          <li>BAD： 您这里几号放假?</li>
          <li>GOOD：什么时候放假?</li>
          <li>BAD： 你们的假一赔一是怎么回事？</li>
          <li>GOOD：假一赔一是什么？</li>
          <li>BAD： 你们的假一赔一是怎么回事？</li>
          <li>4 优先使用泛化问题，减少过于具体的问题？</li>
          <li>BAD： 购买的味多美蛋糕一直没有发货？</li>
          <li>GOOD：购买的商品一直没有发货？</li>
          <li>BAD： 肯德基的不支持优惠券怎么办？</li>
          <li>GOOD：商家不支持优惠券怎么办？</li>
          <li>5 不要使用中英文混杂的问句，请全部使用中文。</li>
          <li>饺子 or 包子哪个好吃？</li>
          <li>饺子和包子哪个好吃？</li>
          <li>6 重复问题可以用一个语料表达即可。</li>
          <li>BAD</li>
          <li>收到的商品尺寸偏大，怎么办？</li>
          <li>收到的商品尺寸偏小，怎么办？</li>
          <li>GOOD</li>
          <li>收到的商品尺寸不合适，怎么办？ or 收到的商品尺寸偏大/偏下，怎么办？</li>
        </ul>
      </div>
      <div class='line'></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'web'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#app {
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  color: #2c3e50;
}
/*= font-size
-----------------------------------------------------------------*/

h1 {
  font-size: 3em;
  font-weight: normal;
}

h2 {
  font-size: 2.1em;
  font-weight: normal;
}

h3 {
  font-size: 1.8em;
  font-weight: normal;
}

h4 {
  font-size: 1em;
  font-weight: normal;
}

h5 {
  font-size: 0.5em;
  font-weight: normal;
}

p {
  font-size: 1.3em;
}

.guide li {
  font-size: 1.3em;
}
/*= main
-----------------------------------------------------------------*/

.main-content-head h1 {
  margin-bottom: 0;
}

.main-content-head {
  padding-bottom: 2em;
}

.main-content-body ul {
  padding: 0.7em 1.3em;
}

.line {
  margin: 2em 0em;
  border: 1px solid #2a333b;
  border-top: 0px;
}

.guide a {
  color: #9d2933;
}
</style>
