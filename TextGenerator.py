"""
This file generates text using a higher order Markov Chains
The states are made up of words
"""

import numpy as np
from random import randrange
from textCleaner import textCleaner

#==============================================================================
#enter parameters
#==============================================================================
#file = 'mix.txt' #file name
#noOfWords = 50   #max number of words
#order = 4        #define order
#==============================================================================

def TextGenerator(file):

    noOfWords = 50
    order = 3
    
    #import and clean text
    text = open(file,encoding='latin1').read()
    text = textCleaner(text)

    #split text into words
    words = text.split()

    #split text into sets
    def makeSets(words):
        for i in range(len(words)-order):
            sets = words[i]
            for j in range(order-1):
                sets = ' '.join([sets,words[i+j+1]])
            yield (sets,words[i+order])

    wordSets = makeSets(words)

    #create empty dictionary
    wordDict = {}

    #create dictionary with possible subsequent words
    for prevStates, futState in wordSets:
        if prevStates in wordDict.keys():
            wordDict[prevStates].append(futState)
        else:
            wordDict[prevStates] = [futState]
        
    index = randrange(len(wordDict))
    init = list(wordDict)[index]

    while init[0].islower() and init[0].isalpha():
        index = randrange(len(wordDict))
        init = list(wordDict)[index]

    chain = init.split()

    #define punctuation to end chain
    sentBreak = {'!','.','?'}

    #create Markov chain
    for i in range(noOfWords-order):
        prev = chain[-1] #initiate previous states
        for j in range(order-1):
            prev = ' '.join([chain[-2-j],prev])
        chain.append(np.random.choice(wordDict[prev]))
        if chain[-1][-1] in sentBreak and len(chain) > 25:
            break
    
    #print word chain
    tweet = ' '.join(chain)
    
    return tweet
