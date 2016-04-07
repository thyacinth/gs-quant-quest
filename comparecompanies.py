import sys
import numpy as np
import parser 
def main(argv):
	print "Hello World"
	links = parser.get_snp_500('https://en.wikipedia.org/wiki/List_of_S&P_500_companies')
	assert len(links) == 500

if __name__ == "__main__":
	main(sys.argv[1:])