


class json{
public:
	int ival;
	float fval;
	string sval;
	vector<json>jsonl;
	map<string, json> jsonm;
	bool isi, iss, isl, ism, isn, isb, isf;
	void reset() {
		isi = iss = isl = ism = isn = isb = isf = false;
	}
	json() {
		this->reset();
	}
	json(int x) {
		this->reset();
		ival = x;
		isi = 1;
	}
	json(string x) {
		this->reset();
		sval = x;
		iss = 1;
	}
	json(vector<json>l) {
		this->reset();
		jsonl = l;
		isl = 1;
	}
	json(map<string, json> m) {
		this->reset();
		jsonm = m;
		ism = 1;
	}
	// json(char c, ...) {
	// 	va_list ap;
	// 	va_start(ap, 1);
	// 	this->reset();
	// 	if(c=='i') {
	// 		isi = true;
	// 		ival = va_arg(ap, int);
	// 	}
	// 	else if (c=='s') {
	// 		iss = true;
	// 		sval = va_arg(ap, string);
	// 	}
	// 	else if(c=='n')
	// 		isn = true;
	// 	else if(c=='b') {
	// 		isb = true;
	// 		ival = va_arg(ap, int);
	// 	}
	// 	else if(c=='f') {
	// 		isf = true;
	// 		fval = va_arg(ap, float);
	// 	}
	// 	else {
	// 		int n_args = va_arg(ap, int);
	// 		if (c=='l') {
	// 			isl = true;
	// 			va_start(ap, n_args);
	// 			FL(i, n_args) {
	// 				jsonl.PUSH(va_arg(ap, json));
	// 			}
	// 		} else if(c=='m') {
	// 			ism = true;
	// 			va_start(ap, n_args*2);
	// 			FL(i, n_args) {
	// 				addkey(va_arg(ap, string), va_arg(ap, json));
	// 			}
	// 		}
	// 	}
	// }
	void addkey(string s1, json j) {
		this->jsonm[s1] = j;
		this->jsonl.PUSH(json(s1));
	}
	string __str__();
	void parse(istream& fd);
};

class jsonp {
public:
	json*j;
	jsonp(json*j1) {
		j = j1;
	}
	~jsonp() {
		//cout<<"It is free... Chill"<<endl;
		//free j;
	}
};

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
		string a = va_arg(ap, jsonp).j->sval;
		cout<<a<<endl;
	}
	va_end(ap);
}



