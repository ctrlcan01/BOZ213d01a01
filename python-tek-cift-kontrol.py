# Tek çift bulma kodu

devam = "1"

while devam == "1":
    sayi = int(input("Bir sayı girin: "))
    
    if sayi % 2 == 0:
        print(sayi, "çift sayıdır")
    else:
        print(sayi, "tek sayıdır")
        
    print("")
    devam = input("Devam etmek için 1, kapatmak için 0 yazıp Enter'a basın: ")
