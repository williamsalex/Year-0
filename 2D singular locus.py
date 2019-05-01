# check to make sure all libraries are necessary
import random
import decimal
import thread
import time
from decimal import *
from random import uniform
_=singular.lib('random.lib')
_=singular.lib('sing.lib')
_=singular.lib('poly.lib')
_=singular.lib('absfact.lib')
_=singular.lib('ring.lib')

# generates trivariate polynomials and multiplies them together before testing

class poly():
    def __init__(self, terms, maxcoeff, maxexp):
        self.t = terms
        self.c = maxcoeff
        self.e = maxexp

def test(attempts, terms, maxcoeff, maxexp):
    count = 0
    total = str(attempts)
    current = singular.ring(0,'(x,y,z)','ds')
    for x in range(attempts):
        num = 0
        polys = []
        while num < 2:
            count = count+1
            newpoly = poly(terms, maxcoeff,maxexp)
            polynomial = singular(str(createPolynomial(newpoly)))
            if singular.dim_slocus(polynomial)==2:
                polys.append(polynomial)
            if len(polys) == 2:
                multipliedPoly = polys[0]*polys[1]
                print(multipliedPoly)
                polys = []
                if singular.dim_slocus(multipliedPoly) ==1:
                    print(multipliedPoly)
                if singular.dim_slocus(multipliedPoly) == 1 and singular.is_is(multipliedPoly.jacob())==0 and len(singular.minAssGTZ(multipliedPoly))==1:
                    print(multipliedPoly)
                    count=count+1
                    num = num+1
    print(str(count)+" out of "+total+" were successful.")
    return 0
    # no common factors, one dimension singular sets

def createPolynomial(newpoly):
    # ONLY TRIVARIATE
    polystring = ''
    for Y in range(newpoly.t):
        polystring = polystring+str(int(random.uniform(1,newpoly.c)))
        f = True
        hasvar = 0
        while f == True:
            c = random.uniform(0,10)
            if c<6:
                hasvar=hasvar+1
                u = random.uniform(0,3)
                if u < 1:
                    polystring = polystring+'x'
                if u < 2:
                    polystring = polystring+'y'
                else:
                    polystring = polystring+'z'
            else:
                if hasvar!=0:
                    if Y != newpoly.t-1:
                        polystring = polystring+'+'
                        hasvar=0
                        break
                    else:
                        f = False
    return polystring
