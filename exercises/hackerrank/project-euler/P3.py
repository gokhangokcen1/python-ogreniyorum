from math import sqrt 

def asallik_testi(N): 
    for i in range(2, int(sqrt(N))): 
        if N % i == 0: 
            return False 
    return True 

def asal_bolenler(x): 
    asal_sayilar = [] 
    for i in range(2, int(sqrt(x))): 
        if x % i == 0: 
            if asallik_testi(i): 
                asal_sayilar.append(i) 
            if asallik_testi(x//i): 
                asal_sayilar.append(i) 
    print(max(asal_sayilar)) 

asal_bolenler(600851475143)