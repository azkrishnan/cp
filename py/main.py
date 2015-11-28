_sql = sqllib();

execfile(ROOT+"py/cp.py");

_cp = cp();

class pagehandler:
	def __init__(self, name):
		self.name = name;
		if(False and _server == "gcl"):
			elc("python client.py 10.208.20.186 ./compile");
		self.jsdata = {"HOST": HOST, "BASE": BASE, "curpage": self.name, "_server": _server};
		self.methodmap = {"index": self.index, "test": self.index, "upload": self.upload};
		self.alltable = ["maininfo", "tabs", "cat", "subcat", "provider", "providerform"];

	def call(self):
		return sifu(( rifn(self.methodmap[self.name](), {}) if self.methodmap.has_key(self.name) else {}), "jsdata", json.dumps(self.jsdata));

	def index(self):
		pid = intf(g(_get, "pid"));
		nhost = g(_get, "nhost" , HOST);
		# catgs = catgtree()
		# mifu(self.jsdata, sifu(catgs, "pid", pid));
		catgs = {"maininfocatg": {"1": {"1": {"1": [{"provider_index": 1}, {"provider_index": 2}, {"provider_index": 1}, {"provider_index": 2}, {"provider_index": 1}, {"provider_index": 2}], "2": [{"provider_index": 1}, {"provider_index": 5}, {"provider_index": 1}, {"provider_index": 5}, {"provider_index": 1}, {"provider_index": 5}], "3": [{"provider_index": 1}, {"provider_index": 1}, {"provider_index": 1}], "4": [{"provider_index": 1}, {"provider_index": 1}, {"provider_index": 1}], "5": [{"provider_index": 1}, {"provider_index": 3}, {"provider_index": 1}, {"provider_index": 3}, {"provider_index": 1}, {"provider_index": 3}], "6": [{"provider_index": 1}, {"provider_index": 1}, {"provider_index": 1}], "7": [{"provider_index": 1}, {"provider_index": 6}, {"provider_index": 1}, {"provider_index": 6}, {"provider_index": 1}, {"provider_index": 6}], "8": [{"provider_index": 4}, {"provider_index": 4}, {"provider_index": 4}], "9": [{"provider_index": 7}, {"provider_index": 7}, {"provider_index": 7}]}, "2": {"10": [{"provider_index": 8}, {"provider_index": 9}, {"provider_index": 10}, {"provider_index": 8}, {"provider_index": 9}, {"provider_index": 10}, {"provider_index": 8}, {"provider_index": 9}, {"provider_index": 10}]}, "3": {"11": [{"provider_index": 8}, {"provider_index": 9}, {"provider_index": 10}, {"provider_index": 8}, {"provider_index": 9}, {"provider_index": 10}, {"provider_index": 8}, {"provider_index": 9}, {"provider_index": 10}]}, "4": {"12": [{"provider_index": 11}, {"provider_index": 11}, {"provider_index": 11}], "13": [{"provider_index": 11}, {"provider_index": 11}, {"provider_index": 11}], "14": [{"provider_index": 11}, {"provider_index": 11}, {"provider_index": 11}]}, "5": {"16": [{"provider_index": 12}, {"provider_index": 12}, {"provider_index": 12}], "17": [{"provider_index": 12}, {"provider_index": 12}, {"provider_index": 12}], "18": [{"provider_index": 12}, {"provider_index": 12}, {"provider_index": 12}], "19": [{"provider_index": 12}, {"provider_index": 12}, {"provider_index": 12}], "20": [{"provider_index": 12}, {"provider_index": 12}, {"provider_index": 12}], "15": [{"provider_index": 12}, {"provider_index": 12}, {"provider_index": 12}]}, "10": {"2": [{"provider_index": 1}]}}, "2": {"1": {"1": [{"provider_index": 1}, {"provider_index": 2}, {"provider_index": 1}, {"provider_index": 2}, {"provider_index": 1}, {"provider_index": 2}], "2": [{"provider_index": 1}, {"provider_index": 5}, {"provider_index": 1}, {"provider_index": 5}, {"provider_index": 1}, {"provider_index": 5}], "3": [{"provider_index": 1}, {"provider_index": 1}, {"provider_index": 1}], "4": [{"provider_index": 1}, {"provider_index": 1}, {"provider_index": 1}], "5": [{"provider_index": 1}, {"provider_index": 3}, {"provider_index": 1}, {"provider_index": 3}, {"provider_index": 1}, {"provider_index": 3}], "6": [{"provider_index": 1}, {"provider_index": 1}, {"provider_index": 1}], "7": [{"provider_index": 1}, {"provider_index": 6}, {"provider_index": 1}, {"provider_index": 6}, {"provider_index": 1}, {"provider_index": 6}], "8": [{"provider_index": 4}, {"provider_index": 4}, {"provider_index": 4}], "9": [{"provider_index": 7}, {"provider_index": 7}, {"provider_index": 7}]}, "2": {"10": [{"provider_index": 8}, {"provider_index": 9}, {"provider_index": 10}, {"provider_index": 8}, {"provider_index": 9}, {"provider_index": 10}, {"provider_index": 8}, {"provider_index": 9}, {"provider_index": 10}]}, "3": {"11": [{"provider_index": 8}, {"provider_index": 9}, {"provider_index": 10}, {"provider_index": 8}, {"provider_index": 9}, {"provider_index": 10}, {"provider_index": 8}, {"provider_index": 9}, {"provider_index": 10}]}, "5": {"16": [{"provider_index": 12}, {"provider_index": 12}, {"provider_index": 12}], "17": [{"provider_index": 12}, {"provider_index": 12}, {"provider_index": 12}], "18": [{"provider_index": 12}, {"provider_index": 12}, {"provider_index": 12}], "19": [{"provider_index": 12}, {"provider_index": 12}, {"provider_index": 12}], "20": [{"provider_index": 12}, {"provider_index": 12}, {"provider_index": 12}], "15": [{"provider_index": 12}, {"provider_index": 12}, {"provider_index": 12}]}}, "3": {"8": {"10": [{"provider_index": 15}, {"provider_index": 15}, {"provider_index": 15}]}, "9": {"10": [{"provider_index": 15}, {"provider_index": 16}, {"provider_index": 15}, {"provider_index": 16}, {"provider_index": 15}, {"provider_index": 16}]}, "6": {"10": [{"provider_index": 13}, {"provider_index": 13}, {"provider_index": 13}]}, "7": {"10": [{"provider_index": 14}, {"provider_index": 14}, {"provider_index": 14}]}}}, "catg": [{"child": [{"child": [{"child": [{"info": None, "id": 1}, {"info": None, "id": 2}, {"info": None, "id": 1}, {"info": None, "id": 2}, {"info": None, "id": 1}, {"info": None, "id": 2}], "name": "Piano", "id": 1}, {"child": [{"info": None, "id": 1}, {"info": None, "id": 5}, {"info": None, "id": 1}, {"info": None, "id": 5}, {"info": None, "id": 1}, {"info": None, "id": 5}], "name": "Flute", "id": 2}, {"child": [{"info": None, "id": 1}, {"info": None, "id": 1}, {"info": None, "id": 1}], "name": "Clarinet", "id": 3}, {"child": [{"info": None, "id": 1}, {"info": None, "id": 1}, {"info": None, "id": 1}], "name": "Saxophone", "id": 4}, {"child": [{"info": None, "id": 1}, {"info": None, "id": 3}, {"info": None, "id": 1}, {"info": None, "id": 3}, {"info": None, "id": 1}, {"info": None, "id": 3}], "name": "Violin", "id": 5}, {"child": [{"info": None, "id": 1}, {"info": None, "id": 1}, {"info": None, "id": 1}], "name": "Guitar", "id": 6}, {"child": [{"info": None, "id": 1}, {"info": None, "id": 6}, {"info": None, "id": 1}, {"info": None, "id": 6}, {"info": None, "id": 1}, {"info": None, "id": 6}], "name": "Vocal", "id": 7}, {"child": [{"info": None, "id": 4}, {"info": None, "id": 4}, {"info": None, "id": 4}], "name": "Viola", "id": 8}, {"child": [{"info": None, "id": 7}, {"info": None, "id": 7}, {"info": None, "id": 7}], "name": "Cello", "id": 9}], "name": "Music", "id": 1}, {"child": [{"child": [{"info": None, "id": 8}, {"info": None, "id": 9}, {"info": None, "id": 10}, {"info": None, "id": 8}, {"info": None, "id": 9}, {"info": None, "id": 10}, {"info": None, "id": 8}, {"info": None, "id": 9}, {"info": None, "id": 10}], "name": "Miscellaneous", "id": 10}], "name": "Gym", "id": 2}, {"child": [{"child": [{"info": None, "id": 8}, {"info": None, "id": 9}, {"info": None, "id": 10}, {"info": None, "id": 8}, {"info": None, "id": 9}, {"info": None, "id": 10}, {"info": None, "id": 8}, {"info": None, "id": 9}, {"info": None, "id": 10}], "name": "Gym", "id": 11}], "name": "Body, Health & Fitness", "id": 3}, {"child": [{"child": [{"info": None, "id": 11}, {"info": None, "id": 11}, {"info": None, "id": 11}], "name": "Arts", "id": 12}, {"child": [{"info": None, "id": 11}, {"info": None, "id": 11}, {"info": None, "id": 11}], "name": "Ceramics", "id": 13}, {"child": [{"info": None, "id": 11}, {"info": None, "id": 11}, {"info": None, "id": 11}], "name": "Pottery Painting", "id": 14}], "name": "Arts", "id": 4}, {"child": [{"child": [{"info": None, "id": 12}, {"info": None, "id": 12}, {"info": None, "id": 12}], "name": "Tamil", "id": 16}, {"child": [{"info": None, "id": 12}, {"info": None, "id": 12}, {"info": None, "id": 12}], "name": "Malayalam", "id": 17}, {"child": [{"info": None, "id": 12}, {"info": None, "id": 12}, {"info": None, "id": 12}], "name": "Kannada", "id": 18}, {"child": [{"info": None, "id": 12}, {"info": None, "id": 12}, {"info": None, "id": 12}], "name": "Telugu", "id": 19}, {"child": [{"info": None, "id": 12}, {"info": None, "id": 12}, {"info": None, "id": 12}], "name": "Sanskrit", "id": 20}, {"child": [{"info": None, "id": 12}, {"info": None, "id": 12}, {"info": None, "id": 12}], "name": "Hindi", "id": 15}], "name": "Foreign Languages", "id": 5}, {"child": [{"child": [{"info": None, "id": 1}], "name": "Flute", "id": 2}], "name": "Music1", "id": 10}], "icon": "photo/kid1.png", "name": "Kids", "id": 1}, {"child": [{"child": [{"child": [{"info": None, "id": 1}, {"info": None, "id": 2}, {"info": None, "id": 1}, {"info": None, "id": 2}, {"info": None, "id": 1}, {"info": None, "id": 2}], "name": "Piano", "id": 1}, {"child": [{"info": None, "id": 1}, {"info": None, "id": 5}, {"info": None, "id": 1}, {"info": None, "id": 5}, {"info": None, "id": 1}, {"info": None, "id": 5}], "name": "Flute", "id": 2}, {"child": [{"info": None, "id": 1}, {"info": None, "id": 1}, {"info": None, "id": 1}], "name": "Clarinet", "id": 3}, {"child": [{"info": None, "id": 1}, {"info": None, "id": 1}, {"info": None, "id": 1}], "name": "Saxophone", "id": 4}, {"child": [{"info": None, "id": 1}, {"info": None, "id": 3}, {"info": None, "id": 1}, {"info": None, "id": 3}, {"info": None, "id": 1}, {"info": None, "id": 3}], "name": "Violin", "id": 5}, {"child": [{"info": None, "id": 1}, {"info": None, "id": 1}, {"info": None, "id": 1}], "name": "Guitar", "id": 6}, {"child": [{"info": None, "id": 1}, {"info": None, "id": 6}, {"info": None, "id": 1}, {"info": None, "id": 6}, {"info": None, "id": 1}, {"info": None, "id": 6}], "name": "Vocal", "id": 7}, {"child": [{"info": None, "id": 4}, {"info": None, "id": 4}, {"info": None, "id": 4}], "name": "Viola", "id": 8}, {"child": [{"info": None, "id": 7}, {"info": None, "id": 7}, {"info": None, "id": 7}], "name": "Cello", "id": 9}], "name": "Music", "id": 1}, {"child": [{"child": [{"info": None, "id": 8}, {"info": None, "id": 9}, {"info": None, "id": 10}, {"info": None, "id": 8}, {"info": None, "id": 9}, {"info": None, "id": 10}, {"info": None, "id": 8}, {"info": None, "id": 9}, {"info": None, "id": 10}], "name": "Miscellaneous", "id": 10}], "name": "Gym", "id": 2}, {"child": [{"child": [{"info": None, "id": 8}, {"info": None, "id": 9}, {"info": None, "id": 10}, {"info": None, "id": 8}, {"info": None, "id": 9}, {"info": None, "id": 10}, {"info": None, "id": 8}, {"info": None, "id": 9}, {"info": None, "id": 10}], "name": "Gym", "id": 11}], "name": "Body, Health & Fitness", "id": 3}, {"child": [{"child": [{"info": None, "id": 12}, {"info": None, "id": 12}, {"info": None, "id": 12}], "name": "Tamil", "id": 16}, {"child": [{"info": None, "id": 12}, {"info": None, "id": 12}, {"info": None, "id": 12}], "name": "Malayalam", "id": 17}, {"child": [{"info": None, "id": 12}, {"info": None, "id": 12}, {"info": None, "id": 12}], "name": "Kannada", "id": 18}, {"child": [{"info": None, "id": 12}, {"info": None, "id": 12}, {"info": None, "id": 12}], "name": "Telugu", "id": 19}, {"child": [{"info": None, "id": 12}, {"info": None, "id": 12}, {"info": None, "id": 12}], "name": "Sanskrit", "id": 20}, {"child": [{"info": None, "id": 12}, {"info": None, "id": 12}, {"info": None, "id": 12}], "name": "Hindi", "id": 15}], "name": "Foreign Languages", "id": 5}], "icon": "photo/adult1.png", "name": "Adults", "id": 2}, {"child": [{"child": [{"child": [{"info": None, "id": 15}, {"info": None, "id": 15}, {"info": None, "id": 15}], "name": "Miscellaneous", "id": 10}], "name": "Pet Walking", "id": 8}, {"child": [{"child": [{"info": None, "id": 15}, {"info": None, "id": 16}, {"info": None, "id": 15}, {"info": None, "id": 16}, {"info": None, "id": 15}, {"info": None, "id": 16}], "name": "Miscellaneous", "id": 10}], "name": "Pet Walking1", "id": 9}, {"child": [{"child": [{"info": None, "id": 13}, {"info": None, "id": 13}, {"info": None, "id": 13}], "name": "Miscellaneous", "id": 10}], "name": "Pet Training", "id": 6}, {"child": [{"child": [{"info": None, "id": 14}, {"info": None, "id": 14}, {"info": None, "id": 14}], "name": "Miscellaneous", "id": 10}], "name": "Pet Sitting", "id": 7}], "icon": "photo/dog1.png", "name": "Pets", "id": 3}], "pid": 0, "HOST": "http://54.149.49.212/cp/", "BASE": "http://54.149.49.212/cp/index.php/", "curpage": "index", "provider": {"1": {"name_provider": "Fremont\u00a0Mission\u00a0Music\u00a0Institute", "phone": "510-438-9752", "address": "40932 Fremont Blvd, Fremont, CA 94538", "website": "http://fremontmissionmusicinstitute.com/", "lat": 37.5335276, "lng": -121.9600244}, "2": {"name_provider": "Anna Poklewski Academy of Music, LLC", "phone": "(510) 791-2726", "address": "39660 Mission Blvd, Fremont, CA 94539", "website": "http://www.annapoklewskiacademyofmusic.com/", "lat": 37.5607886, "lng": -121.9562632}, "3": {"name_provider": "Anna Poklewski Academy of Music, LLC", "phone": "(510) 791-2726", "address": "39661 Mission Blvd, Fremont, CA 94539", "website": "http://www.annapoklewskiacademyofmusic.com/", "lat": 37.5601772, "lng": -121.9564058}, "4": {"name_provider": "Anna Poklewski Academy of Music, LLC", "phone": "(510) 791-2726", "address": "39662 Mission Blvd, Fremont, CA 94539", "website": "http://www.annapoklewskiacademyofmusic.com/", "lat": 37.560386, "lng": -121.9564362}, "5": {"name_provider": "Anna Poklewski Academy of Music, LLC", "phone": "(510) 791-2726", "address": "39663 Mission Blvd, Fremont, CA 94539", "website": "http://www.annapoklewskiacademyofmusic.com/", "lat": 37.5601616, "lng": -121.9563806}, "6": {"name_provider": "Anna Poklewski Academy of Music, LLC", "phone": "(510) 791-2726", "address": "39664 Mission Blvd, Fremont, CA 94539", "website": "http://www.annapoklewskiacademyofmusic.com/", "lat": 37.56038, "lng": -121.9564274}, "7": {"name_provider": "Anna Poklewski Academy of Music, LLC", "phone": "(510) 791-2726", "address": "39665 Mission Blvd, Fremont, CA 94539", "website": "http://www.annapoklewskiacademyofmusic.com/", "lat": 37.5601459, "lng": -121.9563554}, "8": {"name_provider": "24 Hour Fitness", "phone": "(510) 795-6666", "address": "39300 Paseo Padre Pkwy\nFremont, CA", "website": "http://www.24hourfitness.com/", "lat": 37.5536275, "lng": -121.9780933}, "9": {"name_provider": "24 Hour Fitness", "phone": "(510) 226-6900", "address": "4500 Auto Mall Pkwy\nFremont, CA", "website": "http://www.24hourfitness.com/", "lat": 37.509425, "lng": -121.9583859}, "10": {"name_provider": "24 Hour Fitness", "phone": "(510) 494-9348", "address": "Newpark Plaza, 5234 Newpark Mall\nNewark, CA", "website": "http://www.24hourfitness.com/", "lat": 37.5268552, "lng": -122.0017578}, "11": {"name_provider": "Green Forest Art Studio", "phone": "(415) 595-4680", "address": "32627 Alvarado Blvd\nUnion City, CA 94587", "website": "greenforestartstudio.com", "lat": 37.5862062, "lng": -122.0634933}, "12": {"name_provider": "Chinmaya Mission Bala Vihar", "phone": "", "address": "Washington High School\n38442 Fremont Blvd\nFremont,CA", "website": "http://www.cmsj.org/chinmaya-bala-vihar/location/fremont/", "lat": 37.5520431, "lng": -121.9948844}, "13": {"name_provider": "Titan's Kingdom", "phone": "(510) 538-7837", "address": "597 C St, Hayward, CA 94541", "website": "", "lat": 37.6686276, "lng": -122.088587}, "14": {"name_provider": "Pawsitive Steps Dog Training", "phone": "(510) 461-2205", "address": "Hayward, CA 94545", "website": "", "lat": 37.6063621, "lng": -122.1178261}, "15": {"name_provider": "New Age Pet", "phone": "(510) 887-5976", "address": "25063 Viking St, Hayward, CA 94545", "website": "http://www.newagepet.net/", "lat": 37.6367247, "lng": -122.1251753}, "16": {"name_provider": "Just Fun !", "phone": "(510) 887-5976", "address": "25063 Viking St, Hayward, CA 94545", "website": "http://www.newagepet.net/", "lat": 37.6367247, "lng": -122.1251753}}, "_server": "aws"}
		mifu(catgs, {"commoncats": eval(read_file("data/commondata.pyf")), "pid": pid, "nhost": nhost, "our_story_content": read_file("data/aboutusc")});
		return catgs;

	def test(self):
		return {"maininfocatg": {"1": {"1": {"1": [{"provider_index": 1}, {"provider_index": 2}, {"provider_index": 1}, {"provider_index": 2}, {"provider_index": 1}, {"provider_index": 2}], "2": [{"provider_index": 1}, {"provider_index": 5}, {"provider_index": 1}, {"provider_index": 5}, {"provider_index": 1}, {"provider_index": 5}], "3": [{"provider_index": 1}, {"provider_index": 1}, {"provider_index": 1}], "4": [{"provider_index": 1}, {"provider_index": 1}, {"provider_index": 1}], "5": [{"provider_index": 1}, {"provider_index": 3}, {"provider_index": 1}, {"provider_index": 3}, {"provider_index": 1}, {"provider_index": 3}], "6": [{"provider_index": 1}, {"provider_index": 1}, {"provider_index": 1}], "7": [{"provider_index": 1}, {"provider_index": 6}, {"provider_index": 1}, {"provider_index": 6}, {"provider_index": 1}, {"provider_index": 6}], "8": [{"provider_index": 4}, {"provider_index": 4}, {"provider_index": 4}], "9": [{"provider_index": 7}, {"provider_index": 7}, {"provider_index": 7}]}, "2": {"10": [{"provider_index": 8}, {"provider_index": 9}, {"provider_index": 10}, {"provider_index": 8}, {"provider_index": 9}, {"provider_index": 10}, {"provider_index": 8}, {"provider_index": 9}, {"provider_index": 10}]}, "3": {"11": [{"provider_index": 8}, {"provider_index": 9}, {"provider_index": 10}, {"provider_index": 8}, {"provider_index": 9}, {"provider_index": 10}, {"provider_index": 8}, {"provider_index": 9}, {"provider_index": 10}]}, "4": {"12": [{"provider_index": 11}, {"provider_index": 11}, {"provider_index": 11}], "13": [{"provider_index": 11}, {"provider_index": 11}, {"provider_index": 11}], "14": [{"provider_index": 11}, {"provider_index": 11}, {"provider_index": 11}]}, "5": {"16": [{"provider_index": 12}, {"provider_index": 12}, {"provider_index": 12}], "17": [{"provider_index": 12}, {"provider_index": 12}, {"provider_index": 12}], "18": [{"provider_index": 12}, {"provider_index": 12}, {"provider_index": 12}], "19": [{"provider_index": 12}, {"provider_index": 12}, {"provider_index": 12}], "20": [{"provider_index": 12}, {"provider_index": 12}, {"provider_index": 12}], "15": [{"provider_index": 12}, {"provider_index": 12}, {"provider_index": 12}]}, "10": {"2": [{"provider_index": 1}]}}, "2": {"1": {"1": [{"provider_index": 1}, {"provider_index": 2}, {"provider_index": 1}, {"provider_index": 2}, {"provider_index": 1}, {"provider_index": 2}], "2": [{"provider_index": 1}, {"provider_index": 5}, {"provider_index": 1}, {"provider_index": 5}, {"provider_index": 1}, {"provider_index": 5}], "3": [{"provider_index": 1}, {"provider_index": 1}, {"provider_index": 1}], "4": [{"provider_index": 1}, {"provider_index": 1}, {"provider_index": 1}], "5": [{"provider_index": 1}, {"provider_index": 3}, {"provider_index": 1}, {"provider_index": 3}, {"provider_index": 1}, {"provider_index": 3}], "6": [{"provider_index": 1}, {"provider_index": 1}, {"provider_index": 1}], "7": [{"provider_index": 1}, {"provider_index": 6}, {"provider_index": 1}, {"provider_index": 6}, {"provider_index": 1}, {"provider_index": 6}], "8": [{"provider_index": 4}, {"provider_index": 4}, {"provider_index": 4}], "9": [{"provider_index": 7}, {"provider_index": 7}, {"provider_index": 7}]}, "2": {"10": [{"provider_index": 8}, {"provider_index": 9}, {"provider_index": 10}, {"provider_index": 8}, {"provider_index": 9}, {"provider_index": 10}, {"provider_index": 8}, {"provider_index": 9}, {"provider_index": 10}]}, "3": {"11": [{"provider_index": 8}, {"provider_index": 9}, {"provider_index": 10}, {"provider_index": 8}, {"provider_index": 9}, {"provider_index": 10}, {"provider_index": 8}, {"provider_index": 9}, {"provider_index": 10}]}, "5": {"16": [{"provider_index": 12}, {"provider_index": 12}, {"provider_index": 12}], "17": [{"provider_index": 12}, {"provider_index": 12}, {"provider_index": 12}], "18": [{"provider_index": 12}, {"provider_index": 12}, {"provider_index": 12}], "19": [{"provider_index": 12}, {"provider_index": 12}, {"provider_index": 12}], "20": [{"provider_index": 12}, {"provider_index": 12}, {"provider_index": 12}], "15": [{"provider_index": 12}, {"provider_index": 12}, {"provider_index": 12}]}}, "3": {"8": {"10": [{"provider_index": 15}, {"provider_index": 15}, {"provider_index": 15}]}, "9": {"10": [{"provider_index": 15}, {"provider_index": 16}, {"provider_index": 15}, {"provider_index": 16}, {"provider_index": 15}, {"provider_index": 16}]}, "6": {"10": [{"provider_index": 13}, {"provider_index": 13}, {"provider_index": 13}]}, "7": {"10": [{"provider_index": 14}, {"provider_index": 14}, {"provider_index": 14}]}}}, "catg": [{"child": [{"child": [{"child": [{"info": None, "id": 1}, {"info": None, "id": 2}, {"info": None, "id": 1}, {"info": None, "id": 2}, {"info": None, "id": 1}, {"info": None, "id": 2}], "name": "Piano", "id": 1}, {"child": [{"info": None, "id": 1}, {"info": None, "id": 5}, {"info": None, "id": 1}, {"info": None, "id": 5}, {"info": None, "id": 1}, {"info": None, "id": 5}], "name": "Flute", "id": 2}, {"child": [{"info": None, "id": 1}, {"info": None, "id": 1}, {"info": None, "id": 1}], "name": "Clarinet", "id": 3}, {"child": [{"info": None, "id": 1}, {"info": None, "id": 1}, {"info": None, "id": 1}], "name": "Saxophone", "id": 4}, {"child": [{"info": None, "id": 1}, {"info": None, "id": 3}, {"info": None, "id": 1}, {"info": None, "id": 3}, {"info": None, "id": 1}, {"info": None, "id": 3}], "name": "Violin", "id": 5}, {"child": [{"info": None, "id": 1}, {"info": None, "id": 1}, {"info": None, "id": 1}], "name": "Guitar", "id": 6}, {"child": [{"info": None, "id": 1}, {"info": None, "id": 6}, {"info": None, "id": 1}, {"info": None, "id": 6}, {"info": None, "id": 1}, {"info": None, "id": 6}], "name": "Vocal", "id": 7}, {"child": [{"info": None, "id": 4}, {"info": None, "id": 4}, {"info": None, "id": 4}], "name": "Viola", "id": 8}, {"child": [{"info": None, "id": 7}, {"info": None, "id": 7}, {"info": None, "id": 7}], "name": "Cello", "id": 9}], "name": "Music", "id": 1}, {"child": [{"child": [{"info": None, "id": 8}, {"info": None, "id": 9}, {"info": None, "id": 10}, {"info": None, "id": 8}, {"info": None, "id": 9}, {"info": None, "id": 10}, {"info": None, "id": 8}, {"info": None, "id": 9}, {"info": None, "id": 10}], "name": "Miscellaneous", "id": 10}], "name": "Gym", "id": 2}, {"child": [{"child": [{"info": None, "id": 8}, {"info": None, "id": 9}, {"info": None, "id": 10}, {"info": None, "id": 8}, {"info": None, "id": 9}, {"info": None, "id": 10}, {"info": None, "id": 8}, {"info": None, "id": 9}, {"info": None, "id": 10}], "name": "Gym", "id": 11}], "name": "Body, Health & Fitness", "id": 3}, {"child": [{"child": [{"info": None, "id": 11}, {"info": None, "id": 11}, {"info": None, "id": 11}], "name": "Arts", "id": 12}, {"child": [{"info": None, "id": 11}, {"info": None, "id": 11}, {"info": None, "id": 11}], "name": "Ceramics", "id": 13}, {"child": [{"info": None, "id": 11}, {"info": None, "id": 11}, {"info": None, "id": 11}], "name": "Pottery Painting", "id": 14}], "name": "Arts", "id": 4}, {"child": [{"child": [{"info": None, "id": 12}, {"info": None, "id": 12}, {"info": None, "id": 12}], "name": "Tamil", "id": 16}, {"child": [{"info": None, "id": 12}, {"info": None, "id": 12}, {"info": None, "id": 12}], "name": "Malayalam", "id": 17}, {"child": [{"info": None, "id": 12}, {"info": None, "id": 12}, {"info": None, "id": 12}], "name": "Kannada", "id": 18}, {"child": [{"info": None, "id": 12}, {"info": None, "id": 12}, {"info": None, "id": 12}], "name": "Telugu", "id": 19}, {"child": [{"info": None, "id": 12}, {"info": None, "id": 12}, {"info": None, "id": 12}], "name": "Sanskrit", "id": 20}, {"child": [{"info": None, "id": 12}, {"info": None, "id": 12}, {"info": None, "id": 12}], "name": "Hindi", "id": 15}], "name": "Foreign Languages", "id": 5}, {"child": [{"child": [{"info": None, "id": 1}], "name": "Flute", "id": 2}], "name": "Music1", "id": 10}], "icon": "photo/kid1.png", "name": "Kids", "id": 1}, {"child": [{"child": [{"child": [{"info": None, "id": 1}, {"info": None, "id": 2}, {"info": None, "id": 1}, {"info": None, "id": 2}, {"info": None, "id": 1}, {"info": None, "id": 2}], "name": "Piano", "id": 1}, {"child": [{"info": None, "id": 1}, {"info": None, "id": 5}, {"info": None, "id": 1}, {"info": None, "id": 5}, {"info": None, "id": 1}, {"info": None, "id": 5}], "name": "Flute", "id": 2}, {"child": [{"info": None, "id": 1}, {"info": None, "id": 1}, {"info": None, "id": 1}], "name": "Clarinet", "id": 3}, {"child": [{"info": None, "id": 1}, {"info": None, "id": 1}, {"info": None, "id": 1}], "name": "Saxophone", "id": 4}, {"child": [{"info": None, "id": 1}, {"info": None, "id": 3}, {"info": None, "id": 1}, {"info": None, "id": 3}, {"info": None, "id": 1}, {"info": None, "id": 3}], "name": "Violin", "id": 5}, {"child": [{"info": None, "id": 1}, {"info": None, "id": 1}, {"info": None, "id": 1}], "name": "Guitar", "id": 6}, {"child": [{"info": None, "id": 1}, {"info": None, "id": 6}, {"info": None, "id": 1}, {"info": None, "id": 6}, {"info": None, "id": 1}, {"info": None, "id": 6}], "name": "Vocal", "id": 7}, {"child": [{"info": None, "id": 4}, {"info": None, "id": 4}, {"info": None, "id": 4}], "name": "Viola", "id": 8}, {"child": [{"info": None, "id": 7}, {"info": None, "id": 7}, {"info": None, "id": 7}], "name": "Cello", "id": 9}], "name": "Music", "id": 1}, {"child": [{"child": [{"info": None, "id": 8}, {"info": None, "id": 9}, {"info": None, "id": 10}, {"info": None, "id": 8}, {"info": None, "id": 9}, {"info": None, "id": 10}, {"info": None, "id": 8}, {"info": None, "id": 9}, {"info": None, "id": 10}], "name": "Miscellaneous", "id": 10}], "name": "Gym", "id": 2}, {"child": [{"child": [{"info": None, "id": 8}, {"info": None, "id": 9}, {"info": None, "id": 10}, {"info": None, "id": 8}, {"info": None, "id": 9}, {"info": None, "id": 10}, {"info": None, "id": 8}, {"info": None, "id": 9}, {"info": None, "id": 10}], "name": "Gym", "id": 11}], "name": "Body, Health & Fitness", "id": 3}, {"child": [{"child": [{"info": None, "id": 12}, {"info": None, "id": 12}, {"info": None, "id": 12}], "name": "Tamil", "id": 16}, {"child": [{"info": None, "id": 12}, {"info": None, "id": 12}, {"info": None, "id": 12}], "name": "Malayalam", "id": 17}, {"child": [{"info": None, "id": 12}, {"info": None, "id": 12}, {"info": None, "id": 12}], "name": "Kannada", "id": 18}, {"child": [{"info": None, "id": 12}, {"info": None, "id": 12}, {"info": None, "id": 12}], "name": "Telugu", "id": 19}, {"child": [{"info": None, "id": 12}, {"info": None, "id": 12}, {"info": None, "id": 12}], "name": "Sanskrit", "id": 20}, {"child": [{"info": None, "id": 12}, {"info": None, "id": 12}, {"info": None, "id": 12}], "name": "Hindi", "id": 15}], "name": "Foreign Languages", "id": 5}], "icon": "photo/adult1.png", "name": "Adults", "id": 2}, {"child": [{"child": [{"child": [{"info": None, "id": 15}, {"info": None, "id": 15}, {"info": None, "id": 15}], "name": "Miscellaneous", "id": 10}], "name": "Pet Walking", "id": 8}, {"child": [{"child": [{"info": None, "id": 15}, {"info": None, "id": 16}, {"info": None, "id": 15}, {"info": None, "id": 16}, {"info": None, "id": 15}, {"info": None, "id": 16}], "name": "Miscellaneous", "id": 10}], "name": "Pet Walking1", "id": 9}, {"child": [{"child": [{"info": None, "id": 13}, {"info": None, "id": 13}, {"info": None, "id": 13}], "name": "Miscellaneous", "id": 10}], "name": "Pet Training", "id": 6}, {"child": [{"child": [{"info": None, "id": 14}, {"info": None, "id": 14}, {"info": None, "id": 14}], "name": "Miscellaneous", "id": 10}], "name": "Pet Sitting", "id": 7}], "icon": "photo/dog1.png", "name": "Pets", "id": 3}], "pid": 0, "HOST": "http://54.149.49.212/cp/", "BASE": "http://54.149.49.212/cp/index.php/", "curpage": "index", "provider": {"1": {"name_provider": "Fremont\u00a0Mission\u00a0Music\u00a0Institute", "phone": "510-438-9752", "address": "40932 Fremont Blvd, Fremont, CA 94538", "website": "http://fremontmissionmusicinstitute.com/", "lat": 37.5335276, "lng": -121.9600244}, "2": {"name_provider": "Anna Poklewski Academy of Music, LLC", "phone": "(510) 791-2726", "address": "39660 Mission Blvd, Fremont, CA 94539", "website": "http://www.annapoklewskiacademyofmusic.com/", "lat": 37.5607886, "lng": -121.9562632}, "3": {"name_provider": "Anna Poklewski Academy of Music, LLC", "phone": "(510) 791-2726", "address": "39661 Mission Blvd, Fremont, CA 94539", "website": "http://www.annapoklewskiacademyofmusic.com/", "lat": 37.5601772, "lng": -121.9564058}, "4": {"name_provider": "Anna Poklewski Academy of Music, LLC", "phone": "(510) 791-2726", "address": "39662 Mission Blvd, Fremont, CA 94539", "website": "http://www.annapoklewskiacademyofmusic.com/", "lat": 37.560386, "lng": -121.9564362}, "5": {"name_provider": "Anna Poklewski Academy of Music, LLC", "phone": "(510) 791-2726", "address": "39663 Mission Blvd, Fremont, CA 94539", "website": "http://www.annapoklewskiacademyofmusic.com/", "lat": 37.5601616, "lng": -121.9563806}, "6": {"name_provider": "Anna Poklewski Academy of Music, LLC", "phone": "(510) 791-2726", "address": "39664 Mission Blvd, Fremont, CA 94539", "website": "http://www.annapoklewskiacademyofmusic.com/", "lat": 37.56038, "lng": -121.9564274}, "7": {"name_provider": "Anna Poklewski Academy of Music, LLC", "phone": "(510) 791-2726", "address": "39665 Mission Blvd, Fremont, CA 94539", "website": "http://www.annapoklewskiacademyofmusic.com/", "lat": 37.5601459, "lng": -121.9563554}, "8": {"name_provider": "24 Hour Fitness", "phone": "(510) 795-6666", "address": "39300 Paseo Padre Pkwy\nFremont, CA", "website": "http://www.24hourfitness.com/", "lat": 37.5536275, "lng": -121.9780933}, "9": {"name_provider": "24 Hour Fitness", "phone": "(510) 226-6900", "address": "4500 Auto Mall Pkwy\nFremont, CA", "website": "http://www.24hourfitness.com/", "lat": 37.509425, "lng": -121.9583859}, "10": {"name_provider": "24 Hour Fitness", "phone": "(510) 494-9348", "address": "Newpark Plaza, 5234 Newpark Mall\nNewark, CA", "website": "http://www.24hourfitness.com/", "lat": 37.5268552, "lng": -122.0017578}, "11": {"name_provider": "Green Forest Art Studio", "phone": "(415) 595-4680", "address": "32627 Alvarado Blvd\nUnion City, CA 94587", "website": "greenforestartstudio.com", "lat": 37.5862062, "lng": -122.0634933}, "12": {"name_provider": "Chinmaya Mission Bala Vihar", "phone": "", "address": "Washington High School\n38442 Fremont Blvd\nFremont,CA", "website": "http://www.cmsj.org/chinmaya-bala-vihar/location/fremont/", "lat": 37.5520431, "lng": -121.9948844}, "13": {"name_provider": "Titan's Kingdom", "phone": "(510) 538-7837", "address": "597 C St, Hayward, CA 94541", "website": "", "lat": 37.6686276, "lng": -122.088587}, "14": {"name_provider": "Pawsitive Steps Dog Training", "phone": "(510) 461-2205", "address": "Hayward, CA 94545", "website": "", "lat": 37.6063621, "lng": -122.1178261}, "15": {"name_provider": "New Age Pet", "phone": "(510) 887-5976", "address": "25063 Viking St, Hayward, CA 94545", "website": "http://www.newagepet.net/", "lat": 37.6367247, "lng": -122.1251753}, "16": {"name_provider": "Just Fun !", "phone": "(510) 887-5976", "address": "25063 Viking St, Hayward, CA 94545", "website": "http://www.newagepet.net/", "lat": 37.6367247, "lng": -122.1251753}}, "_server": "aws"}


	def upload(self):
		if(has_key(_files, "sheet")):
			datafile = "data/providers.xlsx";
			datafile = _files["sheet"]["tmp_name"];
			def updatelatlng():
				allp = _sql.sval("provider", "provider_id, address");
				for i in allp:
					latlng = google_addrtolanlat(i["address"]);
					time.sleep(0.5);
					if(latlng):
						mprint(latlng);
						_sql.uval("provider", latlng, {"provider_id": i["provider_id"]}, 1);
						mprint(latlng, i["address"]);

			def deletealltable():
				mprint(list(_sql.q("drop table if exists "+i) for i in self.alltable));

			def createtables():
				readxlx_dbdump(datafile, ['tabs', 'cat', 'subcat', 'name_provider', 'phone', 'address', 'website', 'lat', 'lng'], _sql.tabtype("vu20, vu50, vu50, v200, v20, v200, v200, r, r"), "maininfo", {"tabs":[0], "cat": [1], "subcat": [2], "provider":[3, 4, 5, 6, 7, 8]});
			if(True):
				list(_sql.q("drop table if exists "+i) for i in ["tabs", "cat", "subcat", "provider"]);
				createtables();
				updatelatlng();
		else:
			pass



	def ajaxactions(self):
		time.sleep(1);
		if( has_key(_actions, g(_post, "action"))):
			return _cp.handler(_post,  _actions[_post["action"]]);
		else:
			return {"ec": -4};

	def init(self):
		""" Read Xslx Sheet and put in Database """
		def updatelatlng():
			allp = _sql.sval("provider", "provider_id, address");
			for i in allp:
				latlng = google_addrtolanlat(i["address"]);
				if(latlng):
					_sql.uval("provider", latlng, {"provider_id": i["provider_id"]}, 1);
					print latlng, i["address"];

		def deletealltable():
			print list(_sql.q("drop table if exists "+i) for i in self.alltable);

		def createtables():
			readxlx_dbdump("data/providers.xlsx", ['tabs', 'cat', 'subcat', 'name_provider', 'phone', 'address', 'website', 'lat', 'lng'], _sql.tabtype("vu20, vu50, vu50, v200, v20, v200, v200, r, r"), "maininfo", {"tabs":[0], "cat": [1], "subcat": [2], "provider":[3, 4, 5, 6, 7, 8]});
		if(True):
			deletealltable();
			createtables();
			updatelatlng();
			#updateindbcatg(allcatgmap());
		print _sql.q("create table providerform (id int not null auto_increment, form_catg varchar(200), form_subcatg varchar(200), form_prov varchar(200), form_email varchar(200), form_phone varchar(200), form_address varchar(300), form_web varchar(200), form_sechedule varchar(300), primary key(id))");



