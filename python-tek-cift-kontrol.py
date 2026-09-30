"""
Tek / Çift Sayı Kontrol Programı
Bu program, kullanıcının girdiği bir tam sayının tek mi yoksa çift mi olduğunu hesaplar.
Sınıf ödevi/projesi için hazırlanmıştır.
"""

def ana_program():
    print("--- Tek ve Çift Sayı Kontrolcüsüne Hoş Geldiniz ---")
    
    try:
        # Kullanıcıdan veri alıyoruz
        sayi = int(input("Lütfen kontrol etmek için bir tam sayı girin: "))
        
        # Sayının 2'ye bölümünden kalan 0 ise çifttir
        if sayi % 2 == 0:
            print(f"Sonuç: {sayi} bir ÇİFT sayıdır.")
        else:
            print(f"Sonuç: {sayi} bir TEK sayıdır.")
            
    except ValueError:
        # Kullanıcı sayı yerine harf veya sembol girerse hata fırlatmasını önlüyoruz
        print("Hata: Lütfen sadece geçerli bir tam sayı giriniz!")
        
    # EKRANIN KAPANMASINI ENGELLEYEN KISIM:
    input("\nÇıkmak için Enter tuşuna basın...")

# Programın doğrudan çalıştırıldığından emin oluyoruz
if __name__ == "__main__":
    ana_program()
