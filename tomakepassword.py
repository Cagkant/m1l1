import random
import time

a = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ4567890123"
kh = "abcdefghijklnopqrstuvwxyz"
bh = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smbl = "-/*!&$#?=@"
sy = "4567890123"
tm = random.randint(1,10)

print("Parola oluşturucu burada.")
b = int(input("Parolanın uzunluğunun ne kaç karakter olmasını istersin(en az 8)"))
hebelebe = input("Parolanız nasıl olsun? küçük harfler için 1, büyük harfle iiçin 2, semboller için 3, sayılar için 4, hepsi birden rasgele için 5 yaz.")
print("Parolanız oluşturuluyor. Birazcık bekleyin.")
time.sleep(tm)

parola = ""

if hebelebe == "1":
    for i in range(b):
        c = random.choice(kh)
        parola += c
    print(parola)
elif hebelebe == "2":
    for i in range(b):
        c = random.choice(bh)
        parola += c
    print(parola)
elif hebelebe == "3":
    for i in range(b):
        c = random.choice(smbl)
        parola += c
    print(parola)
elif hebelebe == "4":
    for i in range(b):
        c = random.choice(sy)
        parola += c
    print(parola)
elif hebelebe == "5":
    for i in range(b):
        c = random.choice(a)
        parola += c
    print(parola)
