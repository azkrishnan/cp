def newtag_main(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	inp["css"] = myadd(inp["acss"], inp["css"]);
	inp["js"] = myadd(inp["ajs"], inp["js"]);
	outpvar.open(htmlnode("p","<!DOCTYPE html>"));
	outpvar.close();
	outpvar.open(htmlnode("html",{"style": inp["htmlstyle"]}));
	outpvar.open(htmlnode("head",{}));
	outpvar.open(htmlnode("base",{"attr": {"href": inp["HOST"]}}));
	outpvar.close();
	outpvar.open(htmlnode("title",{}));
	outpvar.open(htmlnode("p",inp["title"]));
	outpvar.close();
	outpvar.close();
	for i in forlist(inp["css"]) :
		outpvar.open(htmlnode("link",{"attr": {"href": i, "rel": "stylesheet", "type": "text/css"}}));
		outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("body",{"style": inp["bodystyle"]}));
	outpvar.cur.addfcdata("innerHTML");
	outpvar.addchilds(newtag_innerHTML({}, outpvar.cur.fcalldata["innerHTML"].root.content).root.content);
	outpvar.open(htmlnode("script",{"attr": {"type": "text/javascript"}}));
	outpvar.open(htmlnode("p",myadd(myadd("var jsdata = ", inp["jsdata"]), ";")));
	outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("script",{"attr": {"type": "text/javascript"}}));
	outpvar.open(htmlnode("p","var ec  = jsdata['_ec'] ;"));
	outpvar.close();
	outpvar.close();
	for i in forlist(inp["js"]) :
		outpvar.open(htmlnode("script",{"attr": {"type": "text/javascript", "src": i}}));
		outpvar.close();
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_disptabs(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	for j in forlist(inp["tabname"]) :
		i = inp["tabname"][j];
		outpvar.open(htmlnode("li",{"class": inp["liclass"]}));
		inp["isactive"] = ("active" if ((inp["active"]==inp["tablink"][j])) else " ");
		outpvar.open(htmlnode("a",{"attr": {"href": inp["tablink"][j]}, "class": inp["isactive"]}));
		outpvar.open(htmlnode("p",i));
		outpvar.close();
		outpvar.close();
		outpvar.close();
	return outpvar;
  
def newtag_header1(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("div",{"class": "navbar-fixed "}));
	outpvar.open(htmlnode("nav",{"class": "white", "attr": {"role": "container"}}));
	outpvar.open(htmlnode("div",{"class": "nav-wrapper container"}));
	outpvar.open(htmlnode("a",{"attr": {"id": "logo-container", "href": inp["HOST"]}, "class": "brand-logo"}));
	outpvar.open(htmlnode("img",{"attr": {"src": "photo/mylogo1.png"}, "class": "circle responsive-img", "style": {"vertical-align": "middle"}}));
	outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("ul",{"class": "right hide-on-med-and-down"}));
	outpvar.cur.addfcdata("disptabs");
	outpvar.addchilds(newtag_disptabs({"tabname": inp["tabname"], "tablink": inp["tablink"]}, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
	outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_header1_cp(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("div",{"class": "navbar-fixed "}));
	outpvar.open(htmlnode("nav",{"class": "white", "attr": {"role": "container"}}));
	outpvar.open(htmlnode("div",{"class": "nav-wrapper container"}));
	outpvar.open(htmlnode("a",{"attr": {"id": "logo-container", "href": inp["HOST"]}, "class": "brand-logo"}));
	outpvar.open(htmlnode("img",{"attr": {"src": "photo/mylogo1.png"}, "class": "circle responsive-img", "style": {"vertical-align": "middle"}}));
	outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("ul",{"class": "right hide-on-med-and-down"}));
	outpvar.cur.addfcdata("disptabs");
	outpvar.addchilds(newtag_disptabs({"tabname": inp["tabname"], "tablink": inp["tablink"]}, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
	outpvar.cur.addfcdata("headertabs_cp");
	outpvar.addchilds(newtag_headertabs_cp({}, outpvar.cur.fcalldata["headertabs_cp"].root.content).root.content);
	outpvar.close();
	outpvar.open(htmlnode("ul",{"id": "nav-mobile", "class": "side-nav"}));
	outpvar.cur.addfcdata("headertabs_cp");
	outpvar.addchilds(newtag_headertabs_cp({}, outpvar.cur.fcalldata["headertabs_cp"].root.content).root.content);
	outpvar.close();
	outpvar.open(htmlnode("a",{"attr": {"data-activates": "nav-mobile"}, "class": "button-collapse"}));
	outpvar.cur.addfcdata("icon");
	outpvar.addchilds(newtag_icon({"name": "menu"}, outpvar.cur.fcalldata["icon"].root.content).root.content);
	outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_header2(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("div",{"class": "navbar-fixed "}));
	outpvar.open(htmlnode("nav",{"class": "white", "attr": {"role": "container"}}));
	outpvar.open(htmlnode("div",{"class": "nav-wrapper container"}));
	outpvar.open(htmlnode("ul",{"class": "left hide-on-med-and-down"}));
	outpvar.open(htmlnode("a",{"attr": {"id": "logo-container", "href": inp["HOST"]}, "class": "brand-logo"}));
	outpvar.open(htmlnode("img",{"attr": {"src": "photo/logo4.png"}, "class": "responsive-img", "style": {"vertical-align": "middle"}}));
	outpvar.close();
	outpvar.close();
	outpvar.cur.addfcdata("disptabs");
	outpvar.addchilds(newtag_disptabs({"tabname": inp["tabname1"], "tablink": inp["tablink1"]}, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
	outpvar.close();
	outpvar.open(htmlnode("ul",{"class": "right hide-on-med-and-down"}));
	outpvar.cur.addfcdata("disptabs");
	outpvar.addchilds(newtag_disptabs({"tabname": inp["tabname"], "tablink": inp["tablink"]}, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
	outpvar.open(htmlnode("li",{}));
	outpvar.cur.addfcdata("a1");
	outpvar.addchilds(newtag_a1({"href": "#loginmodal", "class": "modal-trigger", "name": "Login"}, outpvar.cur.fcalldata["a1"].root.content).root.content);
	outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("ul",{"attr": {"id": "nav-mobile"}, "class": "side-nav"}));
	outpvar.cur.addfcdata("disptabs");
	outpvar.addchilds(newtag_disptabs({"tabname": inp["tabname"], "tablink": inp["tablink"]}, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
	outpvar.close();
	outpvar.open(htmlnode("a",{"attr": {"data-activates": "nav-mobile"}, "class": "button-collapse"}));
	outpvar.cur.addfcdata("icon");
	outpvar.addchilds(newtag_icon({"name": "menu"}, outpvar.cur.fcalldata["icon"].root.content).root.content);
	outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_header2_user(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("div",{"class": "navbar-fixed "}));
	outpvar.open(htmlnode("ul",{"id": "dropdown1", "class": "dropdown-content"}));
	outpvar.open(htmlnode("li",{}));
	outpvar.cur.addfcdata("a1");
	outpvar.addchilds(newtag_a1({"href": myadd(inp["BASE"], "account"), "name": "Account"}, outpvar.cur.fcalldata["a1"].root.content).root.content);
	outpvar.close();
	outpvar.open(htmlnode("li",{}));
	outpvar.cur.addfcdata("a1");
	outpvar.addchilds(newtag_a1({"href": myadd(inp["BASE"], "orders"), "name": "Orders"}, outpvar.cur.fcalldata["a1"].root.content).root.content);
	outpvar.close();
	outpvar.open(htmlnode("li",{}));
	outpvar.cur.addfcdata("a1");
	outpvar.addchilds(newtag_a1({"href": myadd(inp["HOST"], "?logout"), "name": "Logout"}, outpvar.cur.fcalldata["a1"].root.content).root.content);
	outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("nav",{"class": "white", "attr": {"role": "container"}}));
	outpvar.open(htmlnode("div",{"class": "nav-wrapper container"}));
	outpvar.open(htmlnode("a",{"attr": {"id": "logo-container", "href": inp["HOST"]}, "class": "brand-logo"}));
	outpvar.open(htmlnode("img",{"attr": {"src": "photo/mylogo1.png"}, "class": "circle responsive-img", "style": {"vertical-align": "middle"}}));
	outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("ul",{"class": "right hide-on-med-and-down"}));
	outpvar.cur.addfcdata("disptabs");
	outpvar.addchilds(newtag_disptabs({"tabname": inp["tabname"], "tablink": inp["tablink"]}, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
	outpvar.open(htmlnode("li",{}));
	outpvar.cur.addfcdata("a1");
	outpvar.addchilds(newtag_a1({"class": "dropdown-button", "name": myadd(myadd(("&nbsp;"*5), inp["loginname"]), ("&nbsp;"*10)), "data": {"activates": "dropdown1"}}, outpvar.cur.fcalldata["a1"].root.content).root.content);
	outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("ul",{"attr": {"id": "nav-mobile"}, "class": "side-nav"}));
	outpvar.cur.addfcdata("disptabs");
	outpvar.addchilds(newtag_disptabs({"tabname": inp["tabname"], "tablink": inp["tablink"]}, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
	outpvar.close();
	outpvar.open(htmlnode("a",{"attr": {"data-activates": "nav-mobile"}, "class": "button-collapse"}));
	outpvar.cur.addfcdata("icon");
	outpvar.addchilds(newtag_icon({"name": "menu"}, outpvar.cur.fcalldata["icon"].root.content).root.content);
	outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_header2_chef(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("div",{"class": "navbar-fixed "}));
	outpvar.open(htmlnode("ul",{"id": "dropdown1", "class": "dropdown-content"}));
	outpvar.open(htmlnode("li",{}));
	outpvar.cur.addfcdata("a1");
	outpvar.addchilds(newtag_a1({"href": myadd(inp["BASE"], "profile"), "name": "Profile"}, outpvar.cur.fcalldata["a1"].root.content).root.content);
	outpvar.close();
	outpvar.open(htmlnode("li",{}));
	outpvar.cur.addfcdata("a1");
	outpvar.addchilds(newtag_a1({"href": myadd(inp["BASE"], "orders"), "name": "Orders"}, outpvar.cur.fcalldata["a1"].root.content).root.content);
	outpvar.close();
	outpvar.open(htmlnode("li",{}));
	outpvar.cur.addfcdata("a1");
	outpvar.addchilds(newtag_a1({"href": myadd(inp["HOST"], "?logout"), "name": "Logout"}, outpvar.cur.fcalldata["a1"].root.content).root.content);
	outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("nav",{"class": "white", "attr": {"role": "container"}}));
	outpvar.open(htmlnode("div",{"class": "nav-wrapper container"}));
	outpvar.open(htmlnode("a",{"attr": {"id": "logo-container", "href": inp["HOST"]}, "class": "brand-logo"}));
	outpvar.open(htmlnode("img",{"attr": {"src": "photo/mylogo1.png"}, "class": "circle responsive-img", "style": {"vertical-align": "middle"}}));
	outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("ul",{"class": "right hide-on-med-and-down"}));
	outpvar.cur.addfcdata("disptabs");
	outpvar.addchilds(newtag_disptabs({"tabname": inp["tabname"], "tablink": inp["tablink"]}, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
	outpvar.open(htmlnode("li",{}));
	outpvar.cur.addfcdata("a1");
	outpvar.addchilds(newtag_a1({"class": "dropdown-button", "name": myadd(myadd(("&nbsp;"*5), "Profile"), ("&nbsp;"*10)), "data": {"activates": "dropdown1"}}, outpvar.cur.fcalldata["a1"].root.content).root.content);
	outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("ul",{"attr": {"id": "nav-mobile"}, "class": "side-nav"}));
	outpvar.cur.addfcdata("disptabs");
	outpvar.addchilds(newtag_disptabs({"tabname": inp["tabname"], "tablink": inp["tablink"]}, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
	outpvar.close();
	outpvar.open(htmlnode("a",{"attr": {"data-activates": "nav-mobile"}, "class": "button-collapse"}));
	outpvar.cur.addfcdata("icon");
	outpvar.addchilds(newtag_icon({"name": "menu"}, outpvar.cur.fcalldata["icon"].root.content).root.content);
	outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_header2_admin(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("div",{"class": "navbar-fixed "}));
	outpvar.open(htmlnode("ul",{"id": "dropdown1", "class": "dropdown-content"}));
	outpvar.open(htmlnode("li",{}));
	outpvar.cur.addfcdata("a1");
	outpvar.addchilds(newtag_a1({"href": myadd(inp["BASE"], "account"), "name": "Account"}, outpvar.cur.fcalldata["a1"].root.content).root.content);
	outpvar.close();
	outpvar.open(htmlnode("li",{}));
	outpvar.cur.addfcdata("a1");
	outpvar.addchilds(newtag_a1({"href": myadd(inp["BASE"], "orders"), "name": "Orders"}, outpvar.cur.fcalldata["a1"].root.content).root.content);
	outpvar.close();
	outpvar.open(htmlnode("li",{}));
	outpvar.cur.addfcdata("a1");
	outpvar.addchilds(newtag_a1({"href": myadd(inp["HOST"], "?logout"), "name": "Logout"}, outpvar.cur.fcalldata["a1"].root.content).root.content);
	outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("nav",{"class": "white", "attr": {"role": "container"}}));
	outpvar.open(htmlnode("div",{"class": "nav-wrapper container"}));
	outpvar.open(htmlnode("a",{"attr": {"id": "logo-container", "href": inp["HOST"]}, "class": "brand-logo"}));
	outpvar.open(htmlnode("img",{"attr": {"src": "photo/mylogo1.png"}, "class": "circle responsive-img", "style": {"vertical-align": "middle"}}));
	outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("ul",{"class": "right hide-on-med-and-down"}));
	outpvar.cur.addfcdata("disptabs");
	outpvar.addchilds(newtag_disptabs({"tabname": inp["tabname"], "tablink": inp["tablink"]}, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
	outpvar.open(htmlnode("li",{}));
	outpvar.cur.addfcdata("a1");
	outpvar.addchilds(newtag_a1({"class": "dropdown-button", "name": myadd(myadd(("&nbsp;"*5), "Profile"), ("&nbsp;"*10)), "data": {"activates": "dropdown1"}}, outpvar.cur.fcalldata["a1"].root.content).root.content);
	outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("ul",{"attr": {"id": "nav-mobile"}, "class": "side-nav"}));
	outpvar.cur.addfcdata("disptabs");
	outpvar.addchilds(newtag_disptabs({"tabname": inp["tabname"], "tablink": inp["tablink"]}, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
	outpvar.close();
	outpvar.open(htmlnode("a",{"attr": {"data-activates": "nav-mobile"}, "class": "button-collapse"}));
	outpvar.cur.addfcdata("icon");
	outpvar.addchilds(newtag_icon({"name": "menu"}, outpvar.cur.fcalldata["icon"].root.content).root.content);
	outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_icon(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("i",{"class": myadd("material-icons ", inp["aclass"]), "style": inp["style"]}));
	outpvar.open(htmlnode("p",inp["name"]));
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_icon1(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	inp["attr"]["src"] = inp["img"];
	outpvar.open(htmlnode("img",{"attr": inp["attr"], "style": {"margin-bottom": "-5px"}, "class": inp["class"]}));
	outpvar.close();
	return outpvar;
  
def newtag_checkbox1(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("span",{}));
	outpvar.open(htmlnode("input",{"attr": {"type": "checkbox", "id": inp["id"], "checked": inp["checked"]}, "class": myadd("filled-in ", inp["aclass"]), "data": inp["data"]}));
	outpvar.close();
	outpvar.open(htmlnode("label",{"attr": {"for": inp["id"]}, "style": inp["labels"]}));
	outpvar.open(htmlnode("p",inp["label"]));
	outpvar.close();
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_checkbox2(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("span",{}));
	outpvar.open(htmlnode("input",{"attr": {"type": "radio", "id": inp["id"], "checked": inp["checked"]}, "class": myadd("with-gap ", inp["aclass"]), "data": inp["data"]}));
	outpvar.close();
	outpvar.open(htmlnode("label",{"attr": {"for": inp["id"]}, "style": inp["labels"]}));
	outpvar.open(htmlnode("p",inp["label"]));
	outpvar.close();
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_bigf(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("span",{"style": {"font-size": inp["font"], "text-shadow": "3px 3px 3px #000, 2px 2px 2px blue"}, "color": inp["color"]}));
	outpvar.open(htmlnode("p",inp["name"]));
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_bigf1(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.cur.addfcdata("bigf");
	outpvar.addchilds(newtag_bigf({"color": inp["color"], "font": inp["font"], "name": inp["name"]}, outpvar.cur.fcalldata["bigf"].root.content).root.content);
	return outpvar;
  
def newtag_height(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("div",{"style": {"height": myadd(inp["val"], "px")}}));
	outpvar.close();
	return outpvar;
  
def newtag_resimg(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("img",{"class": myadd("responsive-img ", inp["aclass"]), "attr": {"src": inp["src"]}, "style": {"opacity": inp["opacity"]}}));
	outpvar.close();
	return outpvar;
  
def newtag_circleimg(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.cur.addfcdata("resimg");
	outpvar.addchilds(newtag_resimg({"aclass": "circle", "src": inp["src"], "opacity": inp["opacity"]}, outpvar.cur.fcalldata["resimg"].root.content).root.content);
	return outpvar;
  
def newtag_divpedding(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("div",{"style": {"padding": inp["padding"]}, "class": inp["class"]}));
	outpvar.open(htmlnode("p",inp["text"]));
	outpvar.close();
	outpvar.cur.addfcdata("innerHTML");
	outpvar.addchilds(newtag_innerHTML({}, outpvar.cur.fcalldata["innerHTML"].root.content).root.content);
	outpvar.close();
	return outpvar;
  
def newtag_textdiv(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("div",{"style": {"font-size": inp["font"], "font-weight": inp["fontw"]}, "color": inp["color"], "class": inp["class"], "id": inp["id"]}));
	outpvar.cur.addfcdata("innerHTML");
	outpvar.addchilds(newtag_innerHTML({}, outpvar.cur.fcalldata["innerHTML"].root.content).root.content);
	outpvar.open(htmlnode("p",inp["name"]));
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_textdiv1(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.cur.addfcdata("textdiv");
	outpvar.addchilds(newtag_textdiv({"font": inp["font"], "fontw": inp["fontw"], "color": inp["color"], "class": inp["class"], "name": inp["name"]}, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
	return outpvar;
  
def newtag_a1(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	inp["attr"]["href"] = inp["href"];
	outpvar.open(htmlnode("a",{"attr": inp["attr"], "style": inp["style"], "class": inp["class"]}));
	outpvar.open(htmlnode("p",inp["name"]));
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_starrating(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	for i in forlist(inp["val"]) :
		outpvar.open(htmlnode("img",{"attr": {"src": "photo/rating4.png"}, "style": {"margin": "-1px", "width": "22px"}}));
		outpvar.close();
	return outpvar;
  
def newtag_input1(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("div",{"class": myadd("input-field ", inp["aclass"])}));
	if (inp["icon"]): 
		outpvar.cur.addfcdata("icon");
		outpvar.addchilds(newtag_icon({"name": inp["icon"], "aclass": "prefix"}, outpvar.cur.fcalldata["icon"].root.content).root.content);
	inp["data"]["name"] = inp["label"];
	inp["data"]["dc"] = inp["dc"];
	if ((inp["dname"]!=None)): 
		inp["data"]["name"] = inp["dname"];
	outpvar.open(htmlnode("input",{"attr": {"id": inp["id"], "type": inp["type"], "value": inp["value"]}, "class": inp["iclass"], "data": inp["data"]}));
	outpvar.close();
	outpvar.open(htmlnode("label",{"attr": {"for": inp["id"]}}));
	outpvar.open(htmlnode("p",inp["label"]));
	outpvar.close();
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_input2(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("div",{"class": myadd("input-field ", inp["aclass"])}));
	outpvar.open(htmlnode("input",{"attr": {"id": inp["id"], "type": inp["type"], "name": inp["id"]}, "class": inp["iclass"]}));
	outpvar.close();
	outpvar.open(htmlnode("label",{"attr": {"for": inp["id"]}}));
	outpvar.open(htmlnode("p",inp["label"]));
	outpvar.close();
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_textarea1(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("div",{"class": myadd("input-field ", inp["aclass"])}));
	outpvar.open(htmlnode("textarea",{"attr": {"id": inp["id"], "name": inp["id"]}, "class": "materialize-textarea"}));
	outpvar.close();
	outpvar.open(htmlnode("label",{"attr": {"for": inp["id"]}}));
	outpvar.open(htmlnode("p",inp["label"]));
	outpvar.close();
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_button1(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("button",{"class": myadd("btn waves-effect waves-light btn ", inp["aclass"]), "data": inp["data"], "attr": inp["attr"], "datas": inp["datas"]}));
	outpvar.open(htmlnode("p",inp["name"]));
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_main1(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	inp["js"] = myadd(["js/main.js"], inp["js"]);
	outpvar.open(htmlnode("main",{"title": inp["title"], "css": inp["css"], "js": inp["js"], "bodystyle": inp["bodystyle"], "htmlstyle": inp["htmlstyle"]}));
	outpvar.cur.addfcdata("innerHTML");
	outpvar.addchilds(newtag_innerHTML({}, outpvar.cur.fcalldata["innerHTML"].root.content).root.content);
	outpvar.close();
	return outpvar;
  
def newtag_main2(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	inp["js"] = myadd(["js/main.js"], inp["js"]);
	outpvar.open(htmlnode("main",{"title": inp["title"], "css": inp["css"], "js": inp["js"], "bodystyle": inp["bodystyle"], "htmlstyle": inp["htmlstyle"], "acss": ["css/materialize.min.css", "css/lib.css", "css/materialize.min.css", "css/custom-stylesheet.css", "css/jquery.bxslider.css", "mslib/css/gfont.css", "css/lib.css", "css/main.css", "css/style.css"]}));
	outpvar.cur.addfcdata("innerHTML");
	outpvar.addchilds(newtag_innerHTML({}, outpvar.cur.fcalldata["innerHTML"].root.content).root.content);
	outpvar.cur.addfcdata("loginmodal");
	outpvar.addchilds(newtag_loginmodal({}, outpvar.cur.fcalldata["loginmodal"].root.content).root.content);
	outpvar.close();
	return outpvar;
  
def newtag_bigsearch(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("div",{"class": "row", "style": {"background-color": ""}}));
	outpvar.open(htmlnode("div",{"class": "col l1 m1"}));
	outpvar.open(htmlnode("p","&nbsp;"));
	outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("div",{"class": "col m8 s12 l9", "style": {"padding": "0px", "margin": "0px"}}));
	outpvar.open(htmlnode("input",{"attr": {"placeholder": inp["ph"], "id": inp["id"], "autofocus": inp["autofocus"]}, "class": "bigsearch definput", "style": {"border-radius": "0px"}}));
	outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("div",{"class": "col m2 s12 l1 ", "style": {"padding": "0px", "margin": "0px"}}));
	outpvar.open(htmlnode("button",{"class": "bigsearchbutton waves-effect waves-light btn", "style": {"border-radius": "0px"}, "attr": {"type": "submit"}}));
	outpvar.open(htmlnode("p","Go"));
	outpvar.close();
	outpvar.cur.addfcdata("icon");
	outpvar.addchilds(newtag_icon({"name": "send", "aclass": "right"}, outpvar.cur.fcalldata["icon"].root.content).root.content);
	outpvar.close();
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_header4(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	if ((inp["islogin"]==None)): 
		outpvar.cur.addfcdata("header2");
		outpvar.addchilds(newtag_header2({"tablink": ["", "", myadd(inp["BASE"], "chefjoin")], "tabname": ["Our Story", "Blog", "Be a Chef"]}, outpvar.cur.fcalldata["header2"].root.content).root.content);
	elif ((inp["islogin"]=="u")): 
		outpvar.cur.addfcdata("header2_user");
		outpvar.addchilds(newtag_header2_user({"tablink": [inp["HOST"], "", "", myadd(inp["BASE"], "cart")], "tabname": ["Home", "Our Story", "Blog", "Cart"]}, outpvar.cur.fcalldata["header2_user"].root.content).root.content);
	elif ((inp["islogin"]=="a")): 
		outpvar.cur.addfcdata("header2_admin");
		outpvar.addchilds(newtag_header2_admin({"tablink": [inp["HOST"], "", "", "", "", ""], "tabname": ["Home", "Our Story", "Blog"]}, outpvar.cur.fcalldata["header2_admin"].root.content).root.content);
	elif ((inp["islogin"]=="c")): 
		outpvar.cur.addfcdata("header2_chef");
		outpvar.addchilds(newtag_header2_chef({"tablink": [inp["HOST"], "", "", "", "", ""], "tabname": ["Home", "Our Story", "Blog"]}, outpvar.cur.fcalldata["header2_chef"].root.content).root.content);
	return outpvar;
  
def newtag_header3(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("div",{"class": "navbar-fixed "}));
	outpvar.open(htmlnode("nav",{"class": "white", "attr": {"role": "container"}}));
	outpvar.open(htmlnode("div",{"class": "nav-wrapper container"}));
	outpvar.open(htmlnode("a",{"attr": {"id": "logo-container", "href": inp["BASE"]}, "class": "brand-logo"}));
	outpvar.open(htmlnode("img",{"attr": {"src": "photo/mylogo1.png"}, "class": "circle responsive-img", "style": {"vertical-align": "middle"}}));
	outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("ul",{"class": "right hide-on-med-and-down"}));
	outpvar.open(htmlnode("li",{}));
	outpvar.open(htmlnode("a",{"class": "dropdown-button", "attr": {"data-activates": "dropdown2"}}));
	outpvar.open(htmlnode("p",myadd(myadd(("&nbsp;"*10), "Today, 28th Oct"), ("&nbsp;"*10))));
	outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("li",{}));
	outpvar.open(htmlnode("a",{"class": "dropdown-button", "attr": {"data-activates": "dropdown1"}}));
	outpvar.open(htmlnode("p",myadd(myadd(("&nbsp;"*5), "All"), ("&nbsp;"*20))));
	outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.cur.addfcdata("disptabs");
	outpvar.addchilds(newtag_disptabs({"tabname": inp["tabname"], "tablink": inp["tablink"]}, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
	outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("ul",{"attr": {"id": "dropdown1"}, "class": "dropdown-content"}));
	inp["foodtype"] = ["All", "Veg", "Non-Veg"];
	for ii in forlist(inp["foodtype"]) :
		i = inp["foodtype"][ii];
		outpvar.open(htmlnode("li",{}));
		outpvar.open(htmlnode("a",{"attr": {"href": ""}}));
		outpvar.open(htmlnode("p",i));
		outpvar.close();
		outpvar.close();
		outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("ul",{"attr": {"id": "dropdown2"}, "class": "dropdown-content"}));
	inp["nextdays"] = ["Today, 26 Oct", "27 Oct", "28 Oct"];
	for ii in forlist(inp["nextdays"]) :
		i = inp["nextdays"][ii];
		outpvar.open(htmlnode("li",{}));
		outpvar.open(htmlnode("a",{"attr": {"href": ""}}));
		outpvar.open(htmlnode("p",i));
		outpvar.close();
		outpvar.close();
		outpvar.close();
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_dispfood(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("div",{"class": "col s12 l4 m6 ", "style": {}}));
	outpvar.open(htmlnode("div",{"class": " card-panel", "style": {"margin-bottom": "40px", "padding": "0px"}}));
	outpvar.open(htmlnode("div",{}));
	outpvar.cur.addfcdata("resimg");
	outpvar.addchilds(newtag_resimg({"src": inp["dishinfo"]["pic"]}, outpvar.cur.fcalldata["resimg"].root.content).root.content);
	outpvar.close();
	outpvar.open(htmlnode("div",{"style": {"padding-bottom": "10px"}}));
	outpvar.open(htmlnode("div",{"style": {"padding": "10px"}}));
	outpvar.open(htmlnode("div",{"class": "row"}));
	outpvar.open(htmlnode("div",{"class": "col l8", "attr": {"align": "left"}}));
	outpvar.open(htmlnode("div",{}));
	outpvar.open(htmlnode("p",inp["dishinfo"]["title"]));
	outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("div",{"class": "col l4"}));
	outpvar.cur.addfcdata("icon1");
	outpvar.addchilds(newtag_icon1({"img": "photo/inr1.png"}, outpvar.cur.fcalldata["icon1"].root.content).root.content);
	outpvar.open(htmlnode("span",{"style": {"font-size": "25px", "font-weight": "600"}}));
	outpvar.open(htmlnode("p",inp["dishinfo"]["price"]));
	outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("div",{"class": "row valign-wrapper", "attr": {"align": "left"}}));
	outpvar.open(htmlnode("div",{"class": "col l2"}));
	outpvar.cur.addfcdata("circleimg");
	outpvar.addchilds(newtag_circleimg({"src": inp["dishinfo"]["profilepic"]}, outpvar.cur.fcalldata["circleimg"].root.content).root.content);
	outpvar.close();
	outpvar.open(htmlnode("div",{"class": "col l10"}));
	outpvar.open(htmlnode("div",{"style": {"font-weight": "500"}}));
	outpvar.cur.addfcdata("profilea1");
	outpvar.addchilds(newtag_profilea1({"name": myadd("Chef ", inp["dishinfo"]["name"]), "uid": inp["dishinfo"]["cid"]}, outpvar.cur.fcalldata["profilea1"].root.content).root.content);
	outpvar.close();
	outpvar.open(htmlnode("div",{}));
	outpvar.cur.addfcdata("starrating");
	outpvar.addchilds(newtag_starrating({"val": 3}, outpvar.cur.fcalldata["starrating"].root.content).root.content);
	outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("div",{"class": "row"}));
	if ((inp["islogin"]=="a")): 
		outpvar.open(htmlnode("div",{"class": "col l4 "}));
		outpvar.open(htmlnode("button",{"class": "btn waves-effect waves-light btn", "datas": {"datetime": inp["dishinfo"]["datetime"], "lord": inp["dishinfo"]["lord"], "dishid": inp["dishinfo"]["id"]}, "data": {"onclick": "sreq", "action": "deletedisp", "restext": "Deleted !"}}));
		outpvar.open(htmlnode("p","Delete"));
		outpvar.close();
		outpvar.close();
		outpvar.close();
		outpvar.open(htmlnode("div",{"class": "col l4 offset-l3"}));
		outpvar.open(htmlnode("button",{"class": "btn waves-effect waves-light btn"}));
		outpvar.open(htmlnode("p","Edit"));
		outpvar.close();
		outpvar.close();
		outpvar.close();
	elif ((inp["loginid"]==inp["dishinfo"]["cid"])): 
	elif (1): 
		outpvar.open(htmlnode("div",{"class": "col l4 "}));
		outpvar.open(htmlnode("button",{"class": "btn waves-effect waves-light btn", "data": {"onclick": "addfav"}, "attr": {"id": "mohit"}}));
		outpvar.open(htmlnode("p","Favourite"));
		outpvar.close();
		outpvar.close();
		outpvar.close();
		outpvar.open(htmlnode("div",{"class": "col l4 offset-l3"}));
		outpvar.open(htmlnode("button",{"class": "btn waves-effect waves-light btn", "data": {"onclick": "sreq", "action": "addincart", "restext": "Added!"}, "datas": {"datetime": inp["dishinfo"]["datetime"], "lord": inp["dishinfo"]["lord"], "dishid": inp["dishinfo"]["id"]}}));
		outpvar.open(htmlnode("p","Add + "));
		outpvar.close();
		outpvar.close();
		outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_l_otp_button(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("button",{"class": "btn waves-effect waves-light", "attr": {"type": "button"}, "data": {"onclick": "sreq", "action": "sendotp", "fobj": "$(obj).parent().parent()[0]", "restext": "Re-send"}}));
	outpvar.open(htmlnode("p","Send OTP"));
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_loginmodal(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("div",{"attr": {"id": "loginmodal"}, "class": "modal"}));
	outpvar.open(htmlnode("div",{"class": "modal-content container-fluid"}));
	outpvar.open(htmlnode("div",{"class": "row"}));
	outpvar.open(htmlnode("ul",{"class": "tabs"}));
	outpvar.cur.addfcdata("disptabs");
	outpvar.addchilds(newtag_disptabs({"liclass": "tab col l6", "tablink": ["#logintab", "#signuptab"], "tabname": ["Login", "Signup"]}, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
	outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("div",{"attr": {"id": "logintab"}}));
	outpvar.open(htmlnode("form",{"data": {"onsubmit": "sreq", "bobj": "", "action": "login", "res": "ms.reload();", "errorh": "error_login"}}));
	outpvar.cur.addfcdata("errorbox");
	outpvar.addchilds(newtag_errorbox({}, outpvar.cur.fcalldata["errorbox"].root.content).root.content);
	outpvar.open(htmlnode("div",{"class": "row"}));
	outpvar.cur.addfcdata("input1");
	outpvar.addchilds(newtag_input1({"label": "Phone number", "icon": "phone", "aclass": "col s12 l7 m6", "id": "loginphone", "dc": "phone"}, outpvar.cur.fcalldata["input1"].root.content).root.content);
	outpvar.open(htmlnode("div",{"class": "col l4 m6"}));
	outpvar.cur.addfcdata("l_otp_button");
	outpvar.addchilds(newtag_l_otp_button({}, outpvar.cur.fcalldata["l_otp_button"].root.content).root.content);
	outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("div",{"class": "row"}));
	outpvar.cur.addfcdata("input1");
	outpvar.addchilds(newtag_input1({"label": "Password or OTP", "icon": "vpn_key", "aclass": "col s12 l12 m12", "id": "loginpass", "type": "password", "dc": "password1"}, outpvar.cur.fcalldata["input1"].root.content).root.content);
	outpvar.close();
	outpvar.open(htmlnode("div",{"class": "row"}));
	outpvar.open(htmlnode("div",{"class": "col"}));
	outpvar.open(htmlnode("button",{"class": "btn waves-effect waves-light", "attr": {"type": "submit"}}));
	outpvar.open(htmlnode("p","Login"));
	outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("div",{"attr": {"id": "signuptab"}}));
	outpvar.open(htmlnode("form",{"data": {"onsubmit": "sreq", "bobj": "", "action": "signup", "res": "ms.reload();", "errorh": "error_login"}}));
	outpvar.cur.addfcdata("errorbox");
	outpvar.addchilds(newtag_errorbox({}, outpvar.cur.fcalldata["errorbox"].root.content).root.content);
	outpvar.open(htmlnode("div",{"class": "row"}));
	outpvar.cur.addfcdata("input1");
	outpvar.addchilds(newtag_input1({"label": "Phone number", "icon": "phone", "aclass": "col s12 l7 m6", "id": "signupphone", "dc": "phone"}, outpvar.cur.fcalldata["input1"].root.content).root.content);
	outpvar.open(htmlnode("div",{"class": "col l4 m6"}));
	outpvar.cur.addfcdata("l_otp_button");
	outpvar.addchilds(newtag_l_otp_button({}, outpvar.cur.fcalldata["l_otp_button"].root.content).root.content);
	outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("div",{"class": "row"}));
	outpvar.cur.addfcdata("input1");
	outpvar.addchilds(newtag_input1({"label": "Choose Password", "icon": "vpn_key", "aclass": "col s12 l6 m6", "id": "signuppass", "type": "password", "dc": "password1"}, outpvar.cur.fcalldata["input1"].root.content).root.content);
	outpvar.cur.addfcdata("input1");
	outpvar.addchilds(newtag_input1({"label": "OTP", "icon": "vpn_key", "aclass": "col s12 l6 m6", "id": "signupotp", "type": "password", "dc": "otp"}, outpvar.cur.fcalldata["input1"].root.content).root.content);
	outpvar.close();
	outpvar.open(htmlnode("div",{"class": "row"}));
	outpvar.cur.addfcdata("input1");
	outpvar.addchilds(newtag_input1({"label": "Name", "icon": "account_circle", "aclass": "col s12 l12 m12", "id": "signupname"}, outpvar.cur.fcalldata["input1"].root.content).root.content);
	outpvar.close();
	outpvar.open(htmlnode("div",{"class": "row"}));
	outpvar.open(htmlnode("div",{"class": "col"}));
	outpvar.open(htmlnode("button",{"class": "btn waves-effect waves-light", "attr": {"type": "submit"}}));
	outpvar.open(htmlnode("p","Signup"));
	outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_table1(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("table",{"class": inp["class"]}));
	outpvar.open(htmlnode("thead",{}));
	for i in forlist(inp["thead"]) :
		outpvar.open(htmlnode("th",{}));
		outpvar.open(htmlnode("p",i));
		outpvar.close();
		outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("tbody",{}));
	for ii in forlist(inp["rows"]) :
		i = inp["rows"][ii];
		outpvar.open(htmlnode("tr",{}));
		for jj in forlist(i) :
			j = i[jj];
			outpvar.open(htmlnode("td",{}));
			outpvar.open(htmlnode("p",j));
			outpvar.close();
			outpvar.close();
		outpvar.close();
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_profilea1(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.cur.addfcdata("a1");
	outpvar.addchilds(newtag_a1({"name": inp["name"], "href": myadd(myadd(inp["BASE"], "profile?uid="), inp["uid"])}, outpvar.cur.fcalldata["a1"].root.content).root.content);
	return outpvar;
  
def newtag_account_admin(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("div",{"attr": {"align": "center"}}));
	outpvar.cur.addfcdata("height");
	outpvar.addchilds(newtag_height({"val": 20}, outpvar.cur.fcalldata["height"].root.content).root.content);
	outpvar.cur.addfcdata("textdiv");
	outpvar.addchilds(newtag_textdiv({"name": "Hey Admin,\n you are welcome", "font": "20px"}, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
	outpvar.cur.addfcdata("height");
	outpvar.addchilds(newtag_height({"val": 50}, outpvar.cur.fcalldata["height"].root.content).root.content);
	outpvar.close();
	outpvar.open(htmlnode("table",{"class": "bordered striped centered highlight"}));
	outpvar.open(htmlnode("thead",{}));
	for i in forlist(["UserID", "Name", "Email", "Phone", "User Type"]) :
		outpvar.open(htmlnode("th",{}));
		outpvar.open(htmlnode("p",i));
		outpvar.close();
		outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("tbody",{}));
	for ii in forlist(inp["users"]) :
		i = inp["users"][ii];
		outpvar.open(htmlnode("tr",{}));
		for jj in forlist(["id", "name", "email", "phone", "typetext"]) :
			jjj = ["id", "name", "email", "phone", "typetext"][jj];
			inp["j"] = i[jjj];
			outpvar.open(htmlnode("td",{}));
			if (((jjj=="name")and(i["type"]=="c"))): 
				outpvar.cur.addfcdata("profilea1");
				outpvar.addchilds(newtag_profilea1({"name": inp["j"], "uid": i["id"]}, outpvar.cur.fcalldata["profilea1"].root.content).root.content);
			elif (1): 
				outpvar.open(htmlnode("p",inp["j"]));
				outpvar.close();
			outpvar.close();
		outpvar.open(htmlnode("td",{}));
		outpvar.cur.addfcdata("button1");
		outpvar.addchilds(newtag_button1({"name": ("UnBlock" if (i["conf"]) else "Block"), "datas": {"uid": i["id"], "isblock": (i["conf"]!=None)}, "data": {"onclick": "sreq", "action": "blockunblock", "restext": "Done!"}}, outpvar.cur.fcalldata["button1"].root.content).root.content);
		outpvar.close();
		outpvar.close();
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_profile_chef_top2(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("div",{"class": "row valign-wrapper"}));
	outpvar.open(htmlnode("div",{"class": "col l3", "attr": {"align": "center"}}));
	outpvar.open(htmlnode("div",{}));
	outpvar.cur.addfcdata("circleimg");
	outpvar.addchilds(newtag_circleimg({"src": inp["uinfo"]["profilepic"]}, outpvar.cur.fcalldata["circleimg"].root.content).root.content);
	outpvar.close();
	if (inp["canedit"]): 
		outpvar.open(htmlnode("form",{"attr": {"enctype": "multipart/form-data", "method": "post"}}));
		outpvar.cur.addfcdata("a1");
		outpvar.addchilds(newtag_a1({"name": "Upload Profile Pic", "attr": {"onclick": "uploadfile(this, \"profilepic\");"}}, outpvar.cur.fcalldata["a1"].root.content).root.content);
		outpvar.close();
	outpvar.open(htmlnode("div",{}));
	outpvar.cur.addfcdata("textdiv");
	outpvar.addchilds(newtag_textdiv({"name": myadd("Chef ", inp["uinfo"]["name"]), "font": "25px", "fontw": "500"}, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
	outpvar.open(htmlnode("div",{"class": "row"}));
	outpvar.open(htmlnode("div",{"class": "col l6"}));
	outpvar.cur.addfcdata("textdiv");
	outpvar.addchilds(newtag_textdiv({"name": 38456, "fontw": 600}, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
	outpvar.cur.addfcdata("textdiv");
	outpvar.addchilds(newtag_textdiv({"name": "Dished Delivered"}, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
	outpvar.close();
	outpvar.open(htmlnode("div",{"class": "col l6"}));
	outpvar.cur.addfcdata("textdiv");
	outpvar.addchilds(newtag_textdiv({"name": 56, "fontw": 600}, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
	outpvar.cur.addfcdata("textdiv");
	outpvar.addchilds(newtag_textdiv({"name": "People reviewed"}, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
	outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("div",{"class": "col l8 offset-l1"}));
	outpvar.cur.addfcdata("textdiv");
	outpvar.addchilds(newtag_textdiv({"font": "25px", "name": myadd("About ", inp["uinfo"]["name"]), "fontw": 600}, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
	if (inp["canedit"]): 
		outpvar.cur.addfcdata("a1");
		outpvar.addchilds(newtag_a1({"name": "Edit", "attr": {"onclick": "ms.showtextarea(this);"}}, outpvar.cur.fcalldata["a1"].root.content).root.content);
		outpvar.open(htmlnode("div",{"class": "edittext", "style": {"display": "none"}}));
		outpvar.open(htmlnode("form",{"data": {"onsubmit": "sreq", "bobj": "", "action": "saveaboutinfo", "res": "ms.reload();"}}));
		outpvar.open(htmlnode("input",{"attr": {"type": "hidden", "name": "chefid", "value": inp["uid"]}}));
		outpvar.close();
		outpvar.open(htmlnode("textarea",{"attr": {"name": "aboutus"}, "class": "materialize-textarea"}));
		outpvar.open(htmlnode("p",inp["uinfo"]["aboutus"].gchars));
		outpvar.close();
		outpvar.close();
		outpvar.cur.addfcdata("button1");
		outpvar.addchilds(newtag_button1({"name": "Save", "attr": {"type": "submit"}}, outpvar.cur.fcalldata["button1"].root.content).root.content);
		outpvar.close();
		outpvar.close();
	outpvar.cur.addfcdata("textdiv");
	outpvar.addchilds(newtag_textdiv({"font": "16px", "name": inp["uinfo"]["aboutus"].gchars}, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
	outpvar.open(htmlnode("div",{}));
	outpvar.open(htmlnode("b",{}));
	outpvar.open(htmlnode("p","Address: "));
	outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("p",inp["uinfo"]["address"]));
	outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_profile_chef(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("div",{"class": "container-fluid"}));
	outpvar.open(htmlnode("div",{"class": "row"}));
	outpvar.open(htmlnode("div",{"class": "col l10 offset-l1 s10 m10 offset-s1 offset-m1"}));
	outpvar.cur.addfcdata("profile_chef_top2");
	outpvar.addchilds(newtag_profile_chef_top2({}, outpvar.cur.fcalldata["profile_chef_top2"].root.content).root.content);
	outpvar.open(htmlnode("div",{"class": "msdivider"}));
	outpvar.close();
	outpvar.open(htmlnode("div",{"class": "container-fluid"}));
	outpvar.open(htmlnode("div",{"class": "row"}));
	outpvar.close();
	outpvar.close();
	if (inp["canedit"]): 
		outpvar.open(htmlnode("div",{"class": "container-fluid"}));
		outpvar.open(htmlnode("div",{"class": "row"}));
		outpvar.open(htmlnode("div",{}));
		outpvar.open(htmlnode("ul",{"class": "tabs"}));
		outpvar.cur.addfcdata("disptabs");
		outpvar.addchilds(newtag_disptabs({"liclass": "tab col s2", "tabname": myadd(["All Dishes"], inp["day5times"]["textl"]), "tablink": myadd(["#alldishes"], inp["day5times"]["tabkeys1"])}, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
		outpvar.close();
		outpvar.close();
		outpvar.open(htmlnode("div",{"class": ""}));
		outpvar.open(htmlnode("div",{"attr": {"id": "alldishes"}}));
		outpvar.cur.addfcdata("height");
		outpvar.addchilds(newtag_height({"val": 20}, outpvar.cur.fcalldata["height"].root.content).root.content);
		if ((inp["viewtype"]=="a")): 
			outpvar.cur.addfcdata("button1");
			outpvar.addchilds(newtag_button1({"name": "Add a New Dish", "data": {"onclick": "slideform"}}, outpvar.cur.fcalldata["button1"].root.content).root.content);
			outpvar.open(htmlnode("form",{"style": {"display": "none"}, "attr": {"enctype": "multipart/form-data", "method": "post"}}));
			outpvar.open(htmlnode("div",{"class": "row"}));
			outpvar.open(htmlnode("input",{"attr": {"type": "hidden", "name": "cid", "value": inp["uid"]}}));
			outpvar.close();
			outpvar.cur.addfcdata("input2");
			outpvar.addchilds(newtag_input2({"label": "Title of Dish", "aclass": "col s12 l6 m6", "id": "dishtitle"}, outpvar.cur.fcalldata["input2"].root.content).root.content);
			outpvar.cur.addfcdata("input2");
			outpvar.addchilds(newtag_input2({"label": "Price of Dish", "aclass": "col s12 l6 m6", "id": "dishprice"}, outpvar.cur.fcalldata["input2"].root.content).root.content);
			outpvar.close();
			outpvar.open(htmlnode("div",{"class": "row"}));
			outpvar.open(htmlnode("textarea",{"class": "materialize-textarea", "attr": {"name": "descp", "placeholder": "Dish Description"}}));
			outpvar.close();
			outpvar.close();
			outpvar.open(htmlnode("div",{"class": "row"}));
			outpvar.open(htmlnode("div",{"class": "file-field input-field"}));
			outpvar.open(htmlnode("div",{"class": "btn"}));
			outpvar.open(htmlnode("span",{}));
			outpvar.open(htmlnode("p","Upload Image"));
			outpvar.close();
			outpvar.close();
			outpvar.open(htmlnode("input",{"attr": {"type": "file", "name": "dishpic"}}));
			outpvar.close();
			outpvar.close();
			outpvar.open(htmlnode("div",{"class": "file-path-wrapper"}));
			outpvar.open(htmlnode("input",{"class": "file-path-validate", "attr": {"type": "text"}}));
			outpvar.close();
			outpvar.close();
			outpvar.close();
			outpvar.close();
			outpvar.open(htmlnode("div",{"class": "row"}));
			outpvar.open(htmlnode("div",{"class": "col"}));
			outpvar.open(htmlnode("button",{"class": "btn waves-effect waves-light", "attr": {"type": "submit", "name": "adddish"}}));
			outpvar.open(htmlnode("p","Add"));
			outpvar.close();
			outpvar.close();
			outpvar.close();
			outpvar.close();
			outpvar.close();
		outpvar.open(htmlnode("div",{"class": "row", "attr": {"align": "center"}}));
		for i in forlist(inp["dispdata"]) :
			outpvar.cur.addfcdata("dispfood");
			outpvar.addchilds(newtag_dispfood({"dishinfo": i}, outpvar.cur.fcalldata["dispfood"].root.content).root.content);
		outpvar.close();
		outpvar.close();
		for ii in forlist(inp["day5times"]["tabkeys"]) :
			i = inp["day5times"]["tabkeys"][ii];
			outpvar.open(htmlnode("div",{"attr": {"id": i}}));
			outpvar.open(htmlnode("div",{"class": "row"}));
			outpvar.open(htmlnode("table",{"class": "bordered"}));
			outpvar.open(htmlnode("thead",{}));
			for j in forlist(["Title", "Price", "Booked For Lunch", "Booked for Dinner"]) :
				outpvar.open(htmlnode("th",{}));
				outpvar.open(htmlnode("p",j));
				outpvar.close();
				outpvar.close();
			outpvar.close();
			for jj in forlist(inp["dispdata"]) :
				j = inp["dispdata"][jj];
				outpvar.open(htmlnode("tr",{}));
				outpvar.open(htmlnode("th",{}));
				outpvar.open(htmlnode("p",myadd(j["title"], "").gchars));
				outpvar.close();
				outpvar.close();
				outpvar.open(htmlnode("th",{}));
				outpvar.open(htmlnode("p",j["price"]));
				outpvar.close();
				outpvar.close();
				outpvar.open(htmlnode("th",{}));
				outpvar.cur.addfcdata("input1");
				outpvar.addchilds(newtag_input1({"label": myadd(myadd("Plate Limit (", j[myadd("ollimit", ii)]), " Booked)"), "id": myadd(myadd(myadd("lunch_", jj), "_"), ii), "data": {"dishid": j["id"], "day": ii}, "iclass": "numplatelimit", "value": j[myadd("llimit", ii)]}, outpvar.cur.fcalldata["input1"].root.content).root.content);
				outpvar.close();
				outpvar.open(htmlnode("th",{}));
				outpvar.cur.addfcdata("input1");
				outpvar.addchilds(newtag_input1({"label": myadd(myadd("Plate Limit (", j[myadd("odlimit", ii)]), " Booked)"), "id": myadd(myadd(myadd("dinner_", jj), "_"), ii), "data": {"dishid": j["id"], "day": ii}, "iclass": "numplatelimit", "value": j[myadd("dlimit", ii)]}, outpvar.cur.fcalldata["input1"].root.content).root.content);
				outpvar.close();
				outpvar.close();
			outpvar.close();
			outpvar.open(htmlnode("div",{}));
			if ((inp["dispdata"].len!=0)): 
				outpvar.cur.addfcdata("button1");
				outpvar.addchilds(newtag_button1({"name": "Save", "data": {"action": "savedaymenu", "onclick": "sreq", "params": myadd(myadd("ms.getnumlimit(", ii), ")")}, "datas": {"datetime": inp["day5times"]["timel"][ii], "cid": inp["uid"]}}, outpvar.cur.fcalldata["button1"].root.content).root.content);
			outpvar.close();
			outpvar.close();
			outpvar.close();
		outpvar.close();
		outpvar.close();
		outpvar.close();
	outpvar.open(htmlnode("div",{"attr": {"align": "center"}, "style": {"margin": "20px"}}));
	outpvar.cur.addfcdata("textdiv");
	outpvar.addchilds(newtag_textdiv({"name": "Dishes Serving today", "font": "25px"}, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
	outpvar.close();
	outpvar.open(htmlnode("div",{"class": "row", "attr": {"align": "center"}}));
	for i in forlist(inp["dispdata"]) :
		if (((i["llimit0"]>0)or(i["dlimit0"]>0))): 
			outpvar.cur.addfcdata("dispfood");
			outpvar.addchilds(newtag_dispfood({"dishinfo": i}, outpvar.cur.fcalldata["dispfood"].root.content).root.content);
	outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_select1(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("select",{"class": myadd(myadd(inp["class"], " "), inp["aclass"]), "name": inp["name"], "attr": inp["attr"]}));
	if ((inp["toptext"]!=None)): 
		outpvar.open(htmlnode("option",{"attr": {"value": ""}}));
		outpvar.open(htmlnode("p",inp["toptext"]));
		outpvar.close();
		outpvar.close();
	for ii in forlist(inp["tlist"]) :
		i = inp["tlist"][ii];
		inp["attrs"] = {};
		if ((inp["vlist"]!=None)): 
			inp["attrs"]["value"] = inp["vlist"][ii];
		elif (1): 
			inp["attrs"]["value"] = myadd(ii, 1);
		if ((inp["selected"]==ii)): 
			inp["attrs"]["selected"] = "";
		outpvar.open(htmlnode("option",{"attr": inp["attrs"]}));
		outpvar.open(htmlnode("p",i));
		outpvar.close();
		outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_select2(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("div",{"class": inp["dclass"]}));
	outpvar.cur.addfcdata("select1");
	outpvar.addchilds(newtag_select1({"class": inp["class"], "tlist": inp["tlist"], "vlist": inp["vlist"], "toptext": inp["toptext"], "selected": inp["selected"]}, outpvar.cur.fcalldata["select1"].root.content).root.content);
	outpvar.close();
	return outpvar;
  
def newtag_mselect(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	for ii in forlist(inp["tlist"]) :
		i = inp["tlist"][ii];
		inp["attrs"] = {};
		if ((inp["vlist"]!=None)): 
			inp["attrs"]["value"] = inp["vlist"][ii];
		elif (1): 
			inp["attrs"]["value"] = myadd(ii, 1);
		if ((inp["selected"]==ii)): 
			inp["attrs"]["selected"] = "";
		outpvar.cur.addfcdata("checkbox1");
		outpvar.addchilds(newtag_checkbox1({"label": i, "id": myadd(myadd(inp["id"], "_"), ii)}, outpvar.cur.fcalldata["checkbox1"].root.content).root.content);
	return outpvar;
  
def newtag_mselect1(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("div",{"id": inp["id"], "class": "dropdown-content p5", "tlist": []}));
	outpvar.cur.addfcdata("mselect");
	outpvar.addchilds(newtag_mselect({"vlist": inp["vlist"], "tlist": inp["tlist"], "id": inp["id"]}, outpvar.cur.fcalldata["mselect"].root.content).root.content);
	outpvar.close();
	outpvar.open(htmlnode("a",{"class": "dropdown-button", "data": {"activates": inp["id"]}}));
	outpvar.open(htmlnode("p",inp["label"]));
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_mselect2(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("div",{"class": inp["class"]}));
	outpvar.open(htmlnode("div",{"class": "mselect complexinput", "data": {"complexinput": "ci_checkbox"}, "attr": {"name": inp["id"]}}));
	outpvar.cur.addfcdata("mselect1");
	outpvar.addchilds(newtag_mselect1({"id": inp["id"], "tlist": inp["tlist"], "label": inp["label"], "selectall": inp["selectall"]}, outpvar.cur.fcalldata["mselect1"].root.content).root.content);
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_switch1(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("div",{"class": "switch"}));
	outpvar.open(htmlnode("label",{}));
	outpvar.open(htmlnode("p",inp["off"]));
	outpvar.close();
	outpvar.open(htmlnode("input",{"attr": {"type": "checkbox", "name": inp["name"]}}));
	outpvar.close();
	outpvar.open(htmlnode("span",{"class": "lever"}));
	outpvar.close();
	outpvar.open(htmlnode("p",inp["on"]));
	outpvar.close();
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_switch2(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("div",{"class": inp["class"]}));
	outpvar.open(htmlnode("div",{"class": "m5"}));
	outpvar.open(htmlnode("p",inp["label"]));
	outpvar.close();
	outpvar.cur.addfcdata("switch1");
	outpvar.addchilds(newtag_switch1({"name": inp["name"]}, outpvar.cur.fcalldata["switch1"].root.content).root.content);
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_orderl_admin(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("table",{"class": "bordered"}));
	outpvar.open(htmlnode("thead",{}));
	for i in forlist(["Odered At", "Delivery Date", "Chef", "User", "Dish", "Price", "Chef Address", "User Address", "Status"]) :
		outpvar.open(htmlnode("th",{}));
		outpvar.open(htmlnode("p",i));
		outpvar.close();
		outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("tbody",{}));
	for ii in forlist(inp["orderl"]) :
		i = inp["orderl"][ii];
		outpvar.open(htmlnode("tr",{"class": "cartitems", "datas": {"datetime": i["datetime"], "cid": i["cid"], "lord": i["lord"], "dishid": i["dishid"]}}));
		outpvar.open(htmlnode("td",{}));
		outpvar.open(htmlnode("p",i["timetext"]));
		outpvar.close();
		outpvar.close();
		outpvar.open(htmlnode("td",{}));
		outpvar.open(htmlnode("p",i["datetimetext"]));
		outpvar.close();
		outpvar.close();
		outpvar.open(htmlnode("td",{}));
		outpvar.cur.addfcdata("profilea1");
		outpvar.addchilds(newtag_profilea1({"name": i["cname"], "uid": i["cid"]}, outpvar.cur.fcalldata["profilea1"].root.content).root.content);
		outpvar.close();
		outpvar.open(htmlnode("td",{}));
		outpvar.cur.addfcdata("profilea1");
		outpvar.addchilds(newtag_profilea1({"name": i["uname"], "uid": i["uid"]}, outpvar.cur.fcalldata["profilea1"].root.content).root.content);
		outpvar.close();
		outpvar.open(htmlnode("td",{}));
		outpvar.open(htmlnode("p",i["title"]));
		outpvar.close();
		outpvar.close();
		outpvar.open(htmlnode("td",{}));
		outpvar.cur.addfcdata("icon1");
		outpvar.addchilds(newtag_icon1({"img": "photo/inr2.png"}, outpvar.cur.fcalldata["icon1"].root.content).root.content);
		outpvar.open(htmlnode("span",{"class": "itemprice"}));
		outpvar.open(htmlnode("p",myadd(myadd(myadd(myadd(i["price"], "*"), i["numplate"]), "="), (i["price"]*i["numplate"]))));
		outpvar.close();
		outpvar.close();
		outpvar.close();
		outpvar.open(htmlnode("td",{}));
		outpvar.open(htmlnode("p",myadd(myadd(myadd(myadd(myadd("(", i["clat"]), ", "), i["clng"]), ")<br>"), i["caddress"])));
		outpvar.close();
		outpvar.close();
		outpvar.open(htmlnode("td",{}));
		outpvar.open(htmlnode("p",myadd(myadd(myadd(myadd(myadd("(", i["lat"]), ", "), i["lng"]), ")<br>"), i["uaddress"])));
		outpvar.close();
		outpvar.close();
		outpvar.open(htmlnode("td",{}));
		outpvar.open(htmlnode("p",i["status"]));
		outpvar.close();
		outpvar.close();
		outpvar.close();
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_orderl_user(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("table",{"class": "bordered"}));
	outpvar.open(htmlnode("thead",{}));
	for i in forlist(["Odered At", "Delivery Date", "Chef", "Dish", "Price", "User Address", "Status"]) :
		outpvar.open(htmlnode("th",{}));
		outpvar.open(htmlnode("p",i));
		outpvar.close();
		outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("tbody",{}));
	for ii in forlist(inp["orderl"]) :
		i = inp["orderl"][ii];
		outpvar.open(htmlnode("tr",{"class": "cartitems", "datas": {"datetime": i["datetime"], "cid": i["cid"], "lord": i["lord"], "dishid": i["dishid"]}}));
		outpvar.open(htmlnode("td",{}));
		outpvar.open(htmlnode("p",i["timetext"]));
		outpvar.close();
		outpvar.close();
		outpvar.open(htmlnode("td",{}));
		outpvar.open(htmlnode("p",i["datetimetext"]));
		outpvar.close();
		outpvar.close();
		outpvar.open(htmlnode("td",{}));
		outpvar.cur.addfcdata("profilea1");
		outpvar.addchilds(newtag_profilea1({"name": i["cname"], "uid": i["cid"]}, outpvar.cur.fcalldata["profilea1"].root.content).root.content);
		outpvar.close();
		outpvar.open(htmlnode("td",{}));
		outpvar.open(htmlnode("p",i["title"]));
		outpvar.close();
		outpvar.close();
		outpvar.open(htmlnode("td",{}));
		outpvar.cur.addfcdata("icon1");
		outpvar.addchilds(newtag_icon1({"img": "photo/inr2.png"}, outpvar.cur.fcalldata["icon1"].root.content).root.content);
		outpvar.open(htmlnode("span",{"class": "itemprice"}));
		outpvar.open(htmlnode("p",myadd(myadd(myadd(myadd(i["price"], "*"), i["numplate"]), "="), (i["price"]*i["numplate"]))));
		outpvar.close();
		outpvar.close();
		outpvar.close();
		outpvar.open(htmlnode("td",{}));
		outpvar.open(htmlnode("p",myadd(myadd(myadd(myadd(myadd("(", i["lat"]), ", "), i["lng"]), ")<br>"), i["uaddress"])));
		outpvar.close();
		outpvar.close();
		outpvar.open(htmlnode("td",{}));
		outpvar.open(htmlnode("p",i["status"]));
		outpvar.close();
		outpvar.close();
		outpvar.close();
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_orderl_chef(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("table",{"class": "bordered"}));
	outpvar.open(htmlnode("thead",{}));
	for i in forlist(["Odered At", "Delivery Date", "User", "Dish", "Price", "User Address", "Status"]) :
		outpvar.open(htmlnode("th",{}));
		outpvar.open(htmlnode("p",i));
		outpvar.close();
		outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("tbody",{}));
	for ii in forlist(inp["orderl"]) :
		i = inp["orderl"][ii];
		outpvar.open(htmlnode("tr",{"class": "cartitems", "datas": {"datetime": i["datetime"], "cid": i["cid"], "lord": i["lord"], "dishid": i["dishid"]}}));
		outpvar.open(htmlnode("td",{}));
		outpvar.open(htmlnode("p",i["timetext"]));
		outpvar.close();
		outpvar.close();
		outpvar.open(htmlnode("td",{}));
		outpvar.open(htmlnode("p",i["datetimetext"]));
		outpvar.close();
		outpvar.close();
		outpvar.open(htmlnode("td",{}));
		outpvar.cur.addfcdata("profilea1");
		outpvar.addchilds(newtag_profilea1({"name": i["cname"], "uid": i["cid"]}, outpvar.cur.fcalldata["profilea1"].root.content).root.content);
		outpvar.close();
		outpvar.open(htmlnode("td",{}));
		outpvar.cur.addfcdata("profilea1");
		outpvar.addchilds(newtag_profilea1({"name": i["uname"], "uid": i["uid"]}, outpvar.cur.fcalldata["profilea1"].root.content).root.content);
		outpvar.close();
		outpvar.open(htmlnode("td",{}));
		outpvar.open(htmlnode("p",i["title"]));
		outpvar.close();
		outpvar.close();
		outpvar.open(htmlnode("td",{}));
		outpvar.cur.addfcdata("icon1");
		outpvar.addchilds(newtag_icon1({"img": "photo/inr2.png"}, outpvar.cur.fcalldata["icon1"].root.content).root.content);
		outpvar.open(htmlnode("span",{"class": "itemprice"}));
		outpvar.open(htmlnode("p",myadd(myadd(myadd(myadd(i["price"], "*"), i["numplate"]), "="), (i["price"]*i["numplate"]))));
		outpvar.close();
		outpvar.close();
		outpvar.close();
		outpvar.open(htmlnode("td",{}));
		outpvar.open(htmlnode("p",myadd(myadd(myadd(myadd(myadd("(", i["clat"]), ", "), i["clng"]), ")<br>"), i["caddress"])));
		outpvar.close();
		outpvar.close();
		outpvar.open(htmlnode("td",{}));
		outpvar.open(htmlnode("p",myadd(myadd(myadd(myadd(myadd("(", i["lat"]), ", "), i["lng"]), ")<br>"), i["uaddress"])));
		outpvar.close();
		outpvar.close();
		outpvar.open(htmlnode("td",{}));
		outpvar.open(htmlnode("p",i["status"]));
		outpvar.close();
		outpvar.close();
		outpvar.close();
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_orderl(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	if ((inp["utype"]=="u")): 
		outpvar.cur.addfcdata("orderl_user");
		outpvar.addchilds(newtag_orderl_user({"orderl": inp["orderl"]}, outpvar.cur.fcalldata["orderl_user"].root.content).root.content);
	if ((inp["utype"]=="c")): 
		outpvar.cur.addfcdata("orderl_chef");
		outpvar.addchilds(newtag_orderl_chef({"orderl": inp["orderl"]}, outpvar.cur.fcalldata["orderl_chef"].root.content).root.content);
	if ((inp["utype"]=="a")): 
		outpvar.cur.addfcdata("orderl_admin");
		outpvar.addchilds(newtag_orderl_admin({"orderl": inp["orderl"]}, outpvar.cur.fcalldata["orderl_admin"].root.content).root.content);
	return outpvar;
  
def newtag_errorbox(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("div",{"class": "row hiddenerror"}));
	outpvar.open(htmlnode("div",{"class": "col s12 l12"}));
	outpvar.open(htmlnode("div",{"class": "card-panel red white-text center errortext"}));
	outpvar.open(htmlnode("p",""));
	outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_menu_nofood(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("div",{"class": "col l12 m12 s12"}));
	outpvar.cur.addfcdata("textdiv");
	outpvar.addchilds(newtag_textdiv({"name": "No chef is serving in this location. We are trying hard to serve you in this location, will let you know once this location is launched", "font": "20px"}, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
	outpvar.close();
	return outpvar;
  
def newtag_kurry_footer(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("div",{"class": "page-footer white darken-4", "style": {"margin-bottom": "0px", "padding-bottom": "0px"}}));
	outpvar.open(htmlnode("div",{"class": "container"}));
	outpvar.open(htmlnode("div",{"class": "row", "style": {"margin-bottom": "-25px"}}));
	outpvar.open(htmlnode("div",{"class": "col s4 m4 l2"}));
	outpvar.close();
	outpvar.open(htmlnode("div",{"class": "col s2 m2 l3"}));
	outpvar.cur.addfcdata("h5");
	outpvar.cur.fcalldata["h5"].open(htmlnode("p","Social Media"));
	outpvar.cur.fcalldata["h5"].close();
	outpvar.addchilds(newtag_h5({}, outpvar.cur.fcalldata["h5"].root.content).root.content);
	outpvar.open(htmlnode("ul",{}));
	outpvar.open(htmlnode("li",{}));
	outpvar.cur.addfcdata("a1");
	outpvar.addchilds(newtag_a1({"name": "Facebook", "href": myadd(inp["BASE"], "aboutus")}, outpvar.cur.fcalldata["a1"].root.content).root.content);
	outpvar.close();
	outpvar.open(htmlnode("li",{}));
	outpvar.cur.addfcdata("a1");
	outpvar.addchilds(newtag_a1({"name": "Twitter"}, outpvar.cur.fcalldata["a1"].root.content).root.content);
	outpvar.close();
	outpvar.open(htmlnode("li",{}));
	outpvar.cur.addfcdata("a1");
	outpvar.addchilds(newtag_a1({"name": "Instagram"}, outpvar.cur.fcalldata["a1"].root.content).root.content);
	outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("div",{"class": "col s2 m2 l3"}));
	outpvar.cur.addfcdata("h5");
	outpvar.cur.fcalldata["h5"].open(htmlnode("p","Help"));
	outpvar.cur.fcalldata["h5"].close();
	outpvar.addchilds(newtag_h5({}, outpvar.cur.fcalldata["h5"].root.content).root.content);
	outpvar.open(htmlnode("ul",{}));
	outpvar.open(htmlnode("li",{}));
	outpvar.cur.addfcdata("a1");
	outpvar.addchilds(newtag_a1({"name": "About us", "href": myadd(inp["BASE"], "aboutus")}, outpvar.cur.fcalldata["a1"].root.content).root.content);
	outpvar.close();
	outpvar.open(htmlnode("li",{}));
	outpvar.cur.addfcdata("a1");
	outpvar.addchilds(newtag_a1({"name": "Contact us"}, outpvar.cur.fcalldata["a1"].root.content).root.content);
	outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("div",{"class": "col s2 m2 l3"}));
	outpvar.cur.addfcdata("h5");
	outpvar.cur.fcalldata["h5"].open(htmlnode("p","Legal"));
	outpvar.cur.fcalldata["h5"].close();
	outpvar.addchilds(newtag_h5({}, outpvar.cur.fcalldata["h5"].root.content).root.content);
	outpvar.open(htmlnode("ul",{}));
	outpvar.open(htmlnode("li",{}));
	outpvar.cur.addfcdata("a1");
	outpvar.addchilds(newtag_a1({"name": "T&C", "href": myadd(inp["BASE"], "aboutus")}, outpvar.cur.fcalldata["a1"].root.content).root.content);
	outpvar.close();
	outpvar.open(htmlnode("li",{}));
	outpvar.cur.addfcdata("a1");
	outpvar.addchilds(newtag_a1({"name": "Policy"}, outpvar.cur.fcalldata["a1"].root.content).root.content);
	outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("div",{"class": "row"}));
	outpvar.open(htmlnode("div",{"class": "col l12 align-left "}));
	outpvar.open(htmlnode("p","&copy; Copyright 2015 KurryBox"));
	outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_cp_contactus_form(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("div",{"class": "row"}));
	outpvar.open(htmlnode("div",{"class": "col s12 l12 m12"}));
	outpvar.cur.addfcdata("h3");
	outpvar.cur.fcalldata["h3"].open(htmlnode("p","Contact US"));
	outpvar.cur.fcalldata["h3"].close();
	outpvar.addchilds(newtag_h3({"class": "grey-text text-darken-4"}, outpvar.cur.fcalldata["h3"].root.content).root.content);
	outpvar.close();
	outpvar.open(htmlnode("div",{"class": "col s12 l6 m6"}));
	outpvar.cur.addfcdata("h5");
	outpvar.cur.fcalldata["h5"].open(htmlnode("p","Address"));
	outpvar.cur.fcalldata["h5"].close();
	outpvar.cur.fcalldata["h5"].cur.addfcdata("icon");
	outpvar.cur.fcalldata["h5"].addchilds(newtag_icon({"name": "navigation", "aclass": "tiny"}, outpvar.cur.fcalldata["h5"].cur.fcalldata["icon"].root.content).root.content);
	outpvar.addchilds(newtag_h5({"class": "grey-text text-darken-2"}, outpvar.cur.fcalldata["h5"].root.content).root.content);
	outpvar.open(htmlnode("div",{"class": "grey-text"}));
	outpvar.open(htmlnode("p","58/1 2nd Floor,<br> Kalu Sarai<br>  Near Hauz Khas Metro Station<br> New Delhi - 110016<br>India"));
	outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("div",{"class": "col s12 l6 m6"}));
	outpvar.cur.addfcdata("h5");
	outpvar.cur.fcalldata["h5"].open(htmlnode("p","Mail"));
	outpvar.cur.fcalldata["h5"].close();
	outpvar.cur.fcalldata["h5"].cur.addfcdata("icon");
	outpvar.cur.fcalldata["h5"].addchilds(newtag_icon({"name": "mail", "aclass": "tiny"}, outpvar.cur.fcalldata["h5"].cur.fcalldata["icon"].root.content).root.content);
	outpvar.addchilds(newtag_h5({"class": "grey-text text-darken-2"}, outpvar.cur.fcalldata["h5"].root.content).root.content);
	outpvar.open(htmlnode("div",{"class": "grey-text"}));
	outpvar.open(htmlnode("p","mohitsaini1196@gmail.com"));
	outpvar.close();
	outpvar.close();
	outpvar.cur.addfcdata("h5");
	outpvar.cur.fcalldata["h5"].open(htmlnode("p","Call"));
	outpvar.cur.fcalldata["h5"].close();
	outpvar.cur.fcalldata["h5"].cur.addfcdata("icon");
	outpvar.cur.fcalldata["h5"].addchilds(newtag_icon({"name": "call", "aclass": "tiny"}, outpvar.cur.fcalldata["h5"].cur.fcalldata["icon"].root.content).root.content);
	outpvar.addchilds(newtag_h5({"class": "grey-text text-darken-2"}, outpvar.cur.fcalldata["h5"].root.content).root.content);
	outpvar.open(htmlnode("div",{"class": "grey-text"}));
	outpvar.open(htmlnode("p","+91 750 375 9053"));
	outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_cp_our_story(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("div",{"class": "card-content"}));
	outpvar.cur.addfcdata("h3");
	outpvar.cur.fcalldata["h3"].open(htmlnode("p","Our Story"));
	outpvar.cur.fcalldata["h3"].close();
	outpvar.addchilds(newtag_h3({"class": "card-title"}, outpvar.cur.fcalldata["h3"].root.content).root.content);
	outpvar.open(htmlnode("div",{}));
	outpvar.open(htmlnode("p",inp["our_story_content"]));
	outpvar.close();
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_headertabs_cp(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("li",{}));
	outpvar.cur.addfcdata("a1");
	outpvar.addchilds(newtag_a1({"name": "MyFav", "attr": {"onclick": "$(\"#myfavlist\").openModal();"}}, outpvar.cur.fcalldata["a1"].root.content).root.content);
	outpvar.close();
	outpvar.open(htmlnode("li",{}));
	outpvar.cur.addfcdata("a1");
	outpvar.addchilds(newtag_a1({"name": "Contact Us", "attr": {"onclick": "$(\"#contactusform\").openModal();"}}, outpvar.cur.fcalldata["a1"].root.content).root.content);
	outpvar.close();
	outpvar.open(htmlnode("li",{}));
	outpvar.cur.addfcdata("a1");
	outpvar.addchilds(newtag_a1({"name": "Our Story", "attr": {"onclick": "$(\"#ourstory\").openModal();"}}, outpvar.cur.fcalldata["a1"].root.content).root.content);
	outpvar.close();
	outpvar.open(htmlnode("li",{}));
	outpvar.cur.addfcdata("a1");
	outpvar.addchilds(newtag_a1({"name": "Provider Form", "attr": {"onclick": "$(\"#providerform\").openModal();"}}, outpvar.cur.fcalldata["a1"].root.content).root.content);
	outpvar.close();
	return outpvar;
  
def newtag_cp_filterform(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("div",{"class": "row"}));
	outpvar.open(htmlnode("div",{"class": "col l11 s11 m11", "id": "mainfilter"}));
	outpvar.open(htmlnode("div",{"style": {"padding": "8px", "margin-bottom": "4px"}, "class": "card-panel"}));
	outpvar.open(htmlnode("input",{"attr": {"placeholder": "Search Location", "autofocus": "true"}, "class": "inputplaceholder mainsearch", "style": {"border-radius": "0px", "border": "solid black 0px", "font-size": "13px"}, "id": "searchloc"}));
	outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("div",{"style": {"margin-top": "0px", "padding": "8px", "margin-bottom": "-5px"}, "class": "card-panel"}));
	outpvar.open(htmlnode("form",{"data": {"onsubmit": "sreq", "bobj": "", "action": "search", "res": "draw_points(data.data);"}}));
	outpvar.open(htmlnode("input",{"attr": {"placeholder": "Search keywords", "name": "keyw"}, "class": "inputplaceholder mainsearch", "style": {"border-radius": "0px", "border": "solid black 0px", "font-size": "13px"}}));
	outpvar.close();
	outpvar.open(htmlnode("button",{"attr": {"type": "submit"}, "style": {"display": "none"}}));
	outpvar.close();
	outpvar.close();
	outpvar.close();
	if (1): 
		outpvar.open(htmlnode("ul",{"class": "collapsible", "attr": {"data-collapsible": "accordion"}}));
		for ii in forlist(inp["catg"]) :
			i = inp["catg"][ii];
			outpvar.open(htmlnode("li",{}));
			outpvar.open(htmlnode("div",{"class": "collapsible-header"}));
			outpvar.cur.addfcdata("icon1");
			outpvar.addchilds(newtag_icon1({"img": i["icon"]}, outpvar.cur.fcalldata["icon1"].root.content).root.content);
			outpvar.open(htmlnode("p",i["name"]));
			outpvar.close();
			outpvar.close();
			outpvar.open(htmlnode("div",{"class": "collapsible-body"}));
			outpvar.open(htmlnode("div",{"class": "subcats1", "style": {"padding": "5px", "padding-left": "20px", "padding-bottom": "0px", "padding-top": "0px"}}));
			outpvar.open(htmlnode("ul",{"class": "collapsible_sub", "attr": {"data-collapsible": "accordion"}}));
			for jj in forlist(i["child"]) :
				j = i["child"][jj];
				outpvar.open(htmlnode("li",{"class": ""}));
				outpvar.open(htmlnode("div",{"class": "collapsible-header", "style": {"border-bottom": "solid black 0px", "border-top": "1px solid #DDD"}}));
				outpvar.open(htmlnode("p",j["name"]));
				outpvar.close();
				outpvar.close();
				outpvar.open(htmlnode("div",{"class": "collapsible-body"}));
				outpvar.open(htmlnode("div",{"class": "subcats2", "style": {"padding-left": "30px"}}));
				outpvar.open(htmlnode("ul",{}));
				outpvar.open(htmlnode("li",{}));
				outpvar.open(htmlnode("div",{}));
				outpvar.cur.addfcdata("checkbox1");
				outpvar.addchilds(newtag_checkbox1({"label": "Select All", "id": myadd(myadd(myadd(myadd(myadd("catsubcat", ii), "_"), jj), "_"), "selectall"), "aclass": "selectall", "data": {"onclick": "selectall redraw", "catgtid": myadd(myadd(i["id"], "_"), j["id"])}, "labels": {"font-size": "12px"}}, outpvar.cur.fcalldata["checkbox1"].root.content).root.content);
				outpvar.close();
				outpvar.close();
				for kk in forlist(j["child"]) :
					k = j["child"][kk];
					outpvar.open(htmlnode("li",{}));
					outpvar.open(htmlnode("div",{}));
					outpvar.cur.addfcdata("checkbox1");
					outpvar.addchilds(newtag_checkbox1({"label": k["name"], "id": myadd(myadd(myadd(myadd(myadd("catsubcat", ii), "_"), jj), "_"), kk), "data": {"catgtid": myadd(myadd(myadd(myadd(i["id"], "_"), j["id"]), "_"), k["id"]), "onclick": "redraw"}, "labels": {"font-size": "12px"}}, outpvar.cur.fcalldata["checkbox1"].root.content).root.content);
					outpvar.close();
					outpvar.close();
				outpvar.close();
				outpvar.close();
				outpvar.close();
				outpvar.close();
			outpvar.close();
			outpvar.close();
			outpvar.close();
			outpvar.close();
		outpvar.open(htmlnode("div",{"style": {"background-color": "white", "padding": "5px"}}));
		outpvar.cur.addfcdata("a1");
		outpvar.addchilds(newtag_a1({"name": "See All Cats", "attr": {"onclick": "$(\"#commoncats\").openModal();"}}, outpvar.cur.fcalldata["a1"].root.content).root.content);
		outpvar.close();
		outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("div",{"class": "col l1 s1 m1"}));
	outpvar.open(htmlnode("div",{"style": {"padding": "8px", "margin-bottom": "4px", "padding-left": "0px", "margin-left": "-20px"}}));
	outpvar.cur.addfcdata("icon1");
	outpvar.addchilds(newtag_icon1({"img": "photo/minimize1.png", "class": "pointer", "attr": {"onclick": "minimaxifilter(1);"}}, outpvar.cur.fcalldata["icon1"].root.content).root.content);
	outpvar.close();
	outpvar.close();
	outpvar.close();
	return outpvar;
  
def newtag_cp_selectallcatgs(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("div",{"class": "row"}));
	outpvar.open(htmlnode("div",{"class": "col s6 l6 m6"}));
	outpvar.open(htmlnode("p","Select The Cats"));
	outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("div",{"class": "col s6 l6 m6"}));
	outpvar.cur.addfcdata("button1");
	outpvar.addchilds(newtag_button1({"name": "OK", "attr": {"onclick": " $(\"#commoncats\").closeModal();"}}, outpvar.cur.fcalldata["button1"].root.content).root.content);
	outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("div",{"class": "row"}));
	outpvar.open(htmlnode("ul",{"class": "tabs"}));
	for ii in forlist(inp["catg"]) :
		i = inp["catg"][ii];
		outpvar.open(htmlnode("li",{"class": "tab col l4 m4 s4"}));
		outpvar.cur.addfcdata("a1");
		outpvar.addchilds(newtag_a1({"href": myadd("#modal", i["name"]), "name": i["name"]}, outpvar.cur.fcalldata["a1"].root.content).root.content);
		outpvar.close();
	outpvar.close();
	outpvar.close();
	outpvar.open(htmlnode("div",{"class": "row"}));
	for ii in forlist(inp["catg"]) :
		i = inp["catg"][ii];
		outpvar.open(htmlnode("div",{"id": myadd("modal", i["name"]), "class": "row"}));
		for j in forlist(4) :
			outpvar.open(htmlnode("div",{"class": "col l3 m3 s6"}));
			for kk in forlist(inp["commoncats"][ii][j]) :
				k = inp["commoncats"][ii][j][kk];
				outpvar.open(htmlnode("div",{}));
				outpvar.cur.addfcdata("checkbox1");
				outpvar.addchilds(newtag_checkbox1({"label": k[0], "id": myadd(myadd(myadd(myadd(myadd("commoncats_", ii), "_"), j), "_"), kk), "lstyle": {"color": "black", "font-size": "20px"}, "data": {"onclick": "selectall"}, "labels": {"color": "black"}}, outpvar.cur.fcalldata["checkbox1"].root.content).root.content);
				outpvar.open(htmlnode("div",{"style": {"font-wight": 700, "font-size": "18px"}}));
				outpvar.close();
				for ll in forlist(k) :
					l = k[ll];
					if ((ll!=0)): 
						outpvar.open(htmlnode("div",{}));
						outpvar.cur.addfcdata("checkbox1");
						outpvar.addchilds(newtag_checkbox1({"label": l, "id": myadd(myadd(myadd(myadd(myadd(myadd(myadd("commoncats_", ii), "_"), j), "_"), kk), "_"), ll), "labels": {"font-size": "12px"}}, outpvar.cur.fcalldata["checkbox1"].root.content).root.content);
						outpvar.close();
				outpvar.close();
			outpvar.close();
		outpvar.close();
	outpvar.close();
	return outpvar;
  