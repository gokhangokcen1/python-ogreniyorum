# cook your dish here
p = input()

günlük_masraf, pazar_masrafı = map(int, p.split())

toplam_masraf = 6 * günlük_masraf + pazar_masrafı

print(toplam_masraf)