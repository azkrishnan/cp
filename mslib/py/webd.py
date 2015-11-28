
def msgdummy(phone, msg):
	msgfile = "data/msgf";
	writefd(open(msgfile, "a"), "To: {0}\nAt: {1}\n{2}\n{3}\n{4}\n{4}\n\n\n".format(phone, t2f_time(), '-'*20, msg, '-'*20));

def maildummy(email, sub, msg):
	mailfile = "data/mailf";
	writefd(open(mailfile, "a"), "To: {0}\nSubject: {1}\nAt: {2}\n{3}\n{4}\n{5}\n{5}\n\n\n".format(email, sub, t2f_time(), '-'*20, msg, '-'*20));

def msgreal(phone, msg):
	return msgreal1(phone, msg);
	key="ad3eaba4216fed6f5197c8beedd0d358";
	u="harshaccent";
	p="85632"
	url="http://mysms.msgclub.net/rest/services/sendSMS/sendGroupSms?"+ urllib.urlencode({"AUTH_KEY": key, "message": msg, "senderId": "SMSTST", "routeId": "1", "mobileNos": phone, "smsContentType": "english"});
	return s2j(mcurl(url));

def msgreal1(phone, msg):
	url="http://216.245.209.132/rest/services/sendSMS/sendGroupSms?AUTH_KEY=14e4de84f23c84d81f24b8fb69d1e0&senderId=GETIIT&routeId=1&smsContentType=english&"+urllib.urlencode({"message": msg, "mobileNos": phone});
	return s2j(mcurl(url));

def mailreal(email, sub, msg):
	pass
	
def sendmsg(phone, msg):
	msgdummy(phone, msg);
	msgreal(phone, msg) if _config["realmsg"] else None;

def sendmail(email, sub, msg):
	maildummy(email, sub, msg);
	mailreal(email, sub, msg) if _config["realmail"] else None;

def filemsg(phone, fn, data={}):
	return sendmsg(phone, read_file(fn).format(**data));

def filemail(email, fn, data={}):
	msg = read_file(fn).format(**data);
	return sendmail(email, msg.split("\n")[0], msg.split("\n", 1)[1]);

def filemail1(email, fn, data={}):
	return filemail(email, "datar/mails/"+fn+".txt", data);

def adminmail(fn, data={}):
	filemail1(_config["adminmail"], fn, data);

def init_mailmsgsystem():
	elc("mkdir -p data; > data/msgf; > data/mailf; chmod 777 data -R ");

def login(id, typ, ext={}):
	global _session;
	_session["login"] = mifu({"id": id, "type": typ}, ext);

def logininfo():
	return g(_session, "login");

def loginname():
	return doifcan(lambda: logininfo()["name"].title(), (), "Profile");

def islogin():#Also return login type
	return _session["login"]["type"] if (g(g(_session, "login"), "id") > 0) else None;

def isloginas(t):
	if type(t) != list:
		t = [t];
	return (islogin() and (_session["login"]["type"] in t));

def logout():
	global _session;
	_session["login"] = None;

def loginid():
	if(islogin()):
		return _session["login"]["id"];

def redirect(url):
	global _phpheader;
	_phpheader += "Location: " + url;

def getnewfilename(ext='mohit', extra=''):
	nname = _addinfo["ip"]+"_"+str(tnow())+"_"+str(loginid())+"_"+str(random.randint(1, 100000))+extra+"."+ext
	return "data/files/"+nname;

def getext(name):
	ext = name.split(".")[-1];
	return (ext if ext != name else 'mohit');

def resizeimg(name, nname, width, height):
	_toresize[name] =[nname, width, height];

def uploadimg(tmpname, name, size=None, extra=''):
	nname = getnewfilename(getext(name), extra);
	if(size == None):
		if( _server == "csc"):
			resizeimg(tmpname, nname, -1, -1);
		else:
			write_file(nname, read_file(tmpname));
			os.chmod(nname, 0777);
	else:
		resizeimg(tmpname, nname, size[0], size[1]);
	return nname;

def gtable(name, astable = True):
	return "("+_config["sql"][name]+")"+name if astable else _config["sql"][name];

def sqlhelp(name, args={}):
	return _config["sql_help"][name](**args);

def sqlr2table(r):
	if(len(r) == 0):
		return {"thead": [], "rows": []};
	else:
		thead = r[0].keys();
		rows = mappl(lambda x: x.values() ,r);
		return {"thead": thead, "rows": rows};

def mcurl(url):
	if(_agent == "poorvi" and _server == "gcl" ):
		return elc_virtual('curl -s "'+url+'" ');
	else:
		return curl(url);


def isuserexist(u, umatch = 'phone'):
	return _sql.sval("users", "*", {umatch: u} , 1);


def latlngdist(lat1, lng1, lat2, lng2) :
	degtorad = lambda x: x*(math.pi/180);
	R = 6371000; # metres
	ph1 = degtorad(lat1);
	ph2 = degtorad(lat2);
	dph = degtorad(lat2 - lat1);
	dlem = degtorad(lng2 - lng1);
	sin = math.sin;
	a = sin(dph/2) * sin(dph/2) + sin(ph1)*sin(ph2)*sin(dlem/2)*sin(dlem/2);
	c = 2*math.atan2(a**0.5, (1-a)**0.5);
	return R*c;
