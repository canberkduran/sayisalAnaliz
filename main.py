import math

def faktoriyel(n):
    if n ==0:
        return 1
    else:
        sonuc =1
        for i in range(1,n+1):
            sonuc *= i
        return sonuc

def taylorHesapla(x, y):
    toplam =0
    for i in range(y):
        taylor =((-1) ** i) * (x ** (2 * i)) / faktoriyel(2*i)
        toplam +=taylor
    return toplam

x = math.pi /5
y= 3
cosTaylor =taylorHesapla(x,y)
print(f"cosx in pi/5 noktasındaki 3 terimli taylor serisi:{cosTaylor}")
