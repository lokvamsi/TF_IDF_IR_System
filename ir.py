from __future__ import division
import time
from math import log
from nltk.corpus import stopwords
import re
import os
from nltk.corpus.reader.plaintext import PlaintextCorpusReader

#Inputing corpus name.
newcorpus = 'movie_reviews'

#Get list of stop words.
stopwords = set(stopwords.words('english'))

#Extracting only text from the files in corpus, returns the string.
def textExtract(corpus,name):
    string=''
    from nltk.corpus import movie_reviews
    string = movie_reviews.raw(fileids=name)
    return string

#Splits a string into seperate words not including stop words,returns list.
def stringTokenize(string):
    wordslist = re.split(r'\W+',string)
    return [w.lower() for w in wordslist if w.isalpha() and len(w)>1 and w.lower() not in stopwords]    

#Full tokenize function.
def tokenize(corpus, name):
    string = textExtract(corpus,name)
    return stringTokenize(string)

#Creating list of file ids from the corpus, returns the list.
def fileExtract(corpus):
    listextracted=[]
    from nltk.corpus import movie_reviews
    listextracted = movie_reviews.fileids()
    return listextracted

#Start timer to calculate time to create Inverted Index.
starttimer = time.time()   

#Getting list of fileids of the corpus.
fileids =  fileExtract(newcorpus) 

#Finding total number of documents in corpus.
documentcount = len(fileids)    

#Keeping track of documents and words each contains(term frequency).
tfdictionary={}

#Dictionary based on query.
resultdictionary={}

#Index is the file id and name is the file name.
for (index,name) in enumerate(fileids): 

    wordslist = tokenize(newcorpus,name)
    
    for w in wordslist:
    	#If entry is not present, creating new entry and set to one.
        if tfdictionary.get(w,0)==0:
            tfdictionary[w]={}
            tfdictionary[w][index]=1
        #If entry is present, increment index for that word.
        else:
            tfdictionary[w][index]=tfdictionary[w].get(index,0)
            tfdictionary[w][index]+=1

#End of index creation, print time.
print ("Time taken to create Inverted Index:")
print (time.time() - starttimer, "seconds")
print("\n")

#Input query string.
query = input("Enter your query string: ")
print("\n")

#Start timer for searching through corpus.
starttimer = time.time()

#Tokenizing query string.
querylist = stringTokenize(query)


#Through each query word, calculating tf-idf score and storing in resultdictionary.
for q in querylist:
    
    #Fetching files in which word 'q' is present.
    d = tfdictionary.get(q,0) 
    
    if d!=0:

    	#Number of documents containing word 'q'.
        length=len(d)

        #In all documents containing word 'q', score based on tf-idf, store in resultdictionary.
        for index in d.keys():
            resultdictionary[index] = resultdictionary.get(index,0)
            resultdictionary[index]+=((1+log(d[index]))*(log(documentcount/length)/log(10)))
    
#Sorting and creating list for final scores.
sortedfileids = sorted(resultdictionary.items(), key=lambda x:x[1],reverse = True)

#Printing search time.
print ("Time taken to search: ")
print ((time.time() - starttimer), "seconds.")
print("\n")

#Printing results.
if(len(sortedfileids)!=0):
    print ("Number of results: " , len(sortedfileids))
    print("\n")
    if len(sortedfileids) > 10:
        print ("Top ten results:")
        print("\n")
    count=1
    for (index,item) in enumerate(sortedfileids):
        
        #Printing first 10 results.
        if index==10:
            break

        #item[0] is fileid, item[1] is final score.
        
        print("Document ",count)
        print("File Path: ",fileids[item[0]])
        print("Score:",item[1])

        #Printing first 40 characters of each result document.
        print("Text: ")
        print (textExtract(newcorpus,fileids[item[0]])[:40])
        print ("\n")
        count=count+1
    
else:
    print ("No match found.")
