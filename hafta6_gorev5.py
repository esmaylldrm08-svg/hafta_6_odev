# ============================================================================
# Hafta 6 Laboratuvarı - Görev 5: Adam Asmaca
# Öğrenci Adı Soyadı : Esma Yıldırım
# Öğrenci Numarası   : 20253004004
# Ders               : Python ile Programlama
# Tarih              : 31.10.2026
# Açıklama           : Belirlenen gizli kelimeyi harf tahminleriyle bulma oyunu.
#                      Denenen harfler bir karakter dizisinde biriktirilir.
#                      Geçersiz girişler ve tekrarlanan harfler 'continue' ile
#                      atlanır. Kelime bilinince 'break' ile çıkılır.
#                      6 hata dolduğunda 'while ... else' yapısıyla gizli kelime
#                      açıklanır. Türkçe i/ı dönüşümü kurallara uygun yapılmıştır.
# Kısıtlamalar       : Liste, sözlük ve fonksiyon (def) kullanılmamıştır.
# ============================================================================

# --- 1. GİRDİ VE BAŞLANGIÇ DEĞERLERİ ---
gizli_kelime = "KOŞUL"
tahminler = ""          # Denenen harflerin biriktirileceği karakter dizisi
hata_sayisi = 0
MAKS_HATA = 6

# --- 2. VE 3. TEKRAR, DOĞRULA VE İŞLE (WHILE ... ELSE DÖNGÜSÜ) ---
while hata_sayisi < MAKS_HATA:
    # Kelimenin mevcut görünümünü oluşturma (ör: K _ Ş U _)
    kelime_gorunumu = ""
    for harf in gizli_kelime:
        if harf in tahminler:
            kelime_gorunumu += harf + " "
        else:
            kelime_gorunumu += "_ "
    kelime_gorunumu = kelime_gorunumu.strip()

    # Mevcut durumu ve hata sayısını göster
    print(f"{kelime_gorunumu} (hata: {hata_sayisi}/{MAKS_HATA})")

    # Kullanıcıdan harf girişi alma
    girdi = input("Harf: ").strip()

    # DOĞRULA: Tek harf kontrolü
    if len(girdi) != 1 or not girdi.isalpha():
        print("→ Lütfen yalnızca tek bir harf giriniz.")
        continue

    # Türkçe büyük harf dönüşümü:
    # İpucu: Python'da "i".upper() İngilizce "I" verir; Türkçe "İ" için özel dönüşüm yapılır.
    if girdi == "i":
        harf = "İ"
    elif girdi == "ı":
        harf = "I"
    else:
        harf = girdi.upper()

    # DOĞRULA: Daha önce denenmiş mi kontrolü
    if harf in tahminler:
        print("→ Bu harfi zaten denediniz.")
        continue

    # İŞLE: Yeni harfi tahminler dizesine ekle
    tahminler += harf

    # Harf gizli kelimede yoksa hata sayısını artır
    if harf not in gizli_kelime:
        hata_sayisi += 1

    # Kelime tamamlandı mı kontrolü
    kelime_tamamlandi = True
    for h in gizli_kelime:
        if h not in tahminler:
            kelime_tamamlandi = False
            break

    # Kelime tamamlandıysa break ile çık
    if kelime_tamamlandi:
        son_gorunum = ""
        for h in gizli_kelime:
            son_gorunum += h + " "
        son_gorunum = son_gorunum.strip()
        print(f"{son_gorunum} (hata: {hata_sayisi}/{MAKS_HATA}) Kazandınız!")
        break

else:
    # 6 hata hakkı dolduğunda break çalışmadığı için while ... else bloğu devreye girer
    print(f"Hakkınız bitti! (hata: {hata_sayisi}/{MAKS_HATA}) Kaybettiniz! Gizli kelime: {gizli_kelime}")
