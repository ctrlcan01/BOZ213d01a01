Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> """
... Tek / Çift Sayı Kontrol Programı
... Bu program, kullanıcının girdiği bir tam sayının tek mi yoksa çift mi olduğunu hesaplar.
... Sınıf ödevi/projesi için hazırlanmıştır.
... """
... 
... def ana_program():
...     print("--- Tek ve Çift Sayı Kontrolcüsüne Hoş Geldiniz ---")
...     
...     try:
...         # Kullanıcıdan veri alıyoruz
...         sayi = int(input("Lütfen kontrol etmek için bir tam sayı girin: "))
...         
...         # Sayının 2'ye bölümünden kalan 0 ise çifttir
...         if sayi % 2 == 0:
...             print(f"Sonuç: {sayi} bir ÇİFT sayıdır.")
...         else:
...             print(f"Sonuç: {sayi} bir TEK sayıdır.")
...             
...     except ValueError:
...         # Kullanıcı sayı yerine harf veya sembol girerse hata fırlatmasını önlüyoruz
...         print("Hata: Lütfen sadece geçerli bir tam sayı giriniz!")
... 
... # Programın doğrudan çalıştırıldığından emin oluyoruz
... if __name__ == "__main__":
