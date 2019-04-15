import itertools
def inGenV3(candidates):
    candidates = candidates+1
    ineqs = []
    for X in list(range(candidates)):
        ineqs.append([])
    for Y in range(candidates-2,-1,-1):
        ineqs[0].append(Y)
    ineqs = list(itertools.permutations(ineqs[0]))
    for x in range(len(ineqs)):
        ineqs[x]=list(ineqs[x])
    winner = []
    for X in range(len(ineqs)):
        winner.append(ineqs[X].index(max(ineqs[Y])))
    winConditions = []
    for X in range(candidates)
    winConditions = [ineqs[x] for x in winner if x ]
        for Y in ineqs:

    return ineqs
.sort()

def createProfiles(candidates):
    profileBase = [X for X in range(candidates)]
    profileBase = list(itertools.permutations(profileBase))
    print(profileBase)
    currentINTlist = []
    for X in profileBase:
        for Y in X:
            currentINT = currentINT.append(Y)
    profileBase = profileBase.sort(reverse=True)
    return profileBase



def profileGen(candidates):
    candidatelist = []
    for X in range(candidates):

def ineqOrder(profiles):
    winner = 0
    d = [[] for x in range(len(profiles))
    for Y in range(len(profiles)):
        winner = ineqs[Y].index(max(ineqs[Y]))

profiles = ["ABCD","ABDC","ACBD","ACDB","ADBC","ADCB","BACD","BADC","BCAD","BCDA","BDAC","BDCA","CABD","CADB","CBAD","CBDA","CDAB","CDBA","DABC","DACB","DBAC","DBCA","DCAB","DCBA"]
              1      2      3       4     5      6      7     8        9     10      11    12      13    14     15     16      17    18     19      20    21     22      23    24
scorelist = []

for X in range(len(profiles)):
    [profiles[X] in X if profiles[X][0]=='A']



for X in range(len(profiles)):
    if profiles[X][0] == 'A':
        score3.append(profiles[X])

for X in range(len(profiles)):
    if profiles[X][1] == 'A':
        score2.append(profiles[X])

for X in range(len(profiles)):
    if profiles[X][2] == 'A':
        score1.append(profiles[X])

for X in range(len(profiles)):
    if profiles[X][3] == 'A':
        score0.append(profiles[X])
