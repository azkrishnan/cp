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

execfile(compiledf+"defines.py");
execfile(compiledf+ginp["page"]+".py");

print "\n".join(printoutp(outpvar.root.tostr(), "  ", -2));

