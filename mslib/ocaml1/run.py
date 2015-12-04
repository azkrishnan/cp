import os,copy,sys,inspect,collections

class mtmlparser:
	def parsebyocaml(self, f):
		cmd = self.parser+" "+f+" 2> /dev/null"
		a = self.elc(cmd if _server != "gcl" else "python client.py 10.208.20.186 '"+ cmd +"'" );
		return eval("["+a+"]");

	def parsedefn(self):
		path = _mslib+"alldef/";
		alldefn = path+".alldefn";
		modftime = lambda x: self.elc("stat -c %x "+x).split(".")[0];
		if(not( modftime(path) == modftime(alldefn) ) or True):
			write_file(alldefn, "".join(read_file(i)+"\n\n" for i in allfile_rec(path) if i not in [alldefn] ));
		self.datadef = self.parsebyocaml(alldefn);

	def __init__(self):
		self.parser = _mslib+"ocaml/calc";
		self.tabseprate = "  ";
		self.newlj = lambda x: "\n".join(list(str(i) for i in x if i!=""))
		self.compiled = "templates/.compiled/";
		self.compileddefn = self.compiled+"defines";
		self.returnvardef = "outpvar";
		self.returnvar = self.returnvardef;

	def readcompiled(self, name):
		self.data = eval(read_file(self.compiled+name));

	def readinp(self, fname):
		self.parsedefn();
		self.data = self.datadef + self.parsebyocaml(fname);

	def readonefile(self, fname):
		self.data = self.parsebyocaml(fname);

	def expend(self, t): #Gamma contains list of all function names.
		expend = self.expend;
		if(t[0] == "None"):
			return t[0];
		elif(t[0] == "Assign"):
			if(t[1][0] == "V"):
				return ([""+t[1][1] + " = " + expend(t[2])+";"]);
			elif(t[1][0] == "Get"):
				return ([expend(t[1])+" = " + expend(t[2])+";"])
			return ([""]);
		elif(t[0] == "V"):
			return t[1];
		elif(t[0] in ["S"]):
			return quoted_s(t[1]);
		elif(t[0] ==  "N"):
			return str(t[1]);
		elif(t[0] == "Not"):
			return "not("+expend(t[1])+")"
		elif(t[0] == "Attr"):
			return expend(t[1])+"."+t[2];
		elif(t[0] == "Ife"):
			return "("+ expend(t[2]) +" if (" +expend(t[1]) + ") else "+ expend(t[3])+")";
		elif(t[0] in  ["Get", "Add"]):
			a1,a2 = expend(t[1]), expend(t[2])
			if(t[0] == "Get"):
				return a1+"["+a2+"]";
			elif(t[0] == "Add"):
				return "myadd("+a1+", "+a2+")";
		elif(t[0] in ["Mul", "Sub", "Div", "Mod", "Or", "And", "Isequal", "Le", "Ge", "Ls", "Gt", "Notequal"]):
			a1,a2 = expend(t[1]), expend(t[2])
			return "("+a1+ {"Add": "+", "Mul": "*", "Sub": "-", "Div": "/", "Mod": "%", "Or": "or", "And": "and", "Isequal": "==", "Le": "<=", "Ge": ">=", "Ls": "<", "Gt": ">", "Notequal": "!="}[t[0]] +a2+")";
		elif(t[0] == "Dictle"):
				return (quoted_s(t[1][1]) if t[1][0] == "V" else expend(t[1]) ) +": "+ expend(t[2]);
		elif(t[0] == "Dictl"):
			return "{"+(", ".join(map(lambda x: expend(x), t[1:][::-1])))+"}"
		elif(t[0] == "Listl"):
			return "["+(", ".join(map(lambda x: expend(x), t[1:])))+"]"
		elif(t[0] == "Listi"):
			outp = [];
			for i in t[1:]:
				(outp1) = expend(i);
				outp+=outp1;
			return (outp);
		elif(t[0] == "Ifel"):
			outp = [];
			for j in range(len(t[1:])):
				i = t[1:][j];
				outp.append(("elif" if j!=0 else "if")+" ("+expend(i[1])+"): " );
				outp.append( expend(i[2]) );
			return (outp);
		elif(t[0] == "Forl"):
			lt = expend(t[3]);
			index_var = t[2][1];
			value_var = t[1][1];
			lta = "forlist("+lt+")";

			outp = ["for "+(index_var if index_var != "" else value_var)+" in " + lta + " :"];
			outp.append([""+value_var+" = "+lt+"["+index_var+"];" if (index_var != "") else "" ]+expend(t[4]));
			return (outp);
		elif(t[0] == "Defn"):
			fname = t[1][1];
			return (["def "+fname+"(inp, innerHTML): "]+[[self.returnvar+" = htmltree();"], ["return "+self.returnvar+";"]]);
		elif(t[0] == "Tag"):
			tname = t[1][1];
			if(tname == "print"):
				return ([ self.returnvar+ ".addtext("+expend(t[2])+");"]);
			else:
				inattr = expend(t[2]);
				if(tname in self.allfuncs):
					oldrvar = self.returnvar;
					self.returnvar = self.returnvar+".cur.fcalldata["+quoted_s(tname)+"]"
					innerHTML = expend(t[3]);
					self.returnvar = oldrvar;
					return [self.returnvar+".cur.addfcdata("+quoted_s(tname)+");", innerHTML, self.returnvar+".addchilds("+tname+"("+inattr+", "+ self.returnvar+".cur.fcalldata["+quoted_s(tname)+"].root.content);"];
				else:
					innerHTML = expend(t[3]);
					return [self.returnvar+".open(htmlnode("+quoted_s(tname)+","+inattr+"));"]+innerHTML+[self.returnvar+".close();"]
		else:
			return "";
	def disp(self, gamma = {}):
		self.allfuncs = mappl(lambda x: x[1][1], self.data, lambda x: x[0] == "Defn");
		outp = self.expend(tuple(['Listi']+self.data))
		def printoutp(xl, depth = -1):
			if type(xl) == list :
				return mixl(map(lambda x: printoutp(x, depth+1), xl));
			elif(xl != '') :
				return ['\t'*depth+xl];
			else:
				return [];
		return self.newlj(printoutp(outp));

