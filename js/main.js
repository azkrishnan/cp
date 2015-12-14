
mergeforce(funcs, {
	addfav: function() {
		runf("error", {msg: "You need to login first !"});
	},
	selectall: function() {
		selectAll(obj);
	},
	redraw: function() {
		draw_points(getallproviders(findselected()));
	},
	addfav: function() {//pid
		var cookies = getCookie("myfav");
		sifu(cookies, "plist", []);
		appenduniq(cookies["plist"], pid);
		runf("error", {msg: "Added to Your Favorite"});
		setCookie("myfav", cookies);
		dispfavlist();
	}
});




function runonload(){
	$('.button-collapse').sideNav();
	$('.parallax').parallax();
	$('.materialboxed').materialbox();
	$('.slider').slider({
		full_width: true,
		height:350,
		transition:400,
		interval:3500
	});
	$(".collapsible_sub").collapsible();
    $('select').material_select();
	$(".modal-trigger").leanModal();
}




$( document ).ready(function(){
	runonload();
});


function setCookie(cname, cvalue, exdays) {
	cvalue = JSON.stringify(cvalue);
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires="+d.toUTCString();
    document.cookie = cname + "=" + cvalue + "; " + expires;
}

function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1);
        if (c.indexOf(name) == 0)
        	return JSON.parse(c.substring(name.length, c.length));
    }
    return {};
}



function f() {
	return $("body").width();
}

