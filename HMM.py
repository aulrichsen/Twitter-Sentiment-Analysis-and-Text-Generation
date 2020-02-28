"""
This file generates text using a higher order Markov Chains
The states are made up of words
"""

import numpy as np
from random import randrange
import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer

#==============================================================================
#enter parameters
#==============================================================================
file = 'TrumpTweets.txt' #file name
noOfWords = 50 #max number of words
order = 2 #define order
#==============================================================================

#import text
text = open(file,encoding='utf8').read()

#split text into tokens
tokens = nltk.word_tokenize(text)

tokens = nltk.pos_tag(tokens)

#split states into sets
def makeSets(tokens):
    for i in range(len(tokens)-order):
        sets = tokens[i][1]
        for j in range(order-1):
            sets = ' '.join([sets,tokens[i+j+1][1]])
        yield (sets,tokens[i+order][1])

stateSets = makeSets(tokens)

#create empty dictionary
stateDict = {}

#create dictionary with possible subsequent words
for prevStates, futState in stateSets:
    if prevStates in stateDict.keys():
        stateDict[prevStates].append(futState)
    else:
        stateDict[prevStates] = [futState]
        
#create empty dictionary
emisDict = {}

#create dictionary with possible emissions
for emis, states in tokens:
    if states in emisDict.keys():
        emisDict[states].append(emis)
    else:
        emisDict[states] = [emis]
        
#define first state and emission
index = randrange(len(tokens))
firstState = tokens[index][1]
firstWord = np.random.choice(emisDict[firstState])

#ensure first word is capitalised
while firstWord[0].islower() or firstWord[0].isalpha() == False:
    index = randrange(len(tokens))
    firstState = tokens[index][1]
    firstWord = np.random.choice(emisDict[firstState])
    
#define punctuation to end chain
sentBreak = {'!','.','?'}

#initiate state chain 
chain = firstState
for i in range(1,(order)):
    chain = ' '.join([chain,tokens[index+i][1]])
chain = chain.split()

#create state chain
for i in range(noOfWords-order):
    prev = chain[-1] #initiate previous states
    for j in range(order-1):
        prev = ' '.join([chain[-2-j],prev])
    chain.append(np.random.choice(stateDict[prev]))
    if chain[-1][-1] in sentBreak and len(chain) > 25:
        break
    
#create emission chain
tweet = [firstWord]
for i in range(1,(len(chain))):
    tweet.append(np.random.choice(emisDict[chain[i]]))

#detokanize the chain
tweet = TreebankWordDetokenizer().detokenize(tweet)    

print(tweet)