# ============================================================================
# Hafta 6 Laboratuvarı - Görev 2: Metin Analizörü
# Öğrenci Adı Soyadı : Esma Yıldırım
# Öğrenci Numarası   : 20253004004
# Ders               : Python ile Programlama
# Tarih              : 31.10.2026
# Açıklama           : Verilen cümleyi TEK BİR for döngüsü ile tarayarak harf,
#                      sesli harf, sessiz harf, rakam ve kelime sayısını bulur.
#                      Kelimeleri bayrak (flag) mantığıyla sayar.
#                      Cümlenin tersini yazdırır ve yalnızca harfleri küçük
#                      harfe dönüştürüp birleştirerek palindrom kontrolü yapar.
# Kısıtlamalar       : Liste, sözlük ve fonksiyon (def) kullanılmamıştır.
# ============================================================================

# --- 1. GİRDİ ---
cumle = input("Cümle: ")

# --- 2. DOĞRULA VE DEĞİŞKENLERİ BAŞLAT ---
# Sayaçlar
harf_sayisi = 0
sesli_sayisi = 0
sessiz_sayisi = 0
rakam_sayisi = 0
kelime_sayisi = 0

# Kelime sayımı için mantıksal bayrak (flag)
kelime_icinde = False

# Palindrom kontrolü için harfleri toplayacağımız karakter dizisi
harfler_kucuk = ""

# Ters cümle için toplayıcı karakter dizisi
ters_cumle = ""

# Sesli harfler kümesi (Büyük ve küçük harfler)
sesliler = "aeıioöuüAEIİOÖUÜ"

# --- 3. İŞLE (TEK BİR FOR DÖNGÜSÜ İLE) ---
for ch in cumle:
    # 1. Cümleyi tersten oluşturma
    ters_cumle = ch + ters_cumle

    # 2. Kelimeleri bayrak ile sayma:
    # Boşluk olmayan bir karaktere rastlandığında ve henüz kelime içinde değilsek
    # yeni bir kelime başlamıştır. Boşluk görüldüğünde bayrak indirilir.
    if ch != " " and not ch.isspace():
        if not kelime_icinde:
            kelime_sayisi += 1
            kelime_icinde = True
    else:
        kelime_icinde = False

    # 3. Harf, Sesli, Sessiz, Rakam tespiti ve Palindrom için harf biriktirme
    if ch.isalpha():
        harf_sayisi += 1
        if ch in sesliler:
            sesli_sayisi += 1
        else:
            sessiz_sayisi += 1

        # Türkçe karakter uyumlu küçük harfe dönüştürme
        if ch == "İ":
            harfler_kucuk += "i"
        elif ch == "I":
            harfler_kucuk += "ı"
        else:
            harfler_kucuk += ch.lower()

    elif ch.isdigit():
        rakam_sayisi += 1

# Palindrom kontrolü: Yalnızca harflerin küçük hâlinin tersi kendine eşit mi?
if len(harfler_kucuk) > 0 and harfler_kucuk == harfler_kucuk[::-1]:
    palindrom_sonuc = "Palindrom"
else:
    palindrom_sonuc = "Palindrom değil"

# --- 4. ÇIKTI ---
print(f"Harf: {harf_sayisi} Sesli: {sesli_sayisi} Sessiz: {sessiz_sayisi} Rakam: {rakam_sayisi} Kelime: {kelime_sayisi}")
print(f"Ters: {ters_cumle}")
print(palindrom_sonuc)
