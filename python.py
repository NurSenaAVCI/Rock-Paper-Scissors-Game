import random

xskor = 0
yskor = 0

while xskor <=2 and yskor <=2:

    x = input('tas mi, kagit mi, makas mi? = ')
    y = random.choice(('tas', 'kagit', 'makas'))

    if x !="tas" and x !="kagit" and x !="makas":
        print('Lütfen geçerli bir değer giriniz.')
        i -= 1
    elif x==y:
        print("Kazanan yok.")
    elif x=="tas" and y=="kagit":
        yskor +=1
        print("Bilgisayar kazandı.")
    elif x=="tas" and y=="makas":
        xskor += 1
        print("Sen kazandın.")
    elif x=="kagit" and y=="tas":
        xskor += 1
        print("Sen kazandın.")
    elif x=="kagit" and y=="makas":
        yskor += 1
        print("Bilgisayar kazandı.")
    elif x=="makas" and y=="tas":
        yskor += 1
        print("Bilgisayar kazandı.")
    elif x=="makas" and y=="kagıt":
        xskor += 1
        print("Sen kazandın.")

print(f'Oyun bitti. x = {xskor} y = {yskor}')


