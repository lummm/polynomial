# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "liam"
__date__ = "$Jun 3, 2015 10:43:07 AM$"


class Polynomial:
    
    
    """
        init Polynomial class.  
    Defaults to binary modulus
    """
    def __init__(self, modulus= 2, coefs= []):
        self.modulus= modulus
        self.coefs= coefs
        self._reduce()
        self._trim()
        

    
    
    
    """
        reduce
    To keep coefficient mod classes in the [0, n) range
    """
    def _reduce(self):
        for i in range(0, len(self.coefs)):
            self.coefs[i]= self.coefs[i] % self.modulus
            
    """
        trim
    Trims trailing 0's.
    Only useful after __reduce is run
    """
    def _trim(self):
        if(len(self.coefs) > 1):
            last_non_zero = -1
            while (self.coefs[last_non_zero] == 0) and (last_non_zero+ len(self.coefs)> 0):
                last_non_zero = last_non_zero-1
            
            if (last_non_zero < -1):
                self.coefs = self.coefs[:last_non_zero + 1]    
    
    """
        deg
    Returns the degree of the polynomial
    """
    def deg(self):
        return len(self.coefs)-1
        

    """
    String output
    """
    def __str__(self):
        if self.deg() == 0:
            return str(0)
        s=""
        for i in range(0, len(self.coefs)):
            s=""
            s= self.term_formatter(self.coefs[i], i)+ "+ "+ s
        return s[:-2]
        
    """
    Formats terms for the __str__ method
    """
    def term_formatter(self, coefficient, power):
        if coefficient == 0:
            return ""
        if power == 1:
            if coefficient == 1:
                return "x"
            # coefficient==0 case already covered
            else:
                return str(coefficient)+ "x"
        if power == 0:
            return str(coefficient)
        # power is > 2, and coefficient is nonzero
        else:
            if coefficient ==1:
                return "x^"+ str(power)
            else:
                return str(coefficient) + "x^"+ str(power)
    
    def times(self, multiplicand):
        if(self.modulus != multiplicand.modulus):
            print "Moduli of the products must match!"
            return false
        else: 
            # initialize the new coefficient list with zeroes
            # --> degree is the sum of the degrees of multiplicands (hence 
            # length is one greater)
            new_coefs= [0] * (self.deg()+ multiplicand.deg()+ 1)
            for i in range(0, len(self.coefs)):
                for j in range(0, len(multiplicand.coefs)):
                    new_coefs[i + j] += (self.coefs[i] * multiplicand.coefs[j])
            product = Polynomial(self.modulus, new_coefs)
            product._reduce()
            product._trim()
            return product















