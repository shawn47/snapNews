var page = require('webpage').create();
var system = require('system');
// page.settings.userAgent = 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; fi-fi) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148a Safari/6533.18.5';
// page.settings.userAgent = 'Mozilla/5.0 (Linux; Android 4.4.4; SAMSUNG-SM-N900A Build/tt) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36';
// page.settings.userAgent = "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36";
page.open(system.args[1], function(status){
    console.log('Status:' + status);
    
    if(status === "success") {
    	page.evaluate(function(){
	        var content = document.body.innerHTML
	        var str = content;  
	        
	        var s1 = '陆慷';
	        var s2 = 'Lu Kang';
	        var s3 = '华春莹';
	        var s4 = 'Hua Chunying';
		    var reg1 = new RegExp("(" + s1 + ")", "g");  
		    var reg2 = new RegExp("(" + s2 + ")", "g"); 
		    var reg3 = new RegExp("(" + s3 + ")", "g");  
		    var reg4 = new RegExp("(" + s4 + ")", "g");  
		    
		    var newstr = str.replace(reg1, "<font color=#FF6633>$1</font>");
		    newstr = newstr.replace(reg2, "<font color=#FF6633>$1</font>");
		    newstr = newstr.replace(reg3, "<font color=#FF6633>$1</font>");
		    newstr = newstr.replace(reg4, "<font color=#FF6633>$1</font>");
			document.body.innerHTML = newstr;
	    });

        page.render(system.args[2]);
    }
    phantom.exit();
});
