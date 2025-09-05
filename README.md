# PTO
Phone Tracker Offline

Script ini berisi dua bagian:
1. _gps.py   → log lokasi GPS/Network secara otomatis, kirim via SMS trigger
2. track.py  → visualisasi log GPS dalam bentuk map HTML interaktif

---

## Persiapan

### 1. Install Termux & Python
```
pkg update && pkg upgrade
pkg install python
pkg install termux-api
```
#### Install juga apk Termux:API dan Termux:Boot untuk menjalankan script otomatis setelah smartphone boot

### 2. Install dependensi Python
```
pip install folium jinja2
```

> Catatan: _gps.py hanya membutuhkan modul standar Python. track.py membutuhkan folium & jinja2.

### 3. Izin Termux
```
termux-setup-storage
termux-location
termux-sms-send
termux-sms-list
```

---

## File _gps.py (Logger)

### Fitur
- Mencatat lokasi GPS/Network setiap 10 detik
- Menyimpan log di /sdcard/gps_log.json
- Mengirim log via SMS trigger:
  - "SENDLOG" → kirim ke nomor pengirim
  - "AXIS" + password → kirim ke nomor darurat

### Cara pakai
```
cd /sdcard
python _gps.py
```

- File log otomatis reset saat script dijalankan
- Script berjalan terus dan aman jika terjadi error (try-except loop)

---

## File track.py (Visualizer)

### Fitur
- Membaca log GPS dari gps_log.json
- Membuat map HTML interaktif:
  - Marker glow hijau untuk setiap entry
  - Polyline rute perjalanan
  - MiniMap & fullscreen control
  - Overlay kiri bawah menampilkan raw log

### Cara pakai
```
cd /sdcard
python track.py
```

- Output: gps_map.html
- Buka file HTML di browser untuk melihat peta dan overlay log

---

## Catatan Tambahan
- Data GPS dimasukkan ke /sdcard/gps_log.json pada device yang digunakan untuk tracking
- Untuk menyesuaikan frekuensi log, ubah `time.sleep(10)` di _gps.py
- Pastikan semua modul sudah terinstall agar track.py berjalan tanpa error
