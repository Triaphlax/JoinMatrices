import numpy.linalg
import copy
import math

startingMatrix = [
                        [1, 0, 0, 0, 0, 0],
                        [0, 1, 1, 0, 0, 0],
                        [0, 0, 0, 1, 1, 1],
                        [2, 1, 0, 1, 0, 0],
                        [0, 1, 2, 0, 1, 0],
                        [0, 0, 0, 1, 1, 2]
                 ]


def rankAfterFilter(matrix, columnIndices):
    copyOfMatrix = copy.deepcopy(matrix)
    for row in copyOfMatrix:
        for index in range(0, 6):
            if index in columnIndices:
                row[index] = 0
    rank = numpy.linalg.matrix_rank(copyOfMatrix)
    return rank


def filterableSetsIntro(matrix):
    boolList = [False] * 64
    filterableSets(matrix, [0, 1, 2, 3, 4, 5], 0, boolList, [-1] * 64)
    return boolList


def filterableSets(matrix, filterSet, score, boolList, rankList):
    rankList[score] = rankAfterFilter(matrix, filterSet)
    filterabilityDecided = False
    for join in filterSet:
        newFilterSet = copy.copy(filterSet).remove(join)
        newScore = score + math.pow(2, join)
        if rankList[newScore] == -1:
            rankList[newScore] = rankAfterFilter(matrix, newFilterSet)
            filterableSets(matrix, newFilterSet, newScore, boolList, rankList)
        if rankList[newScore] == rankList[score]:
            filterabilityDecided = True
            boolList[score] = False
        elif rankList[newScore] == rankList[score] + 1:
            continue
        else:
            print("An error has occurred in filterableSets")
    if not filterabilityDecided:
        boolList[score] = True


testMatrix = ([[1, 0, 0],
               [0, 1, 1],
               [2, 1, 0],
               [0, 1, 2]])

boolllll = [False] * 8
filterableSets(testMatrix, [0, 1, 2], 0, boolllll, [-1] * 8)
print(boolllll)

x = 3