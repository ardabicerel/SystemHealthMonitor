# 🖥️ System Health Monitor & Logger

[English](#english) | [Türkçe](#türkçe)

---

## English

### 🚀 Overview
A lightweight, Python-based real-time system monitoring tool. This project was developed to understand the core principles of cloud computing and system administration by dynamically tracking system resources (CPU, RAM, Disk).

### ✨ Features
- **Real-Time Monitoring:** Tracks CPU usage, RAM utilization, and Disk space in 10-second intervals.

- **Smart Error Handling:** Uses `try-except` blocks to ensure the script continues running even if specific drives (e.g., E:) are missing or file system errors occur.

- **Visual Alerts:** Provides visual feedback on the terminal using ANSI color codes for critical thresholds (80%+ CPU or 90%+ RAM).

- **Automatic Logging:** Saves all collected data with timestamps to `system_logs.txt` for historical analysis.

- **Professional Dashboard:** Utilizes `subprocess` to clear the terminal on each update for a clean UI experience.

### 🛠️ Installation & Usage
1. Clone the repository:
   ```bash
   git clone [https://github.com/ardabicerel/SystemHealthMonitor.git](https://github.com/ardabicerel/SystemHealthMonitor.git)
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python sistem_kontrol.py
   ```

## Türkçe

### 🚀 Genel Bakış
Python tabanlı, hafif ve gerçek zamanlı bir sistem izleme aracıdır. Bu proje, bulut bilişim ve sistem yönetimi prensiplerini anlamak amacıyla, sistem kaynaklarını (CPU, RAM, Disk) dinamik olarak takip etmek için geliştirilmiştir.

### ✨ Özellikler
- **Canlı İzleme:** CPU kullanımı, RAM doluluk oranı ve Disk alanlarını 10 saniyelik aralıklarla takip eder.
- 
- **Akıllı Hata Yönetimi:** try-except blokları kullanarak, belirli sürücüler (örn: E: sürücüsü) takılı olmasa bile programın çökmeden çalışmasını sağlar.

- **Görsel Uyarılar:** ANSI renk kodları ile kritik eşiklerde (%80+ CPU veya %90+ RAM) terminal üzerinde görsel uyarılar verir.

- **Otomatik Loglama:** Tüm verileri zaman damgasıyla birlikte system_logs.txt dosyasına kaydederek geçmişe dönük analiz imkanı sunar.

- **Profesyonel Arayüz:** subprocess kullanarak her güncellemede terminali temizler ve düzenli bir görünüm sağlar.

🛠️ Kurulum ve Kullanım
1. Depoyu klonlayın:
   ```bash
   git clone [https://github.com/ardabicerel/SystemHealthMonitor.git](https://github.com/ardabicerel/SystemHealthMonitor.git)
   ```
2. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```
3. Uygulamayı çalıştırın:
   ```bash
   python sistem_kontrol.py
   ```

## 📋 Technical Details / Teknik Detaylar
- **Language/Dil:** Python 3.x

- **Libraries/Kütüphaneler:** psutil, os, subprocess, time
