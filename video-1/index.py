import time
from numpy import random

print("Oyun Başladı...")
time.sleep(1)

number = input("Kaç kelimelik bir oyun istiyorsun: ")

file = open("kelime.txt", "r", encoding="utf-8").readlines()

arr = []
for x in range(int(number)): 
    arr.append(random.choice(file))


start = time.time()

false = []
right = 0
keys = 0
for w in arr:
    world = w.rstrip("\n")
    inp = str(input(f"{world}:  "))
    keys = keys + len(world)
    if world != inp:
        false.append(world)
    else: 
        right = right+1

finish = time.time() - start

print("\nOyun Bitti!\n")
print(f"Doğru Sayısı: {right}  Yanlış Sayısı: {len(false)}\nToplam Kelime: {number}  Toplam Harf: {keys}\nGeçen Süre: {finish}  Saniyede Ortalama: {keys/finish}")

if len(false) > 0:
    time.sleep(3)
    fin = ", ".join(false)
    print(f"Yanlış Kelimeler: {fin}")
