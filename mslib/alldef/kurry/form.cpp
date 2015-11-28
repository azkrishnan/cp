define main1(css:[], js:[], bodystyle:{}, htmlstyle:{}, title: "KurryBox") {
	js = ["js/main.js"] + js;
	main(title: title, css: css, js:js, bodystyle:bodystyle, htmlstyle: htmlstyle) {
		innerHTML();
//		loginmodal();
	}
}


define main2(css:[], js:[], bodystyle:{}, htmlstyle:{}, title: "KurryBox") {
	js = ["js/main.js"] + js;
	main(title: title, css: css, js:js, bodystyle:bodystyle, htmlstyle: htmlstyle, acss: ["css/materialize.min.css", "css/lib.css", 'css/materialize.min.css', 'css/custom-stylesheet.css', 'css/jquery.bxslider.css', 'mslib/css/gfont.css', 'css/lib.css', 'css/main.css', 'css/style.css']) {
		innerHTML();
		loginmodal();
	}
}



define bigsearch() {
	div(class: "row", style: {"background-color":""}) {
		div(class: "col l1 m1") {
			p("&nbsp;");
		}
		div(class: "col m8 s12 l9", style:{"padding": "0px", "margin": "0px"}) {
			input(attr:{placeholder: ph, id: id, autofocus: autofocus}, class:"bigsearch definput", style:{"border-radius": "0px"});
		}
		div(class: "col m2 s12 l1 ", style:{"padding": "0px", "margin": "0px"}) {
			button(class: "bigsearchbutton waves-effect waves-light btn", style:{"border-radius": "0px"}, attr:{type:"submit"}) {
				p("Go");
				icon(name: "send", aclass: "right");
			}
		}
	}
}

define header4() {
	if(islogin == None) {
		header2(tablink:["", "", BASE+"chefjoin"], tabname:["Our Story", "Blog", "Be a Chef"]);
	} elif (islogin == "u") {
		header2_user(tablink:[HOST, "", "", BASE+"cart"], tabname:["Home", "Our Story", "Blog", "Cart"]);
	} elif (islogin == "a") {
		header2_admin(tablink:[HOST, "", "", "", "", ""], tabname:["Home", "Our Story", "Blog"]);
	} elif (islogin == "c") {
		header2_chef(tablink:[HOST, "", "", "", "", ""], tabname:["Home", "Our Story", "Blog"]);
	}
}


define header3(tabname:[], tablink:[]) {
	div(class: "navbar-fixed ") {
		nav(class:"white", attr:{role: "container"}) {
			div(class: "nav-wrapper container") {
				a(attr:{id: "logo-container", href: BASE}, class: "brand-logo") {
					img(attr:{src: "photo/mylogo1.png"}, class: "circle responsive-img", style:{"vertical-align": "middle"});
				}
				ul(class: "right hide-on-med-and-down" ) {
					li() {
						a(class: "dropdown-button", attr:{"data-activates": "dropdown2"}) {
							p("&nbsp;"*10+"Today, 28th Oct"+"&nbsp;"*10);
						}
					}
					li() {
						a(class: "dropdown-button", attr:{"data-activates": "dropdown1"}) {
							p("&nbsp;"*5+"All"+"&nbsp;"*20);
						}
					}
					disptabs(tabname: tabname, tablink: tablink);
				}
			}
		}
		ul(attr:{id: "dropdown1"}, class: "dropdown-content") {
			foodtype = ["All", "Veg", "Non-Veg"];
			for(i, ii, foodtype) {
				li() {
					a(attr:{href: ""}) {
						p(i);
					}
				}
			}
		}
		ul(attr:{id: "dropdown2"}, class: "dropdown-content") {
			nextdays = ["Today, 26 Oct", "27 Oct", "28 Oct"];
			for(i, ii, nextdays) {
				li() {
					a(attr:{href: ""}) {
						p(i);
					}
				}
			}
		}
	}
}

define dispfood() {
	div(class: "col s12 l4 m6 ", style:{}) {
		div(class: " card-panel", style:{"margin-bottom":"40px", "padding":"0px"}) {
			div() {
//				resimg(src: "photo/food4.jpg");
				resimg(src: dishinfo["pic"]);
			}
			div(style: {"padding-bottom": "10px"}) {
				div(style:{padding: "10px"}) {
					div(class: "row") {
						div(class: "col l8", attr:{align: "left"}) {
							div() {
								p(dishinfo["title"]);
							}
						}
						div(class: "col l4") {
							icon1(img: "photo/inr1.png");
							span(style:{"font-size": "25px", "font-weight": "600"}){
								p(dishinfo["price"]);
							}
						}
					}
					div(class: "row valign-wrapper", attr:{align: "left"}) {
						div(class: "col l2") {
							// circleimg(src: "photo/chef.jpg");
							circleimg(src: dishinfo["profilepic"]);
						}
						div(class: "col l10"){
							div(style:{"font-weight": "500"}) {
								profilea1(name:"Chef "+dishinfo["name"], uid: dishinfo["cid"]);
							}
							div() {
								starrating(val:3);
							}
						}
					}
				}
				div(class: "row") {
					if(islogin == "a" ) {
						div(class: "col l4 ") {
							button(class: "btn waves-effect waves-light btn", datas:{datetime: dishinfo["datetime"], lord: dishinfo["lord"], dishid: dishinfo["id"]}, data:{onclick: "sreq", action: "deletedisp", restext: "Deleted !"}) {
								p("Delete");
							}
						}
						div(class: "col l4 offset-l3") {
							button(class: "btn waves-effect waves-light btn") {
								p("Edit");
							}
						}
					} elif( loginid == dishinfo["cid"] ) {

					} else {
						div(class: "col l4 ") {
							button(class: "btn waves-effect waves-light btn", data:{onclick: "addfav"}, attr:{"id": "mohit"}) {
								p("Favourite");
							}
						}
						div(class: "col l4 offset-l3") {
							button(class: "btn waves-effect waves-light btn", data:{onclick: "sreq", action: "addincart", restext: "Added!"}, datas: {datetime: dishinfo["datetime"], lord: dishinfo["lord"], dishid: dishinfo["id"]}) {
								p("Add + ");
							}
						}
					}
				}
			}
		}
	}
}

define l_otp_button() {
	button(class: "btn waves-effect waves-light", attr:{type: "button"}, data:{onclick: "sreq", action: "sendotp", fobj: "$(obj).parent().parent()[0]", restext: "Re-send"}) {
		p("Send OTP");
	}
}




define loginmodal() {
	div(attr:{id: "loginmodal"}, class: "modal") {
		div(class: "modal-content container-fluid") {
			div(class: "row") {
				ul(class: "tabs") {
					disptabs(liclass: "tab col l6", tablink:["#logintab", "#signuptab"], tabname:["Login", "Signup"]);
				}
			}
			div(attr:{id: "logintab"}) {
				form(data:{onsubmit:"sreq", bobj: "", action:"login", res: "ms.reload();", errorh: "error_login"}) {
					errorbox();
					div(class: "row") {
						input1(label: "Phone number", icon: "phone", aclass: "col s12 l7 m6", id:"loginphone", dc: "phone");
						div(class: "col l4 m6") {
							l_otp_button();
						}
					}
					div(class: "row"){
						input1(label: "Password or OTP", icon: "vpn_key", aclass: "col s12 l12 m12", id: "loginpass", type: "password", dc: "password1");
					}
					div(class: "row") {
						div(class: "col") {
							button(class: "btn waves-effect waves-light", attr:{type: "submit"}) {
								p("Login");
							}
						}
					}					
				}
			}

			div(attr:{id: "signuptab"}) {
				form(data:{onsubmit:"sreq", bobj: "", action:"signup", res: "ms.reload();", errorh: "error_login"}) {
					errorbox();
					div(class: "row") {
						input1(label: "Phone number", icon: "phone", aclass: "col s12 l7 m6", id:"signupphone", dc: "phone");
						div(class: "col l4 m6") {
							l_otp_button();
						}
					}
					div(class: "row"){
						input1(label: "Choose Password", icon: "vpn_key", aclass: "col s12 l6 m6", id: "signuppass", type:"password", dc: "password1");
						input1(label: "OTP", icon: "vpn_key", aclass: "col s12 l6 m6", id: "signupotp", type: "password", dc: "otp");
					}
					div(class: "row"){
						input1(label: "Name", icon: "account_circle", aclass: "col s12 l12 m12", id: "signupname");
					}
					div(class: "row") {
						div(class: "col") {
							button(class: "btn waves-effect waves-light", attr:{type: "submit"}) {
								p("Signup");
							}
						}
					}
				}
			}

		}
	}
}


define table1(rows:[], thead:[]) {
	table(class: class) {
		thead() {
			for(i, thead) {
				th() {
					p(i);
				}
			}
		}
		tbody() {
			for(i, ii, rows) {
				tr() {
					for(j, jj, i) {
						td() {
							p(j);
						}
					}
				}
			}
		}
	}
}

define profilea1() {
	a1(name: name, href: BASE+"profile?uid="+uid);
}

define account_admin() {
	div(attr:{align: "center"}) {
		height(val: 20);
		textdiv(name: "Hey Admin,\n you are welcome", font: "20px");
		height(val: 50);
	}
	table(class: "bordered striped centered highlight") {
		thead() {
			for(i, ["UserID", "Name", "Email", "Phone", "User Type"]) {
				th() {
					p(i);
				}
			}
		}
		tbody() {
			for(i, ii, users) {
				tr() {
					for(jjj, jj, ["id", "name", "email", "phone", "typetext"]) {
						j = i[jjj];
						td() {
							if( (jjj=="name") && (i["type"] == "c") ) {
								profilea1(name:j, uid: i["id"]);
							} else {
								p(j);
							}
						}
					}
					td() {
						button1(name: (i["conf"] ? "UnBlock": "Block"), datas:{uid: i['id'], isblock: (i["conf"] != None)}, data:{onclick: "sreq", action: "blockunblock", restext: "Done!"});
					}
				}
			}
		}
	}
}


define profile_chef_top2() {
	div(class: "row valign-wrapper") {
		div(class: "col l3", attr:{align: "center"}) {
			div() {
				circleimg(src: uinfo["profilepic"]);
			}
			if(canedit) {
				form(attr:{enctype: "multipart/form-data", method: "post"}) {
					a1(name: "Upload Profile Pic", attr:{onclick: 'uploadfile(this, "profilepic");'});
				}
			}
			div() {
				textdiv(name: "Chef "+uinfo["name"], font: "25px", fontw: "500");
				div(class: "row") {
					div(class: "col l6") {
						textdiv(name:38456, fontw:600);
						textdiv(name: "Dished Delivered");
					}
					div(class: "col l6") {
						textdiv(name: 56, fontw:600);
						textdiv(name: "People reviewed");
					}
				}
			}
		}
		div(class: "col l8 offset-l1") {
			textdiv(font:"25px", name:"About "+uinfo["name"], fontw:600);
			if(canedit) {
				a1(name: "Edit", attr:{"onclick": "ms.showtextarea(this);"});
				div(class: 'edittext', style: {display: "none"}) {
					form(data: {onsubmit:"sreq", bobj: "", action:"saveaboutinfo", res: "ms.reload();"}) {
						input(attr: {type: "hidden", name: "chefid", value: uid});
						textarea(attr:{name: "aboutus"}, class: "materialize-textarea") {
							p(uinfo["aboutus"].gchars);
						}
						button1(name: "Save", attr:{type: "submit"});
					}
				}
			}
			textdiv(font:"16px", name: uinfo["aboutus"].gchars);
			div() {
				b() {
					p("Address: ");
				}
				p(uinfo["address"]);
			}
		}

	}
}


define profile_chef() {
	div(class: "container-fluid") {
		div(class: "row") {
			div(class: "col l10 offset-l1 s10 m10 offset-s1 offset-m1") {
				profile_chef_top2();
				div(class: "msdivider");

				div(class: "container-fluid") {
					div(class: "row") {
					}
				}
				if(canedit) {
					div(class: "container-fluid") {
						div(class: "row") {
							div() {
								ul(class: "tabs") {
									disptabs(liclass: "tab col s2", tabname: ["All Dishes"]+ day5times["textl"], tablink: ["#alldishes"]+ day5times["tabkeys1"]);
								}
							}
							div(class: "") {
								div(attr:{id: "alldishes"}) {
									height(val:20);
									if(viewtype == "a") {
										button1(name: "Add a New Dish", data: {onclick: "slideform"});
										form(style: {display: "none"}, attr:{enctype: "multipart/form-data", method: "post"}) {
											div(class: "row") {
												input(attr:{type:"hidden", name: "cid", value: uid });
												input2(label: "Title of Dish", aclass: "col s12 l6 m6", id:"dishtitle");
												input2(label: "Price of Dish", aclass: "col s12 l6 m6", id:"dishprice");
												// input2(label: "Amount Limit", aclass: "col s12 l3 m6", id:"dishlimit");
											}
											div(class: "row"){
												textarea(class: "materialize-textarea", attr:{name: "descp", placeholder: "Dish Description"});
											}
											div(class: "row") {
												div(class: "file-field input-field") {
													div(class: "btn") {
														span() {
															p("Upload Image");
														}
														input(attr:{type:"file", name: "dishpic"});
													}
													div(class: "file-path-wrapper") {
														input(class: "file-path-validate", attr:{type: "text"});
													}
												}
											}
											div(class: "row") {
												div(class: "col") {
													button(class: "btn waves-effect waves-light", attr:{type: "submit", name:"adddish"}) {
														p("Add");
													}
												}
											}					
										}
									}

									div(class: "row", attr:{align: "center"}) {
										for(i, dispdata) {
											dispfood(dishinfo: i) ;
										}
									}
								}
								for(i, ii, day5times["tabkeys"]) {
									div(attr:{id: i}) {
										div(class: "row") {
											table(class: "bordered") {
												thead() {
													for(j, ["Title", "Price", "Booked For Lunch", "Booked for Dinner"]) {
														th() {
															p(j);
														}
													}
												}
												for(j, jj, dispdata) {
													tr() {
														th() {
															p((j["title"]+"").gchars);
														}
														th() {
															p(j["price"]);
														}
														th() {
															input1(label: "Plate Limit ("+j["ollimit"+ii]+" Booked)", id: "lunch_"+jj+"_"+ii, data:{dishid: j["id"], day:ii}, iclass: "numplatelimit", value: j["llimit"+ii]);
														}
														th() {
															input1(label: "Plate Limit ("+j["odlimit"+ii]+" Booked)", id: "dinner_"+jj+"_"+ii, data:{dishid: j["id"], day: ii}, iclass: "numplatelimit", value: j["dlimit"+ii]);
														}
													}
												}
											}
											div() {
												if(dispdata.len != 0) {
													button1(name: "Save", data:{action: "savedaymenu", "onclick": "sreq", params: "ms.getnumlimit("+ii+")"}, datas:{datetime: day5times["timel"][ii], cid: uid});
												}
											}
										}
									}
								}
							}
						}
					}
				}
				div(attr: {align: "center"}, style:{margin:"20px"}) {
					textdiv(name: "Dishes Serving today", font: "25px");
				}
				div(class: "row", attr:{align: "center"}) {
					for(i, dispdata) {
						if( (i["llimit0"] > 0) || (i["dlimit0"] > 0) ) {
							dispfood(dishinfo: i) ;
						}
					}
				}
			}
		}
	}
}


define select1(tlist:[], class: "browser-default", aclass: "") {//class, tlist, vlist, toptext, selected
	select(class: class+" "+aclass, name: name, attr:attr) {
		if(toptext != None) {
			option(attr:{value: ""}) {
				p(toptext);
			}
		}
		for(i, ii, tlist) {
			attrs = {};
			if (vlist != None) {
				attrs["value"] = vlist[ii];
			} else {
				attrs["value"] = (ii+1);
			}
			if( selected == ii ) {
				attrs["selected"] = "";
			}
			option(attr:attrs) {
				p(i);
			}
		}
	}
}

define select2(tlist:[], dclass: "col l3 s12 m6", class: "browser-default") {
	div(class: dclass) {
		select1(class: class, tlist: tlist, vlist: vlist, toptext: toptext, selected: selected);
	}
}

define mselect(tlist:[]) {
	for(i, ii, tlist) {
		attrs = {};
		if (vlist != None) {
			attrs["value"] = vlist[ii];
		} else {
			attrs["value"] = (ii+1);
		}
		if( selected == ii ) {
			attrs["selected"] = "";
		}
		checkbox1(label: i, id: id+"_"+ii);
	}
}


define mselect1(tlist:[]) {
	div(id: id, class: "dropdown-content p5", tlist:[]) {
		mselect(vlist:vlist, tlist: tlist, id: id);
	}
	a(class: "dropdown-button", data:{activates: id}) {
		p(label);
	}
}

define mselect2(class: "col l3 s12 m6") {
	div(class: class) {
		div(class: "mselect complexinput", data:{complexinput: "ci_checkbox"}, attr: {name: id}) {
			mselect1(id: id, tlist: tlist, label: label, selectall: selectall);
		}
	}
}


define switch1(on: "Yes", off: "No") {
	div(class: "switch") {
		label() {
			p(off);
			input(attr:{type: "checkbox", name: name});
			span(class: "lever");
			p(on);
		}
	}
}


define switch2(class: "col l3 s12 m6") {
	div(class: class) {
		div(class: "m5") {
			p(label);
			switch1(name: name);
		}
	}
}



define orderl_admin(){
	table(class: "bordered") {
		thead() {
			for(i, ["Odered At", "Delivery Date", "Chef", "User", "Dish", "Price", "Chef Address", "User Address", "Status"]) {
				th() {
					p(i);
				}
			}
		}
		tbody() {
			for(i, ii, orderl) {
				tr(class: "cartitems", datas:{ datetime: i["datetime"], cid: i["cid"], lord: i["lord"], dishid: i["dishid"]}) {
					td() {
						p(i["timetext"]);
					}
					td() {
						p(i["datetimetext"]);
					}
					td() {
						profilea1(name: i["cname"], uid: i["cid"]);
					}
					td() {
						profilea1(name: i["uname"], uid: i["uid"]);
					}
					td() {
						p(i["title"]);
					}
					td() {
						icon1(img: "photo/inr2.png");
						span(class: "itemprice") {
							p(i["price"]+'*'+i["numplate"]+"="+(i["price"]*i["numplate"]));
						}
					}
					td() {
						p("("+i["clat"]+", "+i["clng"]+")<br>"+i["caddress"]);
					}
					td() {
						p("("+i["lat"]+", "+i["lng"]+")<br>"+i["uaddress"]);
					}
					td() {
						p(i["status"]);
					}
				}
			}
		}
	}
}


define orderl_user(){
	table(class: "bordered") {
		thead() {
			for(i, ["Odered At", "Delivery Date", "Chef", "Dish", "Price", "User Address", "Status"]) {
				th() {
					p(i);
				}
			}
		}
		tbody() {
			for(i, ii, orderl) {
				tr(class: "cartitems", datas:{ datetime: i["datetime"], cid: i["cid"], lord: i["lord"], dishid: i["dishid"]}) {
					td() {
						p(i["timetext"]);
					}
					td() {
						p(i["datetimetext"]);
					}
					td() {
						profilea1(name: i["cname"], uid: i["cid"]);
					}
					td() {
						p(i["title"]);
					}
					td() {
						icon1(img: "photo/inr2.png");
						span(class: "itemprice") {
							p(i["price"]+'*'+i["numplate"]+"="+(i["price"]*i["numplate"]));
						}
					}
					td() {
						p("("+i["lat"]+", "+i["lng"]+")<br>"+i["uaddress"]);
					}
					td() {
						p(i["status"]);
					}
				}
			}
		}
	}
}


define orderl_chef(){
	table(class: "bordered") {
		thead() {
			for(i, ["Odered At", "Delivery Date", "User", "Dish", "Price", "User Address", "Status"]) {
				th() {
					p(i);
				}
			}
		}
		tbody() {
			for(i, ii, orderl) {
				tr(class: "cartitems", datas:{ datetime: i["datetime"], cid: i["cid"], lord: i["lord"], dishid: i["dishid"]}) {
					td() {
						p(i["timetext"]);
					}
					td() {
						p(i["datetimetext"]);
					}
					td() {
						profilea1(name: i["cname"], uid: i["cid"]);
					}
					td() {
						profilea1(name: i["uname"], uid: i["uid"]);
					}
					td() {
						p(i["title"]);
					}
					td() {
						icon1(img: "photo/inr2.png");
						span(class: "itemprice") {
							p(i["price"]+'*'+i["numplate"]+"="+(i["price"]*i["numplate"]));
						}
					}
					td() {
						p("("+i["clat"]+", "+i["clng"]+")<br>"+i["caddress"]);
					}
					td() {
						p("("+i["lat"]+", "+i["lng"]+")<br>"+i["uaddress"]);
					}
					td() {
						p(i["status"]);
					}
				}
			}
		}
	}
}


define orderl(utype: islogin) {
	if(utype == 'u') {
		orderl_user(orderl: orderl);
	}
	if(utype == 'c') {
		orderl_chef(orderl: orderl);
	}
	if(utype == 'a') {
		orderl_admin(orderl: orderl);
	}
}



define errorbox() {
	div(class: "row hiddenerror") {
		div(class: "col s12 l12") {
			div(class: "card-panel red white-text center errortext") {
				p("");
			}
		}
	}
}


define menu_nofood() {
	div(class: "col l12 m12 s12") {
		textdiv(name: "No chef is serving in this location. We are trying hard to serve you in this location, will let you know once this location is launched", font: "20px");
	}
}



define kurry_footer() {
	div(class: "page-footer white darken-4", style: {"margin-bottom": "0px", "padding-bottom": "0px"}) {
		div(class: "container") {
			div(class: "row", style: {"margin-bottom": "-25px"}) {
				div(class: "col s4 m4 l2") {
				}
				div(class: "col s2 m2 l3") {
					h5() {
						p("Social Media");
					}
					ul(){
						li() {
							a1(name: "Facebook", href: BASE+"aboutus");
						}
						li() {
							a1(name: "Twitter");
						}
						li() {
							a1(name: "Instagram");
						}
					}
				}
				div(class: "col s2 m2 l3") {
					h5() {
						p("Help");
					}
					ul(){
						li() {
							a1(name: "About us", href: BASE+"aboutus");
						}
						li() {
							a1(name: "Contact us");
						}
					}
				}
				div(class: "col s2 m2 l3") {
					h5() {
						p("Legal");
					}
					ul(){
						li() {
							a1(name: "T&C", href: BASE+"aboutus");
						}
						li() {
							a1(name: "Policy");
						}
					}
				}
			}
			div(class: "row"){
				div(class: "col l12 align-left ") {
					p("&copy; Copyright 2015 KurryBox");
				}
			}
		}
	}
}


// <footer class="page-footer teal darken-4" id="footer">
// 	<div class="container">
// 		<div class="row">
// 			<div class="col-sm-4 col-xs-6">
// 				<h5>getIITians</h5>
// 				<p><em>Get an IITian Tutor.<br>Any Topic! Any Time!</em></p>
// 			</div>
// 			<div class="col-sm-2 col-xs-6">
// 				<h5>Help</h5>
// 				<ul>
// 					<li><a href="http://getiitians.com/teaching/aboutus">About us</a></li>
// 					<li><a href="http://getiitians.com/teaching/contactus">Contact us</a></li>
// 				</ul>
// 			</div>
// 			<div class="col-sm-2 col-xs-6">
// 				<h5>Legal</h5>
// 				<ul>
// 					<li><a href="http://getiitians.com/teaching/privacypolicy">Privacy Policy</a></li>
// 					<li><a href="http://getiitians.com/teaching/termsofuse">Terms of Use</a></li>
// 				</ul>
// 			</div>
// 			<div class="col-sm-3 col-xs-6">
// 				<div id="images">
// 					<a href="https://www.facebook.com/getiitians">
// 						<img src="images/facebook-ribbon.png" alt="Facebook" width="30" height="60" class="tooltipped" data-toggle="tooltip" data-placement="top" title="Facebook">
// 					</a>
// 					<img src="images/twitter-ribbon.png" alt="Twitter" width="30" height="60">
// 					<img src="images/googleplus-ribbon.png" alt="Google+" width="30" height="60">
// 					<a href="mailto:mail@getiitians.com">
// 						<img src="images/email-ribbon.png" alt="Email" width="30" height="60"  class="tooltipped" data-toggle="tooltip" data-placement="top" title="info@getiitians.com">
// 					</a>
// 				</div>
// 				<ul>
// 					<li><i class="material-icons tiny">phone_iphone</i> +91 931 339 4403</li>
// 					<li><img src="images/feel-free-whatsapp.png" width="15" height="15"> +91 931 339 4403</li>
// 					<li><a  href="mailto:info@getiitians.com"><i class="material-icons tiny">mail</i> info@getiitians.com</a></li>
// 				</ul>
// 			</div>
// 		</div>
// 		<div class="row">
// 			<div class="col-xs-12 align-left footer-copyright">
// 				&copy; Copyright 2015 getIITians
// 			</div>
// 		</div>
// 	</div>
// </footer>
