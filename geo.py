#!/usr/bin/python 
# -*- coding: utf-8 -*-

# 
# @see https://developers.google.com/maps/documentation/geocoding/?hl=ja
# 

import sys, urllib, json, time, csv

writecsv = csv.writer(file("out.csv", 'w')) 

def output(data):
	tmp = []
	# print data.items()
	for col in data:

		if (isinstance(col, unicode)) :
			col = col.encode("utf_8")
		else:
			col = str(col)

		print col,
		tmp.append(col);
	
	print 
	writecsv.writerow(tmp)


def onerror(status):
	print "respones status : " + status
	sys.exit()


def parseresponse(response):
	results		= response['results'][0]
	location	= results['geometry']['location']
	short_name	= results['address_components'][0]['short_name']
	address		= results['formatted_address']
	return location.values() + [short_name, address]


def callapi(query):
	# 
	# サポートされている言語
	# @see https://spreadsheets.google.com/pub?key=p9pdwsai2hDMsLkXsoM05KQ&gid=1
	#
	params = [
	    ('address', query),
	    ('region', 'jp'),
	    ('language', 'ja'),
	    ('sensor', 'false'),
	]

	domain	= 'http://maps.google.com/maps/api/geocode/json'

	url		= domain + '?' + urllib.urlencode(params)
	res		= urllib.urlopen(url)

	return json.load(res)


def main(query):
	res		= callapi(query)
	status	= res['status']
	prefix	= [query, status];

	callback = {
		'OK' : (lambda : output( prefix + parseresponse(res))),
		'ZERO_RESULTS' : (lambda : output(prefix)),
		'REQUEST_DENIED' : (lambda : onerror(status)),
		'INVALID_REQUEST' : (lambda : onerror(status)),
		'OVER_QUERY_LIMIT' : (lambda : onerror(status)),
	}

	if status in callback.keys():
		callback[status]()
	else:
		onerror('unknown error')


for line in sys.stdin:
	query		= line.rstrip()	# 改行を削除

	if query != "":
		main(query)
		time.sleep(5)
