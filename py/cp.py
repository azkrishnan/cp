
#Assume _sql is declared already

_config["markers_density"] = 0.00600;

_config["sql_help"] = {};

_config["sql_help"]["latlng"] = lambda lat1='lat',lng1='lng': "(((acos(sin(({lat}*pi()/180)) * sin(("+lat1+"*pi()/180))+cos(({lat}*pi()/180)) * cos(("+lat1+"*pi()/180)) * cos((({lng}- "+lng1+")* pi()/180))))*180/pi())*60*1.1515*1.609344)"

_config["sql_help"]["latlng1"] = lambda lat1='lat',lng1='lng': "(((acos(sin(({lat1}*pi()/180)) * sin(("+lat1+"*pi()/180))+cos(({lat1}*pi()/180)) * cos(("+lat1+"*pi()/180)) * cos((({lng1}- "+lng1+")* pi()/180))))*180/pi())*60*1.1515*1.609344)"


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
		"need": ["keyw", "zoom", "radius", "home", "viewport"],
		"mapping": {},
	},
	"providerinfo": {
		"need": ['form_catg', 'form_subcatg', 'form_prov', 'form_email', 'form_phone', 'form_address', 'form_web', 'form_sechedule']
	},
	"providergroup": {
		"need": ["zoom", "radius", "home", "viewport"],
		"ignoreother": False
	},
	"getproviderinfo": {
		"need": ["id"],
	}
}

_config["sql"]["maininfo1"] = "select provider_id, concat(tabs_id, ',', cat_id, ',', subcat_id) as classtype, LOWER(concat(tabs.tabs, cat.cat, subcat.subcat, name_provider, phone, address, website)) as searchtext from maininfo left join tabs on tabs_index = tabs.tabs_id left join cat on cat_index = cat.cat_id left join subcat on subcat_index = subcat.subcat_id left join provider on provider_index = provider.provider_id";

_config["sql"]["provider3"] = 'select provider_id, group_concat(tabs,":\\n", mycats,"\\n") as mycats from (select provider_id, tabs, group_concat(concat(cat, ": ", subcats),";") as mycats from (select provider_id, tabs.tabs, cat.cat, group_concat(subcat.subcat) as subcats from maininfo left join tabs on tabs_index = tabs.tabs_id left join cat on cat_index = cat.cat_id left join subcat on subcat_index = subcat.subcat_id left join provider on provider_index = provider.provider_id group by provider_id, tabs.tabs, cat.cat) provider1 group by provider_id, tabs) provider2 group by provider_id';

class cp:
	def __init__(self):
		self.ec = None;
		self.mapping = eval("{"+", ".join(mappl((lambda x: '"'+x+'": self.'+x), _actions.keys()))+"}");

	def handler(self, udata, specf):
		self.ec = 1;
		computed = None;

		mifu(specf, {"need": [], "mapping":{}, "ignoreother": True, "eadd": [], "whocan": "all"});

		if(not(set(specf["need"]) <= set(udata.keys()))):
			self.ec = -5;
		elif(not(specf["whocan"] == "all") and not(islogin())):
			self.ec = -13;
		elif(not(specf["whocan"] == "all") and not( specf["whocan"] == "login") and not(islogin() in specf["whocan"])):
			self.ec = -9;
		else:
			udata_f = mapp(idf, udata, lambda x,y: (not(specf["ignoreother"]) or (y in specf["need"])), lambda x,y: g(specf["mapping"], x, x));
			mifu(udata_f, pkey1({"uid": loginid(), "time": tnow()}, specf["eadd"]), True);
			computed = self.mapping[udata["action"]](udata_f);
		return {"ec": self.ec, "data": computed };

	def getproviderinfo(self, data):
		return _sql.sval("provider", "*", {"provider_id": data["id"]}, limit=1);

	def providergroup(self, data):
		if(has_key(data, "plist")):
			_session["plist"] = data["plist"];
		else:
			data["plist"] = g(_session, "plist", "");
		return {"groups": getmarkergroup(data)};

	def providerinfo(self, data):
		return _sql.ival("providerform", dict(data));

	def search(self, data):
		skeys = searchkeysplit(data["keyw"]);
		conds = mappl(lambda x,y: "searchtext like {x"+str(y)+"} ", skeys); #No worry, we have already filtered the user input.
		darr = dict(mapp(lambda x: "%"+x+"%", skeys, None, lambda x: "x"+str(x) ));
		conds = "true" if len(conds) == 0 else " OR ".join(conds);
		query = "select provider_id, classtype from "+gtable("maininfo1")+" where "+conds
		matchedprov = _sql.g(query, darr)
		providers = list(set(mappl(lambda x: x["provider_id"], matchedprov)));
		_session["plist"] = ",".join(mappl(lambda x:str(x), providers));
		return {"groups": getmarkergroup(sifu(data, "plist", _session["plist"])), "numclasses": len(set(mappl(lambda x: x["classtype"], matchedprov))), "activep": providers};


def getmarkergroup(data):
	query = "select provider_id,lat,lng, "+sqlhelp("latlng")+" as distance, "+sqlhelp("latlng1")+" as distance1 from provider where provider_id in ("+",".join(['0']+msplit(data["plist"], ","))+") AND lat*lng != 0 having (distance <= {distance} AND distance1 <= {distance1}) ";
	plist = mappl(lambda x: [x["lat"], x["lng"], x["provider_id"]], _sql.g(query, mifu(data["home"], {"distance": data["radius"], "lat1": data["viewport"]["lat"], "lng1": data["viewport"]["lng"], "distance1": 80000*(2**(-int(data["zoom"])))})));
	clusters = geolocgroup(plist, int(data["zoom"]), float(_config["markers_density"]));
	return  mappl(lambda x: (lambda z: [z[0]*1.0/len(x), z[1]*1.0/len(x), x[0][2], len(x), ",".join(mappl(lambda y: str(y[2]), x)) ])(fold(lambda y,z: [y[0]+z[0], y[1]+z[1]], x, [0,0])), clusters, lambda x:(len(x) > 0));


def catgtree():
	return catgxlx1(_sql.g("select tabs_index, cat_index, subcat_index, group_concat(provider_index) as providers from maininfo left join tabs on tabs_id=tabs_index left join cat on cat_id = cat_index left join subcat on subcat_id = subcat_index group by tabs_index, cat_index, subcat_index order by tabs.rank, cat.rank, subcat.rank"), ["tabs_index", "cat_index", "subcat_index"], True);

def catgtree_shortlist(allcatgs, catlimit=None, subcatlimit=None):
	return mapp(lambda x: pkey1(mapp(lambda y: pkey1(mapp(lambda z:map(lambda x:int(x), z["providers"].split(",")) if False else z["providers"], y), y.keys()[:subcatlimit]), x), x.keys()[:catlimit]), allcatgs);



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
	return listorrow(data) if (len(keyl) == 0) else mapp(lambda v: catgxlx1(v, keyl[1:], isuniq), fold(lambda x,y: r1(sifu(x, y[keyl[0]], []), x[y[keyl[0]]].append( r1(y.pop(keyl[0]), y) ), x), data, cod()));

def readxlx_val(fn):
	return list(list(list(str(x.value.encode('utf-8')) for x in y) for y in z) for z in readxlx(fn));

def readxlx_val1(fn):
	return list(list(list(unicode(x.value).encode('utf-8') for x in y) for y in z) for z in readxlx(fn));

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




def readxlsx_insertdb():
	sheets = cod([("Kids", "data/FUN_Kids_08052015.xlsx"), ("Adults", "data/FUN_Adults_08132015.xlsx"), ("Pets", "data/FUN_Pets_08052015.xlsx")]);
	itables = mapp(lambda x, y: catgxlx1(x, [y], True), sifu(mapp(lambda x: _sql.sval(x), ["tabs", "cat", "subcat"], None, lambda x, y: y), "provider", _sql.sval("provider", "provider_id, concat(name_provider, '_', address, '_', website) as provider, username")));
	usernames = mappl(lambda x: x["username"], itables["provider"]);
	def insert_uniq(t, data, uindex):
		if itables[t].has_key(uindex) :
			return itables[t][uindex][t+"_id"]
		else :
			if(t=="provider"):
				data["username"] = create_username(data["name_provider"], usernames);
				usernames.append(data["username"]);
				print "Address = ",data["address"];
				latlng = rifn(google_addrtolanlat(row[4]), {"lat": 0, "lng": 0, "countrycode": None});
				time.sleep(0.3);
				print latlng;
				mifu(data, latlng);
				if(data["countrycode"] != None):
					data["username"] = data["countrycode"]+"/"+data["username"];
					elc("mkdir -p "+ROOT+data["countrycode"]);
					elc("mkdir -p "+ROOT+data["username"]+"; cp inside_index.php "+ROOT+data["username"]+"/index.php");	
			data[t+"_id"] = _sql.ival(t, data);
			itables[t][uindex] = data;
			return data[t+"_id"];
	for i in sheets.keys():
		ikey = insert_uniq("tabs", {"tabs": i}, i);
		xldata = readxlx_val1(sheets[i]);
		tabdata = mixl(list(j[1:] for j in xldata));
		for j in xrange(len(tabdata)):
			row = tabdata[j];
			if(row[1] !="" and row[2] != "" and row[4] !=""):
				cat_id = insert_uniq("cat", {"cat": row[1]}, row[1]);
				subcat_id = insert_uniq("subcat", {"subcat": row[2]}, row[2]);
				provider_id = insert_uniq("provider", {"name_provider": row[0], "phone": row[3], "address": row[4], "website": row[5], "email": g(row, 6, "")}, row[0]+"_"+row[4]+"_"+row[5]);
				print provider_id;
				try:
					print _sql.ival("maininfo", {"tabs_index": ikey, "cat_index": cat_id, "subcat_index": subcat_id, "provider_index": provider_id});
				except Exception as e:
					print "Error: "+str(e);


def update_latlng():
	allp = _sql.g("select * from provider where countrycode is NULL");
	for i in allp:
		latlng = google_addrtolanlat(i["address"]);
		print i["address"]
		if(latlng):
			sifu(latlng, "username", latlng["countrycode"]+"/"+i["username"]);
			_sql.uval("provider", latlng, {"provider_id": i["provider_id"]}, 1);
			print latlng, i["address"];
		time.sleep(0.3);
		print "Sleep";

def update_tabsrank():
	mappl(lambda x:_sql.q("update "+x+" set rank = "+x+"_id"), ["tabs", "cat", "subcat"]);
