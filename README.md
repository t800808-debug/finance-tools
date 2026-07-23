# finance-tools
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>FCN 投資質借槓桿試算 ｜ 渣打亞灣貴賓</title>
<style>
  :root{
    --pine:#0A3D3A; --pine2:#072E2B; --pine3:#0F4E4A;
    --gold:#C7A24B; --goldl:#E7D29A;
    --green:#2E7D5B; --greenl:#EAF2EE;
    --ink:#1B2B29; --muted:#6E7F7C; --gray:#9AA6A4; --grayd:#5C6B69;
    --line:#DCE4E2; --surface:#FFFFFF; --bg:#F1F5F4; --card:#EEF3F2;
    --red:#B23A3A;
    --cjk:"Microsoft JhengHei","PingFang TC","Heiti TC",sans-serif;
    --num:"Microsoft JhengHei","PingFang TC",sans-serif;
  }
  *{box-sizing:border-box;}
  html,body{margin:0;padding:0;}
  body{
    font-family:var(--cjk); color:var(--ink); background:var(--bg);
    line-height:1.5; -webkit-font-smoothing:antialiased;
  }
  .num{font-variant-numeric:tabular-nums; font-feature-settings:"tnum" 1;}
  .wrap{max-width:1120px; margin:0 auto; padding:0 20px 64px;}

  /* Header */
  header.top{
    background:linear-gradient(160deg,var(--pine) 0%, var(--pine2) 100%);
    color:#fff; padding:26px 0 30px;
  }
  .top-inner{max-width:1120px; margin:0 auto; padding:0 20px;}
  .eyebrow{font-size:12px; letter-spacing:.22em; font-weight:700; color:var(--goldl); text-transform:uppercase;}
  header.top h1{font-size:clamp(24px,4.4vw,38px); font-weight:900; margin:8px 0 6px; letter-spacing:.01em;}
  header.top h1 .accent{color:var(--gold);}
  header.top p.sub{margin:0; color:#CFE0DD; font-size:15px; max-width:70ch;}

  /* Hero breakeven readout */
  .hero{
    background:var(--pine3); color:#fff; border-radius:16px;
    margin-top:-16px; padding:26px 28px; box-shadow:0 18px 40px -24px rgba(7,46,43,.55);
    display:grid; grid-template-columns:1.15fr .85fr; gap:26px; align-items:center;
    border:1px solid rgba(199,162,75,.35);
  }
  .hero .label{font-size:13px; color:#BFD2CF; font-weight:500; letter-spacing:.02em;}
  .hero .big{font-size:clamp(40px,8vw,68px); font-weight:900; color:var(--goldl); line-height:1.02; margin:6px 0 2px;}
  .hero .big small{font-size:.42em; font-weight:700; color:#fff; margin-left:6px;}
  .hero .prem{font-size:16px; color:#fff;}
  .hero .prem b{color:var(--gold);}
  .hero .note{font-size:12.5px; color:#9FB8B4; margin-top:12px;}
  .hero-right{background:var(--pine2); border-radius:12px; padding:18px 20px; border:1px solid rgba(255,255,255,.06);}
  .hero-right .cap{font-size:12px; color:#9FB8B4; letter-spacing:.02em;}
  .hero-right .yield{font-size:34px; font-weight:900; color:#fff; margin:2px 0 10px;}
  .hero-right .yrow{display:flex; justify-content:space-between; font-size:13.5px; padding:5px 0; border-top:1px solid rgba(255,255,255,.08); color:#DCEAE7;}
  .hero-right .yrow b{color:#fff; font-weight:700;}

  /* Panels grid */
  .grid{display:grid; grid-template-columns:1fr 1fr; gap:20px; margin-top:22px;}
  .panel{background:var(--surface); border:1px solid var(--line); border-radius:14px; padding:22px 22px 24px;}
  .panel h2{font-size:17px; font-weight:900; margin:0 0 4px; color:var(--pine);}
  .panel .desc{font-size:12.5px; color:var(--muted); margin:0 0 16px;}

  /* Controls */
  .ctrl{margin-bottom:18px;}
  .ctrl:last-child{margin-bottom:0;}
  .ctrl .crow{display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;}
  .ctrl label{font-size:14px; font-weight:700; color:var(--ink);}
  .ctrl .valbox{display:flex; align-items:center; gap:4px;}
  .ctrl input[type=number]{
    width:96px; text-align:right; font-family:var(--num); font-variant-numeric:tabular-nums;
    font-size:16px; font-weight:700; color:var(--pine);
    border:1px solid var(--line); border-radius:8px; padding:5px 8px; background:#fff;
  }
  .ctrl .unit{font-size:13px; color:var(--muted); min-width:26px;}
  .ctrl input[type=number]:focus{outline:2px solid var(--gold); outline-offset:1px; border-color:var(--gold);}
  input[type=range]{-webkit-appearance:none; appearance:none; width:100%; height:6px; border-radius:6px;
    background:var(--card); outline:none;}
  input[type=range]::-webkit-slider-thumb{-webkit-appearance:none; appearance:none; width:22px; height:22px;
    border-radius:50%; background:var(--green); border:3px solid #fff; box-shadow:0 1px 4px rgba(0,0,0,.25); cursor:pointer;}
  input[type=range]::-moz-range-thumb{width:20px; height:20px; border-radius:50%; background:var(--green);
    border:3px solid #fff; box-shadow:0 1px 4px rgba(0,0,0,.25); cursor:pointer;}
  input[type=range].g::-webkit-slider-thumb{background:var(--gold);}
  input[type=range].g::-moz-range-thumb{background:var(--gold);}
  input[type=range]:focus-visible{outline:2px solid var(--gold); outline-offset:3px;}

  /* Head-to-head */
  .verdict{border-radius:12px; padding:16px 18px; margin-bottom:18px; text-align:center; font-weight:700;}
  .verdict.win{background:var(--greenl); color:var(--green); border:1px solid #BBD8CC;}
  .verdict.lose{background:#FBF3F1; color:var(--red); border:1px solid #E8CFC9;}
  .verdict.tie{background:#FBF6E9; color:#8A6D1E; border:1px solid #EBDCB0;}
  .verdict .vbig{font-size:26px; font-weight:900; display:block; margin-top:2px;}

  .barset{margin:6px 0 6px;}
  .barrow{margin:12px 0;}
  .barrow .bhead{display:flex; justify-content:space-between; font-size:13.5px; margin-bottom:5px;}
  .barrow .bhead .who{font-weight:700;}
  .barrow .bhead .amt{font-family:var(--num); font-variant-numeric:tabular-nums; font-weight:700;}
  .bartrack{height:26px; background:var(--card); border-radius:7px; overflow:hidden;}
  .barfill{height:100%; border-radius:7px; transition:width .35s ease;}
  .barfill.sc{background:var(--green);}
  .barfill.ot{background:var(--gray);}

  /* Breakdown */
  .bd{border-top:1px solid var(--line); margin-top:16px; padding-top:14px;}
  .bd .brow{display:flex; justify-content:space-between; font-size:14px; padding:6px 0; color:var(--ink);}
  .bd .brow .l{color:var(--muted);}
  .bd .brow .v{font-family:var(--num); font-variant-numeric:tabular-nums; font-weight:700;}
  .bd .brow.tot{border-top:2px solid var(--pine); margin-top:6px; padding-top:10px; font-size:16px;}
  .bd .brow.tot .v{color:var(--green); font-size:20px; font-weight:900;}
  .pos{color:var(--green);} .neg{color:var(--red);}

  /* Sensitivity table */
  .tablewrap{margin-top:22px; background:var(--surface); border:1px solid var(--line); border-radius:14px; padding:22px;}
  .tablewrap h2{font-size:17px; font-weight:900; margin:0 0 4px; color:var(--pine);}
  .tablewrap .desc{font-size:12.5px; color:var(--muted); margin:0 0 16px;}
  table{width:100%; border-collapse:collapse; font-size:14px;}
  thead th{background:var(--pine); color:#fff; font-weight:700; padding:11px 10px; text-align:center; font-size:13.5px;}
  thead th:first-child{border-radius:8px 0 0 0;} thead th:last-child{border-radius:0 8px 0 0;}
  tbody td{padding:10px; text-align:center; border-bottom:1px solid var(--line); font-family:var(--num); font-variant-numeric:tabular-nums;}
  tbody tr:nth-child(even){background:#F7FAF9;}
  tbody tr.be{background:var(--greenl) !important; font-weight:900;}
  tbody tr.be td{color:var(--green);}
  td.sc{color:var(--green); font-weight:700;}
  td.delta.pos{color:var(--green); font-weight:800;}
  td.delta.neg{color:var(--red); font-weight:800;}

  .foot{font-size:11.5px; color:var(--muted); margin-top:22px; line-height:1.7;}
  .foot b{color:var(--grayd);}

  .warn{display:none; background:#FBF3F1; color:var(--red); border:1px solid #E8CFC9;
    border-radius:10px; padding:10px 14px; font-size:13px; margin-top:14px; font-weight:700;}

  @media (max-width:820px){
    .hero{grid-template-columns:1fr; gap:18px;}
    .grid{grid-template-columns:1fr;}
    .ctrl input[type=number]{width:84px; font-size:15px;}
  }
</style>
</head>
<body>
<header class="top">
  <div class="top-inner">
    <div class="eyebrow">渣打亞灣貴賓理財 ‧ 投資質借試算</div>
    <h1>他行票面要贏，<span class="accent">得高過多少？</span></h1>
    <p class="sub">在渣打加「一層」投資質借槓桿後，同一筆資金的實拿會被墊高。調整下方條件，即時看出他行 FCN 票面必須高到哪裡，才追得上渣打。</p>
  </div>
</header>

<div class="wrap">
  <!-- HERO -->
  <section class="hero">
    <div>
      <div class="label">他行 FCN 票面必須 ≥</div>
      <div class="big num"><span id="beCoupon">10.7</span><small>% / 年</small></div>
      <div class="prem">才追得上渣打 — 等於要比渣打票面 <b class="num" id="bePrem">+2.7%</b> 以上</div>
      <div class="note">＊模型：加一層質借（僅借 1 次）、兩邊連結標的相同、未計稅負與費用。</div>
    </div>
    <div class="hero-right">
      <div class="cap">渣打槓桿後 ‧ 實質年化</div>
      <div class="yield num"><span id="scYield">10.7</span>%</div>
      <div class="yrow"><span>一年實拿</span><b class="num" id="scTotalTop">$21,400</b></div>
      <div class="yrow"><span>投入資金</span><b class="num" id="capTop">$200,000</b></div>
    </div>
  </section>

  <div class="grid">
    <!-- LEFT: SC conditions -->
    <div class="panel">
      <h2>渣打條件</h2>
      <p class="desc">這些設定決定「打平線」— 他行要高過多少才追平。</p>

      <div class="ctrl">
        <div class="crow">
          <label for="capN">投入資金</label>
          <div class="valbox"><span class="unit">US$</span><input class="num" type="number" id="capN" min="10000" max="10000000" step="10000" value="200000"></div>
        </div>
        <input type="range" id="capR" min="50000" max="2000000" step="10000" value="200000">
      </div>

      <div class="ctrl">
        <div class="crow">
          <label for="scN">渣打 FCN 票面</label>
          <div class="valbox"><input class="num" type="number" id="scN" min="0" max="30" step="0.1" value="8.0"><span class="unit">%</span></div>
        </div>
        <input type="range" id="scR" min="0" max="20" step="0.1" value="8.0">
      </div>

      <div class="ctrl">
        <div class="crow">
          <label for="ltvN">質借成數（LTV）</label>
          <div class="valbox"><input class="num" type="number" id="ltvN" min="0" max="90" step="1" value="45"><span class="unit">%</span></div>
        </div>
        <input type="range" id="ltvR" min="0" max="90" step="1" value="45">
      </div>

      <div class="ctrl">
        <div class="crow">
          <label for="finN">質借利率</label>
          <div class="valbox"><input class="num" type="number" id="finN" min="0" max="15" step="0.1" value="2.0"><span class="unit">%</span></div>
        </div>
        <input type="range" id="finR" min="0" max="10" step="0.1" value="2.0">
      </div>

      <div class="warn" id="warn">提醒：質借利率已高於渣打票面，加槓桿反而不利，此時他行只要票面更高就會勝出。</div>
    </div>

    <!-- RIGHT: head to head -->
    <div class="panel">
      <h2>和他行正面對決</h2>
      <p class="desc">拉動他行票面，即時看誰的實拿較高。</p>

      <div class="ctrl">
        <div class="crow">
          <label for="otN">他行 FCN 票面</label>
          <div class="valbox"><input class="num" type="number" id="otN" min="0" max="30" step="0.1" value="9.0"><span class="unit">%</span></div>
        </div>
        <input type="range" class="g" id="otR" min="0" max="20" step="0.1" value="9.0">
      </div>

      <div class="verdict win" id="verdict">
        渣打多賺
        <span class="vbig num" id="verdictBig">+US$3,400 / 年</span>
      </div>

      <div class="barset">
        <div class="barrow">
          <div class="bhead"><span class="who" style="color:var(--green)">渣打（槓桿一次）</span><span class="amt num" id="scBarAmt" style="color:var(--green)">$21,400</span></div>
          <div class="bartrack"><div class="barfill sc" id="scBar" style="width:100%"></div></div>
        </div>
        <div class="barrow">
          <div class="bhead"><span class="who" style="color:var(--grayd)">他行（無槓桿）</span><span class="amt num" id="otBarAmt" style="color:var(--grayd)">$18,000</span></div>
          <div class="bartrack"><div class="barfill ot" id="otBar" style="width:84%"></div></div>
        </div>
      </div>

      <div class="bd">
        <div class="brow"><span class="l">本金配息</span><span class="v num" id="bdBase">$16,000</span></div>
        <div class="brow"><span class="l">質借加碼</span><span class="v num pos" id="bdAdd">+$7,200</span></div>
        <div class="brow"><span class="l">借款成本</span><span class="v num neg" id="bdCost">−$1,800</span></div>
        <div class="brow tot"><span class="l" style="color:var(--pine);font-weight:700">渣打一年實拿</span><span class="v num" id="bdTotal">$21,400</span></div>
      </div>
    </div>
  </div>

  <!-- Sensitivity table -->
  <div class="tablewrap">
    <h2>敏感度一覽</h2>
    <p class="desc">他行票面由低到高，渣打實拿固定在 <span class="num" id="descSC">$21,400</span>。綠色列即「打平線」。</p>
    <table>
      <thead>
        <tr><th>他行票面</th><th>他行實拿</th><th>渣打實拿</th><th>渣打多賺</th></tr>
      </thead>
      <tbody id="tbody"></tbody>
    </table>
  </div>

  <p class="foot">
    ＊本工具為情境試算示範，數字依輸入條件即時計算，<b>未計入稅負、手續費、匯率變動與追繳風險</b>，不構成投資建議或招攬。<br>
    ＊模型假設：僅加一層質借（借款 1 次、不重複疊加）、渣打與他行連結標的相同、配息以年化單利計算。<br>
    ＊FCN 為條件式配息，實際依 KO／KI 等產品條款而定；槓桿會同時放大收益與虧損。投資涉及風險，過往績效不代表未來表現。
  </p>
</div>

<script>
(function(){
  "use strict";
  var f0 = new Intl.NumberFormat('en-US',{maximumFractionDigits:0});
  function usd(n){ return '$' + f0.format(Math.round(n)); }
  function usdSign(n){ var s = n<0?'−':'+'; return s + '$' + f0.format(Math.abs(Math.round(n))); }
  function pct(n){ return (Math.round(n*10)/10).toFixed(1); }

  // state (percent inputs stored as percent numbers)
  var st = { cap:200000, sc:8.0, ltv:45, fin:2.0, ot:9.0 };

  // link a slider + number field to a state key
  function bind(key, rId, nId, min, max){
    var r = document.getElementById(rId), n = document.getElementById(nId);
    function set(v, from){
      v = parseFloat(v);
      if(isNaN(v)) return;
      if(v<min) v=min; if(v>max) v=max;
      st[key]=v;
      // keep slider within its own range but let number go beyond
      if(from!=='r'){ r.value = Math.min(Math.max(v, parseFloat(r.min)), parseFloat(r.max)); }
      if(from!=='n'){ n.value = v; }
      render();
    }
    r.addEventListener('input', function(){ set(r.value,'r'); });
    n.addEventListener('input', function(){ set(n.value,'n'); });
    n.addEventListener('blur', function(){ if(n.value==='') { n.value=st[key]; } });
  }

  bind('cap','capR','capN',10000,10000000);
  bind('sc','scR','scN',0,30);
  bind('ltv','ltvR','ltvN',0,90);
  bind('fin','finR','finN',0,15);
  bind('ot','otR','otN',0,30);

  function calc(){
    var P=st.cap, rSC=st.sc/100, ltv=st.ltv/100, f=st.fin/100, rOT=st.ot/100;
    var loan=P*ltv;
    var base=P*rSC;
    var add=loan*rSC;
    var cost=loan*f;
    var scTotal=base+add-cost;
    var scYield=scTotal/P;
    var breakeven=rSC*(1+ltv)-ltv*f;   // == scYield
    var prem=breakeven-rSC;
    var otTotal=P*rOT;
    var gap=scTotal-otTotal;
    return {P:P,loan:loan,base:base,add:add,cost:cost,scTotal:scTotal,scYield:scYield,
            breakeven:breakeven,prem:prem,otTotal:otTotal,gap:gap,rSC:rSC,f:f};
  }

  function buildTable(c){
    var tb=document.getElementById('tbody');
    tb.innerHTML='';
    var beP = c.breakeven*100;              // breakeven coupon in %
    var start = Math.max(0, Math.floor((c.rSC*100)*2)/2); // step 0.5 from SC coupon
    var rows=[];
    for(var v=start; v<=beP+1.0001; v+=0.5){ rows.push(Math.round(v*10)/10); }
    // ensure exact breakeven line present
    var beR = Math.round(beP*10)/10;
    if(rows.indexOf(beR)===-1){ rows.push(beR); rows.sort(function(a,b){return a-b;}); }
    rows.forEach(function(v){
      var ot = c.P*(v/100);
      var d = c.scTotal - ot;
      var isBE = Math.abs(v-beR) < 0.05;
      var tr=document.createElement('tr');
      if(isBE) tr.className='be';
      var dtxt = isBE ? '打平' : usdSign(d);
      var dcls = isBE ? '' : (d>=0?'delta pos':'delta neg');
      tr.innerHTML =
        '<td>'+pct(v)+'%</td>'+
        '<td>'+usd(ot)+'</td>'+
        '<td class="sc">'+usd(c.scTotal)+'</td>'+
        '<td class="'+dcls+'">'+dtxt+'</td>';
      tb.appendChild(tr);
    });
  }

  function render(){
    var c=calc();

    // hero
    document.getElementById('beCoupon').textContent = pct(c.breakeven*100);
    document.getElementById('bePrem').textContent = '+'+pct(c.prem*100)+'%';
    document.getElementById('scYield').textContent = pct(c.scYield*100);
    document.getElementById('scTotalTop').textContent = usd(c.scTotal);
    document.getElementById('capTop').textContent = usd(c.P);
    document.getElementById('descSC').textContent = usd(c.scTotal);

    // warn if leverage unhelpful
    document.getElementById('warn').style.display = (c.rSC - c.f <= 0) ? 'block' : 'none';

    // breakdown
    document.getElementById('bdBase').textContent = usd(c.base);
    document.getElementById('bdAdd').textContent = '+'+usd(c.add);
    document.getElementById('bdCost').textContent = '−'+usd(c.cost);
    document.getElementById('bdTotal').textContent = usd(c.scTotal);

    // head-to-head bars
    var mx = Math.max(c.scTotal, c.otTotal, 1);
    document.getElementById('scBar').style.width = (100*c.scTotal/mx)+'%';
    document.getElementById('otBar').style.width = (100*c.otTotal/mx)+'%';
    document.getElementById('scBarAmt').textContent = usd(c.scTotal);
    document.getElementById('otBarAmt').textContent = usd(c.otTotal);

    // verdict
    var vd=document.getElementById('verdict'), vb=document.getElementById('verdictBig');
    if(Math.abs(c.gap) < 1){
      vd.className='verdict tie'; vd.firstChild.textContent='兩邊打平';
      vb.textContent='US$0 / 年';
    } else if(c.gap>0){
      vd.className='verdict win'; vd.firstChild.textContent='渣打多賺';
      vb.textContent = usdSign(c.gap).replace('$','US$') + ' / 年';
    } else {
      vd.className='verdict lose'; vd.firstChild.textContent='他行多賺';
      vb.textContent = usdSign(-c.gap).replace('$','US$') + ' / 年';
    }

    buildTable(c);
  }

  render();
})();
</script>
</body>
</html>
