import lda
import urllib2
from bs4 import BeautifulSoup as bs

listlist = ['https://en.wikipedia.org/wiki/Category:Companies_listed_on_the_New_York_Stock_Exchange','https://en.wikipedia.org/w/index.php?title=Category:Companies_listed_on_the_New_York_Stock_Exchange&pagefrom=Boeing#mw-pages','https://en.wikipedia.org/w/index.php?title=Category:Companies_listed_on_the_New_York_Stock_Exchange&pagefrom=Cosan#mw-pages','https://en.wikipedia.org/w/index.php?title=Category:Companies_listed_on_the_New_York_Stock_Exchange&pagefrom=Freeport-Mcmoran%0AFreeport-McMoRan#mw-pages','https://en.wikipedia.org/w/index.php?title=Category:Companies_listed_on_the_New_York_Stock_Exchange&pagefrom=Johnson+and+Johnson%0AJohnson+%26+Johnson#mw-pages','https://en.wikipedia.org/w/index.php?title=Category:Companies_listed_on_the_New_York_Stock_Exchange&pagefrom=NewAlliance+Bank#mw-pages','https://en.wikipedia.org/w/index.php?title=Category:Companies_listed_on_the_New_York_Stock_Exchange&pagefrom=Restaurant+Brands+International#mw-pages','https://en.wikipedia.org/w/index.php?title=Category:Companies_listed_on_the_New_York_Stock_Exchange&pagefrom=Tilly%27s#mw-pages','https://en.wikipedia.org/w/index.php?title=Category:Companies_listed_on_the_New_York_Stock_Exchange&pagefrom=Zoetis#mw-pages']
hreflist = []

def gethref(listofpages):
	html = urllib2.urlopen(listofpages)
	soup = bs(html, "html.parser")
	content = soup.body.find(id="content")
	bodycontenttext = content.find(id="bodyContent").find(id="mw-content-text")
	mw_pages = bodycontenttext.find(class_="mw-category-generated").find(id="mw-pages")
	links = mw_pages.find_all('li')

	for n in links[1::]:
		link = n.find('a')
		href = 'http://en.wikipedia.org/'+link.get('href')
		hreflist.append(href)
	return hreflist
for item in listlist:
	gethref(item)		
print hreflist
	#for link in links:
		#href = links.find('a')
		#linklist.append(href)
	#return linklist
#vocab = lda.datasets.load_reuters_vocab()
#	titles = lda.datasets.load_reuters_titles()
#	X.shape
#(395, 4258)
#>>> X.sum()
#84010
#>>> model = lda.LDA(n_topics=20, n_iter=1500, random_state=1)
#>>> model.fit(X)  # model.fit_transform(X) is also available
#>>> topic_word = model.topic_word_  # model.components_ also works
#>>> n_top_words = 8
#>>> for i, topic_dist in enumerate(topic_word):
#...     topic_words = np.array(vocab)[np.argsort(topic_dist)][:-n_top_words:-1]
#...     print('Topic {}: {}'.format(i, ' '.join(topic_words)))

##shit to do:
#go on all the hrefs
#- make soup out of all the <p> stuff before a certain thing
#task for tonight: grab hrefs
#for listofpages in listlist:
	#print gethref(listofpages)
 
