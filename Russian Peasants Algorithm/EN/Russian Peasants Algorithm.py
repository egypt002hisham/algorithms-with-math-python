def Russian_Peasants_Algorithm(a,b):
    x = a
    y = b
    z = 0
    t = 0
    while x > 0:
        if(x % 2 == 1) : z = y + z
        y = y << 1
        x = x >>1
        t +=1
        print(z)
    return z ,t

def binary(n,m):
    n = n >> 1 # n / 2
    m = m <<1 # m * 2
    return n ,m 

print(Russian_Peasants_Algorithm(20,7))

t,y = binary(20,7)
print(f"\n t>> {t} \n y<< {y}")