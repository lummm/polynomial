# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "liam"
__date__ = "$Jun 3, 2015 10:43:07 AM$"


class Polynomial:
    
    
    """
    Polynomial class.  
    
    Defaults to binary modulus
    """
    def __init__(self, modulus= 2, coefs= []):
        self.modulus= modulus
        self.coefs= coefs
        

    """
    To keep coefficient mod classes in the [0, n) range
    """
    def reduce(self):
        for i in range(0, len(self.coefs)):
            self.coefs[i]= self.coefs[i] % self.modulus
            
    """
    Trims trailing 0's.
    Only useful after __reduce is run
    """
    def trim(self):
        lastNonZero= -1
        while self.coefs[lastNonZero]== 0:
            lastNonZero= lastNonZero-1
            
        if (lastNonZero!= len(self.coefs)-1):
            self.coefs= self.coefs[:lastNonZero+1]
    
    """
    Returns the degree of the polynomial
    """
    def deg(self):
        return len(self.coefs)-1
        

    """
    String output
    """
    def __str__(self):
        s=""
        for i in range(0, len(self.coefs)):
            if (self.coefs[i]!= 0 and self.coefs[i]!= 1):
                s= str(self.coefs[i])+ "x^"+ str(i)+ "+ "+ s
                
            elif (self.coefs[i]== 1):
                s= "x^"+ str(i)+ "+ "+ s
        if (s==""):
            return 0
        else:
            return s[:-2]















