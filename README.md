\# 🔋 Energy Monitoring IoT - MQTT to InfluxDB Ingestion Service



\## 📋 IDENTITAS

\- \*\*Nama\*\*: Melfariani Cahya Safitri

\- \*\*NIM\*\*: \[ISI NIM ANDA]

\- \*\*GitHub\*\*: \[@mrcs1735-lgtm](https://github.com/mrcs1735-lgtm)



\## 📌 DESKRIPSI PROYEK

Service ini berfungsi sebagai \*\*data ingestion\*\* untuk sistem monitoring energi. 

Menerima data dari sensor IoT melalui protokol MQTT dan menyimpannya ke InfluxDB 

(time-series database) untuk selanjutnya dianalisis dan divisualisasikan.



\## 🏗️ ARSITEKTUR SISTEM

```

\[Sensor Energi] → \[MQTT Broker] → \[Ingestion Service] → \[InfluxDB] → \[Dashboard]

&#x20;    (ESP32)      (CloudAMQP)         (Python)         (Cloud)      (Grafana)

```



\## 🔧 FITUR

\- ✅ Menerima data MQTT dari multiple device

\- ✅ Parsing JSON payload

\- ✅ Menyimpan ke InfluxDB dengan struktur yang optimal

\- ✅ Error handling dan logging

\- ✅ Environment variables untuk keamanan



\## 📊 FORMAT DATA YANG DITERIMA

```json

{

&#x20; "device\_id": "esp32\_001",

&#x20; "voltage": 220.5,

&#x20; "current": 1.2,

&#x20; "power": 264.6,

&#x20; "energy": 1250.75,

&#x20; "power\_factor": 0.95,

&#x20; "frequency": 50.0

}

```



\## 🔧 CI/CD PIPELINE

Pipeline otomatis dengan GitHub Actions:

1\. \*\*Trigger\*\*: Push ke branch `main`

2\. \*\*Test\*\*: Install dependencies dan cek koneksi

3\. \*\*Deploy\*\*: Auto-deploy ke Render via webhook



!\[Pipeline Status](https://github.com/mrcs1735-lgtm/energy-monitoring-ingestion/actions/workflows/ci-cd.yml/badge.svg)



\## ☁️ DEPLOYMENT

\- \*\*Platform\*\*: Render (Free Tier)

\- \*\*Status\*\*: ✅ Active

\- \*\*URL\*\*: \[https://energy-monitoring-ingestion.onrender.com](https://energy-monitoring-ingestion.onrender.com)



\## 🔐 KEAMANAN (Security Measures)

1\. ✅ \*\*Environment Variables\*\*: Semua credential disimpan di `.env`, tidak di hardcode

2\. ✅ \*\*.env.example disediakan\*\*: Template untuk konfigurasi

3\. ✅ \*\*Input Validation\*\*: Data divalidasi sebelum diproses

4\. ✅ \*\*Error Handling\*\*: Try-catch untuk mencegah crash



\## 📈 MONITORING

Service menampilkan log real-time:

\- Status koneksi MQTT

\- Data yang diterima

\- Status write ke InfluxDB

\- Error jika ada



\## 🚀 CARA MENJALANKAN



\### Prerequisites

```bash

Python 3.8+

pip install -r requirements.txt

```



\### Setup Environment

```bash

cp .env.example .env

\# Edit .env dengan credentials Anda

```



\### Run Lokal

```bash

python ingestion.py

```



\## 📁 STRUKTUR PROYEK

```

.

├── .github/

│   └── workflows/

│       └── ci-cd.yml          # Pipeline CI/CD

├── .env.example                 # Template environment

├── .gitignore                   # File yang diabaikan git

├── ingestion.py                 # Source code utama

├── requirements.txt             # Dependencies Python

└── README.md                    # Dokumentasi ini

```



\## 📸 SCREENSHOT

\*(Tambahkan screenshot di sini setelah deploy)\*



\## 📞 KONTAK

\- \*\*Email\*\*: mrcs1735@gmail.com

\- \*\*GitHub\*\*: \[@mrcs1735-lgtm](https://github.com/mrcs1735-lgtm)

