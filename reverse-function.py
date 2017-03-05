def rev(s):
    x=''
    i=len(s)-1
    while i>=0:
        x = x + s[i]
        i=i-1
    return x
print(rev('paul'))
print(rev('luap'))