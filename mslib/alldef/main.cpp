define main(acss:["css/materialize.min.css", "css/lib.css", 'css/materialize.min.css', 'css/custom-stylesheet.css', 'css/jquery.bxslider.css', 'https://fonts.googleapis.com/icon?family=Material+Icons', 'css/lib.css', 'css/main.css', 'css/style.css'], ajs:['mslib/js/jquery-2.1.1.min.js','mslib/js/materialize.min.js','mslib/js/jquery.bxslider.min.js','mslib/js/jquery.easing.1.3.js','mslib/js/jquery.raty.js','mslib/js/lib.js','mslib/js/mohit.js','mslib/js/mohitlib.js','mslib/js/main.js'], title: "Class Pundit", css:[], js:[], bodystyle:{}, htmlstyle:{}) {
	css = acss + css;
	js = ajs + js;
	p("<!DOCTYPE html>");
	html(style:htmlstyle){
		head(){
			base(attr:{href:HOST});
			title(){ p(title); }
			for(i, css) {
				link(attr:{href:i, rel:"stylesheet", type:"text/css"});
			}
		}
		body(style:bodystyle){
			innerHTML();
			script(attr:{type:"text/javascript"}) {
				p("var jsdata = " + jsdata+";");
			}
			script(attr:{type:"text/javascript"}) {
				p("var ec  = jsdata['_ec'] ;");
			}
			for(i, js) {
				script(attr:{type:"text/javascript", src:i});
			}
		}
	}
}


define disptabs(tabname: [], tablink: []) {
	for(i, j, tabname) {
		li(class: liclass) {
			isactive = ((active == tablink[j]) ? "active" : " ");
			a(attr: { href: tablink[j] }, class: isactive ) {
				p(i);
			}
		}
	}
}

define header1(tabname:[], tablink:[]) {
	div(class: "navbar-fixed ") {
		nav(class:"white", attr:{role: "container"}) {
			div(class: "nav-wrapper container") {
				a(attr:{id: "logo-container", href: HOST}, class: "brand-logo") {
					img(attr:{src: "photo/mylogo1.png"}, class: "circle responsive-img", style:{"vertical-align": "middle"});
				}
				ul(class: "right hide-on-med-and-down") {
					disptabs(tabname: tabname, tablink: tablink);
				}
			}
		}
	}
}


define header1_cp(tabname:[], tablink:[]) {
	div(class: "navbar-fixed ") {
		nav(class:"white", attr:{role: "container"}) {
			div(class: "nav-wrapper container") {
				a(attr:{id: "logo-container", href: HOST}, class: "brand-logo") {
					img(attr:{src: "photo/mylogo1.png"}, class: "circle responsive-img", style:{"vertical-align": "middle"});
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
			}
		}
	}
}

define header2(tabname:[], tablink:[], tabname1:[], tablink1: []) {
	div(class: "navbar-fixed ") {
		nav(class:"white", attr:{role: "container"}) {
			div(class: "nav-wrapper container") {
				ul(class: "left hide-on-med-and-down" ) {
					a(attr:{id: "logo-container", href: HOST}, class: "brand-logo") {
						img(attr:{src: "photo/logo4.png"}, class: "responsive-img", style:{"vertical-align": "middle"});
					}
					disptabs(tabname: tabname1, tablink: tablink1);
				}
				ul(class: "right hide-on-med-and-down" ) {
					disptabs(tabname: tabname, tablink: tablink);
					li() {
						a1(href:"#loginmodal", class: "modal-trigger", name: "Login");
					}
				}
				ul(attr:{id: "nav-mobile"}, "class": "side-nav") {
					disptabs(tabname: tabname, tablink: tablink);
				}
				a(attr:{"data-activates": "nav-mobile"}, "class": "button-collapse") {
					icon(name: "menu");
				}
			}
		}
	}
}


define header2_user(tabname:[], tablink:[]) {
	div(class: "navbar-fixed ") {

		ul(id: "dropdown1", class: "dropdown-content") {
			li() {
				a1(href: BASE+"account", name: "Account");
			}
			li() {
				a1(href: BASE+"orders", name: "Orders");
			}
			li() {
				a1(href: HOST+"?logout", name: "Logout");
			}
		}

		nav(class:"white", attr:{role: "container"}) {
			div(class: "nav-wrapper container") {
				a(attr:{id: "logo-container", href: HOST}, class: "brand-logo") {
					img(attr:{src: "photo/mylogo1.png"}, class: "circle responsive-img", style:{"vertical-align": "middle"});
				}
				ul(class: "right hide-on-med-and-down" ) {
					disptabs(tabname: tabname, tablink: tablink);
					li() {
						a1(class: "dropdown-button", name: "&nbsp;"*5+loginname+"&nbsp;"*10, data:{activates:"dropdown1"});
						//icon(name: "arrow_drop_down", aclass: "right");
					}
				}
				ul(attr:{id: "nav-mobile"}, "class": "side-nav") {
					disptabs(tabname: tabname, tablink: tablink);
				}
				a(attr:{"data-activates": "nav-mobile"}, "class": "button-collapse") {
					icon(name: "menu");
				}
			}
		}
	}
}

define header2_chef(tabname:[], tablink:[]) {
	div(class: "navbar-fixed ") {
		ul(id: "dropdown1", class: "dropdown-content") {
			li() {
				a1(href: BASE+"profile", name: "Profile");
			}
			li() {
				a1(href: BASE+"orders", name: "Orders");
			}
			li() {
				a1(href: HOST+"?logout", name: "Logout");
			}
		}

		nav(class:"white", attr:{role: "container"}) {
			div(class: "nav-wrapper container") {
				a(attr:{id: "logo-container", href: HOST}, class: "brand-logo") {
					img(attr:{src: "photo/mylogo1.png"}, class: "circle responsive-img", style:{"vertical-align": "middle"});
				}
				ul(class: "right hide-on-med-and-down" ) {
					disptabs(tabname: tabname, tablink: tablink);
					li() {
						a1(class: "dropdown-button", name: "&nbsp;"*5+"Profile"+"&nbsp;"*10, data:{activates:"dropdown1"});
						//icon(name: "arrow_drop_down", aclass: "right");
					}
				}
				ul(attr:{id: "nav-mobile"}, "class": "side-nav") {
					disptabs(tabname: tabname, tablink: tablink);
				}
				a(attr:{"data-activates": "nav-mobile"}, "class": "button-collapse") {
					icon(name: "menu");
				}
			}
		}
	}
}


define header2_admin(tabname:[], tablink:[]) {
	div(class: "navbar-fixed ") {
		ul(id: "dropdown1", class: "dropdown-content") {
			li() {
				a1(href: BASE+"account", name: "Account");
			}
			li() {
				a1(href: BASE+"orders", name: "Orders");
			}
			li() {
				a1(href: HOST+"?logout", name: "Logout");
			}
		}
		nav(class:"white", attr:{role: "container"}) {
			div(class: "nav-wrapper container") {
				a(attr:{id: "logo-container", href: HOST}, class: "brand-logo") {
					img(attr:{src: "photo/mylogo1.png"}, class: "circle responsive-img", style:{"vertical-align": "middle"});
				}
				ul(class: "right hide-on-med-and-down" ) {
					disptabs(tabname: tabname, tablink: tablink);
					li() {
						a1(class: "dropdown-button", name: "&nbsp;"*5+"Profile"+"&nbsp;"*10, data:{activates:"dropdown1"});
						//icon(name: "arrow_drop_down", aclass: "right");
					}
				}
				ul(attr:{id: "nav-mobile"}, "class": "side-nav") {
					disptabs(tabname: tabname, tablink: tablink);
				}
				a(attr:{"data-activates": "nav-mobile"}, "class": "button-collapse") {
					icon(name: "menu");
				}
			}
		}
	}
}




define icon(aclass: "") {
	i(class: "material-icons "+aclass, style: style){
		p(name);
	}
}

define icon1() {
	attr["src"] = img;
	img(attr: attr, style:{"margin-bottom": "-5px"}, class: class);
}


define checkbox1(checked: None, label:"Check", aclass:"") {
	span() {
		input(attr:{type: "checkbox", id: id, checked: checked}, class: "filled-in "+aclass, data: data);
		label(attr:{"for": id}) {
			p(label);
		}
	}
}


define bigf(font: "65px") {
	span(style:{"font-size": font, "text-shadow": "3px 3px 3px #000, 2px 2px 2px blue"}, color: color) {
		p(name);
	}
}

define bigf1(font: "40px") {
	bigf(color: color,font: font, name: name);
}


define height() {
	div(style:{height: val+"px"});
}

define resimg(aclass:"") {
	img(class: "responsive-img "+aclass, attr:{src: src}, style:{"opacity": opacity});
}

define circleimg() {
	resimg(aclass:"circle", src:src, opacity:opacity);
}

define divpedding(text:"", padding:"5px") {
	div(style:{padding: padding}, class: class){
		p(text);
		innerHTML();
	}
}


define textdiv(name:"") {
	div(style:{"font-size": font, "font-weight": fontw}, color:color, class: class, id: id){
		innerHTML();
		p(name);
	}
}

define textdiv1(font: "20px") {
	textdiv(font: font, fontw: fontw, color: color, class: class, name: name);
}

define a1() {
	attr["href"] = href;
	a(attr: attr, style: style, class: class) {
		p(name);
	}
}

define starrating(val: 5) {
	for(i, val) {
		img(attr:{src: "photo/rating4.png"}, style:{"margin": "-1px", width: "22px"});
	}
}

define input1(aclass: "col s6",  type: "text", dc: "simple") {
	div(class: "input-field "+aclass) {
		if(icon) {
			icon(name: icon, aclass: "prefix");
		}
		data["name"] = label;
		data["dc"] = dc;
		if(dname != None) {
			data["name"] = dname;
		}
		input(attr:{id: id, type:type, value: value}, class: iclass, data: data);
		label(attr:{"for": id}) {
			p(label);
		}
	}
}



define input2(aclass: "col s6",  type: "text") {
	div(class: "input-field "+aclass) {
		input(attr:{id: id, type:type, name:id}, class: iclass);
		label(attr:{"for": id}) {
			p(label);
		}
	}
}

define textarea1(aclass: "col l12 m12 s12") {
	div(class: "input-field "+aclass) {
		textarea(attr:{id: id, name:id}, class: "materialize-textarea");
		label(attr:{"for": id}) {
			p(label);
		}
	}
}

define button1(aclass: "" ) {
	button(class: "btn waves-effect waves-light btn "+aclass, data: data, attr: attr, datas: datas) {
		p(name);
	}
}


