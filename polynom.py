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
    Only useful after _reduce is run
    """
    def _trim(self):
        if(len(self.coefs) > 1):
            last_non_zero = -1
            while (self.coefs[last_non_zero] == 0) and (last_non_zero+ len(self.coefs)> 0):
                last_non_zero = last_non_zero-1
            
            
            if (last_non_zero < -1):
                # trim up to and including last_non_zero
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
        if len(self.coefs) == 1:
            return str(self.coefs[0])
        s=""
        for i in range(0, len(self.coefs)):
            s= self.term_formatter(self.coefs[i], i)+ s
        return s[:-2]
        
    """
    Formats terms for the __str__ method
    """
    def term_formatter(self, coefficient, power):

        # to avoid formatting as x^1
        if power == 1:
            if coefficient == 1:
                return "x+ "
            if coefficient == 0:
                return ""
            else:
                return str(coefficient)+ "x+ "
            
        # this case has no x at all
        if power == 0:
            if coefficient == 0:
                return ""
            else :
                return str(coefficient)+ "+ "
        
        # else power is > 2
        else:
            if coefficient == 0:
                return ""
            if coefficient == 1:
                return "x^"+ str(power)+ "+ "
            else:
                return str(coefficient) + "x^"+ str(power)+ "+ "
    
    def __mul__(self, multiplicand):
        
        if(isinstance(multiplicand, int)):
            new_coefs= [0] * (self.deg() + 1)
            for i in range(0, self.deg()+1):
                new_coefs[i] = self.coefs[i] * multiplicand
            return Polynomial(self.modulus, new_coefs)
        
        if (isinstance(multiplicand, Polynomial)):
            if(self.modulus != multiplicand.modulus):
                print "Moduli of the products must match!"
                return None
            else: 
                # initialize the new coefficient list with zeroes
                # --> degree is the sum of the degrees of multiplicands (hence 
                # length is one greater)
                new_coefs= [0] * (self.deg()+ multiplicand.deg()+ 1)
                for i in range(0, len(self.coefs)):
                    for j in range(0, len(multiplicand.coefs)):
                        new_coefs[i + j] += (self.coefs[i] * multiplicand.coefs[j])
                return Polynomial(self.modulus, new_coefs)
            
        return None
                


    def __eq__(self, other):
        if isinstance(other, Polynomial):
            if self.modulus != other.modulus:
                return False
            if self.deg() != other.deg():
                return False
            # lengths are equal, test each coefficient
            for i in range(0, len(self.coefs)):
                if self.coefs[i] != other.coefs[i]:
                    return False
                
            return True
        return False
        
    """
    Reduces a given polynomial modulo the original
    """
    def __mod__(self, other):
        if not isinstance(other, Polynomial):
            return None
        if other.deg()< self.deg():
            return other
        
        factor= other.deg() - self.deg()
        cofs= [0]*(other.deg()+1)
        for i in range(0, other.deg()+1):
            if (i >= factor):
                cofs[i] = other.coefs[i] - (other.coefs[other.deg()] * self.coefs[i - factor])
            else :
                cofs[i] = other.coefs[i]
                
        return Polynomial(self.modulus, cofs)
        
    
        
        

    def __sub__(self, other):
        if not isinstance(other, Polynomial):
            return None
        if self.modulus != other.modulus:
            return None
        
        if len(self.coefs) < len(other.coefs):
            return minus_greater_known(self, other, self, other)
        else:
            return minus_greater_known(self, other, other, self)
        


    
def minus_greater_known(self, other, smaller, greater):
    # initialize new_coefs to have the length of the greater polynomial
    new_coefs= [0]*len(greater.coefs)
    # this is the same regardless of whether self is smaller than other or not
    for i in range(0, len(smaller.coefs)):
        new_coefs[i]= self.coefs[i] - other.coefs[i]
    
    # self is smaller case, remaining entries are negative
    if smaller == self:
        for i in range(len(smaller.coefs), len(greater.coefs)):
            new_coefs[i]= 0 - other.coefs[i]
    # self is greater case, remaining entries are positive
    else:
        for i in range(len(smaller.coefs), len(greater.coefs)):
            new_coefs[i]= self.coefs[i]

    return Polynomial(self.modulus, new_coefs)





