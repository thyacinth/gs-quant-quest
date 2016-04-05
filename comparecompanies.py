import numpy as np
import pywikibot as pwb

site = pwb.Site()
page = pwb.Page(site, u"List of S&P 500 companies")
item = pwb.ItemPage.fromPage(page)
item.get()
print item.toJSON()
