

class a:
	def __init__(self):
		self.x= 131;
		print globals()["__builtins__"];
		print self.f;
	def f(self):
		print "Vikash";


b=a();


print b.x