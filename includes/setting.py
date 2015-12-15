execfile("includes/password.py");

if(_server == 'gcl'):
	HOST = 'http://poorvi.cse.iitd.ac.in/~cs1120233/cp/';
	ROOT = '/home/btech/cs1120233/private_html/cp/';
	db_data = {'host': 'poorvi.cse.iitd.ac.in', 'user': 'mohit', 'pass': 'mohitsaini', 'db': 'mohit'};
	_msladd = 'msl/'
	db_data["qs_host"] = "10.208.20.186";


elif(_server == 'csc'):
	HOST = 'http://privateweb.iitd.ac.in/~cs1120233/cp/';
	ROOT = '/home/cse/btech/cs1120233/private_html/cp/';
	db_data = {'host': 'poorvi.cse.iitd.ac.in', 'user': 'mohit', 'pass': 'mohitsaini', 'db': 'mohit'};
	_msladd = '~/.local/lib/python2.7/site-packages/msl/';
	db_data["qs_host"] = "10.208.20.9";


elif(_server == "aws"):
	HOST = 'http://54.149.49.212/cp/';
	ROOT = '/var/www/html/cp/';
	db_data = {'host': 'localhost', 'user': 'root', 'pass': 'mohit', 'db': 'cp'};
	_msladd = '/usr/lib/python2.7/msl/';


elif(_server == "solnki"):
	HOST = 'http://localhost/cp/';
	ROOT = '/var/www/html/cp/';
	db_data = {'host': '10.208.20.8', 'user': 'mohit', 'pass': 'mohitsaini', 'db': 'mohit'};
	_msladd = '/usr/lib/python2.7/msl/';

elif(_server == "mohit"):
	HOST = 'http://localhost/cp/';
	ROOT = '/var/www/cp/';
	db_data = {'host': '10.208.20.8', 'user': 'mohit', 'pass': 'mohitsaini', 'db': 'mohit'};
	db_data = {'host': 'localhost', 'user': 'root', 'pass': 'mohitsaini', 'db': 'cp'};
	_msladd = '/usr/lib/python2.7/msl/';

elif(_server == "aws_cp"):
	HOST = 'http://classpundit.com/';
	ROOT = '/var/www/html/';
	db_data = {'host': 'localhost', 'user': 'root', 'pass': 'mohit', 'db': 'cp'};
	_msladd = '/usr/lib/python2.7/msl/';


db_data["qs_port"] = 1136;



CDN = HOST+'photo/'
BASE = HOST+'index.php/'
_mslib = ROOT+"mslib/";
_includes = [];
