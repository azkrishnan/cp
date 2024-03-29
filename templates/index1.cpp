main_cp(js:["js/index.js", "https://maps.googleapis.com/maps/api/js?signed_in=true&libraries=drawing,places&callback=initMap"]) {
//main_cp(js:["js/jquery-ui.js", "js/index.js"], title: "Class Pundit") {
	header1_cp();
	div(attr:{id: "map"}, style: {height: "100%"});
	div(class: "catgselect", style: {"padding-bottom": "0px"}) {
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
			cp_selectallcatgs();
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

	div(attr:{id: "myfavlist"}, class: "modal bottom-sheet") {
		div(class: "container-fluid") {
			div(class: "row"){
				pkeys = provider.keys;
				for(i, pkeys) {
					pinfo = provider[i];
					div(class: "col l12 m12 s12 favlistelm", data:{pid: i}) {
						a1(text: pinfo["name_provider"]+" "+pinfo["address"], href: nhost+pinfo["username"], attr:{});
					}
				}
			}
		}
	}
	div(style: {display: ""}) {
		pkeys = provider.keys;
		for(i, pkeys) {
			pinfo = provider[i];
			div(attr:{id: "providerinfo_"+i}, class: "modal bottom-sheet") {
				div(class: "container-fluid") {
					div(class: "row"){
						div(class: "col l12 m12 s12") {
							h5() {
								a1(href: pinfo["website"], text: pinfo["name_provider"], class: "truncate", attr:{target:"_blank"});
							}
							div() {
								a1(href: nhost+pinfo["username"], text: "Business Card", class: "truncate", attr:{});
							}
						}
						// div(class: "col l4 m4 s12") {
						// 	h5(class: "grey-text text-darken-2") {
						// 		print("");
						// 		icon(name: "navigation", aclass: "tiny");
						// 	}
						// 	div(class: "grey-text") {
						// 		print(pinfo["address"]);
						// 	}
						// }
						// div(class: "col l4 m4 s12") {
						// 	h5(class: "grey-text text-darken-2") {
						// 		print("");
						// 		icon(name: "call", aclass: "tiny");
						// 	}
						// 	div(class: "grey-text") {
						// 		print(pinfo["phone"]);
						// 	}
						// }
						// div(class: "col l3 m3 s12") {
						// 	button(class: "waves-effect waves-light btn", data:{onclick: "addfav", pid: i}) {
						// 		print("Favorute");
						// 	}
						// }


						div(class: "col l4 m4 s12") {
							div(class: "grey-text text-darken-2 p5") {
								icon(name: "navigation", aclass: "tiny");
								print(pinfo["address"]);
							}
						}
						div(class: "col l4 m4 s12") {
							div(class: "grey-text text-darken-2 p5") {
								icon(name: "call", aclass: "tiny");
								print(pinfo["phone"]);
							}
						}
						div(class: "col l3 m3 s12") {
							button(class: "waves-effect waves-light btn", data:{onclick: "addfav", pid: i}) {
								print("Favorute");
							}
						}

						div(class: "col l12 m12 s12") {
							print(provider2[i]["mycats"]);
						}
					}
				}
			}
		}
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
					input1(label: "Provider's Email", id: "form_email");
					input1(label: "Provider's Phone", id: "form_phone");
					input1(label: "Provider's Address", id: "form_address", aclass: "col l12");
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
}

