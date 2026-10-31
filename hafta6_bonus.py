# ============================================================================
# Hafta 6 Laboratuvarı - Bonus Görev (+10 Puan): Luhn Algoritması
# Öğrenci Adı Soyadı : Esma Yıldırım
# Öğrenci Numarası   : 20253004004
# Ders               : Python ile Programlama
# Tarih              : 31.10.2026
# Açıklama           : Luhn algoritması kullanarak 15 haneli 453914880343646
#                      numarasının sonuna eklendiğinde numarayı geçerli kılan
#                      kontrol hanesini bulur. 0-9 arasındaki rakamları sırayla
#                      deneyerek ilk geçerli olanda break ile döngüden çıkar.
# Kısıtlamalar       : Liste, sözlük ve fonksiyon (def) kullanılmamıştır.
# ============================================================================

# --- 1. GİRDİ ---
numara_15 = "453914880343646"

print(f"15 haneli numara: {numara_15}")
print("Kontrol hanesi aranıyor (0-9 arası deneniyor)...")

# --- 2. VE 3. İŞLE VE DÖNGÜ (0-9 ARASI DENEME) ---
bulunan_kontrol_hanesi = -1

for kontrol in range(10):
    aday_16 = numara_15 + str(kontrol)
    toplam = 0

    # 16 haneli numarada sağdan sola Luhn kuralı:
    # 16 haneli olduğu için:
    # 0, 2, 4, 6, 8, 10, 12, 14 indeksleri (sağdan 16, 14, 12... çift sıralar) 2 ile çarpılır.
    # 1, 3, 5, 7, 9, 11, 13, 15 indeksleri (sağdan 15, 13, 11... tek sıralar) olduğu gibi eklenir.
    for i in range(16):
        rakam = int(aday_16[i])
        if i % 2 == 0:
            carpim = rakam * 2
            # Eğer çarpım 9'dan büyükse 9 çıkarılır (veya basamakları toplanır)
            toplam += (carpim - 9) if carpim > 9 else carpim
        else:
            toplam += rakam

    # Luhn geçerlilik şartı: Toplam 10'a tam bölünmelidir
    if toplam % 10 == 0:
        bulunan_kontrol_hanesi = kontrol
        # İlk geçerli olanda break ile çıkılır
        break

# --- 4. ÇIKTI ---
if bulunan_kontrol_hanesi != -1:
    print(f"Geçerli kontrol hanesi: {bulunan_kontrol_hanesi}")
    print(f"Tam geçerli 16 haneli numara: {numara_15 + str(bulunan_kontrol_hanesi)}")
else:
    print("Geçerli bir kontrol hanesi bulunamadı.")
