from nltk.book import *
from collections import Counter

def Chat(text6):
    voc = len(set(text6))   #Δείκτης πλούτου λεξιλογίου
    Lanc = Counter(text6)   #Αριθμός φορών εμφάνισης της λέξης LAUNCELOT
    PrintLanc = print(f'"omg" appears {Lanc["omg"]} times') 
    PrintLanc = print(f'"OMG" appears {Lanc["OMG"]} times')
    PrintLanc = print(f'"lol" appears {Lanc["lol"]} times')
    PercLanc = 100 * text6.count('omg') / len(text6)  #Ποσοστό εμφάνισης της λέξης omg
    PercOMG = 100 * text6.count('OMG') / len(text6) #Ποσοστό εμφάνισης της λέξης OMG
    Perclol = 100 * text6.count('lol') / len(text6) #Ποσοστό εμφάνισης της λέξης lol
    return[voc, PrintLanc, PercLanc, PercOMG, Perclol]