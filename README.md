# MicroPython-Based Dynamic Text Scrolling with ESP32 and TM1637

This project implements a dynamic text scrolling mechanism on an **ESP32 (HW-069)** microcontroller using **MicroPython**. It is specifically designed to handle character rendering and smooth scrolling animations on **TM1637**-driven 4-digit 7-segment displays, despite the hardware's inherent character limitations.

## 🛠 Technical Approach and Tools

While C++ (Arduino/ESP-IDF) is a common choice for ESP32, this project leverages **MicroPython** for several technical advantages:
* **Interpreted Execution:** Eliminates compilation overhead, allowing for rapid on-device prototyping and real-time debugging.
* **MicroPico Integration:** Utilizes the **MicroPico** extension in VS Code to establish a seamless UART bridge between the host development environment and the target hardware.

## 🔌 Hardware Configuration

The system operates via a two-wire serial communication protocol (CLK and DIO). The pin mapping is configured as follows:

| TM1637 Pin | ESP32 GPIO | Description |
| :--- | :--- | :--- |
| **VCC** | 3.3V / 5V | Power Supply |
| **GND** | G (GND) | Ground |
| **CLK** | GPIO 22 | Serial Clock Line |
| **DIO** | GPIO 21 | Serial Data I/O |



## 💻 Software Architecture and Algorithm

The project is structured into two modular components for maintainability:

### 1. Driver Layer (`tm1637.py`)
Abstracts the hardware specifications and manages the low-level segment mapping required to drive the LED segments.

### 2. Application Layer (`main.py`)
The text scrolling engine is optimized with the following technical features:
* **Character Substitution:** Due to the physical constraints of 7-segment displays (e.g., inability to render 'M' or 'W' properly), visual substitutions such as 'M' -> 'n' and 'S' -> '5' are implemented to maximize legibility.
* **Scrolling Loop:** The `metni_kaydir` (scroll_text) function updates the 4-digit display buffer through `len(text) - 3` iterations, ensuring a fluid visual flow.
* **Error Handling:** Robustness is maintained via `try-except` blocks to prevent runtime crashes when encountering unsupported characters.



## 🚀 Getting Started
1. Upload the `tm1637.py` library from the `src/` directory to your ESP32.
2. Deploy the `main.py` file using the `MicroPico: Upload file to board` command.
3. "Right-click on the `main.py` file and select 'Run current file to Pico` to execute the code.

---
**Developer:** İlker ALKAN - Yıldız Technical University Electronics and Communications Engineering





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
3. `main.py` dosyasına sağ tık yaparak `Run current file to Pico` seçeneğine tıklayarak kodu çalıştırın. 

---
**Geliştirici:** İlker ALKAN - Yıldız Teknik Üniversitesi Elektronik ve Haberleşme Mühendisliği
