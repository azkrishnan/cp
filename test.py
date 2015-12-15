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

# print pagehandler("").init_db();


readxlsx_insertdb();
#update_latlng()

# a=readxlx("data/FUN_Kids_08052015.xlsx");
# print len(a);


_sql.close_db();
