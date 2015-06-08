#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "liam"
__date__ = "$Jun 3, 2015 11:20:42 AM$"

from polynom import *

a= [0]*(8)
index= 0
for i in range(0,2):
    for j in range(0,2):
        for k in range(0,2):
            a[index]= Polynomial(2, [i, j, k])
            index+= 1
            
            



for poly in a:
    print "testing " + str(poly)
    print str(poly) + " has order " + str(poly.order())
    if poly.is_primitive():
        print "PRIM"

print "\nTesting polynomial subtraction"
a = Polynomial(4, [2,3,-1,5,7]) # Implicit test of reduce
b = Polynomial(4, [1,0,3,2])
print "A = ", a
print "B = ", b
print "A - B = ", a-b



if __name__ == "__main__":
    print "Some manual tests";
