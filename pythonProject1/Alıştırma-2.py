print("""***************************************

İş Bankası Atm sine hoşgeldiniz.

İşlemler;

1.Bakiye Sorgulama

2.Para Yatırma

3.Para Çekme

İptal etmek için 4 e basın.
""")

bakiye=1000

while True:
    işlem=input("İşlem Seçiniz:")

    if(işlem == "4"):
        print("Hoşçakalın. Yine bekleriz.")
        break
    elif (işlem == "1"):
        print("Bakiyeniz {} tl dir.".format(bakiye))
    elif(işlem=="2"):
        miktar = int(input("Miktar giriniz:"))
        bakiye+=miktar
    elif(işlem=="3"):
        miktar=int(input("Miktar Giriniz:"))
        if(bakiye-miktar<0):
            print("Böyle bir miktar çekemezsiniz...Yeterli Bakiyeniz bulunmuyor..")
            continue
        bakiye-=miktar
    else:
        print("Geçersiz İşlem.")

