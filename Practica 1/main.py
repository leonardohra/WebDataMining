# -*- coding: utf-8 -*-

"""

Practice exercise for the Web Data Mining Class, UNICEN-Tandil, 2019.
The program will: 
- Download the 27 chapters of the book "The Little Prince" (http://www.angelfire.com/hi/littleprince/frames.html)
- Find the stopwords for this text
- Eliminate noise data, tokenize and normalize the text
- Plot the graph for the dispersion of certain words
{License_info}

"""

__author__ = 'Leonardo'
__copyright__ = 'Copyright 2019, Mining the Little Prince'
__credits__ = ['Leonardo Henrique da Rocha Araujo']
__license__ = 'GNU GLPv3'
__version__ = '0.2.0'
__maintainer__ = 'Leonardo'
__email__ = 'leonardo.araujo@isistan.unicen.edu.ar'
__status__ = 'Dev'


from bs4 import BeautifulSoup
import requests
import os

def save_book(book, location):
	with open(location, 'w') as file:
		file.write(book)
	
def load_book(location):
	book = ''
	with open(location, 'r') as file:
		book = file.readlines()
	return book
	
def clean_text(text):
	# This is going to remove tabs, new lines and etc
	new_text = text.replace('\\n', ' ')
	new_text = new_text.replace('\\r', ' ')
	new_text = new_text.replace('\\t', ' ')
	return new_text

def open_soup(link):
	# This is going to get the link and put it in a soup file
	page_response = requests.get(link, timeout=5)
	soup = BeautifulSoup(page_response.content, "html.parser")
	return soup

def create_book(soups):
	# This will get the set of soup objects and put them all in a variable, with the whole story of the book
	book = ''
	for soup in soups:
		text = soup.find('p').get_text()
		text = clean_text(text)
		book += text + '\n'
		
	return book
	
def main():
	book = ''
	book_file = './Book.txt'
	book_downloaded = os.path.isfile(book_file)
	
	if(not book_downloaded):
		print("Couldn't find book file, downloading it, please wait...")
		links = [
			'http://www.angelfire.com/hi/littleprince/framechapter1.html',
			'http://www.angelfire.com/hi/littleprince/framechapter2.html',
			'http://www.angelfire.com/hi/littleprince/framechapter3.html',
			'http://www.angelfire.com/hi/littleprince/framechapter4.html',
			'http://www.angelfire.com/hi/littleprince/framechapter5.html',
			'http://www.angelfire.com/hi/littleprince/framechapter6.html',
			'http://www.angelfire.com/hi/littleprince/framechapter7.html',
			'http://www.angelfire.com/hi/littleprince/framechapter8.html',
			'http://www.angelfire.com/hi/littleprince/framechapter9.html',
			'http://www.angelfire.com/hi/littleprince/framechapter10.html',
			'http://www.angelfire.com/hi/littleprince/framechapter11.html',
			'http://www.angelfire.com/hi/littleprince/framechapter12.html',
			'http://www.angelfire.com/hi/littleprince/framechapter13.html',
			'http://www.angelfire.com/hi/littleprince/framechapter14.html',
			'http://www.angelfire.com/hi/littleprince/framechapter15.html',
			'http://www.angelfire.com/hi/littleprince/framechapter16.html',
			'http://www.angelfire.com/hi/littleprince/framechapter17.html',
			'http://www.angelfire.com/hi/littleprince/framechapter18.html',
			'http://www.angelfire.com/hi/littleprince/framechapter19.html',
			'http://www.angelfire.com/hi/littleprince/framechapter20.html',
			'http://www.angelfire.com/hi/littleprince/framechapter21.html',
			'http://www.angelfire.com/hi/littleprince/framechapter22.html',
			'http://www.angelfire.com/hi/littleprince/framechapter23.html',
			'http://www.angelfire.com/hi/littleprince/framechapter24.html',
			'http://www.angelfire.com/hi/littleprince/framechapter25.html',
			'http://www.angelfire.com/hi/littleprince/framechapter26.html',
			'http://www.angelfire.com/hi/littleprince/framechapter27.html'
		]
		soups = [open_soup(link) for link in links]
		book = create_book(soups)
		save_book(book, book_file)
		print('Book downloaded and saved as {}'.format(book_file))
	else:
		print("Book found, loading it...")
		book = load_book(book_file)
		print("Done")

if __name__ == "__main__":
    main()