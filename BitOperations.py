def bitShiftLeft(number, times):
    return number << (2 * times)


def bitShiftRight(number, times):
    return number >> (2 * times)


def getDigitAtPlace(number, place):
    return bitShiftRight(number, place) % 4
