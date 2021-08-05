from rake_nltk import Rake
import pandas as pd 
from gensim.summarization import keywords

r = Rake() # Uses stopwords for english from NLTK, and all puntuation characters.

doc = 'The Dow Jones Industrial Average slid from record highs at the end of January, as the current stock market rally continues. The best Dow Jones stocks to buy and watch in February 2021 are Apple, Microsoft and Nike. Boeing recommends airlines suspend use of some 777s after United incident Over 43 mln doses of Sinopharm\'s COVID-19 vaccines used globally-state media U.S. Deaths Near 500,000; Philippines Clears Shot: Virus Update Brent Oil Climbs Back Above $63 With Goldman Seeing More Gains Indonesia issues "priority" investment list under new regulation'

r.extract_keywords_from_text(doc)

rak_ranked = r.get_ranked_phrases() # To get keyword phrases ranked highest to lowest.
print('----------------------------')
#print(rak_ranked)
#print('----------------------------')
rak_key = r.get_ranked_phrases_with_scores()
#print(rak_key)
rak= []
for t in rak_key:
	rak.append(t)


print (rak)
print('---------------')
print(rak[0])
col=['rank','text']
#rak.col=col
print(rak)



df = pd.DataFrame(rak , columns=col)
g = df[:6]
print(g)

print('---------------------')
print(doc)
print(keywords(doc,words = 10,scores = True, lemmatize = True))


import spacy


nlp = spacy.load("en_core_web_sm")
doc = nlp("The Dow Jones Industrial Average slid from record highs at the end of January, as the current stock market rally continues. The best Dow Jones stocks to buy and watch in February 2021 are Apple, Microsoft and Nike. Boeing recommends airlines suspend use of some 777s after United incident Over 43 mln doses of Sinopharm\'s COVID-19 vaccines used globally-state media U.S. Deaths Near 500,000; Philippines Clears Shot: Virus Update Brent Oil Climbs Back Above $63 With Goldman Seeing More Gains Indonesia issues priority investment list under new regulation")

for ent in doc.ents:
    print(ent.text,ent.label_)

from spacy import displacy
nlp = spacy.load("en_core_web_sm")
doc1 = nlp("This is a sentence.")
doc2 = nlp("This is another sentence.")
displacy.serve([doc1, doc2], style="dep")




