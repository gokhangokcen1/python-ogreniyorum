# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())


result = []
for i in range(N):
    

    S = input()   
    word1 = ""
    word2 = ""
    for i in range(len(S)):
        if i % 2 == 0:
            word1 += S[i]
        else:
            word2 += S[i]
    else:
        result.append(word1+" "+word2)

print(*result, sep="\n")



