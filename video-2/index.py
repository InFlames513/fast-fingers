import time
from numpy import random
import json

print("Oyun Başlıyor...")
time.sleep(1)

file = open("kelime.txt", "r", encoding="utf-8").readlines()

ret = True
while ret:
    number = input("Kaç kelimelik bir oyun istiyorsun: ")

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

    finish = int(time.time() - start)

    data = {
        "true": right,
        "false": len(false),
        "total_word": number,
        "total_key": keys,
        "time": finish,
        "time_ort": keys/finish
    }

    data_file = json.load(open("data.json", "r", encoding="utf-8"))
    data_file[f"{time.time()}"] = data

    with open("data.json", "w") as json_file:
        json.dump(data_file, json_file)

    print("\nOyun Bitti!\n")
    print(f"Doğru Sayısı: {right}  Yanlış Sayısı: {len(false)}\nToplam Kelime: {number}  Toplam Harf: {keys}\nGeçen Süre: {finish}  Saniyede Ortalama: {keys/finish}")

    if len(false) > 0:
        time.sleep(3)
        fin = ", ".join(false)
        print(f"Yanlış Kelimeler: {fin}")

    reply = input("Tekrar oynamak ister misin: ")
    if reply.lower() == "evet":
        pass
    else:
        ret = False
