#This code is auto generated code, don't Edit it 
def newtag_main(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("acss", ["css/materialize_mohit.css?reload", "css/lib.css", "css/custom-stylesheet.css", "css/jquery.bxslider.css", "https://fonts.googleapis.com/icon?family=Material+Icons", "css/lib.css", "css/main.css", "css/style.css"]), ("ajs", ["mslib/js/jquery-2.1.1.min.js", "mslib/js/materialize.min.js", "mslib/js/jquery.bxslider.min.js", "mslib/js/jquery.easing.1.3.js", "mslib/js/jquery.raty.js", "mslib/js/lib.js?reload", "mslib/js/mohit.js", "mslib/js/mohitlib.js?reload", "mslib/js/main.js?reload"]), ("title", "Class Pundit"), ("css", []), ("js", []), ("bodystyle", cod([])), ("htmlstyle", cod([]))])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  inp["css"] = myadd(inp["acss"], inp["css"]);
  inp["js"] = myadd(inp["ajs"], inp["js"]);
  outpvar.addtext("<!DOCTYPE html>");
  outpvar.open(htmlnode("html", extentattrs(cod([("style", inp["htmlstyle"])]))));
  outpvar.open(htmlnode("head", extentattrs(cod([]))));
  outpvar.open(htmlnode("base", extentattrs(cod([("attr", cod([("href", inp["HOST"])]))]))));
  outpvar.open(htmlnode("title", extentattrs(cod([]))));
  outpvar.addtext(inp["title"]);
  outpvar.close();
  for i in forlist(inp["css"], False ) :
    outpvar.open(htmlnode("link", extentattrs(cod([("attr", cod([("href", i), ("rel", "stylesheet"), ("type", "text/css")]))]))));
  outpvar.close();
  outpvar.open(htmlnode("body", extentattrs(cod([("style", inp["bodystyle"])]))));
  outpvar.addchilds(innerHTML);
  outpvar.open(htmlnode("script", extentattrs(cod([("attr", cod([("type", "text/javascript")]))]))));
  outpvar.addtext(myadd(myadd("var jsdata = ", inp["jsdata"]), ";"));
  outpvar.close();
  outpvar.open(htmlnode("script", extentattrs(cod([("attr", cod([("type", "text/javascript")]))]))));
  outpvar.addtext("var ec  = jsdata['_ec'] ;");
  outpvar.addtext("var ve  = jsdata['_formerror'];");
  outpvar.close();
  for i in forlist(inp["js"], False ) :
    outpvar.open(htmlnode("script", extentattrs(cod([("attr", cod([("type", "text/javascript"), ("src", i)]))]))));
    outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_disptabs(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("tabname", []), ("tablink", []), ("liclass", None), ("active", None)])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  for j in forlist(inp["tabname"], True ) :
    i = inp["tabname"][j];
    outpvar.open(htmlnode("li", extentattrs(cod([("class", inp["liclass"])]))));
    inp["isactive"] = ("active" if (int((inp["active"] == inp["tablink"][j]))) else " ");
    outpvar.open(htmlnode("a", extentattrs(cod([("attr", cod([("href", inp["tablink"][j])])), ("class", inp["isactive"])]))));
    outpvar.addtext(i);
    outpvar.close();
    outpvar.close();
  return outpvar;
  
def newtag_header1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("tabname", []), ("tablink", [])])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "navbar-fixed ")]))));
  outpvar.open(htmlnode("nav", extentattrs(cod([("class", "white"), ("attr", cod([("role", "container")]))]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "nav-wrapper container")]))));
  outpvar.open(htmlnode("a", extentattrs(cod([("attr", cod([("id", "logo-container"), ("href", inp["HOST"])])), ("class", "brand-logo")]))));
  outpvar.open(htmlnode("img", extentattrs(cod([("attr", cod([("src", "photo/mylogo1.png")])), ("class", "circle responsive-img"), ("style", cod([("vertical-align", "middle")]))]))));
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs(cod([("class", "right hide-on-med-and-down")]))));
  outpvar.cur.addfcdata("disptabs");
  outpvar.addchilds(newtag_disptabs(cod([("tabname", inp["tabname"]), ("tablink", inp["tablink"])]), ginp, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_header1_cp(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("tabname", []), ("tablink", [])])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "navbar-fixed ")]))));
  outpvar.open(htmlnode("nav", extentattrs(cod([("class", "white"), ("attr", cod([("role", "container")]))]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "nav-wrapper container")]))));
  outpvar.open(htmlnode("a", extentattrs(cod([("attr", cod([("id", "logo-container"), ("href", inp["HOST"])])), ("class", "brand-logo")]))));
  outpvar.open(htmlnode("img", extentattrs(cod([("attr", cod([("src", "photo/mylogo1.png")])), ("class", "circle responsive-img"), ("style", cod([("vertical-align", "middle")]))]))));
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs(cod([("class", "right hide-on-med-and-down")]))));
  outpvar.cur.addfcdata("disptabs");
  outpvar.addchilds(newtag_disptabs(cod([("tabname", inp["tabname"]), ("tablink", inp["tablink"])]), ginp, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
  outpvar.cur.addfcdata("headertabs_cp");
  outpvar.addchilds(newtag_headertabs_cp(cod([]), ginp, outpvar.cur.fcalldata["headertabs_cp"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs(cod([("id", "nav-mobile"), ("class", "side-nav")]))));
  outpvar.cur.addfcdata("headertabs_cp");
  outpvar.addchilds(newtag_headertabs_cp(cod([]), ginp, outpvar.cur.fcalldata["headertabs_cp"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("a", extentattrs(cod([("attr", cod([("data-activates", "nav-mobile")])), ("class", "button-collapse")]))));
  outpvar.cur.addfcdata("icon");
  outpvar.addchilds(newtag_icon(cod([("name", "menu")]), ginp, outpvar.cur.fcalldata["icon"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_icon(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("aclass", "")])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("i", extentattrs(cod([("class", myadd("material-icons ", inp["aclass"])), ("style", inp["style"])]))));
  outpvar.addtext(inp["name"]);
  outpvar.close();
  return outpvar;
  
def newtag_icon1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("class", None)])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  inp["attr"]["src"] = inp["img"];
  outpvar.open(htmlnode("img", extentattrs(cod([("attr", inp["attr"]), ("style", cod([("margin-bottom", "-5px")])), ("class", inp["class"])]))));
  return outpvar;
  
def newtag_checkbox1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("checked", None), ("label", "Check"), ("aclass", ""), ("labels", cod([]))])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("span", extentattrs(cod([]))));
  outpvar.open(htmlnode("input", extentattrs(cod([("attr", cod([("type", "checkbox"), ("id", inp["id"]), ("checked", inp["checked"])])), ("class", myadd("filled-in ", inp["aclass"])), ("data", inp["data"])]))));
  outpvar.open(htmlnode("label", extentattrs(cod([("attr", cod([("for", inp["id"])])), ("style", inp["labels"])]))));
  outpvar.addtext(inp["label"]);
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_checkbox2(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("checked", None), ("label", "Check"), ("aclass", ""), ("labels", cod([]))])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("span", extentattrs(cod([]))));
  outpvar.open(htmlnode("input", extentattrs(cod([("attr", cod([("type", "radio"), ("id", inp["id"]), ("checked", inp["checked"])])), ("class", myadd("with-gap ", inp["aclass"])), ("data", inp["data"])]))));
  outpvar.open(htmlnode("label", extentattrs(cod([("attr", cod([("for", inp["id"])])), ("style", inp["labels"])]))));
  outpvar.addtext(inp["label"]);
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_bigf(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("font", "65px")])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("span", extentattrs(cod([("style", cod([("font-size", inp["font"]), ("text-shadow", "3px 3px 3px #000, 2px 2px 2px blue")])), ("color", inp["color"])]))));
  outpvar.addtext(inp["name"]);
  outpvar.close();
  return outpvar;
  
def newtag_bigf1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("font", "40px")])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.cur.addfcdata("bigf");
  outpvar.addchilds(newtag_bigf(cod([("color", inp["color"]), ("font", inp["font"]), ("name", inp["name"])]), ginp, outpvar.cur.fcalldata["bigf"].root.content).root.content);
  return outpvar;
  
def newtag_height(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("style", cod([("height", myadd(inp["val"], "px"))]))]))));
  outpvar.close();
  return outpvar;
  
def newtag_resimg(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("aclass", ""), ("opacity", None)])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("img", extentattrs(cod([("class", myadd("responsive-img ", inp["aclass"])), ("attr", cod([("src", inp["src"])])), ("style", cod([("opacity", inp["opacity"])]))]))));
  return outpvar;
  
def newtag_circleimg(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("opacity", None)])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.cur.addfcdata("resimg");
  outpvar.addchilds(newtag_resimg(cod([("aclass", "circle"), ("src", inp["src"]), ("opacity", inp["opacity"])]), ginp, outpvar.cur.fcalldata["resimg"].root.content).root.content);
  return outpvar;
  
def newtag_divpedding(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("text", ""), ("padding", "5px")])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("style", cod([("padding", inp["padding"])])), ("class", inp["class"])]))));
  outpvar.addtext(inp["text"]);
  outpvar.addchilds(innerHTML);
  outpvar.close();
  return outpvar;
  
def newtag_textdiv(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("text", ""), ("fontw", None), ("font", None), ("color", None), ("class", None), ("id", None)])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("style", cod([("font-size", inp["font"]), ("font-weight", inp["fontw"])])), ("color", inp["color"]), ("class", inp["class"]), ("id", inp["id"])]))));
  outpvar.addchilds(innerHTML);
  outpvar.addtext(inp["text"]);
  outpvar.close();
  return outpvar;
  
def newtag_textdiv1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("font", "20px"), ("fontw", None), ("color", None), ("class", None), ("text", "")])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.cur.addfcdata("textdiv");
  outpvar.addchilds(newtag_textdiv(cod([("font", inp["font"]), ("fontw", inp["fontw"]), ("color", inp["color"]), ("class", inp["class"]), ("text", inp["text"])]), ginp, outpvar.cur.fcalldata["textdiv"].root.content).root.content);
  return outpvar;
  
def newtag_a1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("class", None), ("text", None), ("href", None)])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("a", extentattrs(cod([("attr", inp["attr"]), ("style", inp["style"]), ("class", inp["class"])]))));
  outpvar.addtext(inp["text"]);
  outpvar.close();
  return outpvar;
  
def newtag_starrating(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("val", 5)])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  for i in forlist(inp["val"], False ) :
    outpvar.open(htmlnode("img", extentattrs(cod([("attr", cod([("src", "photo/rating4.png")])), ("style", cod([("margin", "-1px"), ("width", "22px")]))]))));
  return outpvar;
  
def newtag_input1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("aclass", "col s6"), ("type", "text"), ("dc", "simple"), ("icon", None), ("dname", None), ("value", None), ("iclass", None), ("disabled", None)])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", myadd("input-field ", inp["aclass"]))]))));
  if (inp["icon"]): 
    outpvar.cur.addfcdata("icon");
    outpvar.addchilds(newtag_icon(cod([("name", inp["icon"]), ("aclass", "prefix")]), ginp, outpvar.cur.fcalldata["icon"].root.content).root.content);
  inp["data"]["name"] = inp["label"];
  inp["data"]["dc"] = inp["dc"];
  if (int((inp["dname"] != None))): 
    inp["data"]["name"] = inp["dname"];
  outpvar.open(htmlnode("input", extentattrs(cod([("attr", cod([("id", inp["id"]), ("type", inp["type"]), ("value", inp["value"]), ("disabled", inp["disabled"])])), ("class", inp["iclass"]), ("data", inp["data"])]))));
  outpvar.open(htmlnode("label", extentattrs(cod([("attr", cod([("for", inp["id"])]))]))));
  outpvar.addtext(inp["label"]);
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_input2(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("aclass", "col s6"), ("type", "text"), ("iclass", None), ("label", None), ("placeholder", None)])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", myadd("input-field ", inp["aclass"]))]))));
  outpvar.open(htmlnode("input", extentattrs(cod([("attr", cod([("id", inp["id"]), ("type", inp["type"]), ("name", inp["id"]), ("placeholder", inp["placeholder"])])), ("class", inp["iclass"])]))));
  outpvar.open(htmlnode("label", extentattrs(cod([("attr", cod([("for", inp["id"])]))]))));
  outpvar.addtext(inp["label"]);
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_input3(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("aclass", "col s6"), ("type", "text"), ("dc", "simple"), ("icon", None), ("dname", None), ("value", None), ("iclass", ""), ("name", None)])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", myadd("input-field ", inp["aclass"]))]))));
  if (inp["icon"]): 
    outpvar.cur.addfcdata("icon");
    outpvar.addchilds(newtag_icon(cod([("name", inp["icon"]), ("aclass", "prefix")]), ginp, outpvar.cur.fcalldata["icon"].root.content).root.content);
  inp["data"]["name"] = inp["label"];
  inp["data"]["dc"] = inp["dc"];
  if (int((inp["dname"] != None))): 
    inp["data"]["name"] = inp["dname"];
  outpvar.open(htmlnode("input", extentattrs(cod([("attr", cod([("type", inp["type"]), ("value", inp["value"]), ("placeholder", inp["label"]), ("name", inp["name"])])), ("class", myadd("inputph ", inp["iclass"])), ("data", inp["data"])]))));
  outpvar.close();
  return outpvar;
  
def newtag_textarea1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("aclass", "col l12 m12 s12")])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", myadd("input-field ", inp["aclass"]))]))));
  outpvar.open(htmlnode("textarea", extentattrs(cod([("attr", cod([("id", inp["id"]), ("name", inp["id"])])), ("class", "materialize-textarea")]))));
  outpvar.close();
  outpvar.open(htmlnode("label", extentattrs(cod([("attr", cod([("for", inp["id"])]))]))));
  outpvar.addtext(inp["label"]);
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_button1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("aclass", "")])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("button", extentattrs(cod([("class", myadd("btn waves-effect waves-light btn ", inp["aclass"])), ("data", inp["data"]), ("attr", inp["attr"]), ("datas", inp["datas"])]))));
  outpvar.addtext(inp["name"]);
  outpvar.close();
  return outpvar;
  
def newtag_button2(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("aclass", ""), ("text", "Submit")])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("button", extentattrs(cod([("class", myadd("btn waves-effect waves-light btn ", inp["aclass"])), ("data", inp["data"]), ("attr", inp["attr"]), ("datas", inp["datas"])]))));
  outpvar.addtext(inp["text"]);
  outpvar.close();
  return outpvar;
  
def newtag_hidinp(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("name", None), ("value", None)])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("input", extentattrs(cod([("attr", cod([("type", "hidden"), ("name", inp["name"]), ("value", inp["value"])]))]))));
  return outpvar;
  
def newtag_popupmodal(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("title", "Mohit Saini"), ("body", "")])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("attr", cod([("id", inp["id"])])), ("class", "modal")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "modal-content container-fluid")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l12 m12 s12 realtexttitle"), ("style", cod([("font-size", "20px")]))]))));
  outpvar.addtext(inp["title"]);
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l12 m12 s12 realtext")]))));
  outpvar.addtext(inp["body"]);
  outpvar.addchilds(innerHTML);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_popupmodal_confirm(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("title", "Mohit Saini"), ("body", "")])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("attr", cod([("id", inp["id"])])), ("class", "modal")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "modal-content container-fluid")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l12 m12 s12 realtexttitle"), ("style", cod([("font-size", "20px")]))]))));
  outpvar.addtext(inp["title"]);
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l12 m12 s12 realtext")]))));
  outpvar.addtext(inp["body"]);
  outpvar.addchilds(innerHTML);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "modal-footer")]))));
  outpvar.cur.addfcdata("button2");
  outpvar.addchilds(newtag_button2(cod([("aclass", "realyes modal-action modal-close"), ("text", "Agree")]), ginp, outpvar.cur.fcalldata["button2"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_main_cp(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("css", []), ("js", []), ("bodystyle", cod([])), ("htmlstyle", cod([])), ("title", "Class Pundit")])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  inp["js"] = myadd(["js/main.js"], inp["js"]);
  outpvar.cur.addfcdata("main");
  outpvar.cur.fcalldata["main"].addchilds(innerHTML);
  outpvar.addchilds(newtag_main(cod([("title", inp["title"]), ("css", inp["css"]), ("js", inp["js"]), ("bodystyle", inp["bodystyle"]), ("htmlstyle", inp["htmlstyle"])]), ginp, outpvar.cur.fcalldata["main"].root.content).root.content);
  return outpvar;
  
def newtag_header1_cp(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([("tabname", []), ("tablink", [])])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "navbar-fixed ")]))));
  outpvar.open(htmlnode("nav", extentattrs(cod([("class", "white")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "nav-wrapper container")]))));
  outpvar.open(htmlnode("a", extentattrs(cod([("attr", cod([("href", inp["HOST"])])), ("class", ""), ("style", cod([("display", "inline-block")]))]))));
  outpvar.open(htmlnode("img", extentattrs(cod([("attr", cod([("src", "photo/logo2.png")])), ("class", "responsive-img"), ("style", cod([("vertical-align", "middle")]))]))));
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs(cod([("class", "right hide-on-med-and-down")]))));
  outpvar.cur.addfcdata("disptabs");
  outpvar.addchilds(newtag_disptabs(cod([("tabname", inp["tabname"]), ("tablink", inp["tablink"])]), ginp, outpvar.cur.fcalldata["disptabs"].root.content).root.content);
  outpvar.cur.addfcdata("headertabs_cp");
  outpvar.addchilds(newtag_headertabs_cp(cod([]), ginp, outpvar.cur.fcalldata["headertabs_cp"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs(cod([("id", "nav-mobile"), ("class", "side-nav")]))));
  outpvar.cur.addfcdata("headertabs_cp");
  outpvar.addchilds(newtag_headertabs_cp(cod([]), ginp, outpvar.cur.fcalldata["headertabs_cp"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("a", extentattrs(cod([("attr", cod([("data-activates", "nav-mobile")])), ("class", "button-collapse")]))));
  outpvar.cur.addfcdata("icon");
  outpvar.addchilds(newtag_icon(cod([("name", "menu")]), ginp, outpvar.cur.fcalldata["icon"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("ul", extentattrs(cod([("class", "right hide-on-large-only")]))));
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.open(htmlnode("a", extentattrs(cod([]))));
  outpvar.open(htmlnode("span", extentattrs(cod([("class", "hide-on-med-and-up")]))));
  outpvar.addtext("Search");
  outpvar.close();
  outpvar.open(htmlnode("span", extentattrs(cod([("class", "hide-on-small-and-down")]))));
  outpvar.addtext("Filter");
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "hide-on-small-and-down"), ("style", cod([("display", "block"), ("float", "right"), ("line-height", "30px"), ("color", "black"), ("width", "280px"), ("padding-right", "20px")]))]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l12 m12 s12")]))));
  outpvar.open(htmlnode("input", extentattrs(cod([("attr", cod([("placeholder", "Search by address (Street, City, ZIP, etc)"), ("autofocus", "true")])), ("class", "inputplaceholder mainsearch"), ("style", cod([("border-radius", "0px"), ("border", "solid #cccccc 1px"), ("font-size", "13px"), ("padding", "4px")])), ("id", "searchloc1")]))));
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l12 m12 s12")]))));
  outpvar.open(htmlnode("form", extentattrs(cod([("data", cod([("onsubmit", "sreq"), ("bobj", ""), ("action", "search"), ("res", "draw_points(data.data);")]))]))));
  outpvar.open(htmlnode("input", extentattrs(cod([("attr", cod([("placeholder", "Search using keywords (Eg: Piano)"), ("name", "keyw")])), ("class", "inputplaceholder mainsearch"), ("style", cod([("border-radius", "0px"), ("border", "solid #cccccc 1px"), ("font-size", "13px"), ("padding", "4px")]))]))));
  outpvar.open(htmlnode("button", extentattrs(cod([("attr", cod([("type", "submit")])), ("style", cod([("display", "none")]))]))));
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_cp_contactus_form(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col s12 l12 m12")]))));
  outpvar.open(htmlnode("h3", extentattrs(cod([("class", "grey-text text-darken-4")]))));
  outpvar.addtext("Contact US");
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col s12 l12 m12")]))));
  outpvar.open(htmlnode("h5", extentattrs(cod([("class", "grey-text text-darken-2")]))));
  outpvar.addtext("Mail");
  outpvar.cur.addfcdata("icon");
  outpvar.addchilds(newtag_icon(cod([("name", "mail"), ("aclass", "tiny")]), ginp, outpvar.cur.fcalldata["icon"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "grey-text")]))));
  outpvar.addtext("info@classpundit.com");
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_cp_our_story(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "card-content")]))));
  outpvar.open(htmlnode("h3", extentattrs(cod([("class", "card-title")]))));
  outpvar.addtext("Our Story");
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([]))));
  outpvar.addtext(inp["our_story_content"]);
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_headertabs_cp(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1(cod([("text", "Favorites"), ("attr", cod([("onclick", "$(\"#myfavlist\").openModal();")]))]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1(cod([("text", "Contact Us"), ("attr", cod([("onclick", "$(\"#contactusform\").openModal();")]))]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1(cod([("text", "Our Story"), ("attr", cod([("onclick", "$(\"#ourstory\").openModal();")]))]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  outpvar.open(htmlnode("li", extentattrs(cod([]))));
  outpvar.cur.addfcdata("a1");
  outpvar.addchilds(newtag_a1(cod([("text", "Suggest a Provider"), ("attr", cod([("onclick", "$(\"#providerform\").openModal();")]))]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
  outpvar.close();
  return outpvar;
  
def newtag_cp_filterform(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l11 s11 m11"), ("id", "mainfilter")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("style", cod([("padding", "8px"), ("margin-bottom", "4px")])), ("class", "card-panel")]))));
  outpvar.open(htmlnode("input", extentattrs(cod([("attr", cod([("placeholder", "Search by address (Street, City, ZIP, etc)"), ("autofocus", "true")])), ("class", "inputplaceholder mainsearch"), ("style", cod([("border-radius", "0px"), ("border", "solid black 0px"), ("font-size", "13px")])), ("id", "searchloc")]))));
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("style", cod([("margin-top", "0px"), ("padding", "8px"), ("margin-bottom", "-5px")])), ("class", "card-panel")]))));
  outpvar.open(htmlnode("form", extentattrs(cod([("data", cod([("onsubmit", "sreq"), ("bobj", ""), ("action", "search"), ("res", "draw_points(data.data);")]))]))));
  outpvar.open(htmlnode("input", extentattrs(cod([("attr", cod([("placeholder", "Search using keywords (Eg: Piano)"), ("name", "keyw")])), ("class", "inputplaceholder mainsearch"), ("style", cod([("border-radius", "0px"), ("border", "solid black 0px"), ("font-size", "13px")]))]))));
  outpvar.open(htmlnode("button", extentattrs(cod([("attr", cod([("type", "submit")])), ("style", cod([("display", "none")]))]))));
  outpvar.close();
  outpvar.close();
  outpvar.close();
  if (1): 
    outpvar.open(htmlnode("ul", extentattrs(cod([("class", "collapsible"), ("attr", cod([("data-collapsible", "accordion")])), ("style", cod([("margin-bottom", "0px")]))]))));
    for ii in forlist(inp["catg"], True ) :
      i = inp["catg"][ii];
      outpvar.open(htmlnode("li", extentattrs(cod([]))));
      outpvar.open(htmlnode("div", extentattrs(cod([("class", "collapsible-header")]))));
      outpvar.cur.addfcdata("icon1");
      outpvar.addchilds(newtag_icon1(cod([("img", i["icon"])]), ginp, outpvar.cur.fcalldata["icon1"].root.content).root.content);
      outpvar.addtext(i["name"]);
      outpvar.close();
      outpvar.open(htmlnode("div", extentattrs(cod([("class", "collapsible-body")]))));
      outpvar.open(htmlnode("div", extentattrs(cod([("class", "subcats1"), ("style", cod([("padding", "5px"), ("padding-left", "20px"), ("padding-bottom", "0px"), ("padding-top", "0px")]))]))));
      outpvar.open(htmlnode("ul", extentattrs(cod([("class", "collapsible_sub"), ("attr", cod([("data-collapsible", "accordion")]))]))));
      for jj in forlist(i["child"], True ) :
        j = i["child"][jj];
        outpvar.open(htmlnode("li", extentattrs(cod([("class", "")]))));
        outpvar.open(htmlnode("div", extentattrs(cod([("class", "collapsible-header"), ("style", cod([("border-bottom", "solid black 0px"), ("border-top", "1px solid #DDD")]))]))));
        outpvar.addtext(j["name"]);
        outpvar.close();
        outpvar.open(htmlnode("div", extentattrs(cod([("class", "collapsible-body")]))));
        outpvar.open(htmlnode("div", extentattrs(cod([("class", "subcats2"), ("style", cod([("padding-left", "30px")]))]))));
        outpvar.open(htmlnode("ul", extentattrs(cod([]))));
        outpvar.open(htmlnode("li", extentattrs(cod([]))));
        outpvar.open(htmlnode("div", extentattrs(cod([]))));
        outpvar.cur.addfcdata("checkbox1");
        outpvar.addchilds(newtag_checkbox1(cod([("label", "Select All"), ("id", myadd(myadd(myadd(myadd(myadd("catsubcat", ii), "_"), jj), "_"), "selectall")), ("aclass", "selectall"), ("data", cod([("onclick", "selectall redraw"), ("catgtid", myadd(myadd(i["id"], "_"), j["id"]))])), ("labels", cod([("font-size", "12px")]))]), ginp, outpvar.cur.fcalldata["checkbox1"].root.content).root.content);
        outpvar.close();
        outpvar.close();
        for kk in forlist(j["child"], True ) :
          k = j["child"][kk];
          outpvar.open(htmlnode("li", extentattrs(cod([]))));
          outpvar.open(htmlnode("div", extentattrs(cod([]))));
          outpvar.cur.addfcdata("checkbox1");
          outpvar.addchilds(newtag_checkbox1(cod([("label", k["name"]), ("id", myadd(myadd(myadd(myadd(myadd("catsubcat", ii), "_"), jj), "_"), kk)), ("data", cod([("catgtid", myadd(myadd(myadd(myadd(i["id"], "_"), j["id"]), "_"), k["id"])), ("onclick", "redraw")])), ("labels", cod([("font-size", "12px")]))]), ginp, outpvar.cur.fcalldata["checkbox1"].root.content).root.content);
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
    outpvar.open(htmlnode("div", extentattrs(cod([("style", cod([("background-color", "white"), ("padding", "5px")]))]))));
    outpvar.cur.addfcdata("a1");
    outpvar.addchilds(newtag_a1(cod([("text", "See all classes"), ("attr", cod([("onclick", "$(\"#commoncats\").openModal();")]))]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
    outpvar.close();
    outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l1 s1 m1")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("style", cod([("padding", "8px"), ("margin-bottom", "4px"), ("padding-left", "0px"), ("margin-left", "-20px")]))]))));
  outpvar.cur.addfcdata("icon1");
  outpvar.addchilds(newtag_icon1(cod([("img", "photo/minimize1.png"), ("class", "pointer"), ("attr", cod([("onclick", "minimaxifilter(1);")]))]), ginp, outpvar.cur.fcalldata["icon1"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.close();
  return outpvar;
  
def newtag_cp_selectallcatgs(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs(cod([])), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col s6 l6 m6")]))));
  outpvar.addtext("Select The Cats");
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "col s6 l6 m6")]))));
  outpvar.cur.addfcdata("button1");
  outpvar.addchilds(newtag_button1(cod([("name", "OK"), ("attr", cod([("onclick", " $(\"#commoncats\").closeModal();")]))]), ginp, outpvar.cur.fcalldata["button1"].root.content).root.content);
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  outpvar.open(htmlnode("ul", extentattrs(cod([("class", "tabs")]))));
  for ii in forlist(inp["catg"], True ) :
    i = inp["catg"][ii];
    outpvar.open(htmlnode("li", extentattrs(cod([("class", "tab col l4 m4 s4")]))));
    outpvar.cur.addfcdata("a1");
    outpvar.addchilds(newtag_a1(cod([("href", myadd("#modal", i["name"])), ("text", i["name"])]), ginp, outpvar.cur.fcalldata["a1"].root.content).root.content);
    outpvar.close();
  outpvar.close();
  outpvar.close();
  outpvar.open(htmlnode("div", extentattrs(cod([("class", "row")]))));
  for ii in forlist(inp["catg"], True ) :
    i = inp["catg"][ii];
    outpvar.open(htmlnode("div", extentattrs(cod([("id", myadd("modal", i["name"])), ("class", "row")]))));
    for j in forlist(4, False ) :
      outpvar.open(htmlnode("div", extentattrs(cod([("class", "col l3 m3 s6")]))));
      for kk in forlist(inp["commoncats"][ii][j], True ) :
        k = inp["commoncats"][ii][j][kk];
        outpvar.open(htmlnode("div", extentattrs(cod([]))));
        outpvar.cur.addfcdata("checkbox1");
        outpvar.addchilds(newtag_checkbox1(cod([("label", k[0]), ("id", myadd(myadd(myadd(myadd(myadd("commoncats_", ii), "_"), j), "_"), kk)), ("lstyle", cod([("color", "black"), ("font-size", "20px")])), ("data", cod([("onclick", "selectall")])), ("labels", cod([("color", "black")]))]), ginp, outpvar.cur.fcalldata["checkbox1"].root.content).root.content);
        outpvar.open(htmlnode("div", extentattrs(cod([("style", cod([("font-wight", 700), ("font-size", "18px")]))]))));
        outpvar.close();
        for ll in forlist(k, True ) :
          l = k[ll];
          if (int((ll != 0))): 
            outpvar.open(htmlnode("div", extentattrs(cod([]))));
            outpvar.cur.addfcdata("checkbox1");
            outpvar.addchilds(newtag_checkbox1(cod([("label", l), ("id", myadd(myadd(myadd(myadd(myadd(myadd(myadd("commoncats_", ii), "_"), j), "_"), kk), "_"), ll)), ("labels", cod([("font-size", "12px")]))]), ginp, outpvar.cur.fcalldata["checkbox1"].root.content).root.content);
            outpvar.close();
        outpvar.close();
      outpvar.close();
    outpvar.close();
  outpvar.close();
  return outpvar;
  