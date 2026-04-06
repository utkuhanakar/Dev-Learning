"""
Python Vize Hazırlık Çalışma Dosyası
Bu dosya vize sınavında çıkması muhtemel tüm konuları örneklerle açıklar.
PEP8 standartlarına uygun yazılmıştır.
"""

# 1. Değişkenler, İfadeler ve Cümleler (Variables & Expressions)
x = 5  # Değişken ataması (Assignment statement)
y = 10 + x  # İfade (Expression)
print(f"y değeri: {y}")

# 2. Tür Dönüşümleri (Type Conversions)
sayi_str = "100"
sayi_int = int(sayi_str)
sayi_float = float(sayi_int)
print(f"Türler: {type(sayi_str)} -> {type(sayi_int)} -> {type(sayi_float)}")

# 3. Kullanıcı Girdisi (User Input)
# Not: interactive ortamlarda input() bekleyebilir.
# isim = input("Adınız nedir? ") 

# 4. Mantıksal Operatörler & Boolean (Logical Operators)
a = True
b = False
print(f"a AND b: {a and b}")
print(f"a OR b: {a or b}")
print(f"NOT a: {not a}")

# 5. Koşul İfadeleri & Mantıksal Dallanma (Conditionals)
yas = 20
if yas < 18:
    print("Reşit değil")
elif yas == 18:
    print("Yeni reşit")
else:
    print("Reşit")

# 6. Fonksiyonlar & Scope (Functions & Scope)
global_degisken = "Ben globalim"

def selamla(isim="Ziyaretçi"):
    """
    Basit bir selamlama fonksiyonu.
    docstring: Fonksiyonun amacını açıklar.
    """
    yerel_degisken = "Ben yerelim"
    return f"Merhaba {isim}! {yerel_degisken} ve {global_degisken}"

print(selamla("Kullanıcı"))

# 7. Birden Fazla Değer Döndürmek (Multiple Returns)
def koordinat_al():
    return 10, 20  # Tuple olarak döner

x_koor, y_koor = koordinat_al()
print(f"X: {x_koor}, Y: {y_koor}")

# 8. Belirli ve Belirsiz Sayıda Argümanlar (*args, **kwargs)
def toplama(*sayilar):
    """Belirsiz sayıda sayı alır (*args)"""
    toplam = 0
    for s in sayilar:
        toplam += s
    return toplam

print(f"Toplam (1,2,3,4): {toplama(1, 2, 3, 4)}")

def profil_yarat(**bilgiler):
    """İsimli belirsiz argümanlar (**kwargs)"""
    for anahtar, deger in bilgiler.items():
        print(f"{anahtar}: {deger}")

profil_yarat(ad="Ali", soyad="Yılmaz", bolum="Bilgisayar")

# 9. Lambda Fonksiyonları (Lambda)
kare_al = lambda n: n * n
print(f"5'in karesi: {kare_al(5)}")

# 10. Listeler & Liste Kavramı (Lists)
meyveler = ["elma", "armut", "muz"]
meyveler.append("çilek")
print(f"Liste: {meyveler}, Uzunluk: {len(meyveler)}")
print(f"Dilimleme (Slice): {meyveler[1:3]}")

# 11. Dictionaries (Sözlükler)
sozluk = {"anahtar": "deger", "hata": "error"}
print(f"Sözlük değeri: {sozluk.get('hata')}")

# 12. Döngüler (Loops: for, while)
print("For döngüsü:")
for i in range(3):
    print(f"Index: {i}")

# 13. Stringler (Strings)
metin = "  Python Öğreniyorum  "
print(f"Büyük: {metin.upper().strip()}")
print(f"Parçala: {metin.split()}")

# 14. Hata Ayıklama (Error Handling: try-except-raise)
try:
    # pay = int(input("Pay: "))
    pay = 10
    payda = 0
    if payda == 0:
        raise ValueError("Payda sıfır olamaz!") # Manuel hata fırlatma
    sonuc = pay / payda
except ZeroDivisionError:
    print("Sıfıra bölme hatası!")
except ValueError as e:
    print(f"Hata: {e}")
finally:
    print("İşlem tamamlandı (Hata olsa da olmasa da çalışır).")

# 15. Doctest Örneği (Doctest)
def topla(a, b):
    """
    İki sayıyı toplar.
    >>> topla(2, 3)
    5
    >>> topla(-1, 1)
    0
    """
    return a + b

# 16. None Tipi
bos_deger = None
if bos_deger is None:
    print("Bu değer boştur (None).")

# ARTİMLİ GELİŞTİRME (Incremental Development)
# Bu kodun parça parça test edilerek yazılmasıdır.

print("\n--- Hazırlık Tamam! ---")
