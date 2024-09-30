from nltk.book import *
import string
import nltk
nltk.download('stopwords')

def Punctuations():
    cleaned_tokens = []
    sentence = text2[:200]
    #sentence = "General Kenobi! Nice meeting you again."
    #sentence = "Ήταν ένας γάιδαρος με μεγάλα αυτιά, το μαντρί δεν του άρεσε ήθελε αρχοντιά!"
    #sent = list(sentence.split())   #μετατροπή string σε list
    stopwords = nltk.corpus.stopwords.words('english') #καταχώριση stopwords αγγλικών
    #stopwords = nltk.corpus.stopwords.words('greek')    #καταχώριση stopwords ελληνικών
    for token in sentence:  #για το έτοιμο text
    #for token in sent:   #για προτάσεις
        #εκκαθάριση από σημεία στηξης και προθήματα
       if token not in string.punctuation:
           if token not in stopwords:
               cleaned_tokens.append(token)
    return[cleaned_tokens]