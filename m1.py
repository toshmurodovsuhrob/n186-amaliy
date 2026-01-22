import requests as rq

link = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/'

data = rq.get(link).json()

for i in range(len(data)):
    print(f"{i}. 1 {data[i]['CcyNm_UZ']} : {data[i]['Rate']} so'm")
son = int(input("Qaysi valyutani kormoqchisiz? "))

if 0 <= son <= len(data)-1:
    val = data[son]
    print("\nTANLANGAN VALYUTA")
    print(f"1 {val['CcyNm_UZ']} = {val['Rate']} so'm")
    print("1 >>> Somdan valyutaga")
    print("2 >>> Valyutadan somga")
    tanlov = int(input("Hisoblash turini tanlang (1 yoki 2)"))
    val = data[son]
    rate = float(val['Rate'])
    if tanlov == 1:
        som = float(input("Somni kiriting >>> "))
        natija = som / rate
        print(f"{som} som = {natija:.2f} {val['CcyNm_UZ']}")
    if tanlov == 2:
        summa = float(input(f"{val['CcyNm_UZ']} somni kiriting >>> "))
        natija = summa * rate
        print(f"{summa} {val['CcyNm_UZ']} = {natija:.2f} som")
    else:
        print("Notogri tanlov!!!")
else:
    print("Notogri raqam kiritildi!!!")