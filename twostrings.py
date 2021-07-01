#!/bin/python3
def twoStrings(s1, s2): #bikin variabel twoStrings dengan argumen s1 dan s2
 def common_start(sa, sb): #bikin fungsi common_start(dengan argumen sa dan sb)
    
    def _iter(): #bikin fungsi _iter
        for a, b in zip(sa, sb): #for loop a dan b pada zip(berindex sa dan sb)
            if a == b: #cek dan jika a sama dengan b 
                yield a 
            else:
                   return 

    return ''.join(_iter())


def temukan_substring(string):  #bikin fungsi temukan_substring(berargumen string)
    temp_array = [] #buat array kosong
    for i in range(0, len(string)): #for loop dari 0 , sampai panjang dari string
        for j in range(i, len(string)): #for loop dari i sampai panjang string
            temp_array.append(string[i:j+1]) #indeks kosong tsb diappend kepada string indeks dari i sampai j+1
    return set(temp_array) #mereturn set dari nilai temp_array
 
def cek_substring(string1, string2): #bikin fungsi pengecek substring
    for karakter in string1: #for loop karakter pada string1
        if karakter in string2: #dan cek jika karakter pada string2
            return True #return True
    return False #kemudian return False


if __name__ == '__main__': 
    n = input() #variabel untuk menginput
    n = int(n)*2 #kemudian jadikan input an tsb dengan menjadi 2 
    string_array = [] #bikin array kosong
    for i in range(n): #for loop i dalam range n 
        input_dari_string = input() #bikin variabel untuk menerima input bernama input dari string
        string_array.append(input_dari_string ) #append atau menambahan dari array string_array kepada variabel input_dari_string
        
    for i in range(0, n, 2): #for loop untuk  dari 0  sampai kemudian kelipatannya 2
        value = cek_substring(string_array[i], string_array[i+1]) #varaiabel value , cek_substring dari pada string array indeks ke i sampai string array indeks ke i+1
        if value == True: #jika value == TRUE
            print ("YES") #maka print YES
        else: #jika tida
            print ("NO") #MAKA PRINT NO
