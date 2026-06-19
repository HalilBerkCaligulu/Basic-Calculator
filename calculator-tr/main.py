from colorama import Fore

gecmis = []


def toplama(a, b):
    return a + b


def cikarma(a, b):
    return a - b


def carpma(a, b):
    return a * b


def bolme(a, b):
    if b == 0:
        return "Sıfıra bölünemez!"
    return a / b


def hesapla():
    sayi1 = float(input(Fore.LIGHTGREEN_EX + "1. Sayı: "))
    sayi2 = float(input(Fore.LIGHTGREEN_EX + "2. Sayı: "))

    print(Fore.LIGHTCYAN_EX + """
1 - Toplama
2 - Çıkarma
3 - Çarpma
4 - Bölme""")

    islem = input(Fore.CYAN + "İşlem seç: ")

    if islem == "1":
        sonuc = toplama(sayi1, sayi2)
        sembol = "+"

    elif islem == "2":
        sonuc = cikarma(sayi1, sayi2)
        sembol = "-"

    elif islem == "3":
        sonuc = carpma(sayi1, sayi2)
        sembol = "*"

    elif islem == "4":
        sonuc = bolme(sayi1, sayi2)
        sembol = "/"

    else:
        print(Fore.RED + "Geçersiz işlem!")
        return

    print(Fore.MAGENTA + "Sonuç:", sonuc)

    kayit = f"{sayi1} {sembol} {sayi2} = {sonuc}"
    gecmis.append(kayit)


def gecmisi_goster():
    if len(gecmis) == 0:
        print("Henüz işlem yapılmadı.")
    else:
        print(Fore.YELLOW + "\n--- Geçmiş ---")
        for islem in gecmis:
            print(islem)


def ana_menu():
    while True:
        print( Fore.LIGHTCYAN_EX + """
====== HESAP MAKİNESİ ======

1 - Hesap yap
2 - Geçmişi göster
3 - Çıkış

""")

        secim = input("Seçim: ")

        if secim == "1":
            hesapla()

        elif secim == "2":
            gecmisi_goster()

        elif secim == "3":
            print("Program kapatılıyor...")
            break

        else:
            print("Hatalı seçim!")


ana_menu()