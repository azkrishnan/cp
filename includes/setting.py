execfile("includes/password.py");
if(_server == 'gcl'):
	HOST = 'http://poorvi.cse.iitd.ac.in/~cs1120233/cp/';
	ROOT = '/home/btech/cs1120233/private_html/cp/';
	db_data = {'host': 'poorvi.cse.iitd.ac.in', 'user': 'mohit', 'pass': 'mohitsaini', 'db': 'mohit'};
elif(_server == "aws"):
	import xlrd
	HOST = 'http://54.149.49.212/cp/';
	ROOT = '/var/www/html/cp/';
	db_data = {'host': 'localhost', 'user': 'root', 'pass': 'mohit', 'db': 'cp'};
elif(_server == "csc"):
	HOST = 'http://privateweb.iitd.ac.in/~cs1120233/cp/';
	ROOT = '/home/cse/btech/cs1120233/private_html/cp/';
	db_data = {'host': 'poorvi.cse.iitd.ac.in', 'user': 'mohit', 'pass': 'mohitsaini', 'db': 'mohit'};
elif(_server == "aws_cp"):
	HOST = 'http://52.8.246.176/';
	ROOT = '/var/www/html/';
	db_data = {'host': 'localhost', 'user': 'root', 'pass': 'mohit', 'db': 'cp'};
elif(_server == "solnki"):
	HOST = 'http://localhost/cp/';
	ROOT = '/var/www/html/cp/';
	db_data = {'host': '10.208.20.8', 'user': 'mohit', 'pass': 'mohitsaini', 'db': 'mohit'};

CDN = HOST+'photo/'
BASE = HOST+'index.php/'
_mslib = ROOT+"mslib/";
_includes = [];
