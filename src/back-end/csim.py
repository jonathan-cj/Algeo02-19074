# Stemming
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Word Count
import collections

# Cosine Similiarity
import math

# Reading doc
from bs4 import BeautifulSoup # read html
from pdfminer.high_level import extract_text # read pdf

# Reading first sentence
import re

# Getting list file
from glob import glob
from os.path import join
from os import listdir
from os import path

def clear(x): # Clear strings from symbols
    # x         : string (filled with symbols)
    # output    : srings (no symbols)
    if x != None:
        return x.lower().replace('–',' ').replace('-',' ').replace('(','').replace(')',' ').replace(',','').replace('.','').replace('!','').replace('?','').replace('"',' ')
    return None

def tokenit(x): # Tokenizing document
    # x         : string
    # output    : array of strings
    ban = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 
    'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 
    'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 
    's', 't', 'can', "can't", 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 
    'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

    tokens = (clear(x).split())
    tokenswsw = [PorterStemmer().stem(i) for i in tokens if not i in ban]
    return tokenswsw

def wordcount(x): # Count occurence of words
    # x         : array of strings
    # output    : array of tuple (A,B), A is word, B is occurence of the word
    count = collections.Counter(x)
    wcount = (list(count.items()))
    return wcount

def totalword(x): # Sum of all words
    # x         : array of dict
    # output    : integer
    doc = wordcount(list(clear(x).split()))
    sum = 0
    for i in range(len(doc)):
        sum += doc[i][1]
    return sum

def isfilenotempty(dir,x): # Check file is not empty
    # dir       : strings (folder directory)
    # x         : strings (file name)
    # output    : boolean (true if file is not empty, otherwise false)
    return (path.getsize(join(dir,x)) > 0) and (path.isfile(join(dir,x)))

def opendoc(x): # Open a document and convert it into strings
    # x         : strings (file directory)
    # output    : strings
    if x.lower().endswith('.html'):
        return BeautifulSoup(open(x),"html.parser").get_text()
    elif x.lower().endswith('.pdf'):
        return extract_text(x)
    else :
        return open(x,"r",encoding='utf8').read()

def readtitle(x): # Read document title
    # x         : strings (file directory)
    # output    : strings
    A = opendoc(x).splitlines()
    i = 0
    if (len(A) > 0) : # Searching title
        while (i < len(A)) and (A[i].replace(' ','') == ''):
            i += 1
        if (i < len(A)) and (A[i] != ''):
            return (A[i]) # Title is found and return the title in strings
    return 'Error : title not found.' # Title not found and return an error

def readfirstsen(x): # Read first sentence in document's paragraph
    # x         : strings (file directory)
    # output    : strings
    if (readtitle(x) != 'Error : title not found.'):
        A = opendoc(x).splitlines()
        i = 0
        tfound,found = False,False
        while (i < len(A)): # Seaching first sentence in document.
            if (tfound) and A[i].replace(' ','') != '': # Read past title (and title already located)
                B = re.split("\.\s+",A[i])
                return (B[0])
            if (A[i] == readtitle(x)): # Found title
                tfound = True
            i += 1
    return 'Error : body not found.' # First sentence is not found, returning error string

def sim(Q,D): # Cosine similiarity
    # Q         : strings (query)
    # D         : strings (document in strings)
    # output    : float (0-100)
    A = wordcount(tokenit(Q))
    B = wordcount(tokenit(D))
    dot,lQ,lD = 0,0,0
    for i in range(len(A)):
        lQ += pow(A[i][1],2)
        for j in range (len(B)):
            if (B[j][0] == A[i][0]):
                lD += pow(B[j][1],2)
                dot += A[i][1] * B[j][1]
    if lQ*lD != 0:
        return (dot/(math.sqrt(lQ*lD))*100)
    else:
        return 0

def searchq(Q,dir,ext): # Search similiarity for all existing documents in directory
    # Q         : strings (query)
    # dir       : strings (documents file directory)
    # ext       : tuple of strings (file extension allowed)
    # output    : array of dict (below is the format of the dict)
    #             {'title':'','totalword':0,'similiarity':0,'firstsentence':'','filename':''}
    A = [] # Array of file directory
    for types in ext:
        A.extend(glob(join(dir, types)))
    S = [] # Array of search result
    for i in range(len(A)):
        S.append({"title":readtitle(A[i]),"totalword":totalword(opendoc(A[i])),"similiarity":sim(Q,opendoc(A[i])),"firstsentence":readfirstsen(A[i]),"filename":(A[i].partition('\\'))[2]})
    if len(S) != 0:
        return S
    else :
        return 0 # No result found (either no document or no file with required exstension)

def simtable(Q,D): # Creating vector for document from query
    # Q         : strings (query)
    # D         : strings (document in strings)
    # output    : array of int (vector)
    A = wordcount(tokenit(Q))
    B = wordcount(tokenit(D))
    C = [0 for i in range(len(A))]
    for i in range(len(A)):
        for j in range (len(B)):
            if (B[j][0] == A[i][0]):
                C[i] += B[j][1]
    return C

def searchqt(Q,dir,ext): # Creating vector table to be compared with query for all documents with correct extension
    # Q         : strings (query)
    # dir       : strings (document file directory)
    # ext       : tuple of strings (file extension allowed)
    # output    : array of array of string and int
    # Table Initialization
    A = [] # Array of file directory
    for types in ext:
        A.extend(glob(join(dir, types)))
    AT = A.copy()
    for i in range(len(A)):
        A[i] = A[i].partition('\\')[2]
    A = ["Keywords","Query"] + A
    # Array (Table) processing
    B = wordcount(tokenit(Q))
    R = [[B[i][0],B[i][1]] for i in range(len(B))]
    for i in range(0,len(AT)):
        N = simtable(Q,opendoc(AT[i]))
        for j in range(0,len(N)):
            (R[j]).append(N[j])
    R = [A] + R
    return R
