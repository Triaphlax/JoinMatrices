import BitOperations


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


def switchOutputValuesInJoinMatrix(joinMatrix, spot0, spot1, spot2):
    newJoinMatrix = 0
    permutation = [spot0, spot1, spot2, 3]
    for i in range(0, 6):
        digitInOriginalJoinMatrix = BitOperations.getDigitAtPlace(joinMatrix, i)
        newDigit = permutation[digitInOriginalJoinMatrix]
        newJoinMatrix += newDigit * pow(4, i)
    return newJoinMatrix


totalJoinMatricesAtStart = pow(4, 6)
relevantJoinMatrices = set(range(0, totalJoinMatricesAtStart))

# ---Output--- #
print("Number of matrices: " + str(len(relevantJoinMatrices)))
