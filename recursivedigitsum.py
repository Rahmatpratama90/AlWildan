#!/bin/python3

import math
import os
import random
import re
import sys



def superDigit(n, k): #bikin fungsi superDigit dengan argumen n dan k


    if(len(n) == 1):  #ketika panjang n sama dengan 1
        return n #return nilai n 
    else: #Jikai tidak 
        return superDigit( str((recDigit(n) * k)), k) #return superDigit(string dari recDigit(n) dikali dengan k )
    
def recDigit(n): #bikin fungsi recDigit dengan argumen n 
    if(n == "0"): #jika n sama dengan 0 
        return 0 #return nilai 0 
    return ( int(n) % 10 + recDigit(str(int(int(n)/10))) ) #kemudian return nilai int dari n modulo 10 + recDigit(n/10)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
