#!/bin/python3

import math
import os
import random
import re
import sys


def pairs(k, arr): #fungsi pairs dengan argumen k dan arr
    
   
    count = 0 #bikin counter
    panjangarray = len(arr) #variabel panjangarray mengambil panjang dari arr
    for i in range (panjangarray): #iterasi i pada panjangarray
        for j in range(panjangarray): #kemudian  iterasi j pada panjangarray
            if ((arr[i]-arr[j]) == k ): #jika array indeks i dikurang dari array indeks j sama dengan k
                count += 1 #counternya akan bertambah 
                
            
    return count #mereturn nilai count 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
