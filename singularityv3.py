import random
import decimal
from decimal import *
from random import uniform
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
    a = PolyAndVars[0].split('+',2)[0]
    b = PolyAndVars[0].split('-',2)[0]
    c = PolyAndVars[0].split('*',2)[0]
    if(max(a,b,c) ==a):
        b = a
    if(max(a,b,c) == c):
        b = c
    FirstTerm = PolyAndVars[0][0:len(b)]
    PolyAndVars = PolyAndVars[0][len(b)+1:]
    PolyAndVars = PolyAndVars+FirstTerm
    polynomial = singular(PolyAndVars)
    if(polynomial.milnor() != -1 and polynomial.milnor() != 0):
        print(polynomial)
        print(polynomial.milnor())
    final = [polynomial, polynomial.milnor()]
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
