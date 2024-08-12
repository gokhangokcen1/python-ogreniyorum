#!/bin/python3

S = input().strip()

try:
    i = int(S)
    print(i)
except ValueError:
    print("Bad String")


# direkt olarak try except blogunu yazdigimizda hata veriyor.
# Bu yuzden if __name__ == '__main__': satirini sildim
# silmisken kullanmadigimiz importlari da sildim