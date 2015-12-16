_sql = sqllib((_agent == "poorvi" and _server == "gcl") or (doifcan1(lambda: r1(MySQLdb, 0), 1)), db_data);


execfile(ROOT+"py/cp.py");

_cp = cp();

class pagehandler:
	def __init__(self, name):
		self.name = name;
		self.jsdata = {"HOST": HOST, "BASE": BASE, "curpage": self.name, "_server": _server};
		self.methodmap = {"index": self.index, "test": self.test, "upload": self.upload, "seeall": self.seeall};
		self.alltable = ["maininfo", "tabs", "cat", "subcat", "provider", "providerform"];

	def call(self):
		return sifu(( rifn(self.methodmap[self.name](), {}) if self.methodmap.has_key(self.name) else {}), "jsdata", json.dumps(self.jsdata));

	def index(self):
		pid = intf(g(_sql.sval("provider", "provider_id", {"username": _urlpath[0]}, 1), "provider_id") if _urlpath[0] != "" else 0);
		outp = {"icons": mapp(idf, ["photo/kid1.png", "photo/adult1.png", "photo/dog1.png"], None, lambda x: x+1), "pid": pid};
		outp["dictl"] = mapp((lambda x: catgxlx1(_sql.sval(x), [x+"_id"], True)), ["tabs", "cat", "subcat"], None, lambda x,y: y);
		allcatgs = catgtree();
		outp["catgtree"] = catgtree_shortlist(allcatgs, 5 ,5);
		outp["allcatgs"] = catgtree_shortlist(allcatgs);
		outp["our_story_content"] = read_file("data/aboutusc");
		outp["activep"] = mappl(lambda x: x["provider_index"], _sql.g("select distinct provider_index from maininfo where tabs_index = 1")) if pid == 0 else [pid];
		mifu(self.jsdata, pkey1(outp, ["pid", "allcatgs", "activep"]));
		return outp;

	def test(self):
		return {"data": sqlr2table(_sql.g("select provider_id, name_provider, address from provider where countrycode is NULL"))};

	def upload(self):
		pass



	def ajaxactions(self):
		if( has_key(_actions, g(_post, "action"))):
			return _cp.handler(_post,  _actions[_post["action"]]);
		else:
			return {"ec": -4};

	def init(self):
		""" Read Xslx Sheet and put in Database """
		def updatelatlng():
			allp = _sql.sval("provider", "provider_id, address, name_provider");
			for i in allp:
				latlng = google_addrtolanlat(i["address"]);
				if(latlng):
					elc("mkdir -p "+ROOT+latlng["countrycode"]);
					username = latlng["countrycode"]+"/"+create_username(i["name_provider"], alldir(ROOT+latlng["countrycode"]));
					elc("mkdir -p "+ROOT+username+"; cp inside_index.php "+ROOT+username+"/index.php");
					sifu(latlng, "username", username);
					_sql.uval("provider", latlng, {"provider_id": i["provider_id"]}, 1);
					print latlng, i["address"];
				time.sleep(1);
				print "Sleep";

		def deletealltable():
			print list(_sql.q("drop table if exists "+i) for i in ["maininfo", "tabs", "cat", "subcat", "provider"]);

		def createtables():
			readxlx_dbdump("data/providers.xlsx", ['tabs', 'cat', 'subcat', 'name_provider', 'phone', 'address', 'website', 'lat', 'lng', 'countrycode', 'username'], _sql.tabtype("vu20, vu50, vu50, v200, v20, v200, v200, r, r, v5, v50"), "maininfo", {"tabs":[0], "cat": [1], "subcat": [2], "provider":[3, 4, 5, 6, 7, 8, 9, 10]});
		if(False):
			deletealltable();
			createtables();
			updatelatlng();
			print _sql.q("create table if not exists providerform (id int not null auto_increment, form_catg varchar(200), form_subcatg varchar(200), form_prov varchar(200), form_email varchar(200), form_phone varchar(200), form_address varchar(300), form_web varchar(200), form_sechedule varchar(300), primary key(id))");
		else:
			pass


	def init_db(self):
		#print list(_sql.q("drop table if exists "+i) for i in ["maininfo", "tabs", "cat", "subcat", "provider"]);

		print _sql.q("create table if not exists tabs (tabs_id int not null auto_increment, tabs varchar(50), rank int, primary key (tabs_id) )");
		print _sql.q("create table if not exists cat (cat_id int not null auto_increment, cat varchar(50), rank int,  primary key (cat_id) )");
		print _sql.q("create table if not exists subcat (subcat_id int not null auto_increment, subcat varchar(50), rank int, primary key (subcat_id) )");
		print _sql.q("create table if not exists provider (provider_id int not null auto_increment, name_provider varchar(200), phone varchar(20), email varchar(30), address varchar(200), website varchar(200), lat real not null, lng real not null, countrycode varchar(5), username varchar(50), primary key (provider_id))");
		print _sql.q("create table if not exists maininfo (tabs_index int, cat_index int, subcat_index int, provider_index int, UNIQUE (tabs_index, cat_index, subcat_index, provider_index))");

		print _sql.q("create table if not exists providerform (id int not null auto_increment, form_catg varchar(200), form_subcatg varchar(200), form_prov varchar(200), form_email varchar(200), form_phone varchar(200), form_address varchar(300), form_web varchar(200), form_sechedule varchar(300), primary key(id))");

		print _sql.q("alter table tabs add column rank int");
		print _sql.q("alter table cat add column rank int");
		print _sql.q("alter table subcat add column rank int");


	def seeall(self):
		pass