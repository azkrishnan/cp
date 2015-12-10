#This code is auto generated code, don't Edit it 
outpvar.cur.addfcdata("main1");
outpvar.cur.fcalldata["main1"].addtext("Upload the excell sheet here [Only *.xlsx]");
outpvar.cur.fcalldata["main1"].addtext("");
outpvar.cur.fcalldata["main1"].open(htmlnode("form", extentattrs(cod([("attr", cod([("method", "post"), ("enctype", "multipart/form-data")]))]))));
outpvar.cur.fcalldata["main1"].open(htmlnode("input", extentattrs(cod([("attr", cod([("type", "file"), ("name", "sheet")]))]))));
outpvar.cur.fcalldata["main1"].open(htmlnode("button", extentattrs(cod([("attr", cod([("type", "submit")]))]))));
outpvar.cur.fcalldata["main1"].addtext("Submit");
outpvar.cur.fcalldata["main1"].close();
outpvar.cur.fcalldata["main1"].close();
outpvar.addchilds(newtag_main1(cod([]), ginp, outpvar.cur.fcalldata["main1"].root.content).root.content);