from machine import Pin
import tm1637
import time

# Bağlantıların: CLK -> D22, DIO -> D21 (G -> GND, VCC -> 3V3)
tm = tm1637.TM1637(clk=Pin(22), dio=Pin(21))
tm.brightness(3)

# 'M' harfi yerine 'n' kullanmak bazen daha okunaklı olur.
# 'Ş' yerine 'S', 'Ğ' yerine 'G', 'İ' yerine 'i'
# Mesajın başına ve sonuna boşluk ekledik ki yazı ekrana girip çıksın.
mesaj = "    message    "

def metni_kaydir(text, gecikme=0.35):
    # Yazıyı karakter karakter kaydıran döngü
    for i in range(len(text) - 3):
        gosterilecek = text[i:i+4]
        try:
            tm.show(gosterilecek)
        except:
            # Eğer kütüphane bir karakteri tanımazsa hata vermemesi için
            pass
        time.sleep(gecikme)

print("Mesajı Başlatılıyor...")

# Eski "HELL" kodunu temizlemek için ekranı bir kez söndür
tm.write([0, 0, 0, 0])
time.sleep(0.5)

while True:

    metni_kaydir(mesaj)
