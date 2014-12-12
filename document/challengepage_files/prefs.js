function h(a){return function(){return a
}
}fortyone=new function(){this.e=(new Date(2005,0,15)).getTimezoneOffset();
this.f=(new Date(2005,6,15)).getTimezoneOffset();
this.plugins=[];
this.d={Flash:["ShockwaveFlash.ShockwaveFlash",function(b){return b.getVariable("$version")
}],Director:["SWCtl.SWCtl",function(b){return b.ShockwaveVersion("")
}]};
this.q=function(b){var c;
try{c=document.getElementById(b)
}catch(d){}if(c===null||typeof c==="undefined"){try{c=document.getElementsByName(b)[0]
}catch(e){}}if(c===null||typeof c==="undefined"){for(var f=0;
f<document.forms.length;
f++){for(var g=document.forms[f],i=0;
i<g.elements.length;
i++){var a=g[i];
if(a.name===b||a.id===b){return a
}}}}return c
};
this.b=function(b){var c="";
try{if(typeof this.c.getComponentVersion!=="undefined"){c=this.c.getComponentVersion(b,"ComponentID")
}}catch(d){b=d.message.length;
b=b>40?40:b;
c=escape(d.message.substr(0,b))
}return c
};
this.exec=function(b){for(var c=0;
c<b.length;
c++){try{var d=eval(b[c]);
if(d){return d
}}catch(e){}}return""
};
this.o=function(b){var c="";
try{if(navigator.plugins&&navigator.plugins.length){var d=RegExp(b+".* ([0-9._]+)");
for(b=0;
b<navigator.plugins.length;
b++){var e=d.exec(navigator.plugins[b].name);
if(e===null){e=d.exec(navigator.plugins[b].description)
}if(e){c=e[1]
}}}else{if(window.ActiveXObject&&this.d[b]){try{var f=new ActiveXObject(this.d[b][0]);
c=this.d[b][1](f)
}catch(g){c=""
}}}}catch(i){c=i.message
}return c
};
this.p=function(){for(var b=["Acrobat","Flash","QuickTime","Java Plug-in","Director","Office"],c=0;
c<b.length;
c++){var d=b[c];
this.plugins[d]=this.o(d)
}};
this.g=function(){return Math.abs(this.e-this.f)
};
this.h=function(){return this.g()!==0
};
this.i=function(b){var c=Math.min(this.e,this.f);
return this.h()&&b.getTimezoneOffset()===c
};
this.m=function(b){var c=0;
c=0;
if(this.i(b)){c=this.g()
}return c=-(b.getTimezoneOffset()+c)/60
};
this.j=function(b,c,d,e){if(typeof e!=="boolean"){e=false
}for(var f=true,g;
(g=b.indexOf(c))>=0&&(e||f);
){b=b.substr(0,g)+d+b.substr(g+c.length);
f=false
}return b
};
this.l=function(){return(new Date(2005,5,7,21,33,44,888)).toLocaleString()
};
this.r=function(b){var c=new Date,d=[h("TF1"),h("016"),function(){return ScriptEngineMajorVersion()
},function(){return ScriptEngineMinorVersion()
},function(){return ScriptEngineBuildVersion()
},function(a){return a.b("{7790769C-0471-11D2-AF11-00C04FA35D02}")
},function(a){return a.b("{89820200-ECBD-11CF-8B85-00AA005B4340}")
},function(a){return a.b("{283807B5-2C60-11D0-A31D-00AA00B92C03}")
},function(a){return a.b("{4F216970-C90C-11D1-B5C7-0000F8051515}")
},function(a){return a.b("{44BBA848-CC51-11CF-AAFA-00AA00B6015C}")
},function(a){return a.b("{9381D8F2-0288-11D0-9501-00AA00B911A5}")
},function(a){return a.b("{4F216970-C90C-11D1-B5C7-0000F8051515}")
},function(a){return a.b("{5A8D6EE0-3E18-11D0-821E-444553540000}")
},function(a){return a.b("{89820200-ECBD-11CF-8B85-00AA005B4383}")
},function(a){return a.b("{08B0E5C0-4FCB-11CF-AAA5-00401C608555}")
},function(a){return a.b("{45EA75A0-A269-11D1-B5BF-0000F8051515}")
},function(a){return a.b("{DE5AED00-A4BF-11D1-9948-00C04F98BBC9}")
},function(a){return a.b("{22D6F312-B0F6-11D0-94AB-0080C74C7E95}")
},function(a){return a.b("{44BBA842-CC51-11CF-AAFA-00AA00B6015B}")
},function(a){return a.b("{3AF36230-A269-11D1-B5BF-0000F8051515}")
},function(a){return a.b("{44BBA840-CC51-11CF-AAFA-00AA00B6015C}")
},function(a){return a.b("{CC2A9BA0-3BDD-11D0-821E-444553540000}")
},function(a){return a.b("{08B0E5C0-4FCB-11CF-AAA5-00401C608500}")
},function(){return eval("navigator.appCodeName")
},function(){return eval("navigator.appName")
},function(){return eval("navigator.appVersion")
},function(a){return a.exec(["navigator.productSub","navigator.appMinorVersion"])
},function(){return eval("navigator.browserLanguage")
},function(){return eval("navigator.cookieEnabled")
},function(a){return a.exec(["navigator.oscpu","navigator.cpuClass"])
},function(){return eval("navigator.onLine")
},function(){return eval("navigator.platform")
},function(){return eval("navigator.systemLanguage")
},function(){return eval("navigator.userAgent")
},function(a){return a.exec(["navigator.language","navigator.userLanguage"])
},function(){return eval("document.defaultCharset")
},function(){return eval("document.domain")
},function(){return eval("screen.deviceXDPI")
},function(){return eval("screen.deviceYDPI")
},function(){return eval("screen.fontSmoothingEnabled")
},function(){return eval("screen.updateInterval")
},function(a){return a.h()
},function(a){return a.i(c)
},h("@UTC@"),function(a){return a.m(c)
},function(a){return a.l()
},function(){return eval("screen.width")
},function(){return eval("screen.height")
},function(a){return a.plugins.Acrobat
},function(a){return a.plugins.Flash
},function(a){return a.plugins.QuickTime
},function(a){return a.plugins["Java Plug-in"]
},function(a){return a.plugins.Director
},function(a){return a.plugins.Office
},function(){return(new Date).getTime()-c.getTime()
},function(a){return a.e
},function(a){return a.f
},function(){return c.toLocaleString()
},function(){return eval("screen.colorDepth")
},function(){return eval("window.screen.availWidth")
},function(){return eval("window.screen.availHeight")
},function(){return eval("window.screen.availLeft")
},function(){return eval("window.screen.availTop")
},function(a){return a.a("Acrobat")
},function(a){return a.a("Adobe SVG")
},function(a){return a.a("Authorware")
},function(a){return a.a("Citrix ICA")
},function(a){return a.a("Director")
},function(a){return a.a("Flash")
},function(a){return a.a("MapGuide")
},function(a){return a.a("MetaStream")
},function(a){return a.a("PDFViewer")
},function(a){return a.a("QuickTime")
},function(a){return a.a("RealOne")
},function(a){return a.a("RealPlayer Enterprise")
},function(a){return a.a("RealPlayer Plugin")
},function(a){return a.a("Seagate Software Report")
},function(a){return a.a("Silverlight")
},function(a){return a.a("Windows Media")
},function(a){return a.a("iPIX")
},function(a){return a.a("nppdf.so")
},function(a){return a.n()
},h(""),h(""),h(""),h(""),h(""),h("")];
this.p();
for(var e="",f=0;
f<d.length;
f++){if(b){e+=this.j(d[f].toString(),'"',"'",true);
e+="="
}var g;
try{g=d[f](this)
}catch(i){g=""
}e+=b?g:escape(g);
e+=";";
if(b){e+="\\n"
}}return e=this.j(e,escape("@UTC@"),(new Date).getTime())
};
this.k=function(b){try{var c;
c=this.q(b);
if(c!==null){try{c.value=this.r()
}catch(d){c.value=escape(d.message)
}}}catch(e){}};
this.a=function(b){try{if(navigator.plugins&&navigator.plugins.length){for(var c=0;
c<navigator.plugins.length;
c++){var d=navigator.plugins[c];
if(d.name.indexOf(b)>=0){return d.name+(d.description?"|"+d.description:"")
}}}}catch(e){}return""
};
this.n=function(){var b=document.createElement("span");
b.innerHTML="&nbsp;";
b.style.position="absolute";
b.style.left="-9999px";
document.body.appendChild(b);
var c=b.offsetHeight;
document.body.removeChild(b);
return c
}
};
try{fortyone.c=document.createElement("span");
typeof fortyone.c.addBehavior!=="undefined"&&fortyone.c.addBehavior("#default#clientCaps")
}catch(j){}window.fortyone=fortyone;
window.fortyone.collect=fortyone.k;