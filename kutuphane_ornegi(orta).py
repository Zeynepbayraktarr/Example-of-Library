import os
kitapListesi = list()

menu = """
[1] Kitap Ekle
[2] Kitap Al
[3] Tümünü Listele
[Q] Çıkış

"""
print(menu)
def kitapEkle(kitap:tuple,liste:list):
    liste.append(kitap)
    print("Ekleme İşlemi Tamamlnadı")
    print("Ana menuye dönmek için 'entar tuşuna basın' ")

#secim = input("İşleminizi Seçiniz :")



def kontrol(kitap:tuple,liste:list):
    if kitap in liste:
        return True
    else:
        return False

def kitapCikar(kitap:tuple,liste:list):
    if kontrol(kitap,liste):
        liste.remove(kitap)
        print("Kitap Çıkarma İşlemi Tamamlandı..")
        print("Ana menuye dönmek için 'enter tuşuna basın' ")
        input()

    else:
        print("Arattığınız kitap mevcut değildir...")
        print("Ana menuye dönmek için 'entar tuşuna basın' ")
        input()


def listele(liste:list):
    for i in liste:
        print("Kitap Adı: {} ---------   Yazar {}".format(i[0],i[1]))

    print("Ana menuye dönmek için 'enter tuşuna basın' ")
    input()

while True:
  # print(menu)
   os.system("cls")
   secim = input("İşleminizi Seçiniz :")

   if secim == "1":
       kitap_isim = input("Kitabın adı :")
       kitap_yazar = input("Kitabın yazarı : ")
       kitap = (kitap_isim,kitap_yazar)
       kitapEkle(kitap,kitapListesi)

   elif secim == "2":
       kitap_isim = input("Kitabın adı :")
       kitap_yazar = input("Kitabın yazarı : ")
       kitap = (kitap_isim, kitap_yazar)
       kitapCikar(kitap,kitapListesi)

   elif secim == "3":
       listele(kitapListesi)

   elif secim == "q" or secim == "Q":
       print("Keyifli Okumalar...")
       quit()

   else:
       print("Hatalı Giriş Yaptınız.")












