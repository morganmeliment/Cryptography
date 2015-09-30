"""
cryptography.py
Author: Morgan Meliment
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
def repeatkey(mlen, klen):
    if len(mlen) == len(klen):
        return(klen)
    elif len(mlen) > len(klen):
        diff = len(mlen) - 
    
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
start = input("Enter e to encrypt, d to decrypt, or q to quit: ")
if start != "e" and start != "d" and start != "q":
    print("Did not understand command, try again.")
elif start == "q":
    print("Goodbye!")
elif start == "e":
    emes = input("Message: ")
    key = input("Key: ")
    