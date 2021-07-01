#!/bin/python3

import math
import os
import random
import re
import sys



def rotLeft(a, d): #bikin fungsi rotLeft ber argumen a dan d
    
    for i in range(d): #for loop i pada range d
        first_index = a[0] #buat variabel lokal firSt_index berisi a index ke 0
        a.append(first_index) #masukkan firts_index ke dalam list
        a.pop(0) #meremove indeks ke 0 pada arraynya
    return a #mereturn nilai a 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
   
