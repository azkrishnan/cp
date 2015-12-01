_agent = "poorvi";
execfile("includes/setting.py");

import time;

from msl import *
from msl.help import *
from msl.sql import *
from msl.mtime import *;

execfile(_mslib+"ocaml/run.py");

try:
	inpdata = udicttostr(json.loads(sys.argv[1]));
	_session = inpdata["session"];
	_get = inpdata["get"];
	_post = inpdata["post"];
	_urlpath = inpdata["url"]
	_files = inpdata["file"];
	_addinfo = inpdata["addinfo"];
except:
	print "Error in reading php vars";
	(_session, _get, _post, _urlpath, _file, _addinfo) = ({}, {}, {}, '', {}, {});

execfile(_mslib+"py/webd.py");

exec(read_file(ROOT+"py/main.py"));

filename = ("index" if _urlpath == "" else _urlpath);

if( filename == "ajaxactions" ):
	mprint(json.dumps(pagehandler(filename).ajaxactions()));
else:
	pageh = pagehandler(filename).call();
	maincontent = mtmlparser();
	maincontent.readcompiled(filename+".cpp");
#	write_file("cache_mainpage.html", maincontent.disp(mifu(pageh, {"HOST": HOST, "CDN": CDN, "BASE":BASE}, True) ));
	mprint(read_file("cache_mainpage.html"));



_sql.close_db();

print json.dumps({"printout": _printout, "_SESSION": _session, "_header": _phpheader, "toresize": _toresize});
