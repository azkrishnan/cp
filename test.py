#import xlrd, requests, urllib

_agent = "gcl";

execfile("includes/setting.py");

import time, sys, MySQLdb

from msl import *
from msl.help import *
from msl.sql import *
from msl.mtime import *;



#execfile(_mslib+"py/func.py");
#execfile("mslib/ocaml/run.py");


execfile(_mslib+"py/webd.py");


execfile(ROOT+"py/main.py");


#print readxlx("data/providers.xlsx");

print searchkeysplit("Just Fun !");

# maincontent = mtmlparser();

#maincontent.readonefile("templates/test.cpp");

# print maincontent.disp() ;


#print sql.sval("users", limit=1);

#print sql.ival("users", {"name": "Mohit#$%^6''", "email": "timepass@mail.com"});

# a = pagehandler("init").init();

# print curl("google.com");

#print _sql.sval("maininfo");



_sql.close_db();
