import nltk
import math
import random
from random import randrange
from nltk.corpus import brown

def trainTagger():
        fd = nltk.FreqDist(brown.words(categories='news'))
        cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
        most_freq_words = fd.most_common(15000)
        likely_tags = dict((word, cfd[word].max()) for (word, _) in most_freq_words)

        unigram_tagger = nltk.UnigramTagger(model=likely_tags)
        return unigram_tagger

def tokenize():
        quote =  'When the light is green you go. When the light is red you stop. But what do you do When the light turns blue With orange and lavender spots?'
        tokens = nltk.word_tokenize(quote)
        return tokens

def tag(unigram_tagger, tokens):
        tagged = unigram_tagger.tag(tokens)
        return tagged

def tokenRemoval(tokens):
        removed_words = []
        total_removed = math.floor((len(tokens)-1)*.3)
        for i in range(total_removed):
                chosen_index = random.randint(1, len(tokens)-1)
                while(chosen_index in removed_words):
                        chosen_index = random.randint(1, len(tokens)-1)
                removed_words.append(chosen_index)
        return removed_words

def tokenReplacement(tokens, tagged, array):
        brown_corpus = brown.tagged_words()
        for i in range(len(array)-1):
                tag = tagged[array[i]][1]
                matching_tokens = [word for word, pos in brown_corpus if pos.startswith(tag)]
                new_word = random.choice(matching_tokens)
                tokens[array[i]] = new_word
        print(tokens)

def generateMadlib():
        unigram_tagger = trainTagger();
        tokens = tokenize()
        tagged = tag(unigram_tagger, tokens)

        array = tokenRemoval(tokens)
        tokenReplacement(tokens, tagged, array)

generateMadlib()
