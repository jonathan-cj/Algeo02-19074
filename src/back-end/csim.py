# Stemming
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

#import numpy as np

# Word Count
import collections

# Cosine Similiarity
import math

# Reading doc
from bs4 import BeautifulSoup # html
from pdfminer.high_level import extract_text # pdf

# Reading first sentence
import re

# Getting list file
from glob import glob
from os.path import join
from os import listdir

def clear(x): # terima string
    if x != None:
        return x.lower().replace('–',' ').replace('-',' ').replace('(','').replace(')',' ').replace(',','').replace('.','').replace('!','').replace('?','').replace('"',' ')
    return None

def tokenit(x): # ubah string ke list
    ban = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 
    'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 
    'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 
    's', 't', 'can', "can't", 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 
    'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

    tokens = (clear(x).split())
    tokenswsw = [PorterStemmer().stem(i) for i in tokens if not i in ban]
    return tokenswsw

def wordcount(x): # terima list, ubah ke count
    count = collections.Counter(x)
    wcount = (list(count.items()))
    return wcount

def totalword(x): # terima string, return total word
    doc = wordcount(list(clear(x).split()))
    sum = 0
    for i in range(len(doc)):
        sum += doc[i][1]
    return sum

def opendoc(x): # terima directory
    if x.lower().endswith('.html'):
        return BeautifulSoup(open(x),"html.parser").get_text()
    elif x.lower().endswith('.pdf'):
        return extract_text(x)
    else :
        return open(x,"r",encoding='utf8').read()

def readtitle(x): # baca judul (asumsi di line pertama) dari dokumen
    A = opendoc(x).splitlines()
    i = 0
    while (A[i] == '') and (i < len(A)):
        i += 1
    if (A[i] != ''):
        return (A[i])
    return 'Error : title not found.'

def readfirstsen(x): # baca judul (asumsi di line pertama) dari dokumen
    A = opendoc(x).splitlines()
    i = 0
    tfound,found = False,False
    while (i < len(A)):
        if (tfound) and A[i].replace(' ','') != '':
            B = re.split("\.\s+",A[i])
            return (B[0])
        if (A[i] == readtitle(x)): # cari line yang ga kosong
            tfound = True
        i += 1
    return 'Error : body not found.'

def sim(Q,D): # return similiarity
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

def searchq(Q,dir,ext): # Q = Query(string), dir = directory(string)
    # {'title':'','totalword':0,'similiarity':0,'firstsentence':'','docdir':''}
    A = [] # array of file directory
    for types in ext:
        A.extend(glob(join(dir, types)))
    S = [] # array of search result
    for i in range(len(A)):
        S.append({"title":readtitle(A[i]),"totalword":totalword(opendoc(A[i])),"similiarity":sim(Q,opendoc(A[i])),"firstsentence":readfirstsen(A[i]),"filename":(A[i].partition('\\'))[2]})
    if len(S) != 0:
        return S
    else :
        return 0

def simtable(Q,D): # return similiarity
    A = wordcount(tokenit(Q))
    B = wordcount(tokenit(D))
    C = [0 for i in range(len(A))]
    for i in range(len(A)):
        for j in range (len(B)):
            if (B[j][0] == A[i][0]):
                C[i] += B[j][1]
    return C

def searchqt(Q,dir,ext):
    # Membuat base
    A = [] # array of namafile
    for types in ext:
        A.extend(glob(join(dir, types)))
    AT = A.copy()
    for i in range(len(A)):
        A[i] = A[i].partition('\\')[2]
    A = ["Keywords","Query"] + A
    # Membuat tabel
    B = wordcount(tokenit(Q))
    R = [[B[i][0],B[i][1]] for i in range(len(B))]
    for i in range(0,len(AT)):
        N = simtable(Q,opendoc(AT[i]))
        for j in range(0,len(N)):
            (R[j]).append(N[j])
    R = [A] + R
    return R
     
# print(searchq("RSA Prime",'../test/',('*.pdf', '*.txt', '*.html')))
# print(opendoc("../doc/H.pdf"))
# print(opendoc("../doc/b.html"))
# print(opendoc("../doc/a.txt"))

#print(sim("RSA rsa prime",opendoc("../doc/a.txt")))
#wordlist = [avquery[i][0] for i in range(len(avquery))]
#countword = [avquery[i][1] for i in range(len(avquery))]