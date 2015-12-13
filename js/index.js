var radius = 50;//km
var gmap = null;
var curloc = null;
var circle100km = null;
var infowindow = null;
var markers_density = 0.00100;

var marker_icons = ["photo/found2.png", "photo/found4.png", "photo/favloc3.png"];


var provider = jsdata.provider;
var pid = jsdata.pid;

if(pid == 0)
	var activep = array_keys(provider);
else
	var activep = [pid];


function init_cookies() {
	var cookies = getCookie("myfav");
	sifu(cookies, "plist", []);
	setCookie("myfav", cookies);
}


function msgformatching(numclasses) {
	var inmyrange = map(id, mapp(function(i) {
		var ploc = provider[i];
		return latlandist(curloc.position.lat(), curloc.position.lng(), ploc.lat, ploc.lng);
	}, activep), function(x) { return (x<= circle100km.radius); });
	var intrad = int(circle100km.radius/1000);
	if(inmyrange.length > 0 )
		runf("error", {"msg": (numclasses == null ? (inmyrange.length+" Locations"): inmyrange.length+" Locations, "+numclasses+" Classes"  )+" matching in your Area("+intrad+" KM)"});
	else
		runf("error", {"msg": "No Location matching in your Area("+intrad+" KM)"});
	return inmyrange;
}

function redisplay() {
	var myl = getCookie("myfav").plist;//List of Fav providers.
	var plist = map(function(x) {
		return [provider[x].lat, provider[x].lng, x];
	}, activep);
	mapp(function(x){
		x.locmark.setVisible(false);
	}, provider);
	map(function(x) {//assuming x.length > 0
		var thismarker = provider[x[0][2]];
		var locmark = thismarker.locmark;
		locmark.setIcon(marker_icons[ (belongs(myl, x[0][2]) && x.length ==1)  ? 2:(0+(x.length==1))]);
		var avgloc = mapp(function(x2) {
			return x2/x.length;
		}, fold(function (x1, y1) {
			return [x1[0]+y1[0], x1[1]+y1[1]];
		}, x, [0, 0]), null, function (x1) {
			return ["lat", "lng"][x1];
		});
		locmark.setPosition(avgloc);
		//thismarker.infow.setContent(x.toSource()+"\n\n----\n\n"+avgloc.toSource());
		locmark.setVisible(true);
	}, geolocgroup(plist, gmap.zoom, markers_density));
}


function setcurloc(place, showmsg) {
	curloc.setVisible(true);
	gmap.setCenter(place);
	gmap.setZoom(10);
	curloc.setPosition(place);
	circle100km.setCenter(place);
	if(!(showmsg)) {
		msgformatching();
	}
}

function placetoll() {
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
		zoom: 9,
		mapTypeId: google.maps.MapTypeId.ROADMAP
	});
	gmap.addListener("zoom_changed", function() {
		redisplay();
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
	mapp(function(info, i) {
		 var prov_loc= new google.maps.Marker({
			position: {lat: info.lat, lng: info.lng},
			icon: marker_icons[0]
		});
		var prov_infow = new google.maps.InfoWindow({
			content: "<div>Hey mohit.</div>",
			maxWidth: 500
		});
		google.maps.event.addListener(prov_loc, 'click', function() {
			$("#providerinfo_"+i).openModal();
			//prov_infow.open(gmap, prov_loc);
		});
		if(pid>0 && i!=pid) {
			prov_loc.setVisible(false);
		}
		prov_loc.setMap(gmap);
		provider[i]["locmark"] = prov_loc;
		provider[i]["infow"] = prov_infow;
	}, provider);

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
	var autocomplete = new google.maps.places.Autocomplete( $("#searchloc")[0] );
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
		$("#searchloc").val( r["results"][0]["formatted_address"] );
		setcurloc({lat:position.coords.latitude, lng:position.coords.longitude});
	});
}

$(document).ready(function() {
	if( (jsdata["_server"] != "gcl" && jsdata._server != "mohit" ) && pid == 0 )
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
	var allcbox = $(".catgselect").find("input[type=checkbox]");
	var selectedcatg = map(function(i){
		return dattr(allcbox[i]).catgtid.split("_");
	}, range(allcbox.length), function(i) {
		return allcbox[i].checked;
	});
	return selectedcatg;
}

function draw_points(inp) {
	// var tohide = listaminusb(array_keys(provider), providers);
	// map(function(x){ provider[x].locmark.setVisible(false); }, tohide);
	// map(function(x){ provider[x].locmark.setVisible(true); }, providers);
	activep = inp.providers;
	msgformatching(inp.numclasses);
	redisplay();
//	infowindow.close();
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

init_cookies();
dispfavlist();






//$("#myfavlist").openModal();





































// var plist = [[37.5335276, -121.9600244], [37.5607886, -121.9562632], [37.560177, -121.956406], [37.5603862, -121.9564359], [37.5601614, -121.9563808], [37.5603802, -121.9564272], [37.5601459, -121.9563554], [37.5536275, -121.9780933], [37.509425, -121.9583859], [37.5268552, -122.0017578], [37.586206, -122.0634934], [37.5520431, -121.9948844], [37.6686276, -122.088587], [37.6063621, -122.1178261], [37.6367247, -122.1251753], [37.6367247, -122.1251753]];

// t= geolocgroup(plist, 8, 0.00030)
// console.log(t.toSource());

