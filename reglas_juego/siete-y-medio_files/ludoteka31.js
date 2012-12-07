onerror=fallo;
var zabal=ww();
var altu=hh();
var hizk='es';
function fallo(msg,non,num) {
 return(true)
}
function ww() {
 return(150+Math.round(screen.width*.8));
}
function hh() {
 return(80+Math.round(screen.height*.85));
}
function ireki(a,w,s) {
 var x=window.open(a,w,s);
 x.focus();
}
function prest() {
 aditu();
}
function ie() {
 return(navigator.appName.indexOf("Microsoft")!=-1);
}
function ie7() {
 return(navigator.appVersion.indexOf("MSIE 7")!=-1);
}
function ttipi() {
 var x=window.innerWidth;
 var y=window.innerHeight;
 if (ie()) {
  x=document.body.clientWidth;
  y=document.body.clientHeight;
 }
 if (x<350 || y<300) {
  window.top.resizeBy(Math.max(0,350-x),Math.max(0,300-y));
 }
}
function erdian(ww,hh) {
 return(",width="+ww+",height="+hh+(screen.width?",left="+((screen.width-ww)/2):"")+(screen.height?",top="+((screen.height-hh)/2-40):""));
}
function korri3() {
 document.applets['ikus'].korri(3);
}
function aditu() {
 window.scrollTo(0,0);
 if (document.applets['ikus'].foko()=="B") {
  window.focus();
  document.applets['ikus'].focus();
 }
 z=document.applets['ikus'].zklip();
 if (z!="0") {
  irekik("klip?hizk="+document.applets['ikus'].emanHizk()+"&lehia="+z+"&gako="+document.applets['ikus'].emanGako());
 }
 if (document.applets['ikus'].martxanbai()=="B") {
  setTimeout("aditu()",2000);
 }
}
function jokatumak(h,m) {
 jokatumakina(h,m,2);
}
function jokatumakina(h,m,v) {
 hizk=h;
 onerror=irekierr;
/* if (ie7()) {
  var leh=open('','_blank',lehatr());
  if (leh!=null && leh.location.href.indexOf('http')>-1) {
   leh.focus();
   return;
  }
 }*/
 irekizona("bai",m,v);
}
function bajaRes() {
 return(screen.width<801?"low":"high");
}
function irekierr(msg,non,num) {
 irekizona("bai","huts");
}
function lehatr() {
 return("toolbar=0,scrollbars=0,location=0,menubar=0,resizable=1,status=1,directories=0"+erdian(zabal,altu));
}
function irekizona(jav,m) {
 ireki("bikus?mak="+m+"&java="+jav+"&hizk="+hizk+"&rnd="+((new Date()).getTime()%997),"_blank",lehatr());
 return(true);
}
function irekib(s) {
 ireki(s,"_blank","toolbar=0,scrollbars=0,location=0,menubar=0,resizable=0,status=1,directories=0"+(screen.width<801?erdian(720,510):erdian(980,710)));
}
function irekik(s) {
 ireki(s,"_blank","toolbar=0,scrollbars=1,location=0,menubar=0,resizable=1,status=1,directories=0"+erdian(770,560));
}
function popup(s,w,h) {
 ireki(s,"_blank","toolbar=0,scrollbars=1,location=0,menubar=0,resizable=1,status=1,directories=0"+erdian(w,h));
}
function ingurune() {
 var sep=" ; "
 var r=navigator.appCodeName+sep+navigator.appName+sep+navigator.appVersion+sep;
 r=r+navigator.platform+sep; // navigator.userAgent
 r=r+"java "+(navigator.javaEnabled()?"si":"no");
 for (i=0; i<navigator.plugins.length; i++) {
  r=r+(i==0?"<br>Plugins: ":sep)+navigator.plugins[i].name+" "+navigator.plugins[i].description;
 }
 return(r);
}
function hizkik(dat,relax) {
 var hik="0123456789aAâàåáÂÅÁÀbBcCçÇdDeEêéèëÉÊËÈfFgGhHiIïîìíÏÎÌÍjJkKlLmMnNñÑoOôòóÔÒÓpPqQrRsStTuUûùúÚÛÙvVwWxXyYýÝzZ_";
 var hikrelax="ªºæÆÖöÄäÜü";
 var d="document.login."+dat+".value";
 var s=eval(d);
 var r="";
 for (i=0; i<s.length; i++) {
  var c=s.charAt(i);
  if (hik.indexOf(c)>-1 || (relax==1 && hikrelax.indexOf(c)>-1)) {
   r=r+c;
  }
 }
 if (r!=s) {
  eval(d+"='"+r+"'");
 }
}
function htmlpun(cb,cf,p) {
 document.write("<div class='lortu' style='background-color:#"+cb+";color:#"+cf+";'>"+p+"</div>");
}
function idatzi(z) {
 document.getElementById('ff').erantzun.value=z;
 document.getElementById('ff').nola.value=1;
 document.getElementById('ff').submit();
}
function lmsegi(n) {
 document.getElementById('ff').nola.value=n;
 document.getElementById('ff').submit();
}
function irakur(z,n) {
 document.getElementById('ff').nola.value=n;
 document.getElementById('ff').lehen.value=z;
 document.getElementById('ff').submit();
}

function kapaikusi(id) /*, img) */
{
	capa = document.getElementById(id);
	if (capa.style.display == "none")
	{
/*		img.src="minus.gif" */
		capa.style.display = "block";
	}
	else
	{
/*		img.src="plus.gif" */
		capa.style.display = "none";	
	}
	return true;
}

function smskapaikusi(herrialde){
	document.getElementById(herrialde).style.display="block";
	document.getElementById("div"+herrialde).className="aktibo";
	if(document.getElementById("id_hizk").value!=herrialde)
		{
		document.getElementById(document.getElementById("id_hizk").value).style.display="none";
		document.getElementById("div"+document.getElementById("id_hizk").value).className="normal";
		}
	document.getElementById("id_hizk").value=herrialde;
	}
	
	function ludomotaaldatu(harpid){
		for (i=0;ele=document.getElementById("pagomota").denboraharp[i]; i++)
			ele.disabled=!harpid;
		for (i=0;ele=document.getElementById("pagomota").denborasaldo[i]; i++)
			ele.disabled=harpid;
		document.getElementById("li_suscripcion").style.color = harpid?"#000000":"#888888";
		document.getElementById("li_bono").style.color = harpid?"#888888":"#000000";
	}

function putNumber(number){
	if (document.getElementById)
	{
		document.getElementById("tfnumber").innerHTML = number;
	}
	else if (document.all)
	{
		document.all["tfnumber"].innerHTML = number;
	}
}

var wpubli=176;
var tpubli=null;
function tambikus() {
  var ww=$(window).width();
  var hh=$(window).height();
  $("#publi").css("height",hh+"px");
  $("#zona").css("left",wpubli+"px").css("height",hh+"px").css("width",(ww-wpubli)+"px").height(hh).width(ww-publi);
  $("#zona applet").first().height(hh).width(ww-wpubli);  // attr+"px"
}

function loadbikus() {
  $("#publi").css("width",wpubli);
  $("body").css("overflow","hidden").css("background-color","#a7bbc7");
  $(window).resize(tambikus);
  tambikus();
  tpubli=setInterval(zamapubli,600000);
  zamapubli();
  setTimeout(kpubli,15000);
}

function zamapubli() {
  $("#frpubli").attr("src","publizona");
}

function kpubli() {
  var kp=document.applets['ikus'].kpubli();
  if (kp=="bai") {
    kendupubli();
    return;
  }
  setTimeout(kpubli,15000);
}

function kendupubli() {
  wpubli=0;
  tambikus();
  clearInterval(tpubli);
}