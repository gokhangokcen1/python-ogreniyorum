# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())
phoneBook = {}
result = []

for i in range(N):
    yeni_kayit = input().strip()
    if yeni_kayit:
        isim, numara = yeni_kayit.split()
        phoneBook[isim] = numara

while True:
    sorgu = input().strip()
    if sorgu:  
        if sorgu in phoneBook:
            result.append(f"{sorgu}={phoneBook[sorgu]}")
        else:
            result.append("Not found")
    else:
        break

for res in result:
    print(res)