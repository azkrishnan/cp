
class json{
public:
	void* data;
	char type;
	inline void set_int(int x) {
		data = new int(x);
	}
	inline void set_str(string x) {
		data = new string(x);
	}
	inline void init_list() {
		data = new vector<json>();
	}
	inline void init_map() {
		data = new pair<void*, void*>(new map<sting, json>(), new vector<string>());
	}

	inline int get_int() {
		return *((int*)data);
	}
	inline string get_str() {
		return *((string*)data);
	}
	inline vector<json>* get_list() {
		return ((vector<json>*)data);
	}
	inline map<string, json>* get_map() {
		return (((pair<int, int>*)data)->first);
	}
	inline vector<string> get_keys() {// for map only
		return *(((pair<int, int>*)data)->second);
	}
	json() {
	}
	json(double x) {
		type = 'f';
		data = new double(x);
	}
	json(string x) {
		type = 's';
		data = new string(x);
	}
	json(char c) {
		type = c;
	}
	json(char c, int num, ...) {
		type = c;
		va_list ap;
		int n_args = num;
		if(c=='i') {
			this->set_int(num);
		}
		else if (c=='l') {
			va_start(ap, num);
			FL(i, n_args) {
				pushjsonl(va_arg(ap, json*));
			}
			va_end(ap);
		} else if (c=='m') {
			ism = true;
			num*=2;
			va_start(ap, num);
			FL(i, n_args) {
				string key = va_arg(ap, json*)->sval;
				addkey(key, va_arg(ap, json*));
			}
			va_end(ap);
		}
	}
	void pushjsonl(json*j) {
		get_list()->PUSH(*j);
		delete j;
	}
	void addkey(string s1, json j) {
		this->jsonm[s1] = j;
		this->jsonl.PUSH(json(s1));
	}
	void addkey(string s1, json* j) {
		addkey(s1, *j);
		delete j;
	}
	string __str__();
	json*copy();
	void parse(istream& fd);
	void self_Not() {
		ival = !ival;
	}
	json* op_Get(json j);
	void self_Set(json j, json j1);
	json op_Attr(string s);
	json op_Ife();
};

#define VALUE(j) (j.isi ? j.ival: j.sval)
#define INDEXARR(j) (j.isi ? j.ival: j.jsonl.size())
#define INDEXARRVAL(j, i) (j.isi ? i: j.jsonl[i])



json* json::copy() {
	json*j = new json();
	*j = *this;
	return j;
}

json* json::op_Get(json j) {
	return (isl ? &jsonl[j.ival]: &jsonm[j.sval]);
}

json json::op_Attr(string s) {
	if(s=="len") {
		return json('i', jsonl.size());
	} else if( s == "keys" ) {
		json j('l');
		j.jsonl = jsonl;
		return jsonl;
	} else if( s == "gchars" ) {
		return *this;
	}
}



typedef map<string, json> mapsj;
#define MAPSJL(it, m) for(mapsj::iterator it = m.begin(); it != m.end(); it++) 

string json::__str__() {
	json j = *this;
	if (j.isn)
		return "null";
	if (j.isb)
		return (j.ival?"true":"false");
	else if (j.isi) 
		return int2str(j.ival);
	else if (j.isf) 
		return float2str(j.fval);
	else if (j.iss)
		return quotestring(j.sval);
	else if (j.isl) {
		string outp = "[";
		FL(i, j.jsonl.size()) {
			outp+=(j.jsonl[i].__str__());
			if(i!=j.jsonl.size()-1) 
				outp+=", ";
		}
		outp+="]";
		return outp;
	}
	else if(j.ism) {
		string outp = "{";
		FL(i, j.jsonl.size()) {
			outp+=(quotestring(j.jsonl[i].sval)+": "+ j.jsonm[ j.jsonl[i].sval ].__str__());
			if(i!=j.jsonl.size()-1) 
				outp+=", ";
		}
		outp+="}";
		return outp;
	}
	else
		return "0";
}

void json::parse(istream& fd) {
	int type,temp;
	fd>>type;
	if(type == 1) {
		this->isi = true;
		fd>>this->ival;
	} else if(type == 2) {
		this->iss = true;
		getline(fd, this->sval);
		this->sval = invqstring(this->sval.substr(1));
	} else if(type == 3) {
		int listlen;
		fd>>listlen;
		this->isl = true;
		FL(i, listlen) {
			json j;
			j.parse(fd);
			this->jsonl.PUSH(j);
		}
	} else if(type == 4) {
		int listlen;
		fd>>listlen;
		this->ism = true;
		FL(i, listlen) {
			fd>>temp;
			string key;
			getline(fd, key);
			key = invqstring(key.substr(1));
			json j;
			j.parse(fd);
			this->addkey(key, j);
		}
	} else if(type==5) {
		this->isn =true;
	} else if(type == 6) {
		this->isb = true;
		fd>> this->ival;
	} else if(type == 7) {
		this->isf = true;
		fd>>this->fval;
	}
}

json parse(istream& fd) {
	try {
		json j;
		j.parse(fd);
		return j;
	} catch (const char* msg) {
		cout<<":(  " <<msg<<endl;
	}
}

void maxof(int n_args, ...) {
	va_list ap;
	va_start(ap, n_args);
	for(int i = 1; i <= n_args; i++) {
		string a = va_arg(ap, json*)->sval;
		cout<<a<<endl;
	}
	va_end(ap);
}



