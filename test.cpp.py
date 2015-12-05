execfile("includes/setting.py");

import time;

from msl import *
from msl.help import *
from msl.sql import *
from msl.mtime import *;

execfile(_mslib+"py/webd.py");

ginp = {"HOST": HOST};

outpvar = htmltree();

execfile("defines.py");
outpvar.cur.addfcdata("main1");
outpvar.cur.fcalldata["main1"].cur.addfcdata("header1_cp");
outpvar.cur.fcalldata["main1"].addchilds(newtag_header1_cp({}, ginp, outpvar.cur.fcalldata["main1"].cur.fcalldata["header1_cp"].root.content).root.content);
outpvar.addchilds(newtag_main1({"js": ["js/jquery-ui.js", "js/index.js"], "title": "Class Pundit"}, ginp, outpvar.cur.fcalldata["main1"].root.content).root.content);

fout = outpvar.root.tostr();
print "\n".join(printoutp(fout, "  ", -2));

