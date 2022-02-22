print("""
*********************************
Kullanıcı Girişi Programı
*********************************
""")

sys_kullanıcı_adı="Kaan4892"
sys_parola="12345"
giris_hakki=3

while True:
    kullanıcı_adı = input("Kullanıcı Adı:")
    parola = input("Parola:")
    if(kullanıcı_adı != sys_kullanıcı_adı and parola==sys_parola):
        print("Kullanıcı Adı Hatalı...")
        giris_hakki -= 1
    elif(kullanıcı_adı == sys_kullanıcı_adı and parola!=sys_parola):
        print("Parola Hatalı....")
        giris_hakki-=1
    elif(kullanıcı_adı != sys_kullanıcı_adı and parola!=sys_parola):
        print("Kullanıcı Adı ve Parola Hatalı.")
        giris_hakki -=1
    else:
        print("Sisteme başarıyla giriş yaptınız.")
        break
    if(giris_hakki==0):
        print("Giriş hakkınız kalmadı.")
        break
