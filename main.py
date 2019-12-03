import sys
import json
import requests
from pyquery import PyQuery

def ForQueryInAddr(query, addr):
	global listed, primalsource
	print("Searcing in: "+addr)
	html = requests.get(addr,proxies=proxies).text
	if (query.lower() in html.lower()):
		print("Query found in: "+addr)
	data = PyQuery(html)
	links = data('a')
	for link in links:
		ahref = link.attrib['href']
		#print("Found: "+ahref)
		if(ahref[0].lower() == "/"):
			ahref = addr+ahref
		elif(ahref[0].lower() == "?"):
			ahref = addr+"/"+ahref
		if (ahref not in listed):
			if (ahref[0].lower() == "h"):
				if (primalsource in ahref):
					if (ahref[-4:].lower() not in filetypes):
						listed.append(ahref)
						ForQueryInAddr(query, ahref)

def Start():
	global proxies, listed, sources, filetypes, primalsource
	filetypes = [".png",".jpg",".gif",".zip",".rar"]
	primalsource = input("Primal Source: ")
	query = input("Query: ")
	sources = []
	listed = []
	proxies = {
		'http': 'socks5h://127.0.0.1:9050',
		'https': 'socks5h://127.0.0.1:9050'
	}
	ForQueryInAddr(query, primalsource)

Start()
