var STORE_NUMBER_PATTERN="(R[0-9][0-9][0-9])";
var countries=["US","CA"];
String.prototype.endsWith=function(a){return this.indexOf(a,this.length-a.length)!==-1
};
$(document).ready(function(){if($('body[id="ReservationConfirmation"]').length>0){$('#commentoverlayC a[id="submit"]').click(function(){comments=$('textarea[id="commentBox"]').val();
if(comments.length>0){$.ajax({type:"POST",url:location.href.split("?")[0]+"/update",data:"comments="+comments+"&_formToken="+encodeURIComponent($('input[name="_formToken"]').val()),dataType:"html",timeout:3000,success:function(v){},error:function(x,v,w){}});
$("#hasCommentsC #commentsC").text($("#commentsOverlay #commentBox").val());
$("#hasCommentsC").removeClass("NSCSSStateHidden");
$("#CommentsLink").hide()
}});
$('input[id="BusinessRelated"]').click(function(){checked=$(this).prop("checked");
$.ajax({type:"POST",url:location.href.split("?")[0]+"/update",data:"businessRelated="+(checked?"Y":"N")+"&_formToken="+encodeURIComponent($('input[name="_formToken"]').val()),dataType:"html",timeout:3000,success:function(v){},error:function(x,v,w){}})
});
$("#commentsOverlay #close").click(function(){if($("#commentsOverlay #commentBox").val().length>0){$("#commentsOverlay #commentBox").val("")
}})
}if($('body[id="ReservationHistory"]').length>0){var l=false;
$("#TheForm").submit(function(){var v=$(this).attr("action");
if(v.endsWith("cancel")||v.endsWith("cancelMultiSession")){if(!l){$("#cancelOverlay #okButtonC, #cancelOverlay #close").click(function(w){l=true;
$("#TheForm").submit()
});
return false
}else{l=false
}}})
}if($("body").hasClass("MakeAReservation")){var q=null;
var p=null;
var a=null;
var c=null;
var k=null;
var m=new Array();
function r(){$("#TheForm").attr("action",applicationContext+"/reservation/");
var z=document.referrer;
if(z!=null&&(z.indexOf("/geniusbar/")!=-1||z.indexOf("/workshops/")!=-1||z.indexOf("/biz/")!=-1)){var y=t("cwh_cache");
if(y!=null&&y.length>0){m=y.split(",")
}}else{f("cwh_cache")
}var x=m.length>0?m[m.length-1]:location.pathname;
var w=h(x);
$(w).each(function(A,B){switch(A){case 1:q=B;
break;
case 2:p=B;
break;
case 3:if(d(B)){k=B
}else{if(s(B)){c=B
}else{a=B
}}break;
case 4:if(d(B)){k=B
}else{c=B
}break;
case 5:k=B;
break
}});
if(a!=null&&a.length>0){$('select[id="stateMenu"]').val(a.toUpperCase());
b()
}if(c!=null&&c.length>0&&q!=null&&q.toUpperCase()!="US"&&q.toUpperCase()!="CA"){$('select[id="storeMenu"]').val(c);
e()
}if(k!=null&&k.length>0){var v=$('span[name="ruleType"]:contains('+k.toUpperCase()+")").parents(".ruleType");
n()
}i()
}$('select[id="stateMenu"]').change(function(){a=$(this).val().length>0?$(this).val():null;
i();
b()
});
function b(){j();
$('select[id="storeMenu"]').attr("disabled","disabled");
g();
if(a!=null&&a.length>0){$.ajax({type:"POST",url:applicationContext+"/reservation/"+q+"/"+a,data:"_formToken="+encodeURIComponent($('input[name="_formToken"]').val()),dataType:"json",timeout:10000,success:function(v){$.each(v,function(w,x){$("<option>").attr({value:w}).text(x).appendTo('select[id="storeMenu"]')
});
$('select[id="storeMenu"]').removeAttr("disabled");
if(c!=null){$('select[id="storeMenu"]').val(c);
e()
}},error:function(x,v,w){}})
}else{$('select[id="storeMenu"]').removeAttr("disabled");
$('select[id="storeMenu"] :nth-child(1)').attr("selected","selected")
}}$('select[id="storeMenu"]').change(function(){c=$(this).val().length>0?$(this).val():null;
i();
e()
});
function e(){$("#TheForm").find('input[name="storeNumber"]').remove();
if(c!=null&&c.length>0){if(c.length>0){$("<input>").attr({type:"hidden",name:"storeNumber"}).val(c).appendTo("#TheForm")
}var v=k;
if(k!=null&&k.length>0){v=k.toUpperCase()
}var w=null;
$('span[name="ruleType"]').each(function(){if($(this).text()===v){w=$(this).parents(".ruleType");
return false
}});
if(w.length>0){page.setSelection(null,null,true)
}else{j()
}}else{$('select[id="storeMenu"] :nth-child(1)').attr("selected","selected");
j()
}}$('a[class*="ruleType"]').click(function(v){k=$(this).find('span[name="ruleType"]').text();
i();
n();
v.preventDefault()
});
function n(){if(k!=null&&k.length>0){var v=null;
$('span[name="ruleType"]').each(function(){if($(this).text()===k.toUpperCase()){v=$(this).parents(".ruleType");
return false
}});
if(c!=null){page.setSelection(v,".ruleType",true)
}else{page.setSelection(v,".ruleType",false)
}}else{$(".ruleType").removeClass("selected");
j()
}}function i(){historyEntry="/reservation/"+q+"/"+p+(u().length>0?u():"");
m[m.length]=historyEntry
}function j(){$("#fwdButtonC").addClass("dark").removeClass("blue");
$("#fwdButtonC").unbind("click")
}$("#TheForm").submit(function(v){o("cwh_cache",m)
});
$("#backButtonC").unbind("click");
$("#backButtonC").click(function(C){if(m.length==0){window.location=applicationContext+"/reservation/previous"
}else{if(m.length>1){var v=m.splice(m.length-1,1);
var B=null;
var w=null;
var z=null;
var A=m[m.length-1];
var y=h(A);
$(y).each(function(D,E){switch(D){case 3:if(d(E)){z=E
}else{if(s(E)){w=E
}else{B=E
}}break;
case 4:if(d(E)){z=E
}else{w=E
}break;
case 5:z=E;
break
}});
if(B!=a){a=B;
$('select[id="stateMenu"]').val(a.toUpperCase());
b()
}if(w!=c){c=w;
$('select[id="storeMenu"]').val(c);
e()
}if(z!=k){k=z;
var x=$('span[name="ruleType"]:contains('+k.toUpperCase()+")").parents(".ruleType");
n()
}C.preventDefault()
}else{f("cwh_cache");
window.location=applicationContext+"/reservation/previous"
}}});
function g(){var v="Select a Store";
if(typeof selectStorei18nText!=="undefined"&&selectStorei18nText!=null){v=selectStorei18nText
}$('select[id="storeMenu"]').find("option").remove().end();
$("<option>").attr({value:""}).text(v).appendTo('select[id="storeMenu"]')
}function o(x,y,z){if(z){var w=new Date();
w.setTime(w.getTime()+(z*24*60*60*1000));
var v="; expires="+w.toGMTString()
}else{var v=""
}document.cookie=x+"="+y+v+"; path=/"
}function t(w){var y=w+"=";
var v=document.cookie.split(";");
for(var x=0;
x<v.length;
x++){var z=v[x];
while(z.charAt(0)==" "){z=z.substring(1,z.length)
}if(z.indexOf(y)==0){return z.substring(y.length,z.length)
}}return null
}function f(v){o(v,"",-1)
}function d(w){var v=false;
if(w.toUpperCase()=="TECHSUPPORT"||w.toUpperCase()=="WORKSHOP"||w.toUpperCase()=="BIZ_CONSULT"){v=true
}return v
}function s(v){return v.match(STORE_NUMBER_PATTERN)
}function u(){var v="";
if(a!=null){v+="/"+a
}if(c!=null){v+="/"+c
}if(k!=null){v+="/"+k
}return v
}function h(v){var B=v.split("#");
var z=B[0];
if(z.endsWith("/")){z=z.substr(0,z.length-1)
}var w=z.split("/");
w.splice(0,1);
var x=w[0]!="reservation";
if(x){w.splice(0,1)
}if(B.length>1){var y=B[1];
if(y.endsWith("/")){y=y.substr(0,z.length-1)
}var A=y.split("/");
A.splice(0,1);
w=w.concat(A)
}return w
}r()
}});
$.fn.switchReservations=function(b,a,d){var c=$("."+b);
$(c).each(function(f,g){$(g).css("visibility","hidden");
$(g).css("display","none")
});
c=$("."+a);
$(c).each(function(f,g){$(g).css("visibility","visible");
$(g).css("display","")
});
if($(c).length==0){$("#noReservationsMessageC").html(d);
$("#noReservationsC").css("display","")
}};
$.fn.resetSelectedButton=function(){$("#allReservationsC").parent().removeAttr("class");
$("#currentReservationsC").parent().removeAttr("class");
$("#pastReservationsC").parent().removeAttr("class");
$("#noReservationsC").css("display","none")
};
$.fn.showAllReservations=function(c){$(c).resetSelectedButton();
$("#allReservationsC").parent().addClass("on");
var a=$(".current");
$(a).each(function(d,f){$(f).css("visibility","visible");
$(f).css("display","")
});
var b=$(".past");
$(b).each(function(d,f){$(f).css("visibility","visible");
$(f).css("display","")
});
if($(a).length==0&&$(b).length==0){$("#noReservationsMessageC").html($("#noReservations").val());
$("#noReservationsC").css("display","")
}};
$.fn.showPastReservations=function(a){$(a).resetSelectedButton(a);
$("#pastReservationsC").parent().addClass("on");
$(a).switchReservations("current","past",$("#noPastReservationsMessage").val())
};
$.fn.showCurrentReservations=function(a){$(a).resetSelectedButton(a);
$("#currentReservationsC").parent().addClass("on");
$(a).switchReservations("past","current",$("#noFutureReservations").val())
};