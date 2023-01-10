import json

with open("C:\\Users\\ismet\\OneDrive\\Belgeler\\fast write\\data.json") as f:
  datas = json.load(f)

for data in datas:
  x = datas[str(data)]

  print("Doğru Sayısı: {}  Yanlış Sayısı: {}  Toplam Kelime: {}  Toplam Harf {}  Süre: {}  Saniyede Ortalama: {}".format(x["true"], x["false"], x["total_word"], x["total_key"], x["time"], x["time_ort"]))

while True:
  pass
