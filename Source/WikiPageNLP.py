import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class WikiNLP():

    #Removing HTML tags
    def cleanhtml(self,raw_html):
        cleanr = re.compile('<[^>]*>')
        cleanr2 = re.compile('&.*?;')
        cleantext = re.sub(cleanr, ' ', raw_html)
        intText = re.sub( '\s+', ' ', cleantext ).strip()
        return re.sub(cleanr2, '', intText)

    #A measure of symmetric similarity between two bodies of text
    def symsimilarity(self,text1,text2):
        context1 = self.shallowProcessN1(text1)
        context2 = self.shallowProcessN1(text2)
        count = 0.0
        for word in context1:
            if word in context2:
                count = count + 1

        denom = len(context1)+len(context2)
        if denom != 0:
            return count/denom
        else:
            return 0

    #Extracting contextual words from a sentence
    def shallowProcessN1(self,text):
        text = self.cleanhtml(text)
        #lower case
        text = text.lower()
        #split into individual words
        words = word_tokenize(text)
        filtered_sentences = self.removeStopWords(words)
        tagged_words = nltk.pos_tag(filtered_sentences)
        context = self.extractContext(tagged_words)
        return set(context)

    #Only extracting nouns and verbs,except 'analysis' and 'reflection'
    def extractContext(self,tagged_words):
        context = []
        for (word,tag) in tagged_words:
            if tag == 'NN' or tag == 'NNS' or tag == 'VB' or tag == 'VBD' or tag == 'VBG' or tag == 'VBN' or tag == 'VBP' or tag == 'VBZ' and word != 'analysis' and word != 'reflection':
                context.append(word)
        return context

    #To remove English stop words
    def removeStopWords(self,words):
        #stop words
        stop_words = set(stopwords.words("english"))
        filtered_sentence = []
        
        #remove stop words
        for word in words:
            if word not in stop_words:
                filtered_sentence.append(word)

        return filtered_sentence


