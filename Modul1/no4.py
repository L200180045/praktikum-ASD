print("\nNomer 4")
def rerata(p=[]):
    x=0
    n=0
    if p != []:
        for i in p:
            x+=i
            n+=1
        return x/n
z=rerata([1,2,3,4,5])
print(z)
