'''
@author: KHarashima25
Created on Nov 2, 2022
Last Edited on Nov 2, 2022
Bugs:
'''

def get_factorial(n):
    '''
    Description - Function multiples a whole number by all whole numbers below it until 0
    Takes - variable n - determines what number to get factorial of
    Returns - returns the factorial
    '''
    if n > 0:return(n * get_factorial(n-1))                     #setting up the conditions when n is greater than 0 -- the algorithm given in the spec to determine the factorial of a number
    elif n == 0:return(1)                                       #the answer will always be 1 if n =0
                             
def get_summation(n):
    '''
    Description - Function adds a whole number to all whole numbers below it until 0
    Takes - variable n - determines what number to get the summation of
    Returns - returns the summation
    '''
    if n > 0:return(n + get_summation(n-1))                     #setting up the condition when n is greater than 0 -- return the algorithm that was given to us in the spec
    elif n== 0:return(0)                                        #the answer will always be 0 when n =0

def get_powers(a,n):                                            #importing the two variables, a and n
    '''
    Description - Takes exponent and initial number and outputs the number to the ___ power
    Takes - variable a - the exponent that the number is multiplied by - variable n - the initial number
    Returns - returns the result
    '''
    if n > 0:return(a * get_powers(a,n-1))                      #setting up the condition that n is greater than 0 -- return algorithm given by the spec 
    elif n == 0:return(1)                                       #the answer for n=0 will always be 1 

def get_square_root(n,p,e):                                     ## import n, return number
    '''
    Description -
    Takes -
    Returns -
    '''
    if abs((e*e)-n) < p: return(e)                              # condition 1
    else: return(get_square_root(n,p,((e+n)/e)/2))              # condition 2
     
def get_product_of_2_whole_numbers(a,b):                        ## import a,b, return number
    '''
    Description -
    Takes -
    Returns -
    '''
    if b > 0: return(a + get_product_of_2_whole_numbers(a,b-1)) # condition 1
    elif b == 0:return(0)                                       # condition 2 (0)

def get_fibonacci(n):                                           ## import n, return number
    if n == 0: return(0)                                        # condition 1 (0)
    elif n == 1: return(1)                                      # condition 2 (1)
    elif n > 1: return(get_fibonacci(n-1) + get_fibonacci(n-2)) # condition 3

def get_sum_of_numbers_digits(n):
    if n < 10: return(n)                                        # condition 1
    else: return(get_sum_of_numbers_digits(int(n/10)) + n%10)   # condition 2