_sql = sqllib((_agent == "poorvi" and _server == "gcl") or (doifcan1(lambda: r1(MySQLdb, 0), 1)), db_data);


execfile(ROOT+"py/cp.py");

_cp = cp();

class pagehandler:
	def __init__(self, name):
		self.name = name;
		if(False and _server == "gcl"):
			elc("python client.py 10.208.20.186 ./compile");
		self.jsdata = {"HOST": HOST, "BASE": BASE, "curpage": self.name, "_server": _server};
		self.methodmap = {"index": self.index, "test": self.index, "upload": self.upload};
		self.alltable = ["maininfo", "tabs", "cat", "subcat", "provider", "providerform"];

	def call(self):
		return sifu(( rifn(self.methodmap[self.name](), {}) if self.methodmap.has_key(self.name) else {}), "jsdata", json.dumps(self.jsdata));

	def index(self):
		pid = intf(g(_get, "pid"));
		nhost = g(_get, "nhost" , HOST);
		catgs = catgtree()
		mifu(self.jsdata, sifu(catgs, "pid", pid));
		mifu(catgs, {"commoncats": eval(read_file("data/commondata.pyf")), "pid": pid, "nhost": nhost, "our_story_content": read_file("data/aboutusc")});
		return catgs;

	def test(self):
		pass

	def upload(self):
		if(has_key(_files, "sheet")):
			datafile = "data/providers.xlsx";
			datafile = _files["sheet"]["tmp_name"];
			def updatelatlng():
				allp = _sql.sval("provider", "provider_id, address");
				for i in allp:
					latlng = google_addrtolanlat(i["address"]);
					time.sleep(0.5);
					if(latlng):
						mprint(latlng);
						_sql.uval("provider", latlng, {"provider_id": i["provider_id"]}, 1);
						mprint(latlng, i["address"]);

			def deletealltable():
				mprint(list(_sql.q("drop table if exists "+i) for i in self.alltable));

			def createtables():
				readxlx_dbdump(datafile, ['tabs', 'cat', 'subcat', 'name_provider', 'phone', 'address', 'website', 'lat', 'lng'], _sql.tabtype("vu20, vu50, vu50, v200, v20, v200, v200, r, r"), "maininfo", {"tabs":[0], "cat": [1], "subcat": [2], "provider":[3, 4, 5, 6, 7, 8]});
			if(True):
				list(_sql.q("drop table if exists "+i) for i in ["tabs", "cat", "subcat", "provider"]);
				createtables();
				updatelatlng();
		else:
			pass



	def ajaxactions(self):
		time.sleep(1);
		if( has_key(_actions, g(_post, "action"))):
			return _cp.handler(_post,  _actions[_post["action"]]);
		else:
			return {"ec": -4};

	def init(self):
		""" Read Xslx Sheet and put in Database """
		def updatelatlng():
			allp = _sql.sval("provider", "provider_id, address");
			for i in allp:
				latlng = google_addrtolanlat(i["address"]);
				if(latlng):
					_sql.uval("provider", latlng, {"provider_id": i["provider_id"]}, 1);
					print latlng, i["address"];

		def deletealltable():
			print list(_sql.q("drop table if exists "+i) for i in self.alltable);

		def createtables():
			readxlx_dbdump("data/providers.xlsx", ['tabs', 'cat', 'subcat', 'name_provider', 'phone', 'address', 'website', 'lat', 'lng'], _sql.tabtype("vu20, vu50, vu50, v200, v20, v200, v200, r, r"), "maininfo", {"tabs":[0], "cat": [1], "subcat": [2], "provider":[3, 4, 5, 6, 7, 8]});
		if(True):
#			deletealltable();
			createtables();
			updatelatlng();
		print _sql.q("create table if not exists providerform (id int not null auto_increment, form_catg varchar(200), form_subcatg varchar(200), form_prov varchar(200), form_email varchar(200), form_phone varchar(200), form_address varchar(300), form_web varchar(200), form_sechedule varchar(300), primary key(id))");



