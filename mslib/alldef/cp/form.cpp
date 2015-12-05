define cp_contactus_form() {
	div(class: "row") {
		div(class: "col s12 l12 m12") {
			h3(class: "grey-text text-darken-4") {
				print("Contact US");
			}
		}
		div(class: "col s12 l6 m6") {
			h5(class: "grey-text text-darken-2") {
				print("Address");
				icon(name: "navigation", aclass: "tiny");
			}
			div(class: "grey-text") {
				print("58/1 2nd Floor,<br> Kalu Sarai<br>  Near Hauz Khas Metro Station<br> New Delhi - 110016<br>India");
			}
		}
		div(class: "col s12 l6 m6") {
			h5(class: "grey-text text-darken-2") {
				print("Mail");
				icon(name: "mail", aclass: "tiny");
			}
			div(class: "grey-text") {
				print("mohitsaini1196@gmail.com");
			}
			h5(class: "grey-text text-darken-2") {
				print("Call");
				icon(name: "call", aclass: "tiny");
			}
			div(class: "grey-text") {
				print("+91 750 375 9053");
			}
		}
	}
}


define cp_our_story() {
	div(class: "card-content") {
		h3(class: "card-title") {
			print("Our Story");
		}
		div() {
			print(our_story_content);
		}
	}
}


define headertabs_cp() {
	li() {
		a1(text: "MyFav", attr:{onclick: '$("#myfavlist").openModal();'});
	}
	li() {
		a1(text: "Contact Us", attr:{onclick: '$("#contactusform").openModal();'});
	}
	li() {
		a1(text: "Our Story", attr:{onclick: '$("#ourstory").openModal();'});
	}
	li() {
		a1(text: "Provider Form", attr:{onclick: '$("#providerform").openModal();'});
	}
}


define cp_filterform() {
	div(class: "row") {
		div("class": "col l11 s11 m11", id: "mainfilter") {
			div(style:{"padding": "8px", "margin-bottom": "4px"}, class: "card-panel") {
				input(attr:{placeholder: "Search Location", autofocus: "true"}, "class": "inputplaceholder mainsearch", style:{"border-radius":"0px", "border": "solid black 0px", "font-size": "13px"}, "id": "searchloc");
			}
			div(style:{"margin-top": "0px", "padding": "8px", "margin-bottom": "-5px"}, class: "card-panel") {
				form(data: {onsubmit: "sreq", bobj: "", action: "search", res: "draw_points(data.data);"}) {
					input(attr:{placeholder: "Search keywords", name: "keyw"}, "class": "inputplaceholder mainsearch", style:{"border-radius":"0px", "border": "solid black 0px", "font-size": "13px"});
					button(attr: {type: "submit"}, style: {display: "none"});
				}
			}
			if(true) {
				ul(class: "collapsible", attr:{"data-collapsible": "accordion"}) {
					for(i, ii, catg) {
						li() {
							div(class: "collapsible-header") {
								icon1(img: i["icon"]);
								// icon(name: "filter_drama");
								print(i["name"]);
							}
							div(class: "collapsible-body") {
								div(class: "subcats1", style:{padding: "5px", "padding-left":"20px", "padding-bottom":"0px", "padding-top": "0px" }) {
									ul(class: "collapsible_sub", attr:{"data-collapsible": "accordion"}) {
										for(j, jj, i["child"]) {
											li(class: "") {
												div(class: "collapsible-header", style:{"border-bottom": "solid black 0px", "border-top": "1px solid #DDD"}) {
													print(j["name"]);
													// checkbox1(label: j["name"], id: "catsubcat"+ii+"_"+jj);
												}
												div(class: "collapsible-body") {
													div(class: "subcats2", style:{"padding-left": "30px"}) {
														ul() {
															li() {
																div() {
																	checkbox1(label: "Select All", id: "catsubcat"+ii+"_"+jj+"_"+"selectall", aclass:"selectall", data:{onclick:"selectall redraw", catgtid: i["id"]+"_"+j["id"]}, labels:{"font-size": "12px"});
																}
															}
															for(k, kk, j["child"]) {
																li() {
																	div() {
																		checkbox1(label: k["name"], id: "catsubcat"+ii+"_"+jj+"_"+kk, data:{catgtid: i["id"]+"_"+j["id"]+"_"+k["id"], onclick:"redraw"}, labels:{"font-size": "12px"});
																	}
																}
															}
														}
													}
												}
											}
										}
									}
								}
							}
						}
					}
					div(style: {"background-color": "white", padding: "5px"}) {
						a1(text: "See All Cats", attr:{onclick: '$("#commoncats").openModal();'});
					}
				}
			}
		}
		div(class: "col l1 s1 m1") {
			div(style:{"padding": "8px", "margin-bottom": "4px", "padding-left": "0px", "margin-left": "-20px"}) {
				icon1(img: "photo/minimize1.png", class: "pointer", attr:{onclick: 'minimaxifilter(1);'});
			}
		}
	}
}





define cp_selectallcatgs() {
	div(class: "row") {
		div(class: "col s6 l6 m6") {
			print("Select The Cats");
		}
		div(class: "col s6 l6 m6") {
			button1(name: "OK", attr:{onclick: ' $("#commoncats").closeModal();'});
		}
	}
	div(class: "row") {
		ul(class: "tabs") {
			for(i, ii, catg) {
				li(class: "tab col l4 m4 s4") {
					a1(href: "#modal"+i["name"], text: i["name"]);
				}
			}
		}
	}
	div(class: "row") {
		for(i, ii, catg) {
			div(id: "modal"+i["name"], class: "row") {
				for(j, 4) {
					div(class: "col l3 m3 s6") {
						for(k, kk, commoncats[ii][j]) {
							div() {
								checkbox1(label: k[0], id: "commoncats_"+ii+"_"+j+"_"+kk, lstyle: {"color": "black", "font-size": "20px"}, data:{onclick: "selectall"}, labels:{"color": "black"});
								div(style:{ "font-wight": 700, "font-size": "18px" }) {
									//print(k[0]);
								}
								for(l, ll, k) {
									if(ll != 0) {
										div() {
											checkbox1(label: l, id: "commoncats_"+ii+"_"+j+"_"+kk+"_"+ll, labels:{"font-size": "12px"});
										}
									}
								}
							}
						}
					}
				}
			}
		}
	}
}