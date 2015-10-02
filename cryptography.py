"""
cryptography.py
Author: Morgan Meliment
Credit: none

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
def repeatkey(mlen, klen):
    if len(mlen) == len(klen):
        return(klen)
    elif len(mlen) > len(klen):
        diff = int(len(mlen)) % int(len(klen))
        tiem = (int(len(mlen)) - diff) / int(len(klen))
        s = 0
        time = []
        while s < tiem:
            s += 1
            time.append(klen)
        return("".join(x for x in time) + klen[0:diff])
    elif len(mlen) < len(klen):
        return(klen[0:len(mlen)])

associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
start = input("Enter e to encrypt, d to decrypt, or q to quit: ")
if start != "e" and start != "d" and start != "q":
    print("Did not understand command, try again.")
elif start == "q":
    print("Goodbye!")
elif start == "e":
    emes = input("Message: ")
    key = input("Key: ")
    editkey = repeatkey(emes, key)
    encr = []
    isn = 0
    for q in emes:
        ind = associations.find(q)
        twoind = associations.find(editkey[isn])
        isn += 1
        newin = ind + twoind
        if newin > 84:
            newin = newin % 85
        encr.append(associations[newin])
    print("".join(x for x in encr))
elif start == "d":
    emes = input("Message: ")
    key = input("Key: ")
    editkey = repeatkey(emes, key)
    encr = []
    isn = 0
    for q in emes:
        ind = associations.find(q)
        twoind = associations.find(editkey[isn])
        isn += 1
        newin = ind - twoind
        if newin < 0:
            newin = newin + 85
        encr.append(associations[newin])
    print("".join(x for x in encr))
    
    
    
    
    
    
    
    
    
    

        
