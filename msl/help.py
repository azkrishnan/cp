import itertools, socket;

from msl import *

def gen_form(*args):
	return map(lambda x: ''.join(list(str(i) for i in x)), itertools.product(*args));


def getmyip():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("www.iitd.ac.in",80))
	myip=s.getsockname()[0];
	s.close()
	return myip;

def my_send(s, msg):
	return s.send(("%010d" % (len(msg),))+msg);

def my_recv(s):
	num_to_recv = doifcan1(lambda: int(s.recv(10)), 0)
	if(num_to_recv > 0):
		return s.recv(num_to_recv);
	else:
		return "";

def mixl(l):
	return fold(lambda x,y: x+y, l, []);


def quoted_s1(x):
	return replaceall(x, cod([('\\', '\\\\'), ('\t', "\\t"), ('\n', "\\n"), ('"', '\\\"')]));

def quoted_s(x):
	return '"'+quoted_s1(x)+'"';
