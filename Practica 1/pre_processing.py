import contractions
from nltk import word_tokenize, sent_tokenize, bigrams
import nltk
import unicodedata
import re
import inflect
from nltk.corpus import stopwords
from enum import Enum

class StemLem(Enum):
	PORTER = 1
	LANCASTER = 2
	LEMMATIZATION = 3
	

def expand_contractions(text):
	text_uncont = contractions.fix(text)
	return text_uncont
	
def tokenization_sentences(text):
	tokens = []
	tokens = sent_tokenize(text)
	return tokens

def tokenization_words(text):
	tokens = []
	tokens = word_tokenize(text)
	return tokens

def create_bigrams(tokens):
	bigr = bigrams(tokens)
	return bigr
	
def remove_non_ascii(tokens):
	# For each token of tokens we will use unicodedata normalization
	new_tokens = [unicodedata.normalize('NFKD', token).encode('ascii', 'ignore').decode('utf-8', 'ignore') for token in tokens]
	return new_tokens

def to_lowercase(tokens):
	# For each token of tokens we will use the method lower()
	new_tokens = [token.lower() for token in tokens] 
	return new_tokens	

def remove_punctuation(tokens):
	# For each token, if it matches the regex '[^\w\s]' (it's not a word, space or number) substitute for nothing (remove)
	new_tokens = []
	for token in tokens:
		new_token = re.sub(r'[^\w\s]', '', token)
		if(new_token != ''):
			new_tokens.append(new_token)
	
	return new_tokens
	
def replace_numbers(tokens):
	inf = inflect.engine()
	new_tokens = []
	
	for token in tokens:
		if(token.isdigit()):
			new_token = inf.number_to_words(token)
			new_tokens.append(new_token)
		else:
			new_tokens.append(token)
			
	return new_tokens
	
def remove_eng_stopwords(tokens):
	new_tokens = []
	for token in tokens:
		if token not in stopwords.words('english'):
			new_tokens.append(token)
			
	return new_tokens
	
def stem_porter(tokens):
	porter = nltk.PorterStemmer()
	return [porter.stem(t) for t in tokens]
	
def stem_lancaster(tokens):
	lancaster = nltk.LancasterStemmer()
	return [lancaster.stem(t) for t in tokens]
	
def lemmatization(tokens):
	wnl = nltk.WordNetLemmatizer()
	return [wnl.lemmatize(t) for t in tokens]
	
def normalize(tokens):
	tokens = remove_non_ascii(tokens)
	tokens = to_lowercase(tokens)
	tokens = remove_punctuation(tokens)
	tokens = replace_numbers(tokens)
	tokens = remove_eng_stopwords(tokens)
	return tokens
	
def pre_process_text(text, stem_lem = StemLem.LEMMATIZATION):
	# We are going to expand the contractions, as part of the pre-processing.
	text_expanded = expand_contractions(text)
	tokenized_text = tokenization_words(text_expanded)
	normalized_tokens = normalize(tokenized_text)
	
	if(stem_lem == StemLem.PORTER):
		normalized_tokens = stem_porter(normalized_tokens)
	elif(stem_lem == StemLem.LANCASTER):
		normalized_tokens = stem_lancaster(normalized_tokens)
	elif(stem_lem == StemLem.LEMMATIZATION):
		normalized_tokens = lemmatization(normalized_tokens)
		
	return normalized_tokens