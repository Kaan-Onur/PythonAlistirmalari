#Soru2:Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

boy = float(input("Boy:"))
kilo = int(input("Kilo:"))

print("Beden Kitle İndeksi:",kilo / (boy ** 2))