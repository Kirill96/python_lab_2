import tempfile
import os


def splitBigFile(nameFile, bufferSize, listTempfileName, lineSep):
    count = os.path.getsize(nameFile) / bufferSize + 1
    print count

    with open(nameFile, "r") as file:
        offset = 0
        for i in xrange(count):
            addToEndLine = 0
            tempfileName = tempfile.mktemp()
            listTempfileName.append(tempfileName)

            file.seek(offset + bufferSize)
            while True:
                char = file.read(1)
                addToEndLine += 1
                if char == lineSep or char == "":
                    break

            with open(tempfileName, "w") as tempFile:
                file.seek(offset)
                tempFile.write(file.read(bufferSize + addToEndLine))
                offset += bufferSize + addToEndLine


def sortSmallFile(nameFile, lineSep, fieldSep, listKey, isNumber, reverse):
    with open(nameFile, "r") as file:
        listLine = file.read().split(lineSep)

    with open(nameFile, "w") as file:
        for line in sort(listLine, fieldSep, listKey, isNumber, reverse):
            if line != "":
                file.write(line + lineSep)
        #file.writelines()


def sort(listLine, fieldSep, listKey, isNumber, reverse):
    if len(listLine) <= 1:
        return listLine

    left = listLine[:len(listLine) / 2]
    right = listLine[len(listLine) / 2:]

    return mergeList(sort(left, fieldSep, listKey, isNumber, reverse),
                     sort(right, fieldSep, listKey, isNumber, reverse),
                     fieldSep, listKey, isNumber, reverse)


def mergeList(left, right, fieldSep, listKey, isNumber, reverse):
    result = []
    leftIndex = 0
    rightIndex = 0

    funcCmp = definitCmpFunc(fieldSep, listKey, isNumber, reverse)

    while leftIndex < len(left) and rightIndex < len(right):
        if funcCmp(left[leftIndex], right[rightIndex]):
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1

    if leftIndex >= len(left):
        result.extend(right[rightIndex:])
    elif rightIndex >= len(right):
        result.extend(left[leftIndex:])

    return result


def definitCmpFunc(fieldSep, listKey, isNumber, reverse):

    if reverse:
        def funcCmp(first, second, lstKey = listKey):
            if first == "" or second == "":
                return True

            firstFields = str(first).split(fieldSep)
            secondFields = str(second).split(fieldSep)
            firstFieldsCount = len(firstFields)
            secondFieldsCount = len(secondFields)

            if lstKey is None:
                if firstFieldsCount >= secondFieldsCount:
                    Keys = secondFieldsCount
                else:
                    Keys = firstFieldsCount
                lstKey = range(1, Keys + 1)

            for key in lstKey:
                if isNumber:
                    fieldFirst = int(firstFields[key - 1])
                    fieldSecond = int(secondFields[key - 1])
                else:
                    fieldFirst = firstFields[key - 1]
                    fieldSecond = secondFields[key - 1]

                if fieldFirst > fieldSecond:
                    return True
                elif fieldFirst < fieldSecond:
                    return False

            if firstFieldsCount < secondFieldsCount:
                return False
            else:
                return True
        return funcCmp
    elif not reverse:
        def funcCmp(first, second, lstKey = listKey):
            if first == "" or second == "":
                return True

            firstFields = str(first).split(fieldSep)
            secondFields = str(second).split(fieldSep)
            firstFieldsCount = len(firstFields)
            secondFieldsCount = len(secondFields)

            if lstKey is None:
                if firstFieldsCount >= secondFieldsCount:
                    Keys = secondFieldsCount
                else:
                    Keys = firstFieldsCount
                lstKey = range(1, Keys + 2)

            for key in lstKey:
                if isNumber:
                    fieldFirst = int(firstFields[key - 1])
                    fieldSecond = int(secondFields[key - 1])
                else:
                    fieldFirst = firstFields[key - 1]
                    fieldSecond = secondFields[key - 1]

                if fieldFirst < fieldSecond:
                    return True
                elif fieldFirst > fieldSecond:
                    return False

            if firstFieldsCount > secondFieldsCount:
                return False
            else:
                return True
        return funcCmp


def mergeFile(listTempfile, resultFile, lineSep, fieldSep,
                listKey, isNumber, reverse):

    funcCmp = definitCmpFunc(fieldSep, listKey, isNumber, reverse)
    with open(listTempfile.pop(0), "r") as firstFile:
        with open(listTempfile.pop(0), "r") as secondFile:

            if len(listTempfile) == 0:
                tempfileName = resultFile
            else:
                tempfileName = tempfile.mktemp()

            with open(tempfileName, "w") as file:
                firstFileStr = readLine(firstFile, lineSep)
                secondFileStr = readLine(secondFile, lineSep)

                while firstFileStr != "" and secondFileStr != "":
                    if funcCmp(firstFileStr, secondFileStr):
                        file.write(firstFileStr)
                        firstFileStr = readLine(firstFile, lineSep)
                    else:
                        file.write(secondFileStr)
                        secondFileStr = readLine(secondFile, lineSep)

                if firstFileStr == "":
                    while secondFileStr != "":
                        file.write(secondFileStr)
                        secondFileStr = readLine(secondFile, lineSep)
                elif secondFileStr == "":
                    while firstFileStr != "":
                        file.write(firstFileStr)
                        firstFileStr = readLine(firstFile, lineSep)

            listTempfile.append(tempfileName)


def readLine(file, lineSep):
    tempList = []
    while True:
        char = file.read(1)
        tempList.append(char)
        if char == lineSep or char == "":
            break
    return "".join(tempList)

def readLinesecond(file, lineSep):
    tempList = []
    ite = file.tell()
    while True:
        char = file.read(1)
        tempList.append(char)
        if char == lineSep or char == "":
            break
    file.seek(ite)
    return "".join(tempList)

def sortBigFile(nameFile, resultFile, bufferSize,
                lineSep = "\n", fieldSep = "\t",
                listKey = None, isNumber = False,
                reverse = False, isCheck = False):

    if isCheck:
        with open(nameFile, "r") as file:
            while True:
                currentLine = readLine(file, lineSep)
                nextLine = readLinesecond(file, lineSep)
                if nextLine == "":
                    return True
                if not definitCmpFunc(fieldSep, listKey,
                                    isNumber, reverse)(currentLine, nextLine):
                    return False

    listTempfile = []
    splitBigFile(nameFile, bufferSize, listTempfile, lineSep)

    for tempfile in listTempfile:
        sortSmallFile(tempfile, lineSep, fieldSep, listKey, isNumber, reverse)
    print "Sort all small files completed"

    while len(listTempfile) > 1:
        mergeFile(listTempfile, resultFile, lineSep, fieldSep,
                   listKey, isNumber, reverse)

    print "result in :" + resultFile


print sortBigFile("test1.txt", "stest1.txt", 200, listKey=[1,5], isNumber=True)