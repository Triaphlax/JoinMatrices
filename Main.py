import BitOperations

permutations = {
    0: [0, 1, 2],
    1: [0, 2, 1],
    2: [1, 0, 2],
    3: [1, 2, 0],
    4: [2, 0, 1],
    5: [2, 1, 0]
}

def internalStateToDisplayState(internalState):
    displayState = {
        0: "0",
        1: "1",
        2: "2",
        3: " ",
    }[internalState]
    return displayState


def displayJoinMatrix(joinMatrix):
    a = internalStateToDisplayState(BitOperations.getDigitAtPlace(joinMatrix, 0))
    b = internalStateToDisplayState(BitOperations.getDigitAtPlace(joinMatrix, 1))
    c = internalStateToDisplayState(BitOperations.getDigitAtPlace(joinMatrix, 2))
    d = internalStateToDisplayState(BitOperations.getDigitAtPlace(joinMatrix, 3))
    e = internalStateToDisplayState(BitOperations.getDigitAtPlace(joinMatrix, 4))
    f = internalStateToDisplayState(BitOperations.getDigitAtPlace(joinMatrix, 5))
    print("   |*0*|*1*|*2*|")
    print("----------------")
    print("*0*| "+a+" | "+b+" | "+d+" |")
    print("----------------")
    print("*1*| "+b+" | "+c+" | "+e+" |")
    print("----------------")
    print("*2*| "+d+" | "+e+" | "+f+" |")
    print("----------------")


def switchOutputValuesInJoinMatrix(joinMatrix, permutation):
    newJoinMatrix = 0
    permutation.extend([3])
    for i in range(0, 6):
        digitInOriginalJoinMatrix = BitOperations.getDigitAtPlace(joinMatrix, i)
        newDigit = permutation[digitInOriginalJoinMatrix]
        newJoinMatrix += newDigit * pow(4, i)
    return newJoinMatrix


def switchInputValuesInJoinMatrix(joinMatrix, permutation):
    newJoinMatrix = 0
    digits = BitOperations.getAllDigits(joinMatrix)


totalJoinMatricesAtStart = pow(4, 6)
relevantJoinMatrices = set(range(0, totalJoinMatricesAtStart))
newRelevantJoinMatrices = set()

# Equivalency on output
for p, perm in enumerate(permutations):
    for matrix in relevantJoinMatrices:
        equivalentMatrix = switchOutputValuesInJoinMatrix(matrix, permutations[p])
        if matrix <= equivalentMatrix:
            newRelevantJoinMatrices.add(matrix)
    relevantJoinMatrices = newRelevantJoinMatrices
    newRelevantJoinMatrices = set()

for rjm in relevantJoinMatrices:
    displayJoinMatrix(rjm)

# ---Output--- #
print("Number of matrices: " + str(len(relevantJoinMatrices)))
