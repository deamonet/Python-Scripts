import _NLTKQuery
import _classNLTKQuery

print("Welcome to the NLTKQuery Experimentation")
print("Please wait loading NLTK")

oNLTK = _classNLTKQuery.Classnltkquery()
print("Input full path name where intended corpus file or files are stored ")
print("Note: you must enter a quoted string e.g. c://simpson// ")

userSpecifiedPath = input("Path: ")
# Attempt to create a text Corpus
result = oNLTK.textCorpuslnit(userSpecifiedPath)
print(result)
if result == "Success":
    menuSelection = -1
    while menuSelection != 0:
        if menuSelection != -1:
            print
            s = input('Press Enter to continue... ')
        menuSelection = _NLTKQuery .getUserSelection()
        if menuSelection == 1:
            oNLTK.printCorpusLength()
        elif menuSelection == 2:
            oNLTK . printTokensFound()
        elif menuSelection == 3:
            oNLTK.printVocabSize()
        elif menuSelection == 4:
            oNLTK.printSortedVocab()
        elif menuSelection == 5:
            oNLTK .printCollocation()
        elif menuSelection == 6:
            oNLTK .searchWordOccurence()
        elif menuSelection == 7:
            oNLTK.generateConcordance()
        elif menuSelection == 8:
            oNLTK.generateSimilarities()
        elif menuSelection == 9:
            oNLTK . printWordlndex()
        elif menuSelection == 10:
            oNLTK.printVocabulary()
        elif menuSelection == 0:
            print("Goodbye")
        elif menuSelection == -1:
            continue
    else:
        print("unexpected error condition")
        menuSelection = 0
else:
    print("Closing NLTK Query Experimentation")
