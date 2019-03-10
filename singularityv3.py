import random
import decimal
from decimal import *
from random import uniform
import re
_=singular.lib('random.lib')
_=singular.lib('sing.lib')

def main(NumberOfPolynomials,NumberOfVariables):
    for X in range(NumberOfPolynomials):
        if(NumberOfVariables == 0):
            NumberOfVariables = int(random.uniform(1,26))
        singularFixer(polygen(NumberOfVariables))

def singularFixer(PolyAndVars):
    variables = PolyAndVars[1]
    variables = set(variables)
    variables = list(variables)
    ringBuilder = '('+variables[0]
    for X in variables[1:]:
        ringBuilder = ringBuilder+','+X
    ringBuilder = str(ringBuilder+')')
    R = singular.ring(0, ringBuilder, 'ds')
    polynomial = singular.sparsepoly(len(PolyAndVars[1]));"";
    if(polynomial.milnor() != -1 and polynomial.milnor() != 0):
        final = [polynomial, polynomial.milnor()]
    else:
        final = ['NaN']
    return final

def polygen(varnum):
    vars = []
    coeffs = list(range(varnum))
    powers = list(range(varnum))
    for X in range(varnum):
        vars.append(randint(97,122))
        vars[X] = chr(vars[X])
        coeffs[X] = int(random.uniform(1,10))
        powers[X] = int(random.uniform(1,10))
    newPoly = ''
    for Y in vars:
        c = random.uniform(-1,2)
        if(c>1):
            newPoly = newPoly+'+'+str(coeffs[vars.index(Y)])+Y+str(powers[vars.index(Y)])
        if(c<0):
            newPoly = newPoly+'-'+str(coeffs[vars.index(Y)])+Y+str(powers[vars.index(Y)])
        if(c<1 and c>0):
            newPoly = newPoly+'*'+str(coeffs[vars.index(Y)])+Y+str(powers[vars.index(Y)])
    return (newPoly, vars)
