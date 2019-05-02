from bs4 import BeautifulSoup
import requests

def open_soup(link):
	# This is going to get the link and put it in a soup file
	page_response = requests.get(link, timeout=20)
	soup = BeautifulSoup(page_response.content, "html.parser")
	return soup

def create_book():
	# This will get the set of soup objects and put them all in a variable, with the whole story of the book
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
	book = ''
	for soup in soups:
		text = soup.find('p').get_text()
		book += text + '\n'
		
	return book