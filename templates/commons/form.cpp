define main_cp(css:[], js:[], bodystyle:{}, htmlstyle:{}, title: "Class Pundit") {
	js = ["js/main.js"] + js;
	main(title: title, css: css, js:js, bodystyle:bodystyle, htmlstyle: htmlstyle) {
		innerHTML();
	}
}


define header1_cp(tabname:[], tablink:[]) {
	div(class: "navbar-fixed ") {
		nav(class:"white") {
			div(class: "nav-wrapper container") {
				a(attr:{href: HOST}, class: "", style: {display: "inline-block"}) {
					img(attr:{src: "photo/logo2.png"}, class: "responsive-img", style:{"vertical-align": "middle"});
				}
				ul(class: "right hide-on-med-and-down") {
					disptabs(tabname: tabname, tablink: tablink);
					headertabs_cp();
				}
				ul(id: "nav-mobile", class: "side-nav") {
					headertabs_cp();
				}
				a(attr:{"data-activates": "nav-mobile"}, class: "button-collapse") {
					icon(name: "menu");
				}
				ul(class: "right hide-on-large-only") {
					li() {
						a1(text: "Search", attr: {onclick: '$("#searchform").openModal();'});
					}
				}
			}
		}
	}
}


define cp_contactus_form() {
	div(class: "row") {
		div(class: "col s12 l12 m12") {
			h3(class: "grey-text text-darken-4") {
				print("Contact US");
			}
		}
		// div(class: "col s12 l6 m6") {
		// 	h5(class: "grey-text text-darken-2") {
		// 		print("Address");
		// 		icon(name: "navigation", aclass: "tiny");
		// 	}
		// 	div(class: "grey-text") {
		// 		print("58/1 2nd Floor,<br> Kalu Sarai<br>  Near Hauz Khas Metro Station<br> New Delhi - 110016<br>India");
		// 	}
		// }
		div(class: "col s12 l12 m12") {
			h5(class: "grey-text text-darken-2") {
				print("Mail");
				icon(name: "mail", aclass: "tiny");
			}
			div(class: "grey-text") {
				print("info@classpundit.com");
			}
			// h5(class: "grey-text text-darken-2") {
			// 	print("Call");
			// 	icon(name: "call", aclass: "tiny");
			// }
			// div(class: "grey-text") {
			// 	print("+91 750 375 9053");
			// }
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
		a1(text: "Favorites", attr:{onclick: '$("#myfavlist").openModal();'});
	}
	li() {
		a1(text: "Contact Us", attr:{onclick: '$("#contactusform").openModal();'});
	}
	li() {
		a1(text: "Our Story", attr:{onclick: '$("#ourstory").openModal();'});
	}
	li() {
		a1(text: "Suggest a Provider", attr:{onclick: '$("#providerform").openModal();'});
	}
}


define cp_filtertags(typ: "") {
	div(style:{"padding": "8px", "margin-bottom": "4px"}, class: "card-panel") {
		input(attr:{placeholder: "Search by address (Street, City, ZIP, etc)", autofocus: "true"}, "class": "inputplaceholder mainsearch", style:{"border-radius":"0px", "border": "solid black 0px", "font-size": "13px"}, "id": "searchloc"+typ);
	}
	div(style:{"margin-top": "0px", "padding": "8px", "margin-bottom": "-5px"}, class: "card-panel") {
		form(data: {onsubmit: "sreq", bobj: "", params: "ms.searchparam();", action: "search", res: "ms.f1(data);" }) {
			input(attr:{placeholder: "Search using keywords (Eg: Piano)", name: "keyw"}, "class": "inputplaceholder mainsearch", style:{"border-radius":"0px", "border": "solid black 0px", "font-size": "13px"});
			button(attr: {type: "submit"}, style: {display: "none"});
		}
	}
	div(style: {"max-height": "400px", "overflow-y": "auto"}) {
		ul(class: "collapsible", attr:{"data-collapsible": "accordion"}, style: {"margin-bottom": "0px"}) {
			for(i, catgtree) {
				li() {
					div(class: "collapsible-header") {
						icon1(img: icons[i]);
						print(dictl['tabs'][i]['tabs']);
					}
					div(class: "collapsible-body") {
						div(class: "subcats1", style:{padding: "5px", "padding-left":"20px", "padding-bottom":"0px", "padding-top": "0px" }) {
							ul(class: "collapsible_sub", attr:{"data-collapsible": "accordion"}) {
								for(j, catgtree[i]) {
									li(class: "") {
										div(class: "collapsible-header", style:{"border-bottom": "solid black 0px", "border-top": "1px solid #DDD"}) {
											print(dictl["cat"][j]['cat']);
										}
										div(class: "collapsible-body") {
											div(class: "subcats2", style:{"padding-left": "30px"}) {
												ul() {
													li() {
														div() {
															checkbox1(label: "Select All", id: "catsubcat"+i+"_"+j+"_"+"selectall"+typ, aclass:"selectall", data:{onclick:"selectall redraw", catgtid: i+"_"+j}, labels:{"font-size": "12px"});
														}
													}
													for(k, catgtree[i][j]) {
														li() {
															div() {
																checkbox1(label: dictl['subcat'][k]['subcat'], id: "catsubcat"+i+"_"+j+"_"+k+typ, data:{catgtid: i+"_"+j+"_"+k, onclick:"redraw"}, labels:{"font-size": "12px"});
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
			// div(style: {"background-color": "white", padding: "5px"}) {
			// 	a1(text: "See all classes", attr:{onclick: '$("#commoncats").openModal();'});
			// }
		}
	}
}


define cp_filterform() {
	div(class: "row") {
		div("class": "col l11 s11 m11", id: "mainfilter") {
			cp_filtertags();
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



define businesscard() {
	div(attr:{id: "providerinfo"}, class: "modal bottom-sheet") {
		div(class: "container-fluid") {
			div(class: "row"){
				div(class: "col l4 m12 s12") {
					h5() {
						a1(class: "truncate info_name", attr:{target:"_blank"}, text: "New Age Pet");
					}
					div(class: "grey-text text-darken-2 p5") {
						icon(name: "navigation", aclass: "tiny");
						span(class: "info_address") {
							print("C-15, Aravali hostel, IITD");
						}
					}
					div(class: "grey-text text-darken-2 p5") {
						icon(name: "navigation", aclass: "tiny");
						span(class: "info_phone") {
							print("+91 7503759053");
						}
					}
				}
				div(class: "col l4 m12 s12") {
					h5() {
						a1(class: "truncate info_website", attr:{target:"_blank"}, text: "Classes Offered");
					}
					div(class: "grey-text text-darken-2 p5") {
						icon(name: "navigation", aclass: "tiny");
						span(class: "info_address") {
							print("C-15, Aravali hostel, IITD");
						}
					}
					div(class: "grey-text text-darken-2 p5") {
						icon(name: "navigation", aclass: "tiny");
						span(class: "info_address") {
							print("C-15, Aravali hostel, IITD");
						}
					}
				}
				div(class: "col l3 m12 s12") {
					br();
					div(class: "row") {
						div(class: "col s2 cursp", attr: {onclick: "bcard.prevp();"}) {
							icon(name: "skip_previous");
						}
						div(class: "col s7") {
							span(class: "info_cardnum") {
								print("Showing: 1/9");
							}
						}
						div(class: "col s2 cursp", attr: {onclick: "bcard.nextp();"}) {
							icon(name: "skip_next");
						}
					}
					button(class: "waves-effect waves-light btn") {
						print("Favorute");
					}
				}
			}
		}
	}
}

