"""
This file generates higher-order Markov chains
The states are made up of characters
"""

import numpy as np
from random import randrange

#==============================================================================
#enter parameters
#==============================================================================
file = 'TrumpTweets.txt' #file name
noOfWords = 280 #max number of words
order = 4 #define order
#==============================================================================

#import text
text = open(file,encoding='utf8').read()

#split text into characters
def split(text):
    return [char for char in text]

chars = split(text)

#split characters into sets
def makeSets(chars):
    for i in range(len(chars)-order):
        sets = chars[i]
        for j in range(order-1):
            sets = ''.join([sets,chars[i+j+1]])
        yield (sets,chars[i+order])

charSets = makeSets(chars)

#create empty dictionary
charDict = {}

#create dictionary with possible subsequent characters
for prevStates, futState in charSets:
    if prevStates in charDict.keys():
        charDict[prevStates].append(futState)
    else:
        charDict[prevStates] = [futState]
    
#define first character set
index = randrange(len(chars))
firstChar = chars[index]

#ensure first character is a capitalised letter
while chars[index].islower() or chars[index].isalpha() == False:
    index = randrange(len(chars))
    firstChar = chars[index]

#initiate character chain 
chain = firstChar
for i in range(order-1):
    chain = ''.join([chain,chars[index+i+1]])
chain = split(chain)

#define punctuation to end chain
sentBreak = {'!','.','?'}

#create Markov chain
for i in range(noOfWords):
    prev = chain[-1] #initiate previous states
    for j in range(order-1):
        prev = ''.join([chain[-2-j],prev])
    chain.append(np.random.choice(charDict[prev]))
    if chain[-1] in sentBreak and len(chain) > 100:
        break
    
#print character chain
print(''.join(chain))