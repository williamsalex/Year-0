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
    count2 = 0;
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
