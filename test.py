#import xlrd, requests, urllib

_agent = "gcl";

execfile("includes/setting.py");
execfile(_mslib+"py/func.py");
execfile("mslib/ocaml/run.py");
execfile(ROOT+"py/main.py");
execfile(_mslib+"py/webd.py");

# maincontent = mtmlparser();

#maincontent.readonefile("templates/test.cpp");

# print maincontent.disp() ;


#print sql.sval("users", limit=1);

#print sql.ival("users", {"name": "Mohit#$%^6''", "email": "timepass@mail.com"});

#a = pagehandler("init").init();

#print _sql.sval("maininfo");



_sql.close_db();
