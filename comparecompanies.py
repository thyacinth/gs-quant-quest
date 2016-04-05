import numpy as np
import wikipedia as wp

sp = wp.page("List of S&P 500 Companies")

component_stocks = sp.section("Recent and announced changes to the list of S&P 500 Components")
print component_stocks
