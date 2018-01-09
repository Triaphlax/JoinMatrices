def bitShiftLeft(number, times):
    return number << (2 * times)


def bitShiftRight(number, times):
    return number >> (2 * times)


def getDigitAtPlace(number, place):
    return bitShiftRight(number, place) % 4


def getAllDigits(number):
    resultList = []
    for i in range(0, 6):
        resultList.append(getDigitAtPlace(number, i))
    return resultList
