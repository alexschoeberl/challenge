from collections import Counter
import string


def parse_abstract(abstract, char_min=0, char_max=None):
	char_min = max(char_min, 0)
	char_max = char_max or 1000

	translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))
	abstract = abstract.translate(translator)
	words = abstract.strip().split()
	return {word for word in words if test(word, char_min, char_max)}


def analyse_abstract(abstract, char_min=0, char_max=None):
	char_min = max(char_min, 0)
	char_max = char_max or 1000

	translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))
	abstract = abstract.translate(translator)
	words = [word for word in abstract.strip().split() if test(word, char_min, char_max)]
	ordered = Counter(words).most_common()
	return ordered[:10], ordered[-10:]


def test(word, char_min, char_max):
	return word.isalpha() and (char_min <= len(word) <= char_max)
