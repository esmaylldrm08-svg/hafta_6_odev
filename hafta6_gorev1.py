# ============================================================================
# Hafta 6 Laboratuvarı - Görev 1: Üçgen Analizörü
# Öğrenci Adı Soyadı : Esma Yıldırım
# Öğrenci Numarası   : 20253004004
# Ders               : Python ile Programlama
# Tarih              : 31.10.2026
# Açıklama           : Kullanıcıdan alınan 3 kenar uzunluğunu doğrular,
#                      üçgen eşitsizliğini denetler, kenarlarına ve en büyük
#                      açısına göre sınıflandırır. Çevre, Heron formülüyle alan
#                      ve en büyük açıyı hesaplar.
# Kısıtlamalar       : Liste, sözlük ve fonksiyon (def) kullanılmamıştır.
# ============================================================================

import math

# --- 1. GİRDİ ---
# 3 kenar uzunluğu kullanıcıdan okunur.
# Tek satırda boşlukla girilme veya ayrı satırlarda girilme durumu desteklenir.
girdi_a = input("a: ").strip()

if " " in girdi_a:
    # Kullanıcı kenarları tek satırda boşlukla girdiyse (örn: 5 5 8)
    ilk_bosluk = girdi_a.find(" ")
    a = float(girdi_a[:ilk_bosluk])
    kalan = girdi_a[ilk_bosluk:].strip()
    ikinci_bosluk = kalan.find(" ")
    if ikinci_bosluk != -1:
        b = float(kalan[:ikinci_bosluk])
        c = float(kalan[ikinci_bosluk:].strip())
    else:
        b = float(kalan)
        c = float(input("c: "))
else:
    # Standart ayrı satırlarda giriş
    a = float(girdi_a)
    b = float(input("b: "))
    c = float(input("c: "))


# --- 2. DOĞRULA ---
# Kenarların pozitifliğini for döngüsü ve sayaç ile denetliyoruz (Liste kullanılmaz)
pozitif_mi = True
for i in range(3):
    kenar_degeri = a if i == 0 else (b if i == 1 else c)
    if kenar_degeri <= 0:
        pozitif_mi = False
        break

# Üçgen eşitsizliği: Her kenar diğer iki kenarın toplamından küçük olmalıdır
ucgen_esitsizligi = (a + b > c) and (a + c > b) and (b + c > a)

if not pozitif_mi:
    print("Uyarı: Kenar uzunlukları pozitif olmalıdır!")
elif not ucgen_esitsizligi:
    print("Uyarı: Girilen kenar uzunlukları üçgen eşitsizliğini sağlamıyor!")
else:
    # --- 3. İŞLE ---
    # Kenar türünün belirlenmesi (Eşkenar / İkizkenar / Çeşitkenar)
    if a == b == c:
        kenar_turu = "Eşkenar"
    elif a == b or b == c or a == c:
        kenar_turu = "İkizkenar"
    else:
        kenar_turu = "Çeşitkenar"

    # En uzun kenarın (a) ve diğer iki kenarın (b, c) belirlenmesi
    if a >= b and a >= c:
        en_uzun = a
        diger1 = b
        diger2 = c
    elif b >= a and b >= c:
        en_uzun = b
        diger1 = a
        diger2 = c
    else:
        en_uzun = c
        diger1 = a
        diger2 = b

    # Kosinüs teoremi ile en büyük açının bulunması:
    # cos(alpha) = (b^2 + c^2 - a^2) / (2 * b * c) (a en uzun kenar)
    cos_alfa = (diger1**2 + diger2**2 - en_uzun**2) / (2 * diger1 * diger2)

    # Kayan nokta hassasiyeti nedeniyle oluşabilecek değer aşımını [-1, 1] aralığına kırpıyoruz
    if cos_alfa > 1.0:
        cos_alfa = 1.0
    elif cos_alfa < -1.0:
        cos_alfa = -1.0

    aci_radyan = math.acos(cos_alfa)
    en_buyuk_aci = math.degrees(aci_radyan)

    # Açı türünün belirlenmesi: dik açı kontrolü math.isclose ile yapılmalıdır (== kullanılmaz)
    if math.isclose(en_buyuk_aci, 90.0):
        aci_turu = "Dik açılı"
    elif en_buyuk_aci > 90.0:
        aci_turu = "Geniş açılı"
    else:
        aci_turu = "Dar açılı"

    # Çevre ve Heron formülü ile alan hesabı:
    # u = (a + b + c) / 2
    # Alan = sqrt(u * (u - a) * (u - b) * (u - c))
    cevre = a + b + c
    u = cevre / 2
    alan = math.sqrt(u * (u - a) * (u - b) * (u - c))

    # --- 4. ÇIKTI ---
    print(f"Tür: {kenar_turu}, {aci_turu}")
    print(f"Çevre: {cevre:.2f} Alan: {alan:.2f} En büyük açı: {en_buyuk_aci:.2f}°")
