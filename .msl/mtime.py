#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from msl import *
from msl.mtime import *;

from time import mktime

import datetime;

_localtz = doifcan(lambda: pytz.timezone("Asia/Calcutta"));

def timenow():
	return int(mktime(datetime.datetime.now(_localtz).timetuple()));

tnow = timenow;

def time2format(formate, tat = None):#tat: TimeAt
	return datetime.datetime.fromtimestamp(rifn(tat, tnow())).strftime(formate);

t2f = time2format;

def str2time(times, formate = None):
	# formates = gen_form(['']+gen_form(['%d-%m-'], ['%y', '%Y']), [' '], ['', '%I:%M:%S %p', '%H:%M:%S', '%I:%M %p', '%H:%M' ])
	formates = ['', ' %I:%M:%S %p', ' %H:%M:%S', ' %I:%M %p', ' %H:%M', '%d-%m-%y ', '%d-%m-%y %I:%M:%S %p', '%d-%m-%y %H:%M:%S', '%d-%m-%y %I:%M %p', '%d-%m-%y %H:%M', '%d-%m-%Y ', '%d-%m-%Y %I:%M:%S %p', '%d-%m-%Y %H:%M:%S', '%d-%m-%Y %I:%M %p', '%d-%m-%Y %H:%M'];
	return (lambda x: x if type(x) == int else 0 )(fold( lambda x,y: rifn(doifcan(lambda x,y: int(time.mktime(datetime.datetime.strptime(x,y.strip()).timetuple())) , (x, y)), x), formates, re.sub('\s+', ' ', times).strip()));

t2f_date = lambda tat=None: time2format("%d-%m-%Y", tat);
t2f_time = lambda tat=None: time2format("%d-%m-%y %I:%M:%S %p", tat);

def daystarttime(tat = None):
	return s2t(t2f_date(tat));

s2t = str2time;

def timeondate(d, m, y):
	return s2t(str(d)+"-"+str(m)+"-"+str(y));
