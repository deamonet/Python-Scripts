import os  # Standard Library os functions
import logging  # Standard Library Logging functions
import nltk  # Import the Natural Language Toolkit
from nltk.corpus import PlaintextCorpusReader  # Import the PlainText


class Classnltkquery:
    def textCorpuslnit(self, the_path):
        if not os.path.isdir(the_path):
            return "Path is not a Directory"
        if not os.access(the_path, mode=os.R_OK):
            return "Directory is not Readable"
        #try:
        self.Corpus = PlaintextCorpusReader(the_path, ".*")
        print("Processing Files:")
        print(self.Corpus.fileids())
        print("Please wait ...")
        self.rawText = self.Corpus.raw()
        self.tokens = nltk.word_tokenize(self.rawText)
        self.TextCorpus = nltk.Text(self.tokens)
        #except:
            #return "Corpus Creation Failed"
        self.ActiveTextCorpus = True
        return "Success"

    def printCorpusLength(self):
        print("Corpus Text Length: ", end="")
        print(len(self.rawText))

    def printTokensFound(self):
        print("Tokens Found: ", end="")
        print(len(self.tokens))

    def printVocabSize(self):
        print("Calculating...")
        print("Vocabulary Size: ", end="")
        vocabulary_used = set(self.TextCorpus)
        vocabulary_size = len(vocabulary_used)
        print(vocabulary_size)

    def printSortedVocab(self):
        print("Compiling...")
        print("Sorted Vocabulary ", end="")
        print(sorted(set(self.TextCorpus)))

    def printCollocation(self):
        print("Compiling Collocations...")
        self.TextCorpus.collocations()

    def searchWordOccurence(self):
        my_word = input("Enter Search Word : ")

        if my_word:
            word_count = self.TextCorpus.count(my_word)
            print(my_word + " occured: ")
            print(word_count, end="")
            print(" times ")
        else:
            print("Word Entry is Invalid")

    def generateConcordance(self):
        my_word = input("Enter word to Concord : ")
        if my_word:
            self.TextCorpus.concordance(my_word)
        else:
            print("Word Entry is Invalid")

    def generateSimilarities(self):
        my_word = input("Enter seed word : ")

        if my_word:
            self.TextCorpus.similar(my_word)
        else:
            print("Word Entry is Invalid")

    def printWordIndex(self):
        my_word = input("Find first occurrence of what Word?: ")
        if my_word:
            word_index = self.TextCorpus.index(my_word)
            print("First Occurrence of : " + my_word + "is at offset: ", end="")
            print(word_index)
        else:
            print("Word Entry is Invalid")

    def printVocabulary(self):
        print("Compiling Vocabulary Frequencies", end="")

        vocab_freq_list = self.TextCorpus.vocab()
        print(vocab_freq_list.items())
