# TODO Xin - Add methods here that we will need. Try to think carefully about organization and how to separate functionality effectively.
from bs4 import BeautifulSoup as bs
from bs4 import SoupStrainer as ss
import re
import urllib2 as ul

def links(webpage):
	links = []
	biglist = ul.urlopen(webpage)
	soup = bs(biglist, "html.parser")
	tablebody = soup.body.find(id="content")
	bodycontent = tablebody.find(id="bodyContent")
	table = bodycontent.find(id="mw-content-text").table
	for n in range(1, 505):
		row = table.find_all('tr')[n]
		name = row.find_all('td')[1]#this is to get the security td's 
		for element in name:
			links.append('http://en.wikipedia.org/'+element.get('href'))
	print links
links('https://en.wikipedia.org/wiki/List_of_S&P_500_companies')

def contents(webpage):
	biglist = ul.urlopen(webpage)
	soup = bs(biglist, "html.parser")
	tablebody = soup.body.find(id="content")
	bodycontent = tablebody.find(id="bodyContent")
	table = bodycontent.find(id="mw-content-text").table
	content = []
	for n in range(1, 505):
		row = table.find_all('tr')[n]
		name = row.find_all('td')[1]
		for link in name:
			content.append(link.text)
	print content 
contents('https://en.wikipedia.org/wiki/List_of_S&P_500_companies')

#what's left: I need to 
#- perhaps remove unicode
#- convert this to a function
#- grab the links