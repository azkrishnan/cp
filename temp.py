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
#print maincontent.disp(mifu({}, {"HOST": HOST, "CDN": CDN, "BASE":BASE}, True));
#print "%f"%time.time()


def forlist(a):
	return range(a) if(type(a) == int) else a;
		

_onewaytags = ["input", "link", "img", "base"];

class htmlnode():
	def __init__(self, tag=None, attrs={}, ptext=None):
		self.tag = tag;
		self.attrs = attrs;
		self.parent = None;
		self.content = [];
		self.ptext = ptext;

	def addchild(self, n):
		self.content.append(n);
		n.parent = self;

	def tostr(self):
		def tagattrs(a):
			return json.dumps(a);
		opentag = lambda : "<"+self.tag+" "+ tagattrs(self.attrs) + " >";
		closetag = lambda : "</"+self.tag+">"
		if(self.ptext != None):
			return [self.ptext];
		elif (len(self.content) == 0):
			return [opentag()+closetag()]
		elif ( len(self.content) ==1 and self.content[0].ptext != None):
			return [opentag()+self.ptext+closetag()];
		else:
			return [opentag(), mappl(lambda x: x.tostr(), self.content), closetag()];


class htmltree():
	def __init__(self):
		
		self.root = htmlnode();
		self.cur = self.root;

	def open(self, hnode):
		self.cur.addchild(hnode);
		if(hnode.tag != None and not(hnode.tag in _onewaytags)):
			self.cur = hnode;

	def close(self):
		self.cur = self.cur.parent;





m = htmlnode("mangelal");
n1 = htmlnode("sunita");
n2 = htmlnode("Vinod");

mn1 = htmlnode(ptext = "mohit");

n2.addchild(mn1);

m.addchild(n1);
m.addchild(n2);


print n1.parent.content[1].tag

print m.tostr()



outp = htmltree();
outp.open(htmlnode("div", {"color": "blue"}));
outp.open(htmlnode(ptext = "Jai Ho India"));
outp.close();

outp1 = htmltree();

print outp.root.tostr();



