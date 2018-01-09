import BitOperations

permutations = {
    0: [0, 1, 2],
    1: [0, 2, 1],
    2: [1, 0, 2],
    3: [1, 2, 0],
    4: [2, 0, 1],
    5: [2, 1, 0]
}

joinsDictionaryByIndex = {
    0: "00",
    1: "01",
    2: "11",
    3: "02",
    4: "12",
    5: "22"
}

joinsDictionaryByJoin = dict(zip(joinsDictionaryByIndex.values(), joinsDictionaryByIndex.keys()))


def internalStateToDisplayState(internalState):
    displayState = {
        0: "0",
        1: "1",
        2: "2",
        3: " ",
    }[internalState]
    return displayState


def displayJoinMatrix(joinMatrix):
    digits = BitOperations.getAllDigits(joinMatrix)
    a = internalStateToDisplayState(digits[0])
    b = internalStateToDisplayState(digits[1])
    c = internalStateToDisplayState(digits[2])
    d = internalStateToDisplayState(digits[3])
    e = internalStateToDisplayState(digits[4])
    f = internalStateToDisplayState(digits[5])
    print("   |*0*|*1*|*2*|")
    print("----------------")
    print("*0*| "+a+" | "+b+" | "+d+" |")
    print("----------------")
    print("*1*| "+b+" | "+c+" | "+e+" |")
    print("----------------")
    print("*2*| "+d+" | "+e+" | "+f+" |")
    print("----------------")
    print("")


def switchOutputValuesInJoinMatrix(joinMatrix, permutation):
    newJoinMatrix = 0
    permutation.extend([3])
    for i in range(0, 6):
        digitInOriginalJoinMatrix = BitOperations.getDigitAtPlace(joinMatrix, i)
        newDigit = permutation[digitInOriginalJoinMatrix]
        newJoinMatrix += newDigit * pow(4, i)
    return newJoinMatrix


def switchInputValuesInJoinMatrix(joinMatrix, permutation):
    global joinsDictionaryByIndex, joinsDictionaryByJoin
    newJoinMatrix = 0
    digits = BitOperations.getAllDigits(joinMatrix)
    newDigits = [-1, -1, -1, -1, -1, -1]
    for i in range(0, 6):
        joinToTranslate = joinsDictionaryByIndex[i]
        firstJoinDigit = permutation[int(joinToTranslate[0])]
        secondJoinDigit = permutation[int(joinToTranslate[1])]
        translatedJoin = [firstJoinDigit, secondJoinDigit]
        translatedJoin.sort()
        translatedJoinAsString = ''.join((map(str, translatedJoin)))
        newDigitIndex = joinsDictionaryByJoin[translatedJoinAsString]
        newDigits[newDigitIndex] = digits[i]
    for i, newDigit in enumerate(newDigits):
        newJoinMatrix += newDigit * pow(4, i)
    return newJoinMatrix


totalJoinMatricesAtStart = pow(4, 6)
equivalenceClasses = []
for i in range(0,totalJoinMatricesAtStart):
    equivalenceClasses.append({i})
newEquivalenceClasses = []
toSkip = []


def findEquivalenceClassIndexWithElement(eqClasses, element):
    for classIndex, eqClass in enumerate(eqClasses):
        if element in eqClass:
            return classIndex


# Equivalency on output
for permutationIndex in range(1, 6):
    for index, eqC in enumerate(equivalenceClasses):
        if index not in toSkip:
            eqClassToAdd = set()
            representative = next(iter(eqC))
            eqJM = switchOutputValuesInJoinMatrix(representative, permutations[permutationIndex])
            eqJMIndex = findEquivalenceClassIndexWithElement(equivalenceClasses, eqJM)
            if index != eqJMIndex:
                eqClassToAdd = eqC.union(equivalenceClasses[eqJMIndex])
                toSkip.append(eqJMIndex)
            else:
                eqClassToAdd = eqC
            newEquivalenceClasses.append(eqClassToAdd)
    equivalenceClasses = newEquivalenceClasses
    newEquivalenceClasses = []
    toSkip = []

# Equivalency on input
for permutationIndex in range(1, 6):
    for index, eqC in enumerate(equivalenceClasses):
        if index not in toSkip:
            eqClassToAdd = set()
            representative = next(iter(eqC))
            eqJM = switchInputValuesInJoinMatrix(representative, permutations[permutationIndex])
            eqJMIndex = findEquivalenceClassIndexWithElement(equivalenceClasses, eqJM)
            if index != eqJMIndex:
                eqClassToAdd = eqC.union(equivalenceClasses[eqJMIndex])
                toSkip.append(eqJMIndex)
            else:
                eqClassToAdd = eqC
            newEquivalenceClasses.append(eqClassToAdd)
    equivalenceClasses = newEquivalenceClasses
    newEquivalenceClasses = []
    toSkip = []

for eqC in equivalenceClasses:
    representative = next(iter(eqC))
    displayJoinMatrix(representative)

# ---Output--- #
print("Number of matrices: " + str(len(equivalenceClasses)))
