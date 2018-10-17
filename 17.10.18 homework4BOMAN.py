from string import punctuation
from operator import itemgetter
import re

def tokenize(s):
    words = s.lower().strip().split()
    twords = [word.strip(punctuation) for word in words]
    return twords

def gutenberg_file_wc(filename):
    alice = open('alice.txt').read()
    a = alice.find("*** START OF THIS PROJECT GUTENBERG EBOOK")
    z = alice.find("*** END OF THIS PROJECT GUTENBERG EBOOK")
    alice_new = alice[a:z]
    alice_tokens = tokenize(alice_new)
    gutenberg_file_wc = {x: alice_tokens.count(x) for x in alice_tokens}
    return gutenberg_file_wc

def view_wc(d):
    dist = sorted(d.items(), key=itemgetter(1), reverse=True)
    return "".join(" {}:{} " .format(k, v) for k, v in d.items())

def clustercount(d):
    threephonemes = re.findall(r'\b[sS][cCtT][rR]|\b[sS][pP][lLrR]|\b[sS][qQ][uU]', view_wc(gutenberg_file_wc('alice.txt')))
    twophonemes = re.findall(r'\b[sS][cC][hH]|\b[sStT][hH][rRwW]|\b[sS][cCkKmMnNpPtT]|\b[bBcCdDgfFGpPtT][rR]|\b[dDgGsStT][wW]|\b[bBcCfFgGpPsS][lL]', view_wc(gutenberg_file_wc('alice.txt')))
    threephonemesdata = {x: threephonemes.count(x) for x in threephonemes}
    twophonemesdata = {x: twophonemes.count(x) for x in twophonemes}
    #this supposedly only works in Python 3.5 and up
    clusterdata = {**threephonemesdata, **twophonemesdata}
    #this should work for Python 3.4 and lower as well as 3.5 and up
    #clusterdata = merge(threephonemesdata,twophonemesdata)
    orderedclusterdata = sorted(clusterdata.items(),key=itemgetter(1), reverse=True)
    return orderedclusterdata

def merge(dict1, dict2):
    mdict = dict1.copy()
    mdict.update(dict2)
    return mdict

#print(gutenberg_file_wc('alice.txt'))
#print(view_wc(gutenberg_file_wc('alice.txt')))
print(clustercount(view_wc(gutenberg_file_wc('alice.txt'))))
