import random
import sys
import getopt

weyl=13091206342165455529 #constant for PRNG
weyl_init=0
plaintext=input("Enter the message to encipher \n")
plaintext_arr=[]
ciphertext_arr=[]
for char in plaintext:
    plaintext_arr.append(ord(char))
print("The plain text is ")
print(plaintext_arr)
number=int(input("Enter a five digit integer key \n"))
seed_number=number
counter=0
def polynomial(number):
    return number**3-3*number+57
for i in range(0, len(plaintext_arr)):
    weyl_init=weyl_init+weyl
    number=(polynomial(number)+weyl_init) % 100000
    ciphertext_arr.append(plaintext_arr[i] ^ number)
print("The ciphertext array is ")
print(ciphertext_arr)

    
    
