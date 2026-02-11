# ESP32 ve TM1637 ile MikroPython Tabanlı Dinamik Metin Kaydırma

Bu proje, **ESP32 (HW-069)** mikrodenetleyici üzerinde **MikroPython** çalışma zamanı kullanılarak, **TM1637** 7-segment sürücüsü ile dinamik metin kaydırma (scrolling text) işlemlerini gerçekleştirmektedir. Proje, kısıtlı donanım kaynaklarıyla okunabilir metin akışı sağlamak için özelleştirilmiş algoritmalar içerir.

## 🛠 Teknik Yaklaşım ve Araçlar

Geleneksel olarak ESP32 ekosisteminde C++ (Arduino) kullanımı yaygın olsa da, bu çalışmada **MikroPython** tercih edilmiştir. Bu seçimin teknik nedenleri:
* **Yorumlanabilir Kod:** Derleme sürecine ihtiyaç duymadan cihaz üzerinde doğrudan kod yürütme.
* **MicroPico Entegrasyonu:** VS Code üzerindeki **MicroPico** eklentisi aracılığıyla yerel bilgisayar ile donanım arasında kesintisiz UART iletişimi.

## 🔌 Donanım Yapılandırması

Sistem, iki hatlı seri haberleşme protokolü (CLK ve DIO) üzerinden çalışmaktadır. Bağlantı şeması aşağıdadır:

| TM1637 Pini | ESP32 GPIO | Açıklama |
| :--- | :--- | :--- |
| **VCC** | 3.3V / 5V | Güç Beslemesi |
| **GND** | G (GND) | Şasi / Toprak |
| **CLK** | GPIO 22 | Serial Clock Line |
| **DIO** | GPIO 21 | Serial Data I/O |



## 💻 Yazılım Mimarisi ve Algoritma

Proje, modüler bir yapı sunmak adına iki ana bileşenden oluşur:

### 1. Sürücü Katmanı (`tm1637.py`)
Donanım spesifikasyonlarını soyutlar ve segment haritalama (segment mapping) işlemlerini yönetir.

### 2. Uygulama Katmanı (`main.py`)
Metin kaydırma mekanizması şu teknik özelliklerle optimize edilmiştir:
* **Karakter İkamesi:** 7-segment ekranın fiziksel kısıtlamaları (örn. 'M' veya 'Ş' harfleri) nedeniyle; 'M' -> 'n', 'Ş' -> 'S' gibi görsel ikameler yapılarak okunabilirlik artırılmıştır.
* **Kaydırma Döngüsü:** `metni_kaydir` fonksiyonu, 4 haneli ekran tamponunu (buffer) `len(text) - 3` iterasyonla güncelleyerek dinamik bir akış sağlar.
* **Hata Yönetimi:** Tanımlanamayan karakterler için `try-except` blokları kullanılarak çalışma zamanı (runtime) stabilitesi korunmuştur.



## 🚀 Kurulum Adımları
1. `src/` klasöründeki `tm1637.py` kütüphanesini ESP32 içine yükleyin.
2. `main.py` dosyasını `MicroPico: Upload file to board` komutuyla karta gönderin.
3. Seri haberleşme araçlarını kurmak için: `pip install -r requirements.txt`

---
**Geliştirici:** [Adın Soyadın]  
**Kurum:** Yıldız Teknik Üniversitesi - Elektronik ve Haberleşme Mühendisliği
