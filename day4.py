# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def openFile(input):
    with open(input, mode='r', encoding='ascii') as Myfile:
        return ''.join(Myfile.read())
    Myfile.close()


def print_hi():
    data = openFile("data.txt")
    duo = data.split("\n")
    isElvesOneListInElvesTwo = 0
    print("length of duo : ", len(duo))
    for i in range(len(duo)):
        dualElvesShelvesList = []
        duoStr = duo[i]
        eachElves = duoStr.split(",")
        for j in range(len(eachElves)):
            eachShelve = eachElves[j]
            eachShelveNum = eachShelve.split("-")
            startArray = -1
            endArray = -1
            for k in range(len(eachShelveNum)):
                eachShelveInt = int(eachShelveNum[k])
                if k == 0:
                    startArray = eachShelveInt
                elif k == 1:
                    endArray = eachShelveInt
                if k == 1:
                    eachElvesShelvesAssigned = [startArray, endArray]  # [l for l in range(startArray,endArray+1)]
                    dualElvesShelvesList.append(eachElvesShelvesAssigned)
        firstElvesOfDuo = dualElvesShelvesList[0]
        secondElvesOfDuo = dualElvesShelvesList[1]
        start1 = int(firstElvesOfDuo[0])
        start2 = int(secondElvesOfDuo[0])
        end1 = int(firstElvesOfDuo[1])
        end2 = int(secondElvesOfDuo[1])
        if start1 >= start2 and end1 <= end2 or start2 >= start1 and end2 <= end1:
            isElvesOneListInElvesTwo += 1

    print(isElvesOneListInElvesTwo)

    """            if max(firstElvesOfDuo[0], secondElvesOfDuo[0]) <= min(firstElvesOfDuo[1], secondElvesOfDuo[1]):
                """


print_hi()

# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
