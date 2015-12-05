#This code is auto generated code, don't Edit it 
def newtag_header1(inp, ginp, innerHTML): 
  inp = overwriteattrs(extentattrs({}), extentattrs(inp));
  mifu(inp, ginp);
  outpvar = htmltree();
  outpvar.open(htmlnode("div", extentattrs({"color": "black"})));
  for i in forlist(6) :
    outpvar.open(htmlnode("p", extentattrs(myadd("this is my new header", i))));
    outpvar.close();
  outpvar.close();
  return outpvar;
  