import nltk
from nltk.tokenize import RegexpTokenizer
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
import speech_recognition as sr

text = open('examples.txt', 'r').read()
tokenizer = RegexpTokenizer(r'\w+')

def preprocess(text):
    sentences = tokenizer.tokenize(text)
    sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    sentences = [nltk.pos_tag(sentence) for sentence in sentences]
    return sentences



preprocessed_text = preprocess(text)


a = 4