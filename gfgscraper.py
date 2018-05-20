# Script to find the profile link of your friend on GeeksForGeeks
# Requires packages: bs4, lxml, requests

import requests
import sys
from bs4 import BeautifulSoup


def main():
	# Change the range if you have an idea of the score 
    urls = ["https://practice.geeksforgeeks.org/ranking/%d" %(i) for i in range(0,1000)]
    the_word = input("Enter the keyword or the substring of the username to search:")

    try:
	    for i in range(len(urls)):
	        r = requests.get(urls[i], allow_redirects=False)
	        soup = BeautifulSoup(r.content, 'lxml')
	        words = soup.find_all('a', text=lambda t: t and the_word in t)
	        print("Searched {} of {}" .format(i,len(urls)))
	        if(words):
	        	for a in words:
	        		print("FOUND ", a['href'])
	        words = []
    except KeyboardInterrupt:
    	pass


if __name__ == '__main__':
    main()