var radius = 50;//km
var gmap = null;
var curloc = null;
var circle100km = null;
var infowindow = null;

var marker_icons = ["photo/found2.png", "photo/found4.png", "photo/favloc5.png"];

var providers = {};//(provider_id -> marker)List
var pid = jsdata.pid;

var activep = jsdata.activep;

function choosevisiable(inp) {
	return filter(function(x){
		return $(x).is(":visible");
	}, inp)[0];
}

function getsearchinput() {
	return $($("#searchloc").is(":visible") ? "#searchloc": "#searchloc_1");
}

function getfilter() {
	return $($("#catgselect").is(":visible") ? "#catgselect": "#searchform");
}

function init_cookies() {
	var cookies = getCookie("myfav");
	sifu(cookies, "plist", []);
	setCookie("myfav", cookies);
}

function msgformatching(numclasses) {
	// var inmyrange = map(id, mapp(function(i) {
	// 	var ploc = provider[i];
	// 	return latlandist(curloc.position.lat(), curloc.position.lng(), ploc.lat, ploc.lng);
	// }, activep), function(x) { return (x<= circle100km.radius); });
	// var intrad = int(circle100km.radius/1000);
	// if(inmyrange.length > 0 )
	// 	runf("error", {"msg": (numclasses == null ? (inmyrange.length+" Locations"): inmyrange.length+" Locations, "+numclasses+" Classes"  )+" matching"+(numclasses == null ? " in "+intrad+" KM": "")  });
	// else
	// 	runf("error", {"msg": "No Location matching in "+intrad+" KM"});
	// return inmyrange;
}

function drawgroups(groups) {
	var myl = getCookie("myfav").plist;//List of Fav providers.
	mapp(function(x) {
		x.setVisible(false);
	}, providers);
	map(function(x) {// lat:x[0], lng:x[1], provider_id:x[2], num_of_providers:x[3]
		if(!haskey(providers, x[2])) {
			var prov_loc= new google.maps.Marker({
				position: {lat: x[0], lng: x[1]},
				icon: marker_icons[0]
			});
			google.maps.event.addListener(prov_loc, 'click', function() {
				$("#providerinfo").openModal();
				bcard.openbcard(x[4].split(","));
			});
			prov_loc.setMap(gmap);
			providers[x[2]] = prov_loc;
		}
		var thismarker = providers[x[2]];
		thismarker.setIcon( (belongs(myl, x[2]) && x[3] ==1) ? marker_icons[2]: "photo/numicons/marker"+x[3]+".png");
		thismarker.setPosition({lat: x[0], lng: x[1]});
		thismarker.setVisible(true);
	}, groups);
}

function redisplay(needplist) {
	var params = {action: "providergroup", zoom: gmap.zoom, viewport: placetoll(gmap.center), home: placetoll(curloc.position), radius: circle100km.radius/1000.0};
	if(needplist == undefined)
		params.plist = activep.join(",");
	
	runf("req1", {params: params, callback: function(d){
		drawgroups(d["data"]["groups"]);
	}});
}

//geolocgroup(plist, gmap.zoom, markers_density)

function setcurloc(place, showmsg) {
	curloc.setVisible(true);
	gmap.setCenter(place);
	gmap.setZoom(8);
	curloc.setPosition(place);
	circle100km.setCenter(place);
	if(!(showmsg)) {
		msgformatching();
	}
}

function placetoll(place) {
	return {'lat': place.lat(), 'lng': place.lng()};
}

function initMap() {
	if(pid > 0) {
		var myCenter = new google.maps.LatLng( provider[pid].lat, provider[pid].lng );
	} else {
		var myCenter = new google.maps.LatLng( 37.7577627,-122.4727052 );
	}
	gmap = new google.maps.Map(document.getElementById('map'), {
		center: myCenter,
		zoom: 8,
		mapTypeId: google.maps.MapTypeId.ROADMAP
	});
	gmap.addListener("zoom_changed", function() {
		redisplay(1);
	});
	$.get("http://ip-api.com/json", function(data){
		if(pid == 0) {
//			setcurloc({'lat':data.lat, 'lng':data.lon}, 'dontshow');
		}
	});
	curloc = new google.maps.Marker({
		position: myCenter,
		icon: "photo/homem1.png",
		draggable: true
	});
	curloc.addListener("mouseup", function(){
		msgformatching();
		//console.log("Changed marker Position");
	});
	if(pid>0)
		curloc.setVisible(false);
	infowindow = new google.maps.InfoWindow({
		content: "<div>Hey mohit.</div>",
		maxWidth: 500
	});
	circle100km = new google.maps.Circle({
		strokeColor: '#FF0000',
		strokeOpacity: 0.8,
		strokeWeight: 2,
		fillColor: '#aaaaaa',
		fillOpacity: 0.35,
		map: gmap,
		center: myCenter,
		radius: radius * 1000,
		editable: true,
	});
	circle100km.bindTo('center', curloc, 'position');
	circle100km.addListener("radius_changed", function() {
		msgformatching();
	});
	curloc.setMap(gmap);
	var autocomplete = new google.maps.places.Autocomplete( getsearchinput()[0] );
	autocomplete.addListener('place_changed', function() {
		if( haskey(autocomplete.getPlace(), "geometry")) {
			setcurloc( autocomplete.getPlace().geometry.location );
		}
	});
	redisplay();
}


function getLocation() {
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(showPosition);
	}
}

function showPosition(position) {
	$.get("https://maps.googleapis.com/maps/api/geocode/json?latlng="+position.coords.latitude+","+position.coords.longitude, function(r){
		getsearchinput().val( r["results"][0]["formatted_address"]);
		setcurloc({lat:position.coords.latitude, lng:position.coords.longitude});
	});
}

$(document).ready(function() {
	if( (true || (jsdata["_server"] != "gcl" && jsdata._server != "mohit") ) && pid == 0 )
		getLocation();
});


function getallproviders(selectedcatg){
	var outp = [];
	var numclasses = 0;
	for(var i=0; i<selectedcatg.length; i++) {
		if(selectedcatg[i].length == 3){
			var j = selectedcatg[i];
			try {
				var addedprov = map(function(x){return ""+x["provider_index"];}, jsdata.maininfocatg[j[0]][j[1]][j[2]]);
				outp = addluniq(outp, addedprov);
				if(addedprov.length > 0)
					numclasses++;
			} catch (e) {

			}
		}
	}
	return {providers: outp, numclasses: numclasses};
}



function findselected() {
	var allcbox = getfilter().find("input[type=checkbox]");
	var selectedcatg = map(function(i){
		return dattr(allcbox[i]).catgtid.split("_");
	}, range(allcbox.length), function(i) {
		return allcbox[i].checked;
	});
	return selectedcatg;
}

function draw_points(inp) {
	activep = inp.providers;
	msgformatching(inp.numclasses);
	redisplay();
}

//draw_points( getallproviders( findselected() ) )

if(pid>0)
	$("#providerinfo_"+pid).openModal();



function dispfavlist() {
	var myl = getCookie("myfav").plist;
	mapo(function (x) {
		if(belongs(myl, dattr(x)["pid"])) {
			x.style.display = "";
		} else {
			x.style.display = "none";
		}
	}, $(".favlistelm"));

}

function minimaxifilter(i) {
	if(i==1) {
		$('#maincontrol').hide(1000, function(){
			$('#maincontrol1').show();
		});
	} else {
		$('#maincontrol1').hide();
		$('#maincontrol').show(1000);
	}
}

ms.searchparam = function() {
	return {zoom: gmap.zoom, viewport: placetoll(gmap.center), home: placetoll(curloc.position), radius: circle100km.radius/1000.0};
}

ms.f1 = function(data) {
	activep = data.data.activep;
	drawgroups(data.data.groups);
}



init_cookies();
dispfavlist();

$("#providerinfo").openModal();




//$("#myfavlist").openModal();





































// var plist = [[37.5335276, -121.9600244], [37.5607886, -121.9562632], [37.560177, -121.956406], [37.5603862, -121.9564359], [37.5601614, -121.9563808], [37.5603802, -121.9564272], [37.5601459, -121.9563554], [37.5536275, -121.9780933], [37.509425, -121.9583859], [37.5268552, -122.0017578], [37.586206, -122.0634934], [37.5520431, -121.9948844], [37.6686276, -122.088587], [37.6063621, -122.1178261], [37.6367247, -122.1251753], [37.6367247, -122.1251753]];

// t= geolocgroup(plist, 8, 0.00030)
// console.log(t.toSource());

