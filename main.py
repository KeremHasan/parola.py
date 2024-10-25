import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

parolauzunlugu = int(input("Parola Uzunluğu giriniz:"))

parola = ""

for i in range(parolauzunlugu):
    parola = parola + random.choice(karakterler)
    
    
print("Parolanız:"+parola)
