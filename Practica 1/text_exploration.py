import nltk
from nltk import word_tokenize
from pre_processing import pre_process_text, StemLem
from nltk import FreqDist
from enum import Enum

class Text(Enum):
	NONE = 0
	PORTERED = 1
	LANCASTERED = 2
	LEMMATIZED = 3

class Text_Explorer():
	
	__nltk_text = []
	__freq_dist = []

	def __read_book_from_source(self, source):
		f = open(source, 'r')
		text = ''
		for line in f:
			if(line != '\n'):
				text += line
		
		return text
	
	def __frequency_distribution(self, text):
		freq_dist = FreqDist(text)
		return freq_dist
	
	def __init__(self, source):
		
		raw = self.__read_book_from_source(source)
		
		# You can use as second attribute: StemLem.PORTER, StemLem.LANCASTER, StemLem.LEMMATIZATION (Default) or None
		tokens_none = pre_process_text(raw, None)
		tokens_porter = pre_process_text(raw, StemLem.PORTER)
		tokens_lancaster = pre_process_text(raw, StemLem.LANCASTER)
		tokens_lemmatization = pre_process_text(raw, StemLem.LEMMATIZATION)
		
		nltk_text_none = nltk.Text(tokens_none)
		freq_dist_none = self.__frequency_distribution(nltk_text_none)
		nltk_text_porter = nltk.Text(tokens_porter)
		freq_dist_porter = self.__frequency_distribution(nltk_text_porter)
		nltk_text_lancaster = nltk.Text(tokens_lancaster)
		freq_dist_lancaster = self.__frequency_distribution(nltk_text_lancaster)
		nltk_text_lemmatization = nltk.Text(tokens_lemmatization)
		freq_dist_lemmatization = self.__frequency_distribution(nltk_text_lemmatization)
		
		self.__nltk_text = [nltk_text_none, nltk_text_porter, nltk_text_lancaster, nltk_text_lemmatization]
		self.__freq_dist = [freq_dist_none, freq_dist_porter, freq_dist_lancaster, freq_dist_lemmatization]
		
	def concordance(self, word, text=Text.LEMMATIZED):
		ret = self.__nltk_text[text.value].concordance(word)
		return ret
		
	def similar(self, word, text=Text.LEMMATIZED):
		ret = self.__nltk_text[text.value].similar(word)
		return ret
		
	def most_frequent_words(self, limit=500, text=Text.LEMMATIZED):
		ret = [i for i in self.__freq_dist[text.value].most_common(limit)]
		return ret
	
	def words_values(self, text=Text.LEMMATIZED):
		ret = [self.__freq_dist[text.value].values()]
		return ret
		
	def number_of_words(self, text=Text.LEMMATIZED):
		ret = self.__freq_dist[text.value].N()
		return ret
		
	def quantity_of_word(self, word, text=Text.LEMMATIZED):
		ret = self.__freq_dist[text.value][word]
		return ret
		
	def frequency_of_word(self, word, text=Text.LEMMATIZED):
		ret = self.__freq_dist[text.value].freq(word)
		return ret
	
	def max_frequency_word(self, text=Text.LEMMATIZED):
		ret = self.__freq_dist[text.value].max()
		return ret
		
	def plot_frequency_distribution(self, text=Text.LEMMATIZED):
		ret = self.__freq_dist[text.value].plot()
		return ret
		
	def dispersion_plot_words(self, words, text=Text.LEMMATIZED):
		ret = self.__nltk_text[text.value].dispersion_plot(words)
		return ret
		
	def plot_frequency_distribution_number(self, number, text=Text.LEMMATIZED):
		ret = self.__freq_dist[text.value].plot(number)
		return ret