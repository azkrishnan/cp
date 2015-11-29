import os,sys,time,socket,json,threading,random;

from msl import *
from msl.help import *
from msl.mtime import *;

listen_port=1136;

cleaner_timeout = 100;

execfile("py/server_action.py");

_server_actions = server_action();



def closewithmsg(conn,msg,ec=-30):
	conn.send( json.dumps({"msg":msg,"ec":ec}) );
	conn.close();

def serv():
	global listen_port
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	lock=threading.Lock();
	while(True):
		try:
			sock.bind(('',listen_port))
			write_file("listenport",str(listen_port));
			break;
		except:
			listen_port+=1;

	sock.listen(1);


	def talk(conn,client_address):#talk to each request
		print "a Client connected me ",client_address;
		send_json = lambda x: my_send(conn, json.dumps(x));
		while(True):
			cmd=s2j(my_recv(conn));
			try:
				mifu(cmd, {"isclose": False});
				if(cmd["isclose"]):
					break;
				send_json(_server_actions.handler(cmd));
			except Exception as e :
				send_json({"ec": "-100", "msg": "Error: "+str(e)});
		print "I am done with him"
		conn.close();

	def timer_cleaner():
		while(True):
			time.sleep(cleaner_timeout);
			print "Cleaner Aquired Lock",;
			lock.acquire();
			lock.release();
			print "Cleaner release Lock";
	threading.Thread(target=timer_cleaner).start();
	while True:
		print "Waiting...";
		conn, client_address = sock.accept();
		print "Found Client";
		lock.acquire();
		talk(conn,client_address);
		lock.release();
	sock.close();

print "I am ",getmyip()," On port ",listen_port;
serv();


