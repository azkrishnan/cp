main_cp(js:["js/index.js?reload", "https://maps.googleapis.com/maps/api/js?signed_in=true&libraries=drawing,places&callback=initMap"]) {
//main_cp(js:["js/index.js"]) {
	header1_cp();
	div(attr:{id: "map"}, style: {height: "100%"});
	div(class: "catgselect hide-on-med-and-down", style: {"padding-bottom": "0px"}) {
		div(id: "maincontrol", style: {"margin-bottom": "-30px"}) {
			cp_filterform();
		}
		div(id: "maincontrol1", style:{display: "none"}) {
			div(class: "row") {
				div(class: "col l1 s1 m1") {
					div(style:{"padding": "8px", "margin-bottom": "4px", "padding-left": "0px", "margin-left": "-20px"}) {
						icon1(img: "photo/plus1.png", class: "pointer", attr:{onclick: 'minimaxifilter(2);'});
					}
				}
			}
		}
	}
	div(class: "modal", id: "commoncats") {
		div(class: "modal-content") {
//			cp_selectallcatgs();
		}
	}
	div(id: "bcard1", class: "modal bottom-sheet") {
		div(class: "modal-content") {
			print("Mohit");
		}
		div(class: "modal-footer") {
			print("Saini");
		}
	}

	div(style: {display: ""}) {
		businesscard();
	}
	div(class: "modal", id: "providerform", style: {padding: "20px"}) {
		div(style: {margin: "10px"}) {
			form(data:{onsubmit: "sreq", bobj: "", action: "providerinfo", restext: "Submitted"}) {
				div(style:{"font-size": "20px"}) {
					print("Fill the provider's Details");
				}
				div(class: "row"){
					input1(label: "Catageroy", id: "form_catg");
					input1(label: "Sub-Catageroy", id: "form_subcatg");
					input1(label: "Provider", id: "form_prov");
					input1(label: "Email", id: "form_email");
					input1(label: "Phone", id: "form_phone");
					input1(label: "Address", id: "form_address", aclass: "col l12");
					input1(label: "Link to Website", id: "form_web", aclass: "col l12");
					input1(label: "Link to Class Sechedule", id: "form_sechedule", aclass: "col l12");
				}
				div() {
					button1(name: "Submit", attr:{type: "submit"});
				}
			}		
		}		
	}
	div(class: "modal", id: "contactusform", style: {padding: "20px"}) {
		cp_contactus_form();
	}
	div(class: "modal", id: "ourstory", style: {padding: "20px"}) {
		cp_our_story();
	}
	div(class: "modal modal-fixed-footer", id: "searchform", style:{ padding: "0"}) {
		div(class: "modal-content", style: {padding: "0px", margin: "0px"}) {
//			cp_filtertags(typ: "_1");
		}
		div(class: "modal-footer", attr: {align: "right"}) {
			button2(aclass: "realyes modal-action modal-close", text: "Go");
		}
	}
}

