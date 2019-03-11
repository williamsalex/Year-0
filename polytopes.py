import itertools
simplex = Polyhedra(ieqs=[])
polytopes.altP1.volume()
def inGen(dimension):
    dimension = dimension+1
    ineqs = []
    for X in list(range(dimension)):
        ineqs.append([])
    for X in range(len(ineqs)-1):
        for Y in range(dimension):
            ineqs[X].append(0)
        ineqs[X][X+1] = 1
    for X in list(range(dimension)):
        ineqs[dimension-1].append(-1)
    ineqs[dimension-1][0] = 1
    return ineqs

def inGenV2(candidates):
    candidates = candidates+1
    ineqs = []
    for X in list(range(candidates)):
        ineqs.append([])
    for Y in range(candidates-2,-1,-1):
        ineqs[0].append(Y)
    ineqs = list(itertools.permutations(ineqs[0]))
    for x in list(range(len(ineqs))):
        ineqs[x]=list(ineqs[x])
    profiles = {}
    for x in list(range(len(ineqs))):
        profiles['profile_'+str(x+1)] = ineqs[x]
    return profiles
