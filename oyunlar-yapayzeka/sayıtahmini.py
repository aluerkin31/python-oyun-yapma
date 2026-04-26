import random

def oyun():
    sayi = random.randint(1, 50)
    print("--- BAŞARILI ELLER SAYI TAHMİN ---")
    print("1-50 arası bir sayı tuttum, bakalım bilecek misin?")
    
    tahmin = 0
    yolculuk = 0
    
    while tahmin != sayi:
        tahmin = int(input("Tahminin nedir kanka? "))
        yolculuk += 1
        if tahmin < sayi:
            print("Çık biraz daha!")
        elif tahmin > sayi:
            print("İn aşağı!")
            
    print(f"BUM! {yolculuk}. denemede bildin. Sen bu işi çözüyorsun Ali Erkin!")

oyun()
