import sys, os

execfile("includes/setting.py");
execfile(_mslib+"py/func.py");

def setp():
	print elc("chmod 777 "+_mslib+"alldef -R");

def compile(): #compile all
	folder = "templates/";
	parser = _mslib+"ocaml/calc";
	compiledf = ".compiled"
	cmd = lambda f: eval("["+ elc(parser+" "+f+" 2> /dev/null") + "]");
	list(write_file(folder+compiledf+"/"+i, str(cmd(folder+i)) ) for i in os.listdir(folder) if os.path.isfile(folder+i) and (i not in [compiledf]));
	write_file(folder+compiledf+"/"+"defines", str(fold(lambda x,y: x+y, list(cmd(x) for x in allfile_rec(_mslib+"alldef/")), []) ));


if(len(sys.argv) >= 2 ):
	cmd = sys.argv[1]
	if( cmd == "setp" ):
		setp();
	elif( cmd == "compile" ):
		compile();

