
#Assume _sql is declared already


mifa(_ec, {
	-1: "Incorrect password or OTP",
	-2: "Phone number already registered",
	-3: "OTP is Incorrect",
	-4: "Action handler not valid",
	-5: "Insufficient arguments",
	-6: "Invalid Input"
});


_actions = {
	"search": {
		"need": ["keyw"],
		"mapping": {},
	},
	"providerinfo": {
		"need": ['form_catg', 'form_subcatg', 'form_prov', 'form_email', 'form_phone', 'form_address', 'form_web', 'form_sechedule']
	}
}

_config["sql"]["maininfo1"] = "select provider_id, LOWER(concat(tabs.tabs, cat.cat, subcat.subcat, name_provider, phone, address, website)) as searchtext from maininfo left join tabs on tabs_index = tabs.tabs_id left join cat on cat_index = cat.cat_id left join subcat on subcat_index = subcat.subcat_id left join provider on provider_index = provider.provider_id";

class cp:
	def __init__(self):
		self.ec = None;
		self.mapping = {"search": self.search, "providerinfo": self.providerinfo};

	def handler(self, udata, specf):
		self.ec = 1;
		computed = None;
		mifu(specf, {"need": [], "mapping":{}, "ignoreother": True});
		if(not(set(specf["need"]) <= set(udata.keys()))):
			self.ec = -5;
		else:
			udata_f = mapp(idf, udata, lambda x,y: (not(specf["ignoreother"]) or (y in specf["need"])), lambda x,y: g(specf["mapping"], x, x));
			computed = self.mapping[udata["action"]](udata_f);
		return {"ec": self.ec, "data": computed };

	def providerinfo(self, data):
		return _sql.ival("providerform", dict(data));

	def search(self, data):
		skeys = searchkeysplit(data["keyw"]);
		conds = mappl(lambda x,y: "searchtext like {x"+str(y)+"} ", skeys); #No worry, we have already filtered the user input.
		darr = dict(mapp(lambda x: "%"+x+"%", skeys, None, lambda x: "x"+str(x) ));
		conds = "true" if len(conds) == 0 else " OR ".join(conds);
		query = "select provider_id from "+gtable("maininfo1")+" where "+conds
		return list(set(mappl(lambda x: x["provider_id"] , _sql.g(query, darr))));






def catgtree():
	sublists = ["tabs", "cat", "subcat", "provider"];
	dictl = mapp((lambda x: catgxlx1(_sql.sval(x), [x+"_id"], True)), sublists, None, lambda x: sublists[x]);


	maininfocatg = catgxlx1( _sql.sval("maininfo"), ["tabs_index", "cat_index", "subcat_index"]);
	icons = ["photo/kid1.png", "photo/adult1.png", "photo/dog1.png", ""];
	return {
		"catg": mappl(lambda x,y: {
				"name": g(g(dictl["tabs"], y), "tabs"), 
				"id": y, "icon": icons[y-1], 
				"child": mappl(lambda x1,y1: {
					"name": dictl["cat"][y1]["cat"], 
					"id": y1, 
					"child": mappl(lambda x2,y2: {
						"name": g(g(dictl["subcat"], y2), "subcat"), 
						"id": y2, 
						"child": mappl(lambda x3,y3: {
							"id": x3["provider_index"], 
							"info": g(g(dictl["provider"], x3), "provider_index") 
						}, x2) 
					}, x1)
				} , x)
		} , maininfocatg), 
		"provider": dictl["provider"], 
		"maininfocatg": maininfocatg
	};



def allcatgmap():
	aa=readxlx_val("data/catsubcat.xlsx");
	outp = [];
	for i in aa:
		catgmap = cod();
		lastkey = None;
		for j in i[1:]:
			if(j[0] != ''):
				lastkey = j[0];
				sifu(catgmap, j[0], []);
			catgmap[lastkey].append(j[1]);
		outp.append(catgmap);
	return outp;

def updateindbcatg(inp):
	for i in inp:
		for j in i:
			doifcan(_sql.ival, ("cat", {"cat": j}));
			for k in i[j]:
				doifcan(_sql.ival, ("subcat", {"subcat": k}));
				print k;
			print j;


def mindiff(l):
	diff = 10000000000
	ijpair = [0, 0];
	for i in xrange(len(l)):
		for j in xrange(i+1, len(l)):
			diffl = mappl(lambda x: sum(x), [l[:i], l[i:j], l[j:]]);
			diffhere = max(diffl)-min(diffl);
			if( diffhere < diff ):
				diff = diffhere;
				ijpair = (i, j);
	return ijpair;


def mindiff1(l):
	diff = 10000000000
	ijpair = [0, 0, 0];
	for i in xrange(len(l)):
		for j in xrange(i+1, len(l)):
			for k in xrange(j+1, len(l)):
				diffl = mappl(lambda x: sum(x), [l[:i], l[i:j], l[j:k], l[k:]]);
				diffhere = max(diffl)-min(diffl);
				if( diffhere < diff ):
					diff = diffhere;
					ijpair = (i, j, k);
	return ijpair;


def commoncats():
	aa = allcatgmap();
#	crmap = mapp(lambda x:x["cat_id"], catgxlx1(_sql.sval("cat"), ["cat"], True));
#	scrmap = mapp(lambda x:x["subcat_id"], catgxlx1(_sql.sval("subcat"), ["subcat"], True));
	outp = [];
	for i in aa:
		(ii, jj, kk) = mindiff1(mappl(lambda y,x: 1+len(i[x]), i));
		listintab = mappl(lambda y,x: [x]+i[x], i);
		outp.append([listintab[:ii], listintab[ii:jj], listintab[jj:kk], listintab[kk:]]);
	return outp;



def loadcommondata():
	write_file("data/commondata.pyf", str(commoncats()));



def insertdata(fn):
	aa=readxlx_val(fn);
	s = aa[0];
	for i in s:
		sifu(i, 7, '');
		sifu(i, 8, '');
	xldata = s;
	title = ['tabs', 'cat', 'subcat', 'name_provider', 'phone', 'address', 'website', 'lat', 'lng']
	grouping = {"tabs":[0], "cat": [1], "subcat": [2], "provider":[3, 4, 5, 6, 7, 8]}
	convodict = lambda x,y, o=None: mappl(lambda x: mifu(cod({y+"_id": None}), (pkey1(x,o) if o != None else cod(x))), x);
	outp = {
		"tabs": convodict(_sql.sval("tabs", "tabs"), "tabs"),
		"cat": convodict(_sql.sval("cat", "cat"), "cat"),
		"subcat": convodict(_sql.sval("subcat", "subcat"), "subcat"),
		"provider": convodict(_sql.sval("provider", "name_provider,phone,address,website,lat,lng"), "provider", ['name_provider', 'phone', 'address', 'website', 'lat', 'lng'])
	}
	outplens = mapp(lambda x:len(x), outp);
	maint = [];
	rkeys = setol(range(len(xldata[0])), mixl(grouping.values()), '-');
	for row in xldata:
		nrow = mapp(idf, pkey1(row, rkeys), None, lambda x:title[x]);
		for i in grouping:
			nrow[i+"_index"] = 1+appenduniq(outp[i], mifu(cod({i+"_id":None}), mapp(idf, pkey1(row, grouping[i]), None, lambda x:title[x]) ));
		maint.append(nrow);
	for i in grouping:
		mappl(lambda x,y: sifu(x, i+"_id", y+1, True), outp[i]);
	mappl(lambda i: _sql.ival("maininfo", dict(i)), maint);
	mapp(lambda tdata,tname: mappl(lambda i: _sql.ival(tname, dict(i)), tdata[outplens[tname]:]), outp);
	return (maint, outp);





def check():
	return insertdata("data/providers1.xlsx");



def catgxlx(data, depth = 0):
	return data if (depth <= 0) else mapp(lambda v: catgxlx(v, depth-1), fold(lambda x,y: r1(sifu(x, y[0], []), x[y[0]].append(y[1:]), x) , data, {}));

def catgxlx1(data, keyl, isuniq = False):
	listorrow = lambda x: x[0] if isuniq else x;
	return data if (len(keyl) == 0) else dict(mapp(lambda v: listorrow(catgxlx1(v, keyl[1:])), fold(lambda x,y: r1(sifu(x, y[keyl[0]], []), x[y[keyl[0]]].append( r1(y.pop(keyl[0]), y) ), x), data, {})));

def readxlx_val(fn):
	return list(list(list(str(x.value.encode('utf-8')) for x in y) for y in z) for z in readxlx(fn));

def readxlx1(fn, depth = 0):
	return catgxlx(readxlx_val(fn)[0][1:], depth);

def readxlx_db(xldata, title, grouping={}): #data: (list of (list of str)), title line removed, Assuming no element is grouped twice
	outp = mapp(lambda: [], cod.fromkeys(grouping.keys()));
	maint = [];
	if(len(xldata) == 0):
		return (maint, outp);
	else:
		rkeys = setol(range(len(xldata[0])), mixl(grouping.values()), '-');
		for row in xldata:
			nrow = pkey1(row, rkeys);
			for i in grouping:
				nrow[i+"_index"] = 1+appenduniq(outp[i], mifu(cod({i+"_id":None}), pkey1(row, grouping[i]) ));
			maint.append(nrow);
		for i in grouping:
			mappl(lambda x,y: sifu(x, i+"_id", y+1, True), outp[i]);
		return (maint, outp);

def readxlx_dbdump(fn, title, coltyp, maintable, grouping={}): #Assuming there is atleast 1 row, other then title.
	(maint, groupt) = readxlx_db(readxlx_val(fn)[0][1:], title, grouping);
	tableattrs = mappl(lambda x,y: x+" "+coltyp[y], title);
	sqlstatement = lambda table, row, isuniqi='': "create table if not exists "+ table+ "("+ ", ".join(mappl(lambda y,x: (tableattrs[x] if type(x) == int else (x+' int'+isuniqi)) , row))+")";
	groupt[maintable] = maint;

	print "Started Executing..";
	createquerys = mappl(lambda x,y: sqlstatement(y, x[0], ' unique' if y != maintable else '' ), groupt);
	groupt = mapp(lambda x, i: mappl(lambda j:mapp(idf, j, None, lambda x: (title[x] if type(x) == int else x)), groupt[i]), groupt);
	list(_sql.q(x) for x in createquerys);
	print "Created All";
	mappl(lambda x,y: mappl(lambda i: _sql.ival(y, dict(i)), x), groupt);
