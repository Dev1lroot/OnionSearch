import sys
import json
import requests
from pyquery import PyQuery

def ForQueryInAddr(query, addr):
	global listed, primalsource
	print("Searcing in: "+addr)
	html = requests.get(addr,proxies=proxies).text
	if (query.lower() in html.lower()):
		print("==============================================")
		print("Query found in: "+addr)
		print("==============================================")
	if ("<html>" in html or "<head>" in html):
		data = PyQuery(html)
		links = data('a')
		for link in links:
			ahref = link.attrib['href']
			#print("Found: "+ahref)
			if (ahref not in listed):
				if (ahref[0].lower() == "h"):
					if (primalsource in ahref):
						if (ahref[-3:].lower() not in filetypes and ahref[-4:].lower() not in filetypes and ahref[-5:].lower() not in filetypes):
							listed.append(ahref)
							ForQueryInAddr(query, ahref)

def Start():
	global proxies, listed, sources, filetypes, primalsource
	filetypes = [".xz",".gz",".7z",".png",".jpg",".gif",".zip",".rar",".mp4",".m4v",".mkv",".mov",".3gp",".avi",".mpeg",".jpeg",".pdf"]
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
