execfile("includes/setting.py");

import time;

from msl import *
from msl.help import *
from msl.sql import *
from msl.mtime import *;

execfile(_mslib+"ocaml1/run.py");

#print "%f"%time.time()
maincontent = mtmlparser();
maincontent.readcompiled("test.cpp");
#print maincontent.data;
print maincontent.disp(mifu({}, {"HOST": HOST, "CDN": CDN, "BASE":BASE}, True));
#print "%f"%time.time()

