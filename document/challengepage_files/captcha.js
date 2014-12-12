var imgtoken;
var audtoken;
var CaptchaFormat={IMAGE:"IMAGE",AUDIO:"AUDIO"};
var CaptchaProcess={getCaptcha:function(){var b=$("#captchaFormat").val();
var a=encodeURIComponent($("#captchaKey").val());
$("#captchaAnswer").val("");
$("#captchaError").html("");
if(b===CaptchaFormat.IMAGE){$("#captcha").html("<img id='imageCaptcha'  style='width: 160px; height: 70px;' src='captcha?&format="+b+"&key="+a+"&t="+new Date().getTime()+"'/>")
}else{$("#captcha").html("<img id='captchaImage' width='170' height='70' style='display: block;' alt='No image found' src='"+applicationContext+"/resources/images/captcha_audio_icon.jpg'></img>");
$("#captcha").append("<embed id='audioCaptcha' style='display: block; width: 0px; height: 0px;' type='audio/x-wav' src='captcha?format="+b+"&key="+a+"&t="+new Date().getTime()+"'></embed>")
}$("#captchaC").show()
},toggle:function(){var a=$("#captchaFormat").val();
if(a==CaptchaFormat.IMAGE){$("#captchaFormat").val(CaptchaFormat.AUDIO);
$("#captchaToggleButton").attr("src",applicationContext+"/resources/images/captcha_text_icon.png");
$("#captchaRefreshSpan").text($("#captchaTryNewAudio").val());
$("#captchaToggleSpan").text($("#captchaBackToText").val())
}else{$("#captchaFormat").val(CaptchaFormat.IMAGE);
$("#captchaToggleButton").attr("src",applicationContext+"/resources/images/captcha_audio.png");
$("#captchaRefreshSpan").text($("#captchaTryNewImg").val());
$("#captchaToggleSpan").text($("#captchaVisionImpaired").val())
}CaptchaProcess.getCaptcha()
}};
jQuery(document).ready(function(){if($("#captcha").length>0){$("#captchaFormat").val(CaptchaFormat.IMAGE);
CaptchaProcess.getCaptcha()
}});