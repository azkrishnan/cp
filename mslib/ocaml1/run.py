import os,copy,sys,inspect,collections

class mtmlparser:
	def elc(self, c):
		f = os.popen(c);
		data = filter(lambda x: (x!="\n" and x!="\r") , f.read())
		f.close();
		return data;

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
		self.newvar = 0;

	def readcompiled(self, name):
		self.data = eval(read_file(self.compiled+name));

	def readinp(self, fname):
		self.parsedefn();
		self.data = self.datadef + self.parsebyocaml(fname);

	def readonefile(self, fname):
		self.data = self.parsebyocaml(fname);

	def gennewvar(self):
		self.newvar+=1;
#		return "random_var_T6OuFteLo_"+str(self.newvar);
		return "random_var_"+str(self.newvar);

	def expend(self, t, funcs, depth = 0): #Gamma contains list of all function names.
		expend = self.expend;
		def fold(f, l, a):
			for i in l:
				a = f(a, i) if len(inspect.getargspec(f).args) == 2 else f(a, l[i], i);
			return a;

		def joinarr(a, b):
			for i in b:
				a[i] = b[i];
			return a;

		def mergeifunset(a, b, isforce = False, checknone = False): #Warning: a is overwritten
			for i in b:
				if ((not a.has_key(i)) or isforce) and (not(checknone and b[i] == None)) :
					a[i] = b[i];
			return a;

		def geta(key, arr): #for dict array only.
			if(arr.has_key(key)):
				return arr[key];
			else:
				return None;

		def overwrite(a, b): #overwrite array a , forced by b
			for i in b:
				if(a.has_key(i) and type(a[i]) == dict and type(b[i]) == dict ):
					overwrite(a[i], b[i]);
				else:
					a[i] = b[i];
			return a;

		cod = lambda: collections.OrderedDict();
		def ouradd(x,y):
			try:
				return x+y;
			except:
				return str(x)+str(y);
		if(1):
			if(t[0] == "None"):
				return "(json('n'))";
			elif(t[0] == "Assign"):
				if(t[1][0] == "V"):
					return (["json "+t[1][1] + " = " + expend(t[2], funcs)+";"], funcs);
				elif(t[1][0] == "Get"):
					return ([expend(t[1], funcs)+" = " + expend(t[2], funcs )+";"], funcs)
				return ([""], funcs);
			elif(t[0] == "V"):
				return t[1];
			elif(t[0] in ["S"]):
				return "(json("+quoted_s(t[1])+"))";
			elif(t[0] ==  "N"):
				return "(json('i', "+str(t[1])+"))";
			elif(t[0] == "Not"):
				return expend(t[1], funcs)+".op_Not()"
			elif(t[0] == "Attr" ):
				return expend(t[1], funcs)+".op_Attr("+quoted_s(t[2])+")";
			elif(t[0] == "Ife"):
				return "("+expend(t[1], funcs) + ".ival ? "+expend(t[2], funcs) + ": "+expend(t[3], funcs)+")";
			elif(t[0] == "Get"):
				a1,a2 = expend(t[1], funcs), expend(t[2], funcs)
				return "(*("+a1+".op_Get("+a2+")))";
			elif(t[0] in ["Add", "Mul", "Sub", "Div", "Mod", "Or", "And", "Isequal", "Le", "Ge", "Ls", "Gt", "Notequal"] ):
				a1,a2 = expend(t[1], funcs), expend(t[2], funcs)
				return a1+".op_Binary("+ quoted_s(t[0])  +", "+a2+")";
			elif(t[0] == "Dictle"):
					return ", "+("new json("+quoted_s(t[1][1])+")" if t[1][0] == "V" else expend(t[1], funcs)+".copy()")+", "+expend(t[2], funcs)+".copy() ";
			elif(t[0] == "Dictl"):
				return fold(lambda x,y: x+expend(y, funcs), t[1:][::-1], "(json('m', "+str(len(t[1:])))+"))";
			elif(t[0] == "Listl"):
				return fold(lambda y,x: y+", "+expend(x, funcs)+".copy()", t[1:], "(json('l', "+str(len(t[1:])))+"))";
			elif(t[0] == "Listi"):
				outp = [];
				for i in t[1:]:
					(outp1, funcs1) = expend(i, funcs);
					outp+=outp1;
					funcs = funcs1;
				return (outp, funcs);
			elif(t[0] == "Ifel"):
				outp = [];
				for j in range(len(t[1:])):
					i = t[1:][j];
					outp.append( ("else " if j!=0 else "")+"if("+expend(i[1], funcs)+".ival) {" );
					outp.append( expend(i[2], funcs)[0] );
					outp.append( "}" );
				return (outp, funcs);
			elif(t[0] == "Forl"):
				lt = expend(t[3], funcs);

				index_var = t[2][1] if(t[2][1] != "") else self.gennewvar();
				value_var = t[1][1];

				outp = ["FL("+index_var+", INDEXARR("+lt+")) {"];
				outp.append(["json "+value_var+" = INDEXARRVAL("+lt+", "+index_var+");"]+expend(t[4], funcs)[0]);
				outp.append("}");
				return (outp, funcs);
			elif(t[0] == "Defn"):
				fname = t[1][1];
				return (["htmltag* "+fname+"(json* inp) {"]+["}"], [fname]+funcs);
			elif(t[0] == "Tag"):
				tname = t[1][1];
				if(tname == "print"):
					return ([ expend(t[2], funcs)+".__str__()"], funcs);
				else:
					return ([(tname+"()" if(tname in funcs) else "new htmltag("+tname+", ..)")], funcs)
			else:
				return "";
	def disp(self, gamma = {}):
		outp = self.expend(tuple(['Listi']+self.data), [])[0];
		def printoutp(xl, depth = -1):
			if type(xl) == list :
				return mixl(map(lambda x: printoutp(x, depth+1), xl));
			else:
				return ['\t'*depth+xl];
		return self.newlj(printoutp(outp));

