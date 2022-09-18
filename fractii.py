q=int(input('q='))
j=int(input('j='))
z=int(input('z='))
g=int(input('g='))
def adunare_fractii(a,b,c,d):
    return (((a*d)+(c*b))/(b*d))
def inmultire_fractii(a,b,c,d):
    return ((a*c)/(b*d))
print(adunare_fractii(q,j,z,g))
print(inmultire_fractii(q,j,z,g))