from bs4 import BeautifulSoup as bs
from bs4 import SoupStrainer 
import re
import urllib2

def get_snp_500(webpage):
	d = {}
	html = urllib2.urlopen(webpage)
	soup = bs(html, "html.parser")
	content = soup.body.find(id="content")
	bodycontent = content.find(id="bodyContent")
	table = bodycontent.find(id="mw-content-text").table
	rows = table.find_all('tr')
	for row in rows[1:]:
		cells = row.find_all('td')
		stock = cells[1].find('a')
		CID = cells[-1].text
		d[CID] = 'http://en.wikipedia.org/'+stock.get('href') # not putting security name b/c i  will derive that from the redirected url
	return d
