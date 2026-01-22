import json

ism = input("Ismingizni kiriting: ")
familya = input("Familyangizni kiriting: ")
yosh = int(input("Yoshingizni kiriting: "))
manzil = input("Manzilingizni kiriting: ")
telefon = input("Telefon raqamingizni kiriting: ")

num = {
  "Ism": ism,
  "Familya": familya,
  "Yosh": yosh,
  "Manzil": manzil,
  "Telefon": telefon
}
with open("foydalanuvchi.json", "w") as f:
    json.dump(num, f,  indent=4)
