import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def main():

    sentence1="THIS IS A TEST SENTENCE. This is the second test sentence that is cool"
    sentence2="THIS IS A TEST SENTENCE. This is the second test sentence that is cool"
    print similarity(sentence1,sentence2)

#A measure of symmetric similarity between two bodies of text
def similarity(text1,text2):
    context1 = shallowProcessN1(text1)
    context2 = shallowProcessN1(text2)
    count = 0.0
    for word in context1:
        if word in context2:
            count = count + 1
    return count/(len(context1)+len(context2))    

#Extracting contextual words from a sentence
def shallowProcessN1(text):
    contextWords = []
    
    #lower case
    text = text.lower()

    #split into individual words
    words = word_tokenize(text)

    filtered_sentences = removeStopWords(words)

    tagged_words = nltk.pos_tag(filtered_sentences)

    context = extractContext(tagged_words)

    return context

#Only extracting nouns
def extractContext(tagged_words):
    context = []
    for (word,tag) in tagged_words:
        if tag == 'NN' or tag == 'NNS':
            context.append(word)
    return context

def removeStopWords(words):
    #stop words
    stop_words = set(stopwords.words("english"))
    filtered_sentence = []

    #remove stop words
    for word in words:
        if word not in stop_words:
            filtered_sentence.append(word)

    return filtered_sentence


            
if __name__ == "__main__":
     main()
        
