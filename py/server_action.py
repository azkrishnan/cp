
class server_action:
	def handler(self, cmd):
		self.ec = 1;
		computed = eval("self."+cmd["action"]+"(cmd)");
		return {"ec": self.ec, "data": computed};

	def tnow(self, cmd):
		return tnow();

	def query(self, cmd):
		return "Saini";

