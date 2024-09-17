N = int(input())
L1 = list(map(int, input().split()))
c1 =  c2 = 0
for i in L1:
    if i% 2 == 0 : c1+=1 
    else: c2+=1 
if c1 > c2:
    print('READY FOR BATTLE')
else:
    print("NOT READY")