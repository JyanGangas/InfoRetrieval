from nltk.book import *
from collections import Counter

def Monty(text6):
    voc = len(set(text6))   #Δείκτης πλούτου λεξιλογίου
    Lanc = Counter(text6)   #Αριθμός φορών εμφάνισης της λέξης LAUNCELOT
    PrintLanc = print(f'"LAUNCELOT" appears {Lanc["LAUNCELOT"]} times') 
    PercLanc = 100 * text6.count('LAUNCELOT') / len(text6)  #Ποσοστό εμφάνισης της λέξης
    return[voc, PrintLanc, PercLanc]