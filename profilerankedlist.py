import itertools
def m(candidates):
    return subtraction(candidates,findWinners(candidates,createProfiles(candidates)))

def createProfiles(candidates):
    profileBase = [X for X in range(candidates)]
    profileBase = list(itertools.permutations(profileBase))
    string = ""
    currentINTlist = []
    for X in profileBase:
        for Y in X:
            string = string+str(Y)
        currentINTlist.append(string)
        string = ""
    for X in range(len(currentINTlist)):
        currentINTlist[X] = int(currentINTlist[X])
    currentINTlist = sorted(currentINTlist, reverse=True)
    for X in range(len(currentINTlist)):
        currentINTlist[X] = str(currentINTlist[X])
    for X in range(len(currentINTlist)):
        if len(currentINTlist[X]) != candidates:
            currentINTlist[X] = "0"+currentINTlist[X]
    return currentINTlist

def findWinners(candidates, profiles):
    pointsList = []
    for X in range(candidates):
        pointsList.append([])
        for Y in range(len(profiles)):
            pointsList[X].append([0,profiles[Y]])
    for X in range(candidates):
        for Y in range(len(profiles)):
            pointsList[X][Y][0] = (candidates-1)-profiles[Y].find(str(X))
    return pointsList

def subtraction(candidates,pointsList):
    answerList = []
    for Z in range(candidates-1):
        answerList.append([])
        for X in range(len(pointsList[0])):
            answerList[Z].append(pointsList[0][X][1])
    for F in range(candidates):
        answerList.append([])
        print(answerList)
        for S in [X for X in range(candidates) if X != F]:
            print(answerList)
            for X in range(len(pointsList[0])):
                if pointsList[F][X][0]-pointsList[S][X][0] > 0:
                    answerList[F].append([pointsList[F][X][0]-pointsList[S][X][0], pointsList[F][X][0]])
    return answerList


    for X in range(len(answerList)):
        answerList[X].append(pointsList[])
    for X in range(len(pointsList[0])):
        for Y in range(candidates):


    return answerList
