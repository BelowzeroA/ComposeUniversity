from gensim.summarization import keywords
from gensim.summarization import summarize


with open('text.txt', 'r', encoding='utf-8') as text_file:
    text = text_file.read()

#print('Keywords:')
#print(keywords(text))
print(summarize(text))