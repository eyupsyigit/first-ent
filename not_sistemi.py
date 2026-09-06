import random
import math
try:
    ogrenci_sayisi = int(input("Öğrenci sayısını giriniz: "))
    if ogrenci_sayisi<0:
        ogrenci_sayisi*-1==ogrenci_sayisi
    notlar = [] 
    


    for i in range(ogrenci_sayisi):
        notlar.append(random.randint(0, 100))  # bu satırda notlar listesini rastgele oluşturduk

    
    ort = sum(notlar) / len(notlar) #ogrenci_sayisi da len(notlar) yerine kullanılabilirdi

    toplam = 0 # 0 toplamada etkisiz eleman olduğu için 0 yazdık
    for n in notlar:
        toplam += (n - ort) ** 2  # standart sapmayı hesapladık

    ss = math.sqrt(toplam / ogrenci_sayisi) #math.sqrt kullanmak için en basta python matematik kütüphanesini(import math) kullandık
 
    print("Not ortalaması ve harf notu:")

   
    for x in notlar:
        if x >= ort + 1.5 * ss:
            harf = "A"
        elif x >= ort + 0.5 * ss:
            harf = "B"
        elif x >= ort - 0.5 * ss:
            harf = "C"
        elif x >= ort - 1.5 * ss:
            harf = "D"
        else:
            harf = "E"       # harf notunu hesapladık

        print("Not:", x, "→ Harf Notu:", harf)
    print("Not ortalaması:", ort)
    print("Standart Sapma:", ss)
except ValueError:
    print("geçerli tam sayı değeri giriniz")
except ZeroDivisionError:
    print("liste boş oldugu için ortalama hesaplanamadı")
