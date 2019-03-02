# create polynomials
# look at behavior at x=0
# search for isolated singularities at the origin
# if found, calculate milnor number using sage
import random
import decimal
import secrets
from decimal import *
from random import uniform
def main(variables,limits,number):
    return functionandMilnorNumber

def polygen(varnum):
    vars = []
    for X in range(varnum):
        vars.append(randint(97,122))
        vars[X] = chr(vars[X])
        vars[X] = (vars[X],random.uniform(-10,10))
    return vars
    # take a polynomial that is formatted in ()
def singFind(polynomial):
    variables = []
    coeffs = []
    count = len(polynomial)
    for X in range(0,len(polynomial),1):
        for Y in (0,1):
            if Y == 1:
                coeffs.append(polynomial[X][Y])
            if Y == 0:
                variables.append(polynomial[X][Y])
    ringBuilder = ''
    for X in variables:
        ringBuilder = ringBuilder+X
    R = singular.ring(0, ringBuilder, 'dp')
    print ringBuilder
    print R
    return variables
    for X in polynomial:
        fixedPoly = singular([X,0]*[X,1])
    for Y in 0:len(variables):
        if Z.diff(variables[Y]) == 0:
            Z.diff(variables[Y])
            count++
    if count == len(variables):

    return ShinyNewPoly
