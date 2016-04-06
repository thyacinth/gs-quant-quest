import sys
import numpy as np
import parser as pa
def main(argv):
	print "Hello World"
	# TODO Xin: Call parsing methods here. Get us to the point where we have a data structure that contains all the companies and all the links.
pa.links('https://en.wikipedia.org/wiki/List_of_S&P_500_companies')
pa.contents('https://en.wikipedia.org/wiki.List_of_S&P_500_companies')
if __name__ == "__main__":
   main(sys.argv[1:])
 #so in here I hardcoded the number of stocks, which is actually 505 (wow, whoa. wauw. not 500.) i'll probably have to figure out how to determine the number of rows in the table and use that in line 29 of my thing.