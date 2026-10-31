# ============================================================================
# Hafta 6 Laboratuvarı - Görev 4: Collatz Kaşifi
# Öğrenci Adı Soyadı : Esma Yıldırım
# Öğrenci Numarası   : 20253004004
# Ders               : Python ile Programlama
# Tarih              : 31.10.2026
# Açıklama           : (a) Girilen pozitif n sayısı için Collatz dizisinin 1'e
#                      ulaşana kadarki adım sayısını ve dizinin gördüğü en
#                      yüksek tepe değerini hesaplar.
#                      (b) Girilen bir üst sınıra kadar (1'den sınıra) iç içe
#                      döngüler kullanarak en uzun Collatz zincirini veren
#                      başlangıç sayısını ve adım sayısını tespit eder.
#                      Collatz kuralı koşullu ifade (ternary) ile tek satırda
#                      yazılmıştır.
# Kısıtlamalar       : Liste, sözlük ve fonksiyon (def) kullanılmamıştır.
# ============================================================================

# ==========================================
# (a) Tek Bir n Değeri İçin Collatz Analizi
# ==========================================

# --- 1. GİRDİ ---
n_girdi = input("n: ").strip()

# --- 2. DOĞRULA ---
if not n_girdi.isdigit() or int(n_girdi) <= 0:
    print("Hata: Pozitif bir tam sayı girilmelidir.")
else:
    n = int(n_girdi)
    adim_sayisi = 0
    en_yuksek_deger = n
    gecici_n = n

    # --- 3. İŞLE ---
    while gecici_n > 1:
        # Collatz kuralı koşullu ifade (ternary) ile tek satırda:
        gecici_n = gecici_n // 2 if gecici_n % 2 == 0 else 3 * gecici_n + 1
        adim_sayisi += 1

        if gecici_n > en_yuksek_deger:
            en_yuksek_deger = gecici_n

    # --- 4. ÇIKTI ---
    print(f"{n} → 1: {adim_sayisi} adım, en yüksek değer {en_yuksek_deger}")


# =========================================================
# (b) Üst Sınıra Kadar En Uzun Zinciri Veren Sayıyı Bulma
# =========================================================

# --- 1. GİRDİ ---
ust_sinir_girdi = input("Üst sınır: ").strip()

# --- 2. DOĞRULA ---
if not ust_sinir_girdi.isdigit() or int(ust_sinir_girdi) <= 0:
    print("Hata: Üst sınır pozitif bir tam sayı olmalıdır.")
else:
    ust_sinir = int(ust_sinir_girdi)

    en_uzun_zincir = 0
    en_iyi_baslangic = 1

    # --- 3. İŞLE (İÇ İÇE DÖNGÜLERLE) ---
    for baslangic in range(1, ust_sinir + 1):
        mevcut_sayi = baslangic
        mevcut_adim = 0

        while mevcut_sayi > 1:
            # Collatz kuralı koşullu ifade ile tek satırda:
            mevcut_sayi = mevcut_sayi // 2 if mevcut_sayi % 2 == 0 else 3 * mevcut_sayi + 1
            mevcut_adim += 1

        if mevcut_adim > en_uzun_zincir:
            en_uzun_zincir = mevcut_adim
            en_iyi_baslangic = baslangic

    # --- 4. ÇIKTI ---
    print(f"1–{ust_sinir} arasında en uzun zincir: {en_iyi_baslangic} ({en_uzun_zincir} adım)")
