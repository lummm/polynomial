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
            print str(a[index]) + " from " + str([i, j, k])
            index+= 1
            

for poly in a:
    print str(poly) + " times " + str(a[6]) + " equals " + str(poly.times(a[6]))

if __name__ == "__main__":
    print "Some manual tests";
