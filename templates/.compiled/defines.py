#This code is auto generated code, don't Edit it 
def newtag_main(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({"acss": ["css/materialize.min.css", "css/lib.css", "css/materialize.min.css", "css/custom-stylesheet.css", "css/jquery.bxslider.css", "https://fonts.googleapis.com/icon?family=Material+Icons", "css/lib.css", "css/main.css", "css/style.css"], "ajs": ["mslib/js/jquery-2.1.1.min.js", "mslib/js/materialize.min.js", "mslib/js/jquery.bxslider.min.js", "mslib/js/jquery.easing.1.3.js", "mslib/js/jquery.raty.js", "mslib/js/lib.js", "mslib/js/mohit.js", "mslib/js/mohitlib.js", "mslib/js/main.js"], "title": "Class Pundit", "css": [], "js": [], "bodystyle": {}, "htmlstyle": {}}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  inp["css"] = myadd(inp["acss"], inp["css"]);
  inp["js"] = myadd(inp["ajs"], inp["js"]);
  outpvar.addtext("<!--\n\nThis code is auto generated code, don't Edit it \n-MS1.5\n\n-->");
  outpvar.addtext("<!DOCTYPE html>");
  outpvar.open(htmlnode("html", extentattrs({"style": inp["htmlstyle"]})));
  outpvar.open(htmlnode("head", extentattrs({})));
  outpvar.open(htmlnode("base", extentattrs({"attr": {"href": inp["HOST"]}})));
  outpvar.open(htmlnode("title", extentattrs({})));
  outpvar.addtext(inp["title"]);
  outpvar.close();
  for i in forlist(inp["css"]) :
    outpvar.open(htmlnode("link", extentattrs({"attr": {"href": i, "rel": "stylesheet", "type": "text/css"}})));
  outpvar.close();
  outpvar.open(htmlnode("body", extentattrs({"style": inp["bodystyle"]})));
  outpvar.addchilds(innerHTML);
  outpvar.open(htmlnode("script", extentattrs({"attr": {"type": "text/javascript"}})));
  outpvar.addtext(myadd(myadd("var jsdata = ", inp["jsdata"]), ";"));
  outpvar.close();
  outpvar.open(htmlnode("script", extentattrs({"attr": {"type": "text/javascript"}})));
  outpvar.addtext("var ec  = jsdata['_ec'] ;");
  outpvar.close();
  for i in forlist(inp["js"]) :
    outpvar.open(htmlnode("script", extentattrs({"attr": {"type": "text/javascript", "src": i}})));
    outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_disptabs(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({"tabname": [], "tablink": []}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  for j in range(len(forlist(inp["tabname"]))) :
    i = inp["tabname"][j];
    outpvar.open(htmlnode("li", extentattrs({"class": inp["liclass"]})));
    inp["isactive"] = ("active" if ((inp["active"]==inp["tablink"][j])) else " ");
    outpvar.open(htmlnode("a", extentattrs({"attr": {"href": inp["tablink"][j]}, "class": inp["isactive"]})));
    outpvar.addtext(i);
    outpvar.close();
    outpvar.close();
  return outpvar;
  
def newtag_header1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({"tabname": [], "tablink": []}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs({"class": "navbar-fixed "})));
  outpvar.open(htmlnode("nav", extentattrs({"class": "white", "attr": {"role": "container"}})));
  outpvar.open(htmlnode("div", extentattrs({"class": "nav-wrapper container"})));
  outpvar.open(htmlnode("a", extentattrs({"attr": {"id": "logo-container", "href": inp["HOST"]}, "class": "brand-logo"})));
  outpvar.open(htmlnode("img", extentattrs({"attr": {"src": "photo/mylogo1.png"}, "class": "circle responsive-img", "style": {"vertical-align": "middle"}})));
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs({"class": "right hide-on-med-and-down"})));
  outpvar.cur.addfcdata("disptabs");
  outpvar.addchilds(newtag_disptabs({"tabname": inp["tabname"], "tablink": inp["tablink"]}, ginp, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_header1_cp(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({"tabname": [], "tablink": []}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs({"class": "navbar-fixed "})));
  outpvar.open(htmlnode("nav", extentattrs({"class": "white", "attr": {"role": "container"}})));
  outpvar.open(htmlnode("div", extentattrs({"class": "nav-wrapper container"})));
  outpvar.open(htmlnode("a", extentattrs({"attr": {"id": "logo-container", "href": inp["HOST"]}, "class": "brand-logo"})));
  outpvar.open(htmlnode("img", extentattrs({"attr": {"src": "photo/mylogo1.png"}, "class": "circle responsive-img", "style": {"vertical-align": "middle"}})));
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs({"class": "right hide-on-med-and-down"})));
  outpvar.cur.addfcdata("disptabs");
  outpvar.addchilds(newtag_disptabs({"tabname": inp["tabname"], "tablink": inp["tablink"]}, ginp, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
  outpvar.cur.addfcdata("headertabs_cp");
  outpvar.addchilds(newtag_headertabs_cp({}, ginp, outpvar.cur.fcalldata["headertabs_cp"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs({"id": "nav-mobile", "class": "side-nav"})));
  outpvar.cur.addfcdata("headertabs_cp");
  outpvar.addchilds(newtag_headertabs_cp({}, ginp, outpvar.cur.fcalldata["headertabs_cp"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("a", extentattrs({"attr": {"data-activates": "nav-mobile"}, "class": "button-collapse"})));
  outpvar.cur.addfcdata("icon");
  outpvar.addchilds(newtag_icon({"name": "menu"}, ginp, outpvar.cur.fcalldata["icon"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_header2(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({"tabname": [], "tablink": [], "tabname1": [], "tablink1": []}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs({"class": "navbar-fixed "})));
  outpvar.open(htmlnode("nav", extentattrs({"class": "white", "attr": {"role": "container"}})));
  outpvar.open(htmlnode("div", extentattrs({"class": "nav-wrapper container"})));
  outpvar.open(htmlnode("ul", extentattrs({"class": "left hide-on-med-and-down"})));
  outpvar.open(htmlnode("a", extentattrs({"attr": {"id": "logo-container", "href": inp["HOST"]}, "class": "brand-logo"})));
  outpvar.open(htmlnode("img", extentattrs({"attr": {"src": "photo/logo4.png"}, "class": "responsive-img", "style": {"vertical-align": "middle"}})));
  outpvar.close();
  outpvar.cur.addfcdata("disptabs");
  outpvar.addchilds(newtag_disptabs({"tabname": inp["tabname1"], "tablink": inp["tablink1"]}, ginp, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs({"class": "right hide-on-med-and-down"})));
  outpvar.cur.addfcdata("disptabs");
  outpvar.addchilds(newtag_disptabs({"tabname": inp["tabname"], "tablink": inp["tablink"]}, ginp, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
  outpvar.open(htmlnode("li", extentattrs({})));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1({"href": "#loginmodal", "class": "modal-trigger", "name": "Login"}, ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs({"attr": {"id": "nav-mobile"}, "class": "side-nav"})));
  outpvar.cur.addfcdata("disptabs");
  outpvar.addchilds(newtag_disptabs({"tabname": inp["tabname"], "tablink": inp["tablink"]}, ginp, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("a", extentattrs({"attr": {"data-activates": "nav-mobile"}, "class": "button-collapse"})));
  outpvar.cur.addfcdata("icon");
  outpvar.addchilds(newtag_icon({"name": "menu"}, ginp, outpvar.cur.fcalldata["icon"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_header2_user(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({"tabname": [], "tablink": []}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs({"class": "navbar-fixed "})));
  outpvar.open(htmlnode("ul", extentattrs({"id": "dropdown1", "class": "dropdown-content"})));
  outpvar.open(htmlnode("li", extentattrs({})));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1({"href": myadd(inp["BASE"], "account"), "name": "Account"}, ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("li", extentattrs({})));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1({"href": myadd(inp["BASE"], "orders"), "name": "Orders"}, ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("li", extentattrs({})));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1({"href": myadd(inp["HOST"], "?logout"), "name": "Logout"}, ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("nav", extentattrs({"class": "white", "attr": {"role": "container"}})));
  outpvar.open(htmlnode("div", extentattrs({"class": "nav-wrapper container"})));
  outpvar.open(htmlnode("a", extentattrs({"attr": {"id": "logo-container", "href": inp["HOST"]}, "class": "brand-logo"})));
  outpvar.open(htmlnode("img", extentattrs({"attr": {"src": "photo/mylogo1.png"}, "class": "circle responsive-img", "style": {"vertical-align": "middle"}})));
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs({"class": "right hide-on-med-and-down"})));
  outpvar.cur.addfcdata("disptabs");
  outpvar.addchilds(newtag_disptabs({"tabname": inp["tabname"], "tablink": inp["tablink"]}, ginp, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
  outpvar.open(htmlnode("li", extentattrs({})));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1({"class": "dropdown-button", "name": myadd(myadd(("&nbsp;"*5), inp["loginname"]), ("&nbsp;"*10)), "data": {"activates": "dropdown1"}}, ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs({"attr": {"id": "nav-mobile"}, "class": "side-nav"})));
  outpvar.cur.addfcdata("disptabs");
  outpvar.addchilds(newtag_disptabs({"tabname": inp["tabname"], "tablink": inp["tablink"]}, ginp, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("a", extentattrs({"attr": {"data-activates": "nav-mobile"}, "class": "button-collapse"})));
  outpvar.cur.addfcdata("icon");
  outpvar.addchilds(newtag_icon({"name": "menu"}, ginp, outpvar.cur.fcalldata["icon"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_header2_chef(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({"tabname": [], "tablink": []}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs({"class": "navbar-fixed "})));
  outpvar.open(htmlnode("ul", extentattrs({"id": "dropdown1", "class": "dropdown-content"})));
  outpvar.open(htmlnode("li", extentattrs({})));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1({"href": myadd(inp["BASE"], "profile"), "name": "Profile"}, ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("li", extentattrs({})));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1({"href": myadd(inp["BASE"], "orders"), "name": "Orders"}, ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("li", extentattrs({})));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1({"href": myadd(inp["HOST"], "?logout"), "name": "Logout"}, ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("nav", extentattrs({"class": "white", "attr": {"role": "container"}})));
  outpvar.open(htmlnode("div", extentattrs({"class": "nav-wrapper container"})));
  outpvar.open(htmlnode("a", extentattrs({"attr": {"id": "logo-container", "href": inp["HOST"]}, "class": "brand-logo"})));
  outpvar.open(htmlnode("img", extentattrs({"attr": {"src": "photo/mylogo1.png"}, "class": "circle responsive-img", "style": {"vertical-align": "middle"}})));
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs({"class": "right hide-on-med-and-down"})));
  outpvar.cur.addfcdata("disptabs");
  outpvar.addchilds(newtag_disptabs({"tabname": inp["tabname"], "tablink": inp["tablink"]}, ginp, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
  outpvar.open(htmlnode("li", extentattrs({})));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1({"class": "dropdown-button", "name": myadd(myadd(("&nbsp;"*5), "Profile"), ("&nbsp;"*10)), "data": {"activates": "dropdown1"}}, ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs({"attr": {"id": "nav-mobile"}, "class": "side-nav"})));
  outpvar.cur.addfcdata("disptabs");
  outpvar.addchilds(newtag_disptabs({"tabname": inp["tabname"], "tablink": inp["tablink"]}, ginp, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("a", extentattrs({"attr": {"data-activates": "nav-mobile"}, "class": "button-collapse"})));
  outpvar.cur.addfcdata("icon");
  outpvar.addchilds(newtag_icon({"name": "menu"}, ginp, outpvar.cur.fcalldata["icon"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_header2_admin(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({"tabname": [], "tablink": []}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs({"class": "navbar-fixed "})));
  outpvar.open(htmlnode("ul", extentattrs({"id": "dropdown1", "class": "dropdown-content"})));
  outpvar.open(htmlnode("li", extentattrs({})));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1({"href": myadd(inp["BASE"], "account"), "name": "Account"}, ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("li", extentattrs({})));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1({"href": myadd(inp["BASE"], "orders"), "name": "Orders"}, ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("li", extentattrs({})));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1({"href": myadd(inp["HOST"], "?logout"), "name": "Logout"}, ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("nav", extentattrs({"class": "white", "attr": {"role": "container"}})));
  outpvar.open(htmlnode("div", extentattrs({"class": "nav-wrapper container"})));
  outpvar.open(htmlnode("a", extentattrs({"attr": {"id": "logo-container", "href": inp["HOST"]}, "class": "brand-logo"})));
  outpvar.open(htmlnode("img", extentattrs({"attr": {"src": "photo/mylogo1.png"}, "class": "circle responsive-img", "style": {"vertical-align": "middle"}})));
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs({"class": "right hide-on-med-and-down"})));
  outpvar.cur.addfcdata("disptabs");
  outpvar.addchilds(newtag_disptabs({"tabname": inp["tabname"], "tablink": inp["tablink"]}, ginp, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
  outpvar.open(htmlnode("li", extentattrs({})));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1({"class": "dropdown-button", "name": myadd(myadd(("&nbsp;"*5), "Profile"), ("&nbsp;"*10)), "data": {"activates": "dropdown1"}}, ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs({"attr": {"id": "nav-mobile"}, "class": "side-nav"})));
  outpvar.cur.addfcdata("disptabs");
  outpvar.addchilds(newtag_disptabs({"tabname": inp["tabname"], "tablink": inp["tablink"]}, ginp, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("a", extentattrs({"attr": {"data-activates": "nav-mobile"}, "class": "button-collapse"})));
  outpvar.cur.addfcdata("icon");
  outpvar.addchilds(newtag_icon({"name": "menu"}, ginp, outpvar.cur.fcalldata["icon"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_icon(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({"aclass": ""}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("i", extentattrs({"class": myadd("material-icons ", inp["aclass"]), "style": inp["style"]})));
  outpvar.addtext(inp["name"]);
  outpvar.close();
  return outpvar;
  
def newtag_icon1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  inp["attr"]["src"] = inp["img"];
  outpvar.open(htmlnode("img", extentattrs({"attr": inp["attr"], "style": {"margin-bottom": "-5px"}, "class": inp["class"]})));
  return outpvar;
  
def newtag_checkbox1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({"checked": None, "label": "Check", "aclass": "", "labels": {}}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("span", extentattrs({})));
  outpvar.open(htmlnode("input", extentattrs({"attr": {"type": "checkbox", "id": inp["id"], "checked": inp["checked"]}, "class": myadd("filled-in ", inp["aclass"]), "data": inp["data"]})));
  outpvar.open(htmlnode("label", extentattrs({"attr": {"for": inp["id"]}, "style": inp["labels"]})));
  outpvar.addtext(inp["label"]);
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_checkbox2(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({"checked": None, "label": "Check", "aclass": "", "labels": {}}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("span", extentattrs({})));
  outpvar.open(htmlnode("input", extentattrs({"attr": {"type": "radio", "id": inp["id"], "checked": inp["checked"]}, "class": myadd("with-gap ", inp["aclass"]), "data": inp["data"]})));
  outpvar.open(htmlnode("label", extentattrs({"attr": {"for": inp["id"]}, "style": inp["labels"]})));
  outpvar.addtext(inp["label"]);
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_bigf(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({"font": "65px"}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("span", extentattrs({"style": {"font-size": inp["font"], "text-shadow": "3px 3px 3px #000, 2px 2px 2px blue"}, "color": inp["color"]})));
  outpvar.addtext(inp["name"]);
  outpvar.close();
  return outpvar;
  
def newtag_bigf1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({"font": "40px"}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.cur.addfcdata("bigf");
  outpvar.addchilds(newtag_bigf({"color": inp["color"], "font": inp["font"], "name": inp["name"]}, ginp, outpvar.cur.fcalldata["bigf"].root.content).root.content);
  return outpvar;
  
def newtag_height(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs({"style": {"height": myadd(inp["val"], "px")}})));
  outpvar.close();
  return outpvar;
  
def newtag_resimg(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({"aclass": ""}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("img", extentattrs({"class": myadd("responsive-img ", inp["aclass"]), "attr": {"src": inp["src"]}, "style": {"opacity": inp["opacity"]}})));
  return outpvar;
  
def newtag_circleimg(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.cur.addfcdata("resimg");
  outpvar.addchilds(newtag_resimg({"aclass": "circle", "src": inp["src"], "opacity": inp["opacity"]}, ginp, outpvar.cur.fcalldata["resimg"].root.content).root.content);
  return outpvar;
  
def newtag_divpedding(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({"text": "", "padding": "5px"}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs({"style": {"padding": inp["padding"]}, "class": inp["class"]})));
  outpvar.addtext(inp["text"]);
  outpvar.addchilds(innerHTML);
  outpvar.close();
  return outpvar;
  
def newtag_textdiv(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({"name": ""}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs({"style": {"font-size": inp["font"], "font-weight": inp["fontw"]}, "color": inp["color"], "class": inp["class"], "id": inp["id"]})));
  outpvar.addchilds(innerHTML);
  outpvar.addtext(inp["name"]);
  outpvar.close();
  return outpvar;
  
def newtag_textdiv1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({"font": "20px"}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.cur.addfcdata("textdiv");
  outpvar.addchilds(newtag_textdiv({"font": inp["font"], "fontw": inp["fontw"], "color": inp["color"], "class": inp["class"], "name": inp["name"]}, ginp, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
  return outpvar;
  
def newtag_a1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({"class": None, "text": None, "href": None}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("a", extentattrs({"attr": inp["attr"], "style": inp["style"], "class": inp["class"]})));
  outpvar.addtext(inp["text"]);
  outpvar.close();
  return outpvar;
  
def newtag_starrating(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({"val": 5}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  for i in forlist(inp["val"]) :
    outpvar.open(htmlnode("img", extentattrs({"attr": {"src": "photo/rating4.png"}, "style": {"margin": "-1px", "width": "22px"}})));
  return outpvar;
  
def newtag_input1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({"aclass": "col s6", "type": "text", "dc": "simple"}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs({"class": myadd("input-field ", inp["aclass"])})));
  if (inp["icon"]): 
    outpvar.cur.addfcdata("icon");
    outpvar.addchilds(newtag_icon({"name": inp["icon"], "aclass": "prefix"}, ginp, outpvar.cur.fcalldata["icon"].root.content).root.content);
  inp["data"]["name"] = inp["label"];
  inp["data"]["dc"] = inp["dc"];
  if ((inp["dname"]!=None)): 
    inp["data"]["name"] = inp["dname"];
  outpvar.open(htmlnode("input", extentattrs({"attr": {"id": inp["id"], "type": inp["type"], "value": inp["value"]}, "class": inp["iclass"], "data": inp["data"]})));
  outpvar.open(htmlnode("label", extentattrs({"attr": {"for": inp["id"]}})));
  outpvar.addtext(inp["label"]);
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_input2(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({"aclass": "col s6", "type": "text"}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs({"class": myadd("input-field ", inp["aclass"])})));
  outpvar.open(htmlnode("input", extentattrs({"attr": {"id": inp["id"], "type": inp["type"], "name": inp["id"]}, "class": inp["iclass"]})));
  outpvar.open(htmlnode("label", extentattrs({"attr": {"for": inp["id"]}})));
  outpvar.addtext(inp["label"]);
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_textarea1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({"aclass": "col l12 m12 s12"}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs({"class": myadd("input-field ", inp["aclass"])})));
  outpvar.open(htmlnode("textarea", extentattrs({"attr": {"id": inp["id"], "name": inp["id"]}, "class": "materialize-textarea"})));
  outpvar.close();
  outpvar.open(htmlnode("label", extentattrs({"attr": {"for": inp["id"]}})));
  outpvar.addtext(inp["label"]);
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_button1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({"aclass": ""}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("button", extentattrs({"class": myadd("btn waves-effect waves-light btn ", inp["aclass"]), "data": inp["data"], "attr": inp["attr"], "datas": inp["datas"]})));
  outpvar.addtext(inp["name"]);
  outpvar.close();
  return outpvar;
  
def newtag_main1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({"css": [], "js": [], "bodystyle": {}, "htmlstyle": {}, "title": "KurryBox"}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  inp["js"] = myadd(["js/main.js"], inp["js"]);
  outpvar.cur.addfcdata("main");
  outpvar.cur.fcalldata["main"].addchilds(innerHTML);
  outpvar.addchilds(newtag_main({"title": inp["title"], "css": inp["css"], "js": inp["js"], "bodystyle": inp["bodystyle"], "htmlstyle": inp["htmlstyle"]}, ginp, outpvar.cur.fcalldata["main"].root.content).root.content);
  return outpvar;
  
def newtag_main2(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({"css": [], "js": [], "bodystyle": {}, "htmlstyle": {}, "title": "KurryBox"}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  inp["js"] = myadd(["js/main.js"], inp["js"]);
  outpvar.cur.addfcdata("main");
  outpvar.cur.fcalldata["main"].addchilds(innerHTML);
  outpvar.cur.fcalldata["main"].cur.addfcdata("loginmodal");
  outpvar.cur.fcalldata["main"].addchilds(newtag_loginmodal({}, ginp, outpvar.cur.fcalldata["main"].cur.fcalldata["loginmodal"].root.content).root.content);
  outpvar.addchilds(newtag_main({"title": inp["title"], "css": inp["css"], "js": inp["js"], "bodystyle": inp["bodystyle"], "htmlstyle": inp["htmlstyle"], "acss": ["css/materialize.min.css", "css/lib.css", "css/materialize.min.css", "css/custom-stylesheet.css", "css/jquery.bxslider.css", "mslib/css/gfont.css", "css/lib.css", "css/main.css", "css/style.css"]}, ginp, outpvar.cur.fcalldata["main"].root.content).root.content);
  return outpvar;
  
def newtag_bigsearch(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs({"class": "row", "style": {"background-color": ""}})));
  outpvar.open(htmlnode("div", extentattrs({"class": "col l1 m1"})));
  outpvar.addtext("&nbsp;");
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs({"class": "col m8 s12 l9", "style": {"padding": "0px", "margin": "0px"}})));
  outpvar.open(htmlnode("input", extentattrs({"attr": {"placeholder": inp["ph"], "id": inp["id"], "autofocus": inp["autofocus"]}, "class": "bigsearch definput", "style": {"border-radius": "0px"}})));
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs({"class": "col m2 s12 l1 ", "style": {"padding": "0px", "margin": "0px"}})));
  outpvar.open(htmlnode("button", extentattrs({"class": "bigsearchbutton waves-effect waves-light btn", "style": {"border-radius": "0px"}, "attr": {"type": "submit"}})));
  outpvar.addtext("Go");
  outpvar.cur.addfcdata("icon");
  outpvar.addchilds(newtag_icon({"name": "send", "aclass": "right"}, ginp, outpvar.cur.fcalldata["icon"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_header4(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  if ((inp["islogin"]==None)): 
    outpvar.cur.addfcdata("header2");
    outpvar.addchilds(newtag_header2({"tablink": ["", "", myadd(inp["BASE"], "chefjoin")], "tabname": ["Our Story", "Blog", "Be a Chef"]}, ginp, outpvar.cur.fcalldata["header2"].root.content).root.content);
  elif ((inp["islogin"]=="u")): 
    outpvar.cur.addfcdata("header2_user");
    outpvar.addchilds(newtag_header2_user({"tablink": [inp["HOST"], "", "", myadd(inp["BASE"], "cart")], "tabname": ["Home", "Our Story", "Blog", "Cart"]}, ginp, outpvar.cur.fcalldata["header2_user"].root.content).root.content);
  elif ((inp["islogin"]=="a")): 
    outpvar.cur.addfcdata("header2_admin");
    outpvar.addchilds(newtag_header2_admin({"tablink": [inp["HOST"], "", "", "", "", ""], "tabname": ["Home", "Our Story", "Blog"]}, ginp, outpvar.cur.fcalldata["header2_admin"].root.content).root.content);
  elif ((inp["islogin"]=="c")): 
    outpvar.cur.addfcdata("header2_chef");
    outpvar.addchilds(newtag_header2_chef({"tablink": [inp["HOST"], "", "", "", "", ""], "tabname": ["Home", "Our Story", "Blog"]}, ginp, outpvar.cur.fcalldata["header2_chef"].root.content).root.content);
  return outpvar;
  
def newtag_header3(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({"tabname": [], "tablink": []}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs({"class": "navbar-fixed "})));
  outpvar.open(htmlnode("nav", extentattrs({"class": "white", "attr": {"role": "container"}})));
  outpvar.open(htmlnode("div", extentattrs({"class": "nav-wrapper container"})));
  outpvar.open(htmlnode("a", extentattrs({"attr": {"id": "logo-container", "href": inp["BASE"]}, "class": "brand-logo"})));
  outpvar.open(htmlnode("img", extentattrs({"attr": {"src": "photo/mylogo1.png"}, "class": "circle responsive-img", "style": {"vertical-align": "middle"}})));
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs({"class": "right hide-on-med-and-down"})));
  outpvar.open(htmlnode("li", extentattrs({})));
  outpvar.open(htmlnode("a", extentattrs({"class": "dropdown-button", "attr": {"data-activates": "dropdown2"}})));
  outpvar.addtext(myadd(myadd(("&nbsp;"*10), "Today, 28th Oct"), ("&nbsp;"*10)));
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("li", extentattrs({})));
  outpvar.open(htmlnode("a", extentattrs({"class": "dropdown-button", "attr": {"data-activates": "dropdown1"}})));
  outpvar.addtext(myadd(myadd(("&nbsp;"*5), "All"), ("&nbsp;"*20)));
  outpvar.close();
  outpvar.close();
  outpvar.cur.addfcdata("disptabs");
  outpvar.addchilds(newtag_disptabs({"tabname": inp["tabname"], "tablink": inp["tablink"]}, ginp, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs({"attr": {"id": "dropdown1"}, "class": "dropdown-content"})));
  inp["foodtype"] = ["All", "Veg", "Non-Veg"];
  for ii in range(len(forlist(inp["foodtype"]))) :
    i = inp["foodtype"][ii];
    outpvar.open(htmlnode("li", extentattrs({})));
    outpvar.open(htmlnode("a", extentattrs({"attr": {"href": ""}})));
    outpvar.addtext(i);
    outpvar.close();
    outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs({"attr": {"id": "dropdown2"}, "class": "dropdown-content"})));
  inp["nextdays"] = ["Today, 26 Oct", "27 Oct", "28 Oct"];
  for ii in range(len(forlist(inp["nextdays"]))) :
    i = inp["nextdays"][ii];
    outpvar.open(htmlnode("li", extentattrs({})));
    outpvar.open(htmlnode("a", extentattrs({"attr": {"href": ""}})));
    outpvar.addtext(i);
    outpvar.close();
    outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_dispfood(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs({"class": "col s12 l4 m6 ", "style": {}})));
  outpvar.open(htmlnode("div", extentattrs({"class": " card-panel", "style": {"margin-bottom": "40px", "padding": "0px"}})));
  outpvar.open(htmlnode("div", extentattrs({})));
  outpvar.cur.addfcdata("resimg");
  outpvar.addchilds(newtag_resimg({"src": inp["dishinfo"]["pic"]}, ginp, outpvar.cur.fcalldata["resimg"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs({"style": {"padding-bottom": "10px"}})));
  outpvar.open(htmlnode("div", extentattrs({"style": {"padding": "10px"}})));
  outpvar.open(htmlnode("div", extentattrs({"class": "row"})));
  outpvar.open(htmlnode("div", extentattrs({"class": "col l8", "attr": {"align": "left"}})));
  outpvar.open(htmlnode("div", extentattrs({})));
  outpvar.addtext(inp["dishinfo"]["title"]);
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs({"class": "col l4"})));
  outpvar.cur.addfcdata("icon1");
  outpvar.addchilds(newtag_icon1({"img": "photo/inr1.png"}, ginp, outpvar.cur.fcalldata["icon1"].root.content).root.content);
  outpvar.open(htmlnode("span", extentattrs({"style": {"font-size": "25px", "font-weight": "600"}})));
  outpvar.addtext(inp["dishinfo"]["price"]);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs({"class": "row valign-wrapper", "attr": {"align": "left"}})));
  outpvar.open(htmlnode("div", extentattrs({"class": "col l2"})));
  outpvar.cur.addfcdata("circleimg");
  outpvar.addchilds(newtag_circleimg({"src": inp["dishinfo"]["profilepic"]}, ginp, outpvar.cur.fcalldata["circleimg"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs({"class": "col l10"})));
  outpvar.open(htmlnode("div", extentattrs({"style": {"font-weight": "500"}})));
  outpvar.cur.addfcdata("profilea1");
  outpvar.addchilds(newtag_profilea1({"name": myadd("Chef ", inp["dishinfo"]["name"]), "uid": inp["dishinfo"]["cid"]}, ginp, outpvar.cur.fcalldata["profilea1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs({})));
  outpvar.cur.addfcdata("starrating");
  outpvar.addchilds(newtag_starrating({"val": 3}, ginp, outpvar.cur.fcalldata["starrating"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs({"class": "row"})));
  if ((inp["islogin"]=="a")): 
    outpvar.open(htmlnode("div", extentattrs({"class": "col l4 "})));
    outpvar.open(htmlnode("button", extentattrs({"class": "btn waves-effect waves-light btn", "datas": {"datetime": inp["dishinfo"]["datetime"], "lord": inp["dishinfo"]["lord"], "dishid": inp["dishinfo"]["id"]}, "data": {"onclick": "sreq", "action": "deletedisp", "restext": "Deleted !"}})));
    outpvar.addtext("Delete");
    outpvar.close();
    outpvar.close();
    outpvar.open(htmlnode("div", extentattrs({"class": "col l4 offset-l3"})));
    outpvar.open(htmlnode("button", extentattrs({"class": "btn waves-effect waves-light btn"})));
    outpvar.addtext("Edit");
    outpvar.close();
    outpvar.close();
  elif ((inp["loginid"]==inp["dishinfo"]["cid"])): 
    pass
  elif (1): 
    outpvar.open(htmlnode("div", extentattrs({"class": "col l4 "})));
    outpvar.open(htmlnode("button", extentattrs({"class": "btn waves-effect waves-light btn", "data": {"onclick": "addfav"}, "attr": {"id": "mohit"}})));
    outpvar.addtext("Favourite");
    outpvar.close();
    outpvar.close();
    outpvar.open(htmlnode("div", extentattrs({"class": "col l4 offset-l3"})));
    outpvar.open(htmlnode("button", extentattrs({"class": "btn waves-effect waves-light btn", "data": {"onclick": "sreq", "action": "addincart", "restext": "Added!"}, "datas": {"datetime": inp["dishinfo"]["datetime"], "lord": inp["dishinfo"]["lord"], "dishid": inp["dishinfo"]["id"]}})));
    outpvar.addtext("Add + ");
    outpvar.close();
    outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_l_otp_button(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("button", extentattrs({"class": "btn waves-effect waves-light", "attr": {"type": "button"}, "data": {"onclick": "sreq", "action": "sendotp", "fobj": "$(obj).parent().parent()[0]", "restext": "Re-send"}})));
  outpvar.addtext("Send OTP");
  outpvar.close();
  return outpvar;
  
def newtag_loginmodal(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs({"attr": {"id": "loginmodal"}, "class": "modal"})));
  outpvar.open(htmlnode("div", extentattrs({"class": "modal-content container-fluid"})));
  outpvar.open(htmlnode("div", extentattrs({"class": "row"})));
  outpvar.open(htmlnode("ul", extentattrs({"class": "tabs"})));
  outpvar.cur.addfcdata("disptabs");
  outpvar.addchilds(newtag_disptabs({"liclass": "tab col l6", "tablink": ["#logintab", "#signuptab"], "tabname": ["Login", "Signup"]}, ginp, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs({"attr": {"id": "logintab"}})));
  outpvar.open(htmlnode("form", extentattrs({"data": {"onsubmit": "sreq", "bobj": "", "action": "login", "res": "ms.reload();", "errorh": "error_login"}})));
  outpvar.cur.addfcdata("errorbox");
  outpvar.addchilds(newtag_errorbox({}, ginp, outpvar.cur.fcalldata["errorbox"].root.content).root.content);
  outpvar.open(htmlnode("div", extentattrs({"class": "row"})));
  outpvar.cur.addfcdata("input1");
  outpvar.addchilds(newtag_input1({"label": "Phone number", "icon": "phone", "aclass": "col s12 l7 m6", "id": "loginphone", "dc": "phone"}, ginp, outpvar.cur.fcalldata["input1"].root.content).root.content);
  outpvar.open(htmlnode("div", extentattrs({"class": "col l4 m6"})));
  outpvar.cur.addfcdata("l_otp_button");
  outpvar.addchilds(newtag_l_otp_button({}, ginp, outpvar.cur.fcalldata["l_otp_button"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs({"class": "row"})));
  outpvar.cur.addfcdata("input1");
  outpvar.addchilds(newtag_input1({"label": "Password or OTP", "icon": "vpn_key", "aclass": "col s12 l12 m12", "id": "loginpass", "type": "password", "dc": "password1"}, ginp, outpvar.cur.fcalldata["input1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs({"class": "row"})));
  outpvar.open(htmlnode("div", extentattrs({"class": "col"})));
  outpvar.open(htmlnode("button", extentattrs({"class": "btn waves-effect waves-light", "attr": {"type": "submit"}})));
  outpvar.addtext("Login");
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs({"attr": {"id": "signuptab"}})));
  outpvar.open(htmlnode("form", extentattrs({"data": {"onsubmit": "sreq", "bobj": "", "action": "signup", "res": "ms.reload();", "errorh": "error_login"}})));
  outpvar.cur.addfcdata("errorbox");
  outpvar.addchilds(newtag_errorbox({}, ginp, outpvar.cur.fcalldata["errorbox"].root.content).root.content);
  outpvar.open(htmlnode("div", extentattrs({"class": "row"})));
  outpvar.cur.addfcdata("input1");
  outpvar.addchilds(newtag_input1({"label": "Phone number", "icon": "phone", "aclass": "col s12 l7 m6", "id": "signupphone", "dc": "phone"}, ginp, outpvar.cur.fcalldata["input1"].root.content).root.content);
  outpvar.open(htmlnode("div", extentattrs({"class": "col l4 m6"})));
  outpvar.cur.addfcdata("l_otp_button");
  outpvar.addchilds(newtag_l_otp_button({}, ginp, outpvar.cur.fcalldata["l_otp_button"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs({"class": "row"})));
  outpvar.cur.addfcdata("input1");
  outpvar.addchilds(newtag_input1({"label": "Choose Password", "icon": "vpn_key", "aclass": "col s12 l6 m6", "id": "signuppass", "type": "password", "dc": "password1"}, ginp, outpvar.cur.fcalldata["input1"].root.content).root.content);
  outpvar.cur.addfcdata("input1");
  outpvar.addchilds(newtag_input1({"label": "OTP", "icon": "vpn_key", "aclass": "col s12 l6 m6", "id": "signupotp", "type": "password", "dc": "otp"}, ginp, outpvar.cur.fcalldata["input1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs({"class": "row"})));
  outpvar.cur.addfcdata("input1");
  outpvar.addchilds(newtag_input1({"label": "Name", "icon": "account_circle", "aclass": "col s12 l12 m12", "id": "signupname"}, ginp, outpvar.cur.fcalldata["input1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs({"class": "row"})));
  outpvar.open(htmlnode("div", extentattrs({"class": "col"})));
  outpvar.open(htmlnode("button", extentattrs({"class": "btn waves-effect waves-light", "attr": {"type": "submit"}})));
  outpvar.addtext("Signup");
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_table1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({"rows": [], "thead": []}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("table", extentattrs({"class": inp["class"]})));
  outpvar.open(htmlnode("thead", extentattrs({})));
  for i in forlist(inp["thead"]) :
    outpvar.open(htmlnode("th", extentattrs({})));
    outpvar.addtext(i);
    outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("tbody", extentattrs({})));
  for ii in range(len(forlist(inp["rows"]))) :
    i = inp["rows"][ii];
    outpvar.open(htmlnode("tr", extentattrs({})));
    for jj in range(len(forlist(i))) :
      j = i[jj];
      outpvar.open(htmlnode("td", extentattrs({})));
      outpvar.addtext(j);
      outpvar.close();
    outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_profilea1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1({"name": inp["name"], "href": myadd(myadd(inp["BASE"], "profile?uid="), inp["uid"])}, ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  return outpvar;
  
def newtag_account_admin(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs({"attr": {"align": "center"}})));
  outpvar.cur.addfcdata("height");
  outpvar.addchilds(newtag_height({"val": 20}, ginp, outpvar.cur.fcalldata["height"].root.content).root.content);
  outpvar.cur.addfcdata("textdiv");
  outpvar.addchilds(newtag_textdiv({"name": "Hey Admin,\n you are welcome", "font": "20px"}, ginp, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
  outpvar.cur.addfcdata("height");
  outpvar.addchilds(newtag_height({"val": 50}, ginp, outpvar.cur.fcalldata["height"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("table", extentattrs({"class": "bordered striped centered highlight"})));
  outpvar.open(htmlnode("thead", extentattrs({})));
  for i in forlist(["UserID", "Name", "Email", "Phone", "User Type"]) :
    outpvar.open(htmlnode("th", extentattrs({})));
    outpvar.addtext(i);
    outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("tbody", extentattrs({})));
  for ii in range(len(forlist(inp["users"]))) :
    i = inp["users"][ii];
    outpvar.open(htmlnode("tr", extentattrs({})));
    for jj in range(len(forlist(["id", "name", "email", "phone", "typetext"]))) :
      jjj = ["id", "name", "email", "phone", "typetext"][jj];
      inp["j"] = i[jjj];
      outpvar.open(htmlnode("td", extentattrs({})));
      if (((jjj=="name")and(i["type"]=="c"))): 
        outpvar.cur.addfcdata("profilea1");
        outpvar.addchilds(newtag_profilea1({"name": inp["j"], "uid": i["id"]}, ginp, outpvar.cur.fcalldata["profilea1"].root.content).root.content);
      elif (1): 
        outpvar.addtext(inp["j"]);
      outpvar.close();
    outpvar.open(htmlnode("td", extentattrs({})));
    outpvar.cur.addfcdata("button1");
    outpvar.addchilds(newtag_button1({"name": ("UnBlock" if (i["conf"]) else "Block"), "datas": {"uid": i["id"], "isblock": (i["conf"]!=None)}, "data": {"onclick": "sreq", "action": "blockunblock", "restext": "Done!"}}, ginp, outpvar.cur.fcalldata["button1"].root.content).root.content);
    outpvar.close();
    outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_profile_chef_top2(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs({"class": "row valign-wrapper"})));
  outpvar.open(htmlnode("div", extentattrs({"class": "col l3", "attr": {"align": "center"}})));
  outpvar.open(htmlnode("div", extentattrs({})));
  outpvar.cur.addfcdata("circleimg");
  outpvar.addchilds(newtag_circleimg({"src": inp["uinfo"]["profilepic"]}, ginp, outpvar.cur.fcalldata["circleimg"].root.content).root.content);
  outpvar.close();
  if (inp["canedit"]): 
    outpvar.open(htmlnode("form", extentattrs({"attr": {"enctype": "multipart/form-data", "method": "post"}})));
    outpvar.cur.addfcdata("a1");
    outpvar.addchilds(newtag_a1({"name": "Upload Profile Pic", "attr": {"onclick": "uploadfile(this, \"profilepic\");"}}, ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
    outpvar.close();
  outpvar.open(htmlnode("div", extentattrs({})));
  outpvar.cur.addfcdata("textdiv");
  outpvar.addchilds(newtag_textdiv({"name": myadd("Chef ", inp["uinfo"]["name"]), "font": "25px", "fontw": "500"}, ginp, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
  outpvar.open(htmlnode("div", extentattrs({"class": "row"})));
  outpvar.open(htmlnode("div", extentattrs({"class": "col l6"})));
  outpvar.cur.addfcdata("textdiv");
  outpvar.addchilds(newtag_textdiv({"name": 38456, "fontw": 600}, ginp, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
  outpvar.cur.addfcdata("textdiv");
  outpvar.addchilds(newtag_textdiv({"name": "Dished Delivered"}, ginp, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs({"class": "col l6"})));
  outpvar.cur.addfcdata("textdiv");
  outpvar.addchilds(newtag_textdiv({"name": 56, "fontw": 600}, ginp, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
  outpvar.cur.addfcdata("textdiv");
  outpvar.addchilds(newtag_textdiv({"name": "People reviewed"}, ginp, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs({"class": "col l8 offset-l1"})));
  outpvar.cur.addfcdata("textdiv");
  outpvar.addchilds(newtag_textdiv({"font": "25px", "name": myadd("About ", inp["uinfo"]["name"]), "fontw": 600}, ginp, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
  if (inp["canedit"]): 
    outpvar.cur.addfcdata("a1");
    outpvar.addchilds(newtag_a1({"name": "Edit", "attr": {"onclick": "ms.showtextarea(this);"}}, ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
    outpvar.open(htmlnode("div", extentattrs({"class": "edittext", "style": {"display": "none"}})));
    outpvar.open(htmlnode("form", extentattrs({"data": {"onsubmit": "sreq", "bobj": "", "action": "saveaboutinfo", "res": "ms.reload();"}})));
    outpvar.open(htmlnode("input", extentattrs({"attr": {"type": "hidden", "name": "chefid", "value": inp["uid"]}})));
    outpvar.open(htmlnode("textarea", extentattrs({"attr": {"name": "aboutus"}, "class": "materialize-textarea"})));
    outpvar.addtext(inp["uinfo"]["aboutus"].gchars);
    outpvar.close();
    outpvar.cur.addfcdata("button1");
    outpvar.addchilds(newtag_button1({"name": "Save", "attr": {"type": "submit"}}, ginp, outpvar.cur.fcalldata["button1"].root.content).root.content);
    outpvar.close();
    outpvar.close();
  outpvar.cur.addfcdata("textdiv");
  outpvar.addchilds(newtag_textdiv({"font": "16px", "name": inp["uinfo"]["aboutus"].gchars}, ginp, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
  outpvar.open(htmlnode("div", extentattrs({})));
  outpvar.open(htmlnode("b", extentattrs({})));
  outpvar.addtext("Address: ");
  outpvar.close();
  outpvar.addtext(inp["uinfo"]["address"]);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_profile_chef(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs({"class": "container-fluid"})));
  outpvar.open(htmlnode("div", extentattrs({"class": "row"})));
  outpvar.open(htmlnode("div", extentattrs({"class": "col l10 offset-l1 s10 m10 offset-s1 offset-m1"})));
  outpvar.cur.addfcdata("profile_chef_top2");
  outpvar.addchilds(newtag_profile_chef_top2({}, ginp, outpvar.cur.fcalldata["profile_chef_top2"].root.content).root.content);
  outpvar.open(htmlnode("div", extentattrs({"class": "msdivider"})));
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs({"class": "container-fluid"})));
  outpvar.open(htmlnode("div", extentattrs({"class": "row"})));
  outpvar.close();
  outpvar.close();
  if (inp["canedit"]): 
    outpvar.open(htmlnode("div", extentattrs({"class": "container-fluid"})));
    outpvar.open(htmlnode("div", extentattrs({"class": "row"})));
    outpvar.open(htmlnode("div", extentattrs({})));
    outpvar.open(htmlnode("ul", extentattrs({"class": "tabs"})));
    outpvar.cur.addfcdata("disptabs");
    outpvar.addchilds(newtag_disptabs({"liclass": "tab col s2", "tabname": myadd(["All Dishes"], inp["day5times"]["textl"]), "tablink": myadd(["#alldishes"], inp["day5times"]["tabkeys1"])}, ginp, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
    outpvar.close();
    outpvar.close();
    outpvar.open(htmlnode("div", extentattrs({"class": ""})));
    outpvar.open(htmlnode("div", extentattrs({"attr": {"id": "alldishes"}})));
    outpvar.cur.addfcdata("height");
    outpvar.addchilds(newtag_height({"val": 20}, ginp, outpvar.cur.fcalldata["height"].root.content).root.content);
    if ((inp["viewtype"]=="a")): 
      outpvar.cur.addfcdata("button1");
      outpvar.addchilds(newtag_button1({"name": "Add a New Dish", "data": {"onclick": "slideform"}}, ginp, outpvar.cur.fcalldata["button1"].root.content).root.content);
      outpvar.open(htmlnode("form", extentattrs({"style": {"display": "none"}, "attr": {"enctype": "multipart/form-data", "method": "post"}})));
      outpvar.open(htmlnode("div", extentattrs({"class": "row"})));
      outpvar.open(htmlnode("input", extentattrs({"attr": {"type": "hidden", "name": "cid", "value": inp["uid"]}})));
      outpvar.cur.addfcdata("input2");
      outpvar.addchilds(newtag_input2({"label": "Title of Dish", "aclass": "col s12 l6 m6", "id": "dishtitle"}, ginp, outpvar.cur.fcalldata["input2"].root.content).root.content);
      outpvar.cur.addfcdata("input2");
      outpvar.addchilds(newtag_input2({"label": "Price of Dish", "aclass": "col s12 l6 m6", "id": "dishprice"}, ginp, outpvar.cur.fcalldata["input2"].root.content).root.content);
      outpvar.close();
      outpvar.open(htmlnode("div", extentattrs({"class": "row"})));
      outpvar.open(htmlnode("textarea", extentattrs({"class": "materialize-textarea", "attr": {"name": "descp", "placeholder": "Dish Description"}})));
      outpvar.close();
      outpvar.close();
      outpvar.open(htmlnode("div", extentattrs({"class": "row"})));
      outpvar.open(htmlnode("div", extentattrs({"class": "file-field input-field"})));
      outpvar.open(htmlnode("div", extentattrs({"class": "btn"})));
      outpvar.open(htmlnode("span", extentattrs({})));
      outpvar.addtext("Upload Image");
      outpvar.close();
      outpvar.open(htmlnode("input", extentattrs({"attr": {"type": "file", "name": "dishpic"}})));
      outpvar.close();
      outpvar.open(htmlnode("div", extentattrs({"class": "file-path-wrapper"})));
      outpvar.open(htmlnode("input", extentattrs({"class": "file-path-validate", "attr": {"type": "text"}})));
      outpvar.close();
      outpvar.close();
      outpvar.close();
      outpvar.open(htmlnode("div", extentattrs({"class": "row"})));
      outpvar.open(htmlnode("div", extentattrs({"class": "col"})));
      outpvar.open(htmlnode("button", extentattrs({"class": "btn waves-effect waves-light", "attr": {"type": "submit", "name": "adddish"}})));
      outpvar.addtext("Add");
      outpvar.close();
      outpvar.close();
      outpvar.close();
      outpvar.close();
    outpvar.open(htmlnode("div", extentattrs({"class": "row", "attr": {"align": "center"}})));
    for i in forlist(inp["dispdata"]) :
      outpvar.cur.addfcdata("dispfood");
      outpvar.addchilds(newtag_dispfood({"dishinfo": i}, ginp, outpvar.cur.fcalldata["dispfood"].root.content).root.content);
    outpvar.close();
    outpvar.close();
    for ii in range(len(forlist(inp["day5times"]["tabkeys"]))) :
      i = inp["day5times"]["tabkeys"][ii];
      outpvar.open(htmlnode("div", extentattrs({"attr": {"id": i}})));
      outpvar.open(htmlnode("div", extentattrs({"class": "row"})));
      outpvar.open(htmlnode("table", extentattrs({"class": "bordered"})));
      outpvar.open(htmlnode("thead", extentattrs({})));
      for j in forlist(["Title", "Price", "Booked For Lunch", "Booked for Dinner"]) :
        outpvar.open(htmlnode("th", extentattrs({})));
        outpvar.addtext(j);
        outpvar.close();
      outpvar.close();
      for jj in range(len(forlist(inp["dispdata"]))) :
        j = inp["dispdata"][jj];
        outpvar.open(htmlnode("tr", extentattrs({})));
        outpvar.open(htmlnode("th", extentattrs({})));
        outpvar.addtext(myadd(j["title"], "").gchars);
        outpvar.close();
        outpvar.open(htmlnode("th", extentattrs({})));
        outpvar.addtext(j["price"]);
        outpvar.close();
        outpvar.open(htmlnode("th", extentattrs({})));
        outpvar.cur.addfcdata("input1");
        outpvar.addchilds(newtag_input1({"label": myadd(myadd("Plate Limit (", j[myadd("ollimit", ii)]), " Booked)"), "id": myadd(myadd(myadd("lunch_", jj), "_"), ii), "data": {"dishid": j["id"], "day": ii}, "iclass": "numplatelimit", "value": j[myadd("llimit", ii)]}, ginp, outpvar.cur.fcalldata["input1"].root.content).root.content);
        outpvar.close();
        outpvar.open(htmlnode("th", extentattrs({})));
        outpvar.cur.addfcdata("input1");
        outpvar.addchilds(newtag_input1({"label": myadd(myadd("Plate Limit (", j[myadd("odlimit", ii)]), " Booked)"), "id": myadd(myadd(myadd("dinner_", jj), "_"), ii), "data": {"dishid": j["id"], "day": ii}, "iclass": "numplatelimit", "value": j[myadd("dlimit", ii)]}, ginp, outpvar.cur.fcalldata["input1"].root.content).root.content);
        outpvar.close();
        outpvar.close();
      outpvar.close();
      outpvar.open(htmlnode("div", extentattrs({})));
      if ((inp["dispdata"].len!=0)): 
        outpvar.cur.addfcdata("button1");
        outpvar.addchilds(newtag_button1({"name": "Save", "data": {"action": "savedaymenu", "onclick": "sreq", "params": myadd(myadd("ms.getnumlimit(", ii), ")")}, "datas": {"datetime": inp["day5times"]["timel"][ii], "cid": inp["uid"]}}, ginp, outpvar.cur.fcalldata["button1"].root.content).root.content);
      outpvar.close();
      outpvar.close();
      outpvar.close();
    outpvar.close();
    outpvar.close();
    outpvar.close();
  outpvar.open(htmlnode("div", extentattrs({"attr": {"align": "center"}, "style": {"margin": "20px"}})));
  outpvar.cur.addfcdata("textdiv");
  outpvar.addchilds(newtag_textdiv({"name": "Dishes Serving today", "font": "25px"}, ginp, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs({"class": "row", "attr": {"align": "center"}})));
  for i in forlist(inp["dispdata"]) :
    if (((i["llimit0"]>0)or(i["dlimit0"]>0))): 
      outpvar.cur.addfcdata("dispfood");
      outpvar.addchilds(newtag_dispfood({"dishinfo": i}, ginp, outpvar.cur.fcalldata["dispfood"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_select1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({"tlist": [], "class": "browser-default", "aclass": ""}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("select", extentattrs({"class": myadd(myadd(inp["class"], " "), inp["aclass"]), "name": inp["name"], "attr": inp["attr"]})));
  if ((inp["toptext"]!=None)): 
    outpvar.open(htmlnode("option", extentattrs({"attr": {"value": ""}})));
    outpvar.addtext(inp["toptext"]);
    outpvar.close();
  for ii in range(len(forlist(inp["tlist"]))) :
    i = inp["tlist"][ii];
    inp["attrs"] = {};
    if ((inp["vlist"]!=None)): 
      inp["attrs"]["value"] = inp["vlist"][ii];
    elif (1): 
      inp["attrs"]["value"] = myadd(ii, 1);
    if ((inp["selected"]==ii)): 
      inp["attrs"]["selected"] = "";
    outpvar.open(htmlnode("option", extentattrs({"attr": inp["attrs"]})));
    outpvar.addtext(i);
    outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_select2(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({"tlist": [], "dclass": "col l3 s12 m6", "class": "browser-default"}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs({"class": inp["dclass"]})));
  outpvar.cur.addfcdata("select1");
  outpvar.addchilds(newtag_select1({"class": inp["class"], "tlist": inp["tlist"], "vlist": inp["vlist"], "toptext": inp["toptext"], "selected": inp["selected"]}, ginp, outpvar.cur.fcalldata["select1"].root.content).root.content);
  outpvar.close();
  return outpvar;
  
def newtag_mselect(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({"tlist": []}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  for ii in range(len(forlist(inp["tlist"]))) :
    i = inp["tlist"][ii];
    inp["attrs"] = {};
    if ((inp["vlist"]!=None)): 
      inp["attrs"]["value"] = inp["vlist"][ii];
    elif (1): 
      inp["attrs"]["value"] = myadd(ii, 1);
    if ((inp["selected"]==ii)): 
      inp["attrs"]["selected"] = "";
    outpvar.cur.addfcdata("checkbox1");
    outpvar.addchilds(newtag_checkbox1({"label": i, "id": myadd(myadd(inp["id"], "_"), ii)}, ginp, outpvar.cur.fcalldata["checkbox1"].root.content).root.content);
  return outpvar;
  
def newtag_mselect1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({"tlist": []}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs({"id": inp["id"], "class": "dropdown-content p5", "tlist": []})));
  outpvar.cur.addfcdata("mselect");
  outpvar.addchilds(newtag_mselect({"vlist": inp["vlist"], "tlist": inp["tlist"], "id": inp["id"]}, ginp, outpvar.cur.fcalldata["mselect"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("a", extentattrs({"class": "dropdown-button", "data": {"activates": inp["id"]}})));
  outpvar.addtext(inp["label"]);
  outpvar.close();
  return outpvar;
  
def newtag_mselect2(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({"class": "col l3 s12 m6"}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs({"class": inp["class"]})));
  outpvar.open(htmlnode("div", extentattrs({"class": "mselect complexinput", "data": {"complexinput": "ci_checkbox"}, "attr": {"name": inp["id"]}})));
  outpvar.cur.addfcdata("mselect1");
  outpvar.addchilds(newtag_mselect1({"id": inp["id"], "tlist": inp["tlist"], "label": inp["label"], "selectall": inp["selectall"]}, ginp, outpvar.cur.fcalldata["mselect1"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_switch1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({"on": "Yes", "off": "No"}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs({"class": "switch"})));
  outpvar.open(htmlnode("label", extentattrs({})));
  outpvar.addtext(inp["off"]);
  outpvar.open(htmlnode("input", extentattrs({"attr": {"type": "checkbox", "name": inp["name"]}})));
  outpvar.open(htmlnode("span", extentattrs({"class": "lever"})));
  outpvar.close();
  outpvar.addtext(inp["on"]);
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_switch2(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({"class": "col l3 s12 m6"}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs({"class": inp["class"]})));
  outpvar.open(htmlnode("div", extentattrs({"class": "m5"})));
  outpvar.addtext(inp["label"]);
  outpvar.cur.addfcdata("switch1");
  outpvar.addchilds(newtag_switch1({"name": inp["name"]}, ginp, outpvar.cur.fcalldata["switch1"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_orderl_admin(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("table", extentattrs({"class": "bordered"})));
  outpvar.open(htmlnode("thead", extentattrs({})));
  for i in forlist(["Odered At", "Delivery Date", "Chef", "User", "Dish", "Price", "Chef Address", "User Address", "Status"]) :
    outpvar.open(htmlnode("th", extentattrs({})));
    outpvar.addtext(i);
    outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("tbody", extentattrs({})));
  for ii in range(len(forlist(inp["orderl"]))) :
    i = inp["orderl"][ii];
    outpvar.open(htmlnode("tr", extentattrs({"class": "cartitems", "datas": {"datetime": i["datetime"], "cid": i["cid"], "lord": i["lord"], "dishid": i["dishid"]}})));
    outpvar.open(htmlnode("td", extentattrs({})));
    outpvar.addtext(i["timetext"]);
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs({})));
    outpvar.addtext(i["datetimetext"]);
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs({})));
    outpvar.cur.addfcdata("profilea1");
    outpvar.addchilds(newtag_profilea1({"name": i["cname"], "uid": i["cid"]}, ginp, outpvar.cur.fcalldata["profilea1"].root.content).root.content);
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs({})));
    outpvar.cur.addfcdata("profilea1");
    outpvar.addchilds(newtag_profilea1({"name": i["uname"], "uid": i["uid"]}, ginp, outpvar.cur.fcalldata["profilea1"].root.content).root.content);
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs({})));
    outpvar.addtext(i["title"]);
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs({})));
    outpvar.cur.addfcdata("icon1");
    outpvar.addchilds(newtag_icon1({"img": "photo/inr2.png"}, ginp, outpvar.cur.fcalldata["icon1"].root.content).root.content);
    outpvar.open(htmlnode("span", extentattrs({"class": "itemprice"})));
    outpvar.addtext(myadd(myadd(myadd(myadd(i["price"], "*"), i["numplate"]), "="), (i["price"]*i["numplate"])));
    outpvar.close();
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs({})));
    outpvar.addtext(myadd(myadd(myadd(myadd(myadd("(", i["clat"]), ", "), i["clng"]), ")<br>"), i["caddress"]));
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs({})));
    outpvar.addtext(myadd(myadd(myadd(myadd(myadd("(", i["lat"]), ", "), i["lng"]), ")<br>"), i["uaddress"]));
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs({})));
    outpvar.addtext(i["status"]);
    outpvar.close();
    outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_orderl_user(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("table", extentattrs({"class": "bordered"})));
  outpvar.open(htmlnode("thead", extentattrs({})));
  for i in forlist(["Odered At", "Delivery Date", "Chef", "Dish", "Price", "User Address", "Status"]) :
    outpvar.open(htmlnode("th", extentattrs({})));
    outpvar.addtext(i);
    outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("tbody", extentattrs({})));
  for ii in range(len(forlist(inp["orderl"]))) :
    i = inp["orderl"][ii];
    outpvar.open(htmlnode("tr", extentattrs({"class": "cartitems", "datas": {"datetime": i["datetime"], "cid": i["cid"], "lord": i["lord"], "dishid": i["dishid"]}})));
    outpvar.open(htmlnode("td", extentattrs({})));
    outpvar.addtext(i["timetext"]);
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs({})));
    outpvar.addtext(i["datetimetext"]);
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs({})));
    outpvar.cur.addfcdata("profilea1");
    outpvar.addchilds(newtag_profilea1({"name": i["cname"], "uid": i["cid"]}, ginp, outpvar.cur.fcalldata["profilea1"].root.content).root.content);
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs({})));
    outpvar.addtext(i["title"]);
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs({})));
    outpvar.cur.addfcdata("icon1");
    outpvar.addchilds(newtag_icon1({"img": "photo/inr2.png"}, ginp, outpvar.cur.fcalldata["icon1"].root.content).root.content);
    outpvar.open(htmlnode("span", extentattrs({"class": "itemprice"})));
    outpvar.addtext(myadd(myadd(myadd(myadd(i["price"], "*"), i["numplate"]), "="), (i["price"]*i["numplate"])));
    outpvar.close();
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs({})));
    outpvar.addtext(myadd(myadd(myadd(myadd(myadd("(", i["lat"]), ", "), i["lng"]), ")<br>"), i["uaddress"]));
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs({})));
    outpvar.addtext(i["status"]);
    outpvar.close();
    outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_orderl_chef(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("table", extentattrs({"class": "bordered"})));
  outpvar.open(htmlnode("thead", extentattrs({})));
  for i in forlist(["Odered At", "Delivery Date", "User", "Dish", "Price", "User Address", "Status"]) :
    outpvar.open(htmlnode("th", extentattrs({})));
    outpvar.addtext(i);
    outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("tbody", extentattrs({})));
  for ii in range(len(forlist(inp["orderl"]))) :
    i = inp["orderl"][ii];
    outpvar.open(htmlnode("tr", extentattrs({"class": "cartitems", "datas": {"datetime": i["datetime"], "cid": i["cid"], "lord": i["lord"], "dishid": i["dishid"]}})));
    outpvar.open(htmlnode("td", extentattrs({})));
    outpvar.addtext(i["timetext"]);
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs({})));
    outpvar.addtext(i["datetimetext"]);
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs({})));
    outpvar.cur.addfcdata("profilea1");
    outpvar.addchilds(newtag_profilea1({"name": i["cname"], "uid": i["cid"]}, ginp, outpvar.cur.fcalldata["profilea1"].root.content).root.content);
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs({})));
    outpvar.cur.addfcdata("profilea1");
    outpvar.addchilds(newtag_profilea1({"name": i["uname"], "uid": i["uid"]}, ginp, outpvar.cur.fcalldata["profilea1"].root.content).root.content);
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs({})));
    outpvar.addtext(i["title"]);
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs({})));
    outpvar.cur.addfcdata("icon1");
    outpvar.addchilds(newtag_icon1({"img": "photo/inr2.png"}, ginp, outpvar.cur.fcalldata["icon1"].root.content).root.content);
    outpvar.open(htmlnode("span", extentattrs({"class": "itemprice"})));
    outpvar.addtext(myadd(myadd(myadd(myadd(i["price"], "*"), i["numplate"]), "="), (i["price"]*i["numplate"])));
    outpvar.close();
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs({})));
    outpvar.addtext(myadd(myadd(myadd(myadd(myadd("(", i["clat"]), ", "), i["clng"]), ")<br>"), i["caddress"]));
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs({})));
    outpvar.addtext(myadd(myadd(myadd(myadd(myadd("(", i["lat"]), ", "), i["lng"]), ")<br>"), i["uaddress"]));
    outpvar.close();
    outpvar.open(htmlnode("td", extentattrs({})));
    outpvar.addtext(i["status"]);
    outpvar.close();
    outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_orderl(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({"utype": ginp["islogin"]}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  if ((inp["utype"]=="u")): 
    outpvar.cur.addfcdata("orderl_user");
    outpvar.addchilds(newtag_orderl_user({"orderl": inp["orderl"]}, ginp, outpvar.cur.fcalldata["orderl_user"].root.content).root.content);
  if ((inp["utype"]=="c")): 
    outpvar.cur.addfcdata("orderl_chef");
    outpvar.addchilds(newtag_orderl_chef({"orderl": inp["orderl"]}, ginp, outpvar.cur.fcalldata["orderl_chef"].root.content).root.content);
  if ((inp["utype"]=="a")): 
    outpvar.cur.addfcdata("orderl_admin");
    outpvar.addchilds(newtag_orderl_admin({"orderl": inp["orderl"]}, ginp, outpvar.cur.fcalldata["orderl_admin"].root.content).root.content);
  return outpvar;
  
def newtag_errorbox(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs({"class": "row hiddenerror"})));
  outpvar.open(htmlnode("div", extentattrs({"class": "col s12 l12"})));
  outpvar.open(htmlnode("div", extentattrs({"class": "card-panel red white-text center errortext"})));
  outpvar.addtext("");
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_menu_nofood(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs({"class": "col l12 m12 s12"})));
  outpvar.cur.addfcdata("textdiv");
  outpvar.addchilds(newtag_textdiv({"name": "No chef is serving in this location. We are trying hard to serve you in this location, will let you know once this location is launched", "font": "20px"}, ginp, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
  outpvar.close();
  return outpvar;
  
def newtag_kurry_footer(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs({"class": "page-footer white darken-4", "style": {"margin-bottom": "0px", "padding-bottom": "0px"}})));
  outpvar.open(htmlnode("div", extentattrs({"class": "container"})));
  outpvar.open(htmlnode("div", extentattrs({"class": "row", "style": {"margin-bottom": "-25px"}})));
  outpvar.open(htmlnode("div", extentattrs({"class": "col s4 m4 l2"})));
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs({"class": "col s2 m2 l3"})));
  outpvar.cur.addfcdata("h5");
  outpvar.cur.fcalldata["h5"].addtext("Social Media");
  outpvar.addchilds(newtag_h5({}, ginp, outpvar.cur.fcalldata["h5"].root.content).root.content);
  outpvar.open(htmlnode("ul", extentattrs({})));
  outpvar.open(htmlnode("li", extentattrs({})));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1({"name": "Facebook", "href": myadd(inp["BASE"], "aboutus")}, ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("li", extentattrs({})));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1({"name": "Twitter"}, ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("li", extentattrs({})));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1({"name": "Instagram"}, ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs({"class": "col s2 m2 l3"})));
  outpvar.cur.addfcdata("h5");
  outpvar.cur.fcalldata["h5"].addtext("Help");
  outpvar.addchilds(newtag_h5({}, ginp, outpvar.cur.fcalldata["h5"].root.content).root.content);
  outpvar.open(htmlnode("ul", extentattrs({})));
  outpvar.open(htmlnode("li", extentattrs({})));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1({"name": "About us", "href": myadd(inp["BASE"], "aboutus")}, ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("li", extentattrs({})));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1({"name": "Contact us"}, ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs({"class": "col s2 m2 l3"})));
  outpvar.cur.addfcdata("h5");
  outpvar.cur.fcalldata["h5"].addtext("Legal");
  outpvar.addchilds(newtag_h5({}, ginp, outpvar.cur.fcalldata["h5"].root.content).root.content);
  outpvar.open(htmlnode("ul", extentattrs({})));
  outpvar.open(htmlnode("li", extentattrs({})));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1({"name": "T&C", "href": myadd(inp["BASE"], "aboutus")}, ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("li", extentattrs({})));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1({"name": "Policy"}, ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs({"class": "row"})));
  outpvar.open(htmlnode("div", extentattrs({"class": "col l12 align-left "})));
  outpvar.addtext("&copy; Copyright 2015 KurryBox");
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_cp_contactus_form(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs({"class": "row"})));
  outpvar.open(htmlnode("div", extentattrs({"class": "col s12 l12 m12"})));
  outpvar.cur.addfcdata("h3");
  outpvar.cur.fcalldata["h3"].open(htmlnode("p", extentattrs("Contact US")));
  outpvar.cur.fcalldata["h3"].close();
  outpvar.addchilds(newtag_h3({"class": "grey-text text-darken-4"}, ginp, outpvar.cur.fcalldata["h3"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs({"class": "col s12 l6 m6"})));
  outpvar.cur.addfcdata("h5");
  outpvar.cur.fcalldata["h5"].open(htmlnode("p", extentattrs("Address")));
  outpvar.cur.fcalldata["h5"].close();
  outpvar.cur.fcalldata["h5"].cur.addfcdata("icon");
  outpvar.cur.fcalldata["h5"].addchilds(newtag_icon({"name": "navigation", "aclass": "tiny"}, ginp, outpvar.cur.fcalldata["h5"].cur.fcalldata["icon"].root.content).root.content);
  outpvar.addchilds(newtag_h5({"class": "grey-text text-darken-2"}, ginp, outpvar.cur.fcalldata["h5"].root.content).root.content);
  outpvar.open(htmlnode("div", extentattrs({"class": "grey-text"})));
  outpvar.open(htmlnode("p", extentattrs("58/1 2nd Floor,<br> Kalu Sarai<br>  Near Hauz Khas Metro Station<br> New Delhi - 110016<br>India")));
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs({"class": "col s12 l6 m6"})));
  outpvar.cur.addfcdata("h5");
  outpvar.cur.fcalldata["h5"].open(htmlnode("p", extentattrs("Mail")));
  outpvar.cur.fcalldata["h5"].close();
  outpvar.cur.fcalldata["h5"].cur.addfcdata("icon");
  outpvar.cur.fcalldata["h5"].addchilds(newtag_icon({"name": "mail", "aclass": "tiny"}, ginp, outpvar.cur.fcalldata["h5"].cur.fcalldata["icon"].root.content).root.content);
  outpvar.addchilds(newtag_h5({"class": "grey-text text-darken-2"}, ginp, outpvar.cur.fcalldata["h5"].root.content).root.content);
  outpvar.open(htmlnode("div", extentattrs({"class": "grey-text"})));
  outpvar.open(htmlnode("p", extentattrs("mohitsaini1196@gmail.com")));
  outpvar.close();
  outpvar.close();
  outpvar.cur.addfcdata("h5");
  outpvar.cur.fcalldata["h5"].open(htmlnode("p", extentattrs("Call")));
  outpvar.cur.fcalldata["h5"].close();
  outpvar.cur.fcalldata["h5"].cur.addfcdata("icon");
  outpvar.cur.fcalldata["h5"].addchilds(newtag_icon({"name": "call", "aclass": "tiny"}, ginp, outpvar.cur.fcalldata["h5"].cur.fcalldata["icon"].root.content).root.content);
  outpvar.addchilds(newtag_h5({"class": "grey-text text-darken-2"}, ginp, outpvar.cur.fcalldata["h5"].root.content).root.content);
  outpvar.open(htmlnode("div", extentattrs({"class": "grey-text"})));
  outpvar.open(htmlnode("p", extentattrs("+91 750 375 9053")));
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_cp_our_story(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs({"class": "card-content"})));
  outpvar.cur.addfcdata("h3");
  outpvar.cur.fcalldata["h3"].open(htmlnode("p", extentattrs("Our Story")));
  outpvar.cur.fcalldata["h3"].close();
  outpvar.addchilds(newtag_h3({"class": "card-title"}, ginp, outpvar.cur.fcalldata["h3"].root.content).root.content);
  outpvar.open(htmlnode("div", extentattrs({})));
  outpvar.open(htmlnode("p", extentattrs(inp["our_story_content"])));
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_headertabs_cp(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("li", extentattrs({})));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1({"name": "MyFav", "attr": {"onclick": "$(\"#myfavlist\").openModal();"}}, ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("li", extentattrs({})));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1({"name": "Contact Us", "attr": {"onclick": "$(\"#contactusform\").openModal();"}}, ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("li", extentattrs({})));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1({"name": "Our Story", "attr": {"onclick": "$(\"#ourstory\").openModal();"}}, ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("li", extentattrs({})));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1({"name": "Provider Form", "attr": {"onclick": "$(\"#providerform\").openModal();"}}, ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  return outpvar;
  
def newtag_cp_filterform(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs({"class": "row"})));
  outpvar.open(htmlnode("div", extentattrs({"class": "col l11 s11 m11", "id": "mainfilter"})));
  outpvar.open(htmlnode("div", extentattrs({"style": {"padding": "8px", "margin-bottom": "4px"}, "class": "card-panel"})));
  outpvar.open(htmlnode("input", extentattrs({"attr": {"placeholder": "Search Location", "autofocus": "true"}, "class": "inputplaceholder mainsearch", "style": {"border-radius": "0px", "border": "solid black 0px", "font-size": "13px"}, "id": "searchloc"})));
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs({"style": {"margin-top": "0px", "padding": "8px", "margin-bottom": "-5px"}, "class": "card-panel"})));
  outpvar.open(htmlnode("form", extentattrs({"data": {"onsubmit": "sreq", "bobj": "", "action": "search", "res": "draw_points(data.data);"}})));
  outpvar.open(htmlnode("input", extentattrs({"attr": {"placeholder": "Search keywords", "name": "keyw"}, "class": "inputplaceholder mainsearch", "style": {"border-radius": "0px", "border": "solid black 0px", "font-size": "13px"}})));
  outpvar.open(htmlnode("button", extentattrs({"attr": {"type": "submit"}, "style": {"display": "none"}})));
  outpvar.close();
  outpvar.close();
  outpvar.close();
  if (1): 
    outpvar.open(htmlnode("ul", extentattrs({"class": "collapsible", "attr": {"data-collapsible": "accordion"}})));
    for ii in range(len(forlist(inp["catg"]))) :
      i = inp["catg"][ii];
      outpvar.open(htmlnode("li", extentattrs({})));
      outpvar.open(htmlnode("div", extentattrs({"class": "collapsible-header"})));
      outpvar.cur.addfcdata("icon1");
      outpvar.addchilds(newtag_icon1({"img": i["icon"]}, ginp, outpvar.cur.fcalldata["icon1"].root.content).root.content);
      outpvar.open(htmlnode("p", extentattrs(i["name"])));
      outpvar.close();
      outpvar.close();
      outpvar.open(htmlnode("div", extentattrs({"class": "collapsible-body"})));
      outpvar.open(htmlnode("div", extentattrs({"class": "subcats1", "style": {"padding": "5px", "padding-left": "20px", "padding-bottom": "0px", "padding-top": "0px"}})));
      outpvar.open(htmlnode("ul", extentattrs({"class": "collapsible_sub", "attr": {"data-collapsible": "accordion"}})));
      for jj in range(len(forlist(i["child"]))) :
        j = i["child"][jj];
        outpvar.open(htmlnode("li", extentattrs({"class": ""})));
        outpvar.open(htmlnode("div", extentattrs({"class": "collapsible-header", "style": {"border-bottom": "solid black 0px", "border-top": "1px solid #DDD"}})));
        outpvar.open(htmlnode("p", extentattrs(j["name"])));
        outpvar.close();
        outpvar.close();
        outpvar.open(htmlnode("div", extentattrs({"class": "collapsible-body"})));
        outpvar.open(htmlnode("div", extentattrs({"class": "subcats2", "style": {"padding-left": "30px"}})));
        outpvar.open(htmlnode("ul", extentattrs({})));
        outpvar.open(htmlnode("li", extentattrs({})));
        outpvar.open(htmlnode("div", extentattrs({})));
        outpvar.cur.addfcdata("checkbox1");
        outpvar.addchilds(newtag_checkbox1({"label": "Select All", "id": myadd(myadd(myadd(myadd(myadd("catsubcat", ii), "_"), jj), "_"), "selectall"), "aclass": "selectall", "data": {"onclick": "selectall redraw", "catgtid": myadd(myadd(i["id"], "_"), j["id"])}, "labels": {"font-size": "12px"}}, ginp, outpvar.cur.fcalldata["checkbox1"].root.content).root.content);
        outpvar.close();
        outpvar.close();
        for kk in range(len(forlist(j["child"]))) :
          k = j["child"][kk];
          outpvar.open(htmlnode("li", extentattrs({})));
          outpvar.open(htmlnode("div", extentattrs({})));
          outpvar.cur.addfcdata("checkbox1");
          outpvar.addchilds(newtag_checkbox1({"label": k["name"], "id": myadd(myadd(myadd(myadd(myadd("catsubcat", ii), "_"), jj), "_"), kk), "data": {"catgtid": myadd(myadd(myadd(myadd(i["id"], "_"), j["id"]), "_"), k["id"]), "onclick": "redraw"}, "labels": {"font-size": "12px"}}, ginp, outpvar.cur.fcalldata["checkbox1"].root.content).root.content);
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
    outpvar.open(htmlnode("div", extentattrs({"style": {"background-color": "white", "padding": "5px"}})));
    outpvar.cur.addfcdata("a1");
    outpvar.addchilds(newtag_a1({"name": "See All Cats", "attr": {"onclick": "$(\"#commoncats\").openModal();"}}, ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
    outpvar.close();
    outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs({"class": "col l1 s1 m1"})));
  outpvar.open(htmlnode("div", extentattrs({"style": {"padding": "8px", "margin-bottom": "4px", "padding-left": "0px", "margin-left": "-20px"}})));
  outpvar.cur.addfcdata("icon1");
  outpvar.addchilds(newtag_icon1({"img": "photo/minimize1.png", "class": "pointer", "attr": {"onclick": "minimaxifilter(1);"}}, ginp, outpvar.cur.fcalldata["icon1"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_cp_selectallcatgs(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs({"class": "row"})));
  outpvar.open(htmlnode("div", extentattrs({"class": "col s6 l6 m6"})));
  outpvar.open(htmlnode("p", extentattrs("Select The Cats")));
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs({"class": "col s6 l6 m6"})));
  outpvar.cur.addfcdata("button1");
  outpvar.addchilds(newtag_button1({"name": "OK", "attr": {"onclick": " $(\"#commoncats\").closeModal();"}}, ginp, outpvar.cur.fcalldata["button1"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs({"class": "row"})));
  outpvar.open(htmlnode("ul", extentattrs({"class": "tabs"})));
  for ii in range(len(forlist(inp["catg"]))) :
    i = inp["catg"][ii];
    outpvar.open(htmlnode("li", extentattrs({"class": "tab col l4 m4 s4"})));
    outpvar.cur.addfcdata("a1");
    outpvar.addchilds(newtag_a1({"href": myadd("#modal", i["name"]), "name": i["name"]}, ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
    outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs({"class": "row"})));
  for ii in range(len(forlist(inp["catg"]))) :
    i = inp["catg"][ii];
    outpvar.open(htmlnode("div", extentattrs({"id": myadd("modal", i["name"]), "class": "row"})));
    for j in forlist(4) :
      outpvar.open(htmlnode("div", extentattrs({"class": "col l3 m3 s6"})));
      for kk in range(len(forlist(inp["commoncats"][ii][j]))) :
        k = inp["commoncats"][ii][j][kk];
        outpvar.open(htmlnode("div", extentattrs({})));
        outpvar.cur.addfcdata("checkbox1");
        outpvar.addchilds(newtag_checkbox1({"label": k[0], "id": myadd(myadd(myadd(myadd(myadd("commoncats_", ii), "_"), j), "_"), kk), "lstyle": {"color": "black", "font-size": "20px"}, "data": {"onclick": "selectall"}, "labels": {"color": "black"}}, ginp, outpvar.cur.fcalldata["checkbox1"].root.content).root.content);
        outpvar.open(htmlnode("div", extentattrs({"style": {"font-wight": 700, "font-size": "18px"}})));
        outpvar.close();
        for ll in range(len(forlist(k))) :
          l = k[ll];
          if ((ll!=0)): 
            outpvar.open(htmlnode("div", extentattrs({})));
            outpvar.cur.addfcdata("checkbox1");
            outpvar.addchilds(newtag_checkbox1({"label": l, "id": myadd(myadd(myadd(myadd(myadd(myadd(myadd("commoncats_", ii), "_"), j), "_"), kk), "_"), ll), "labels": {"font-size": "12px"}}, ginp, outpvar.cur.fcalldata["checkbox1"].root.content).root.content);
            outpvar.close();
        outpvar.close();
      outpvar.close();
    outpvar.close();
  outpvar.close();
  return outpvar;
  