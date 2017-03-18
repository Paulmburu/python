#Write a python program that encrypts and decrypts any string it is given using the reverse cipher.

def rev(s):
    x=''
    i=len(s)-1
    while i>=0:
        x = x + s[i]
        i=i-1
    return x
print(rev('paul'))
print(rev('luap'))