from numpy import random
import time
import json
import sys

print("Oyun Hazırlanıyor...")
time.sleep(1)

file = open("C:\\Users\\ismet\\OneDrive\\Belgeler\\fast write\\kelime.txt", "r", encoding="utf-8").readlines()

while True:
    status = input("Kolay/Orta/Zor: ").lower() # Kolay => kolay
    number = input("Kaç kelimelik bir oyun istiyorsun: ")

    arr = []
    for x in range(int(number)):
        while True:
            word = random.choice(file).rstrip("\n")
            if status == "kolay" and len(word) < 11:
                arr.append(word)
                break
            elif status == "orta" and len(word) < 18:
                arr.append(word)
                break
            elif status == "zor" and len(word) > 9:
                arr.append(word)
                break
            elif status != "kolay" and status != "orta" and status != "zor":
                arr.append(word)
                break
        

    print("Oyun 3 saniye sonra başlıyor...", end=" ")
    for x in range(3,0,-1):
        sys.stdout.flush()
        print(f"\rOyun {x} saniye sonra başlıyor...", end=" ")
        time.sleep(1)
    print("")

    start = time.time()

    false = []
    right = 0
    keys = 0
    for world in arr:
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

    data_file = json.load(open("C:\\Users\\ismet\\OneDrive\\Belgeler\\fast write\\data.json", "r", encoding="utf-8"))
    data_file[f"{time.time()}"] = data

    with open("C:\\Users\\ismet\\OneDrive\\Belgeler\\fast write\\data.json", "w") as json_file:
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
        break
