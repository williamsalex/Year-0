# Loading all libraries and creating a list of the variables that Singular is OK with
import random
import decimal
import thread
import time
from decimal import *
from random import uniform
import re
import _thread
import threading
from multiprocessing import Pool
from multiprocessing import Process
import os
import multiprocessing as mp
_=singular.lib('random.lib')
_=singular.lib('sing.lib')
_=singular.lib('poly.lib')
_=singular.lib('absfact.lib')
_=singular.lib('ring.lib')
possiblevars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
# Automates the process

def test(PolyCount,variablecount,length):
    print("Number of processors: ", mp.cpu_count())
    P = Process()
    count = 0
    count2 = 0
    total = str(PolyCount)
    for x in range(PolyCount):
        ring = ringBuilder(variablecount)
        polynomial = createPolynomial(ring, length)
        jacobian = polynomial.jacob()
        if singular.dim_slocus(polynomial) == 1:
            if singular.is_is(jacobian)[length] == 0:
                if len(singular.minAssGTZ(polynomial)) == 1:
                    print(polynomial)
                    count = count+1
        count2=count2+1
        print(count2)
    print(str(count)+" out of "+total+" were successful.")

def ringBuilder(numVars):
    variables = '('
    currentVariables = set()
    for x in range(numVars):
        x = randint(0,50)
        if x not in currentVariables:
            currentVariables.add(x)
            variables = variables + ',' + possiblevars[x]
    variables = variables[0]+variables[2:]+')'
    return singular.ring(0, variables, 'ds')

def createPolynomial(ring, length):
    return singular.sparsepoly(length,length*3,10,1);

p_iter = pyprocessing()
P = parallel(p_iter=p_iter)
v = list(P(test(100,3,2)))
parallel_iter(test,0,)


## ISSUES ##
### testing not working - ring not being constructed?
###



def testPolynomial(polynomial):
    print(polynomial)
    singular.current_ring()
    jacobianMatrix = polynomial.jacob()
    if singular.dim_slocus(polynomial) == 1:
        if polynomial.factorize()[1][2]==polynomial:
            return polynomial
        else:
            return 'Unsuccessful'

if(singular.is_is(jacobianMatrix)[len(singular.is_is(jacobianMatrix))] == 0):
##### OLD CODE #####

def polynomial(variablecount,length):
    if(variablecount > 24):
        variablecount = 24
    vars = []
    final = []
    arg1 = randint(length,length*3)
    arg2 = randint(length*3,length*5)
    variables = '('
    s = 0
    arg1 = randint(length,2*length)
    arg2 = randint(2*length,3*length)
    for X in range(variablecount):
        s = randint(0,50)
        if s not in vars:
            vars.append(s)
            variables = variables + ',' + possiblevars[s]
    variables = variables[0]+variables[2:]+')'
    R = singular.ring(0,variables,'ds')
    poly = singular.sparsepoly(arg1,arg2);"";
    poly1 = poly.jacob()
    print(singular.is_is(poly1))
    if singular.dim_slocus(poly) == 1:
        print(poly)
        poly1 = singular.jacob(poly)
        for x in range(1,len(vars)+1):
            print(poly1[x][len(vars)])
            print(singular.factorize(poly1[x],1))
            if(poly1[x]==singular.factorize(poly1[x],1)):
                passing=passing+1
        if passing == len(vars):
            print(poly)
            passing = 0



def polynomial(variablecount,length):
    if(variablecount > 24):
        variablecount = 24
    vars = []
    final = []
    variables = '('
    s = 0
    for X in range(variablecount):
        s = randint(0,50)
        if s not in vars:
            vars.append(s)
            variables = variables + ',' + possiblevars[s]
    variables = variables[0]+variables[2:]+')'
    R = singular.ring(0,variables,'ds')
    poly = singular.sparsepoly(length);"";
    false = 0
    for X in range(len(vars)):
        if singular.subst(poly,possiblevars[vars[X]],'*0') == 0:
            false = 1
    if singular.dim_slocus(poly) == 1 and false == 0:
        print(poly)

class poly():



#find the milnor numbers when you test with a large exponent if milnor is below 200 or above 500
#find ones that have small changes in the milnor numbers when increased by 1
#set one variable to zero and test singular locus, should be zero
#find a linear combination of the variables such that when you restrict one variable that that has an isolated critical point
#factor over reals is ok

#  'Γ', 'Δ', 'Ε', 'Ζ', 'Η', 'Θ', 'Ι', 'Κ', 'Λ', 'Μ', 'Ν', 'Ξ', 'Ο', 'Π', 'Ρ', 'Σ', 'Τ', 'Υ', 'Φ', 'Χ', 'Ψ', 'Ω', 'α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ', 'ν', 'ξ', 'ο', 'π', 'ρ', 'σ', 'τ', 'υ', 'φ', 'χ', 'ψ', 'ω',
