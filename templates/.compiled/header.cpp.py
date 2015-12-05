def newtag_header1(inp, innerHTML): 
	mifu(inp, _ginp);
	outpvar = htmltree();
	outpvar.open(htmlnode("div",{"color": "black"}));
	for i in forlist(6) :
		outpvar.open(htmlnode("p",myadd("this is my new header", i)));
		outpvar.close();
	outpvar.close();
	return outpvar;
  