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


import os
from data_retrieval import create_book
from pre_processing import pre_process_text, StemLem

def save_book(book, location):
	with open(location, 'w') as file:
		file.write(book)
	
def load_book(location):
	book = ' '
	with open(location, 'r') as file:
		book = book.join(file.readlines())
	return book

def main():
	book = ''
	book_file = './Book.txt'
	book_downloaded = os.path.isfile(book_file)
	
	if(not book_downloaded):
		print("Couldn't find book file, downloading it, please wait...")
		book = create_book()
		save_book(book, book_file)
		print('Book downloaded and saved as {}'.format(book_file))
	else:
		print("Book found, loading it...")
		book = load_book(book_file)
		print("Done")
	
	# You can use as second attribute: StemLem.PORTER, StemLem.LANCASTER, StemLem.LEMMATIZATION (Default)
	tokenized = pre_process_text(book)
	

if __name__ == "__main__":
    main()