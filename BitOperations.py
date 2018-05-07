def bitShiftLeft(number, times):
    return number << times


def bitShiftRight(number, times):
    return number >> times

# Quaternary
def getDigitAtPlaceQ(number, place):
    return bitShiftRight(number, place * 2) % 4


def getAllDigitsQ(number):
    resultList = []
    for i in range(0, 6):
        resultList.append(getDigitAtPlaceQ(number, i))
    return resultList

# Binary
def getDigitAtPlaceB(number, place):
    return bitShiftRight(number, place) % 2


def getAllDigitsB(number):
    resultList = []
    for i in range(0, 6):
        resultList.append(getDigitAtPlaceB(number, i))
    return resultList