outpvar.cur.addfcdata("main1");
outpvar.cur.fcalldata["main1"].cur.addfcdata("header1_cp");
outpvar.cur.fcalldata["main1"].addchilds(newtag_header1_cp({}, ginp, outpvar.cur.fcalldata["main1"].cur.fcalldata["header1_cp"].root.content).root.content);
outpvar.cur.fcalldata["main1"].open(htmlnode("div", extentattrs({"attr": {"id": "map"}, "style": {"height": "100%"}})));
outpvar.cur.fcalldata["main1"].close();
outpvar.cur.fcalldata["main1"].open(htmlnode("div", extentattrs({"class": "catgselect"})));
outpvar.cur.fcalldata["main1"].open(htmlnode("div", extentattrs({"id": "maincontrol"})));
outpvar.cur.fcalldata["main1"].cur.addfcdata("cp_filterform");
outpvar.cur.fcalldata["main1"].addchilds(newtag_cp_filterform({}, ginp, outpvar.cur.fcalldata["main1"].cur.fcalldata["cp_filterform"].root.content).root.content);
outpvar.cur.fcalldata["main1"].close();
outpvar.cur.fcalldata["main1"].open(htmlnode("div", extentattrs({"id": "maincontrol1", "style": {"display": "none"}})));
outpvar.cur.fcalldata["main1"].open(htmlnode("div", extentattrs({"class": "row"})));
outpvar.cur.fcalldata["main1"].open(htmlnode("div", extentattrs({"class": "col l1 s1 m1"})));
outpvar.cur.fcalldata["main1"].open(htmlnode("div", extentattrs({"style": {"padding": "8px", "margin-bottom": "4px", "padding-left": "0px", "margin-left": "-20px"}})));
outpvar.cur.fcalldata["main1"].cur.addfcdata("icon1");
outpvar.cur.fcalldata["main1"].addchilds(newtag_icon1({"img": "photo/plus1.png", "class": "pointer", "attr": {"onclick": "minimaxifilter(2);"}}, ginp, outpvar.cur.fcalldata["main1"].cur.fcalldata["icon1"].root.content).root.content);
outpvar.cur.fcalldata["main1"].close();
outpvar.cur.fcalldata["main1"].close();
outpvar.cur.fcalldata["main1"].close();
outpvar.cur.fcalldata["main1"].close();
outpvar.cur.fcalldata["main1"].close();
outpvar.cur.fcalldata["main1"].open(htmlnode("div", extentattrs({"class": "modal", "id": "commoncats"})));
outpvar.cur.fcalldata["main1"].open(htmlnode("div", extentattrs({"class": "modal-content"})));
outpvar.cur.fcalldata["main1"].cur.addfcdata("cp_selectallcatgs");
outpvar.cur.fcalldata["main1"].addchilds(newtag_cp_selectallcatgs({}, ginp, outpvar.cur.fcalldata["main1"].cur.fcalldata["cp_selectallcatgs"].root.content).root.content);
outpvar.cur.fcalldata["main1"].close();
outpvar.cur.fcalldata["main1"].close();
outpvar.cur.fcalldata["main1"].open(htmlnode("div", extentattrs({"id": "bcard1", "class": "modal bottom-sheet"})));
outpvar.cur.fcalldata["main1"].open(htmlnode("div", extentattrs({"class": "modal-content"})));
outpvar.cur.fcalldata["main1"].open(htmlnode("p", extentattrs("Mohit")));
outpvar.cur.fcalldata["main1"].close();
outpvar.cur.fcalldata["main1"].close();
outpvar.cur.fcalldata["main1"].open(htmlnode("div", extentattrs({"class": "modal-footer"})));
outpvar.cur.fcalldata["main1"].open(htmlnode("p", extentattrs("Saini")));
outpvar.cur.fcalldata["main1"].close();
outpvar.cur.fcalldata["main1"].close();
outpvar.cur.fcalldata["main1"].close();
outpvar.cur.fcalldata["main1"].open(htmlnode("div", extentattrs({"attr": {"id": "myfavlist"}, "class": "modal bottom-sheet"})));
outpvar.cur.fcalldata["main1"].open(htmlnode("div", extentattrs({"class": "container-fluid"})));
outpvar.cur.fcalldata["main1"].open(htmlnode("div", extentattrs({"class": "row"})));
pkeys = ginp["provider"].keys;
for i in forlist(pkeys) :
  pinfo = ginp["provider"][i];
  outpvar.cur.fcalldata["main1"].open(htmlnode("div", extentattrs({"class": "col l12 m12 s12 favlistelm", "data": {"pid": i}})));
  outpvar.cur.fcalldata["main1"].cur.addfcdata("a1");
  outpvar.cur.fcalldata["main1"].addchilds(newtag_a1({"name": myadd(myadd(pinfo["name_provider"], " "), pinfo["address"]), "href": myadd(myadd(ginp["nhost"], "?pid="), i), "attr": {"target": "_blank"}}, ginp, outpvar.cur.fcalldata["main1"].cur.fcalldata["a1"].root.content).root.content);
  outpvar.cur.fcalldata["main1"].close();
outpvar.cur.fcalldata["main1"].close();
outpvar.cur.fcalldata["main1"].close();
outpvar.cur.fcalldata["main1"].close();
outpvar.cur.fcalldata["main1"].open(htmlnode("div", extentattrs({"style": {"display": ""}})));
pkeys = ginp["provider"].keys;
for i in forlist(pkeys) :
  pinfo = ginp["provider"][i];
  outpvar.cur.fcalldata["main1"].open(htmlnode("div", extentattrs({"attr": {"id": myadd("providerinfo_", i)}, "class": "modal bottom-sheet"})));
  outpvar.cur.fcalldata["main1"].open(htmlnode("div", extentattrs({"class": "container-fluid"})));
  outpvar.cur.fcalldata["main1"].open(htmlnode("div", extentattrs({"class": "row"})));
  outpvar.cur.fcalldata["main1"].open(htmlnode("div", extentattrs({"class": "col l12 m12 s12"})));
  outpvar.cur.fcalldata["main1"].cur.addfcdata("h5");
  outpvar.cur.fcalldata["main1"].cur.fcalldata["h5"].cur.addfcdata("a1");
  outpvar.cur.fcalldata["main1"].cur.fcalldata["h5"].addchilds(newtag_a1({"href": pinfo["website"], "name": pinfo["name_provider"], "class": "truncate", "attr": {"target": "_blank"}}, ginp, outpvar.cur.fcalldata["main1"].cur.fcalldata["h5"].cur.fcalldata["a1"].root.content).root.content);
  outpvar.cur.fcalldata["main1"].addchilds(newtag_h5({}, ginp, outpvar.cur.fcalldata["main1"].cur.fcalldata["h5"].root.content).root.content);
  outpvar.cur.fcalldata["main1"].open(htmlnode("div", extentattrs({})));
  outpvar.cur.fcalldata["main1"].cur.addfcdata("a1");
  outpvar.cur.fcalldata["main1"].addchilds(newtag_a1({"href": myadd(myadd(ginp["nhost"], "?pid="), i), "name": "Business Card", "class": "truncate", "attr": {"target": "_blank"}}, ginp, outpvar.cur.fcalldata["main1"].cur.fcalldata["a1"].root.content).root.content);
  outpvar.cur.fcalldata["main1"].close();
  outpvar.cur.fcalldata["main1"].close();
  outpvar.cur.fcalldata["main1"].open(htmlnode("div", extentattrs({"class": "col l4 m4 s4"})));
  outpvar.cur.fcalldata["main1"].cur.addfcdata("h5");
  outpvar.cur.fcalldata["main1"].cur.fcalldata["h5"].open(htmlnode("p", extentattrs("")));
  outpvar.cur.fcalldata["main1"].cur.fcalldata["h5"].close();
  outpvar.cur.fcalldata["main1"].cur.fcalldata["h5"].cur.addfcdata("icon");
  outpvar.cur.fcalldata["main1"].cur.fcalldata["h5"].addchilds(newtag_icon({"name": "navigation", "aclass": "tiny"}, ginp, outpvar.cur.fcalldata["main1"].cur.fcalldata["h5"].cur.fcalldata["icon"].root.content).root.content);
  outpvar.cur.fcalldata["main1"].addchilds(newtag_h5({"class": "grey-text text-darken-2"}, ginp, outpvar.cur.fcalldata["main1"].cur.fcalldata["h5"].root.content).root.content);
  outpvar.cur.fcalldata["main1"].open(htmlnode("div", extentattrs({"class": "grey-text"})));
  outpvar.cur.fcalldata["main1"].open(htmlnode("p", extentattrs(pinfo["address"])));
  outpvar.cur.fcalldata["main1"].close();
  outpvar.cur.fcalldata["main1"].close();
  outpvar.cur.fcalldata["main1"].close();
  outpvar.cur.fcalldata["main1"].open(htmlnode("div", extentattrs({"class": "col l4 m4 s4"})));
  outpvar.cur.fcalldata["main1"].cur.addfcdata("h5");
  outpvar.cur.fcalldata["main1"].cur.fcalldata["h5"].open(htmlnode("p", extentattrs("")));
  outpvar.cur.fcalldata["main1"].cur.fcalldata["h5"].close();
  outpvar.cur.fcalldata["main1"].cur.fcalldata["h5"].cur.addfcdata("icon");
  outpvar.cur.fcalldata["main1"].cur.fcalldata["h5"].addchilds(newtag_icon({"name": "call", "aclass": "tiny"}, ginp, outpvar.cur.fcalldata["main1"].cur.fcalldata["h5"].cur.fcalldata["icon"].root.content).root.content);
  outpvar.cur.fcalldata["main1"].addchilds(newtag_h5({"class": "grey-text text-darken-2"}, ginp, outpvar.cur.fcalldata["main1"].cur.fcalldata["h5"].root.content).root.content);
  outpvar.cur.fcalldata["main1"].open(htmlnode("div", extentattrs({"class": "grey-text"})));
  outpvar.cur.fcalldata["main1"].open(htmlnode("p", extentattrs(pinfo["phone"])));
  outpvar.cur.fcalldata["main1"].close();
  outpvar.cur.fcalldata["main1"].close();
  outpvar.cur.fcalldata["main1"].close();
  outpvar.cur.fcalldata["main1"].open(htmlnode("div", extentattrs({"class": "col l3 m3 s3"})));
  outpvar.cur.fcalldata["main1"].open(htmlnode("button", extentattrs({"class": "waves-effect waves-light btn", "data": {"onclick": "addfav", "pid": i}})));
  outpvar.cur.fcalldata["main1"].open(htmlnode("p", extentattrs("Favorute")));
  outpvar.cur.fcalldata["main1"].close();
  outpvar.cur.fcalldata["main1"].close();
  outpvar.cur.fcalldata["main1"].close();
  outpvar.cur.fcalldata["main1"].close();
  outpvar.cur.fcalldata["main1"].close();
  outpvar.cur.fcalldata["main1"].close();
outpvar.cur.fcalldata["main1"].close();
outpvar.cur.fcalldata["main1"].open(htmlnode("div", extentattrs({"class": "modal", "id": "providerform", "style": {"padding": "20px"}})));
outpvar.cur.fcalldata["main1"].open(htmlnode("div", extentattrs({"style": {"margin": "10px"}})));
outpvar.cur.fcalldata["main1"].open(htmlnode("form", extentattrs({"data": {"onsubmit": "sreq", "bobj": "", "action": "providerinfo", "restext": "Submitted"}})));
outpvar.cur.fcalldata["main1"].open(htmlnode("div", extentattrs({"style": {"font-size": "20px"}})));
outpvar.cur.fcalldata["main1"].open(htmlnode("p", extentattrs("Fill the provider's Details")));
outpvar.cur.fcalldata["main1"].close();
outpvar.cur.fcalldata["main1"].close();
outpvar.cur.fcalldata["main1"].open(htmlnode("div", extentattrs({"class": "row"})));
outpvar.cur.fcalldata["main1"].cur.addfcdata("input1");
outpvar.cur.fcalldata["main1"].addchilds(newtag_input1({"label": "Catageroy", "id": "form_catg"}, ginp, outpvar.cur.fcalldata["main1"].cur.fcalldata["input1"].root.content).root.content);
outpvar.cur.fcalldata["main1"].cur.addfcdata("input1");
outpvar.cur.fcalldata["main1"].addchilds(newtag_input1({"label": "Sub-Catageroy", "id": "form_subcatg"}, ginp, outpvar.cur.fcalldata["main1"].cur.fcalldata["input1"].root.content).root.content);
outpvar.cur.fcalldata["main1"].cur.addfcdata("input1");
outpvar.cur.fcalldata["main1"].addchilds(newtag_input1({"label": "Provider", "id": "form_prov"}, ginp, outpvar.cur.fcalldata["main1"].cur.fcalldata["input1"].root.content).root.content);
outpvar.cur.fcalldata["main1"].cur.addfcdata("input1");
outpvar.cur.fcalldata["main1"].addchilds(newtag_input1({"label": "Provider's Email", "id": "form_email"}, ginp, outpvar.cur.fcalldata["main1"].cur.fcalldata["input1"].root.content).root.content);
outpvar.cur.fcalldata["main1"].cur.addfcdata("input1");
outpvar.cur.fcalldata["main1"].addchilds(newtag_input1({"label": "Provider's Phone", "id": "form_phone"}, ginp, outpvar.cur.fcalldata["main1"].cur.fcalldata["input1"].root.content).root.content);
outpvar.cur.fcalldata["main1"].cur.addfcdata("input1");
outpvar.cur.fcalldata["main1"].addchilds(newtag_input1({"label": "Provider's Address", "id": "form_address", "aclass": "col l12"}, ginp, outpvar.cur.fcalldata["main1"].cur.fcalldata["input1"].root.content).root.content);
outpvar.cur.fcalldata["main1"].cur.addfcdata("input1");
outpvar.cur.fcalldata["main1"].addchilds(newtag_input1({"label": "Link to Website", "id": "form_web", "aclass": "col l12"}, ginp, outpvar.cur.fcalldata["main1"].cur.fcalldata["input1"].root.content).root.content);
outpvar.cur.fcalldata["main1"].cur.addfcdata("input1");
outpvar.cur.fcalldata["main1"].addchilds(newtag_input1({"label": "Link to Class Sechedule", "id": "form_sechedule", "aclass": "col l12"}, ginp, outpvar.cur.fcalldata["main1"].cur.fcalldata["input1"].root.content).root.content);
outpvar.cur.fcalldata["main1"].close();
outpvar.cur.fcalldata["main1"].open(htmlnode("div", extentattrs({})));
outpvar.cur.fcalldata["main1"].cur.addfcdata("button1");
outpvar.cur.fcalldata["main1"].addchilds(newtag_button1({"name": "Submit", "attr": {"type": "submit"}}, ginp, outpvar.cur.fcalldata["main1"].cur.fcalldata["button1"].root.content).root.content);
outpvar.cur.fcalldata["main1"].close();
outpvar.cur.fcalldata["main1"].close();
outpvar.cur.fcalldata["main1"].close();
outpvar.cur.fcalldata["main1"].close();
outpvar.cur.fcalldata["main1"].open(htmlnode("div", extentattrs({"class": "modal", "id": "contactusform", "style": {"padding": "20px"}})));
outpvar.cur.fcalldata["main1"].cur.addfcdata("cp_contactus_form");
outpvar.cur.fcalldata["main1"].addchilds(newtag_cp_contactus_form({}, ginp, outpvar.cur.fcalldata["main1"].cur.fcalldata["cp_contactus_form"].root.content).root.content);
outpvar.cur.fcalldata["main1"].close();
outpvar.cur.fcalldata["main1"].open(htmlnode("div", extentattrs({"class": "modal", "id": "ourstory", "style": {"padding": "20px"}})));
outpvar.cur.fcalldata["main1"].cur.addfcdata("cp_our_story");
outpvar.cur.fcalldata["main1"].addchilds(newtag_cp_our_story({}, ginp, outpvar.cur.fcalldata["main1"].cur.fcalldata["cp_our_story"].root.content).root.content);
outpvar.cur.fcalldata["main1"].close();
outpvar.addchilds(newtag_main1({"js": ["js/jquery-ui.js", "js/index.js"], "title": "Class Pundit"}, ginp, outpvar.cur.fcalldata["main1"].root.content).root.content);