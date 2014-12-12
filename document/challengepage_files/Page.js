function Page(w){var e="#backButtonC";
var h="#fwdButtonC";
var j="#menuButtonC";
var x="#TheForm";
var u=typeof w==="undefined"?e:typeof w.previousButton==="undefined"?e:w.previousButton;
var k=typeof w==="undefined"?h:typeof w.nextButton=="undefined"?h:w.nextButton;
var t=typeof w==="undefined"?j:typeof w.cancelButton==="undefined"?j:w.cancelButton;
var s=typeof w==="undefined"?x:typeof w.form==="undefined"?x:w.form;
var c;
var f;
var n;
var l;
var y=0;
var o=false;
var p;
var i=true;
var v;
this.scrub=function(){$(document).keypress(function(d){if(($(k).exists()&&$(k).attr("class")).search("blue")!=-1&&d.which==13){var z=false;
$(v).each(function(B,A){var C=$(A).data("overlay");
if(C!=null&&C.isOpened()){z=true
}});
if(z==false){$(s).submit()
}}});
if($(u).exists()){if(previousButton!=null){previous=previousButton
}else{previous=$(u).attr("href")
}$(u).attr("href","#");
$(u).click(function(d){window.location=previous
})
}if($(k).exists()){$(k).attr("href","#");
if(nextButton!=null){$(s).attr("action",nextButton)
}$(k).click(function(d){if(i){d.preventDefault()
}else{$(s).submit()
}});
$(k).keypress(function(d){if(event.which==13){if(i){d.preventDefault()
}else{$(s).submit()
}}})
}if($(t).exists()){if(cancelButton!=null){cancel=cancelButton
}else{cancel=$(t).attr("href")
}$(t).attr("href","#");
$(t).click(function(d){window.location=cancel
})
}if($(".postable").exists()){$(".postable").each(function(){if($(this).is("a")&&$(this).attr("href")!="#"){href=$(this).attr("href");
if($(this).attr("href")!==undefined){if($(this).find(".value").exists()){$(this).attr("href","#");
$(this).attr("url",href)
}else{$(this).attr("href",href.slice(href.lastIndexOf("/")));
$(this).attr("url",href.slice(0,href.lastIndexOf("/")))
}}}})
}if($(".selectable").exists()){$(".selectable").each(function(){if($(this).is("a")&&$(this).attr("href")!="#"){href=$(this).attr("href");
if($(this).attr("href")!==undefined){if($(this).find(".value").exists()){$(this).attr("href","#")
}else{$(this).attr("href",href.slice(href.lastIndexOf("/")))
}}}})
}};
this.bindFadeables=function(){page=this;
fadeables=m($('[class*="fadeable"]'));
$(fadeables).each(function(d,z){placeHolder=$(z).text();
opacity=0;
classes=$(z).attr("class").split(" ");
$.each(classes,function(B,A){if(A.indexOf("fadeable-")!=-1){opacity=A.split("-")[1]
}});
associatedTo=$(z).attr("rel");
$(z).click(function(){$(associatedTo).focus()
});
if($(associatedTo).val().length>0){$(z).text("")
}$(associatedTo).focus(function(){if($(this).val().length==0){$(z).fadeTo("slow",opacity)
}});
$(associatedTo).keyup(function(){if($(this).val().length>0){$(z).text("")
}else{$(z).text(placeHolder)
}});
$(associatedTo).blur(function(){if($(this).val().length==0){$(z).fadeTo("slow",1)
}})
})
};
this.bindPostables=function(){page=this;
postables=m($(".postable"));
$(postables).click(function(d){page.setSelection(this,".postable",false);
$(s).attr("action",$(this).attr("url"));
$(s).submit();
d.stopPropagation();
d.preventDefault();
return false
})
};
this.bindSelectables=function(){page=this;
selectables=m($(".selectable"));
$(selectables).click(function(d){relprop=this.rel;
page.setSelection(this,".selectable",relprop=="");
d.stopPropagation();
return false
})
};
this.bindConditionals=function(){page=this;
$(".conditional").click(function(d){toggle=$(this).attr("rel");
$(toggle).css("display")=="block"?$(toggle).css("display","none"):$(toggle).css("display","block");
$(toggle+" .selectable").removeClass("selected");
if($(".selected").length==0){b()
}if(!page.hasOverlays()){d.stopPropagation();
return false
}})
};
this.hasOverlays=function(){return $(c).exists()?true:false
};
this.hasScrollables=function(){return $(n).exists()?true:false
};
this.hasTooltips=function(){return $(f).exists()?true:false
};
this.initOverlays=function(z){if($(z).length==1){z=new Array(z)
}c=z
};
this.overlayClosed=function(){g()
};
this.initScrollables=function(z){if($(z).length==1){z=new Array(z)
}n=z;
$.easing.times=function(C,D,B,G,F){var E=(D/=F)*D;
var A=E*D;
return B+G*(-1.6475*A*E+5.4925*E*E+-6.39*A+1.395*E+2.15*D)
}
};
this.initTooltips=function(z){if($(z).length==1){z=new Array(z)
}f=z
};
this.setSelection=function(A,z,d){l=A;
q(z);
r();
if(d){g()
}};
function q(d){$(d).removeClass("selected");
$(l).addClass("selected")
}function r(){input=a();
if($(s).exists()&&input!=null){$.each(input,function(d,z){$(s).find("input[name="+d+"]").remove();
$("<input>").attr({type:"hidden",name:d}).val(z).appendTo(s)
})
}}function g(){$(k).addClass("blue").removeClass("dark");
$(k).unbind("click");
$(k).unbind("keypress");
$(k).click(function(d){$(s).submit();
d.stopPropagation();
d.preventDefault();
return false
});
$(k).keypress(function(d){if(d.which==13){$(s).submit();
d.stopPropagation();
d.preventDefault();
return false
}})
}function b(){$(k).addClass("dark").removeClass("blue");
if(i){$(k).unbind("click");
$(k).unbind("keypress")
}}function m(d){ables=new Array();
$(d).each(function(z){if($(this).parents("form").exists()){ables[z]=this
}});
return ables
}function a(){input={};
if($(l).find(".value").exists()){values=$(l).find(".value");
$(values).each(function(d,z){name=$(z).attr("name");
value=$(z).text();
input[name]=value
})
}else{if($(l).is("a")&&$(l).attr("href")!==undefined&&$(l).attr("href")!="#"){name=$(l).attr("name");
parts=$(l).attr("href").splice(l.lastIndexOf("/"));
value=parts[parts.length-1];
input[name]=value
}else{if($(l).is("option")){name=$(l).attr("name");
value=$(l).attr("value");
input[name]=value
}}}return input
}this.setErrorCount=function(d){y=d
};
this.setErrorCountStarted=function(d){o=d
};
this.getForm=function(){return s
};
this.getOverlays=function(){return c
};
this.getOverlayables=function(){return v
};
this.setOverlayables=function(d){v=d
};
this.getTooltips=function(){return f
};
this.getScrollables=function(){return n
};
this.getErrorCount=function(){return y
};
this.hasErrorCountStarted=function(){return o
};
this.getValueAtLoadAttributes=function(){return p
};
this.setValueAtLoadAttributes=function(d){p=d
};
this.setDisableNextButtonAction=function(d){i=d
};
this.isDisableNextButtonAction=function(){return i
}
};