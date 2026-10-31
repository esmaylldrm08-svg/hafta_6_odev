# ============================================================================
# Hafta 6 Laboratuvarı - Görev 3: T.C. Kimlik Numarası Doğrulama
# Öğrenci Adı Soyadı : Esma Yıldırım
# Öğrenci Numarası   : 20253004004
# Ders               : Python ile Programlama
# Tarih              : 31.10.2026
# Açıklama           : Girilen T.C. kimlik numarasının 11 karakter, tamamı rakam
#                      ve ilk hanesinin 0 olmama biçim kurallarını denetler.
#                      Bir döngüyle tek ve çift hanelerin toplamını (T ve Ç)
#                      bularak h10 ve h11 kontrol hanelerini hesaplar ve doğrular.
# Kısıtlamalar       : Liste, sözlük ve fonksiyon (def) kullanılmamıştır.
# ============================================================================

# --- 1. GİRDİ ---
tc = input("T.C. kimlik no: ").strip()

# --- 2. DOĞRULA (BİÇİM DENETİMİ) ---
# Biçim kuralları: 11 karakter olmalı, hepsi rakam olmalı ve ilk hane 0 olmamalıdır
bicim_gecerli = (len(tc) == 11) and (tc.isdigit()) and (len(tc) > 0 and tc[0] != "0")

if not bicim_gecerli:
    print("→ GEÇERSİZ")
else:
    # --- 3. İŞLE ---
    # Döngü ile 1., 3., 5., 7., 9. hanelerin toplamı (T) ve
    # 2., 4., 6., 8. hanelerin toplamı (Ç) hesaplanır (0 tabanlı indeks: 0,2,4,6,8 ve 1,3,5,7)
    T = 0
    C = 0

    for i in range(9):
        rakam = int(tc[i])
        if i % 2 == 0:
            # 1., 3., 5., 7., 9. haneler (indeks 0, 2, 4, 6, 8)
            T += rakam
        else:
            # 2., 4., 6., 8. haneler (indeks 1, 3, 5, 7)
            C += rakam

    # Kontrol hanelerinin formülle hesaplanması:
    # h10 = (7T - Ç) mod 10
    # h11 = (T + Ç + h10) mod 10
    h10 = (7 * T - C) % 10
    h11 = (T + C + h10) % 10

    # Numarada bulunan gerçek 10. ve 11. haneler (indeks 9 ve 10)
    hane10 = int(tc[9])
    hane11 = int(tc[10])

    # --- 4. ÇIKTI ---
    if h10 == hane10 and h11 == hane11:
        print(f"Tek: {T} Çift: {C} 10. hane: {h10} 11. hane: {h11} → GEÇERLİ")
    else:
        print("→ GEÇERSİZ")
