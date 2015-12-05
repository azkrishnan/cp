execfile("includes/setting.py");
import time, sys;

from msl import *
from msl.help import *
from msl.sql import *
from msl.mtime import *;

execfile(_mslib+"py/webd.py");

ginp = s2j(sys.argv[1]);

outpvar = htmltree();
compiledf = ROOT+"templates/.compiled/"

#print("<br>Start1:%f<br>"%time.time());
execfile(compiledf+"defines.py");
#print("<br>Start1.1:%f<br>"%time.time());
execfile(compiledf+ginp["page"]+".py");
#print("<br>Start2:%f<br>"%time.time());

print "\n".join(printoutp(outpvar.root.tostr(), "  ", -2));

#print("<br>Start3:%f<br>"%time.time());
