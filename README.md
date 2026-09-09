Broke Bookies Early Access Auto Submitter
Script Python otomatis untuk melakukan submit pendaftaran Early Access secara massal ke website Broke Bookies ([https://brokebookies.com/api/early-access](https://brokebookies.com/api/early-access)) menggunakan metode API Request langsung. Script ini dilengkapi dengan fitur pembacaan daftar EVM wallet, rotasi User-Agent, serta penanganan Rate Limit (429 Too Many Requests) secara otomatis.
📋 Fitur Utama
 * Tanpa Browser (Headless/API): Menggunakan pustaka requests sehingga proses jauh lebih cepat dan ringan dibanding menggunakan Selenium.
 * Multi-Wallet dari File: Membaca daftar alamat wallet langsung dari file eksternal evm.txt.
 * Rotasi User-Agent: Menggunakan variasi User-Agent secara acak dari file user-agent.txt.
 * Anti Rate-Limit: Dilengkapi jeda waktu acak (random delay) dan fitur jeda otomatis saat mendeteksi status 429 Too Many Requests.
🛠️ Persyaratan Sistem
 * Python 3.x sudah terinstal di komputer/perangkat Anda.
 * Pustaka Python requests.
🚀 Cara Instalasi & Penggunaan
1. Download/Buat Script
Buat file baru bernama brokebookies_bot.py dan salin kode script Python yang Anda miliki ke dalam file tersebut.
2. Install Dependencies
Buka terminal/command prompt di folder tempat file script Anda berada, lalu install pustaka yang dibutuhkan:
pip install requests

3. Siapkan File Pendukung (evm.txt & user-agent.txt)
Script ini memerlukan dua file teks pendukung di folder yang sama:
 * evm.txt: Berisi daftar alamat wallet EVM Anda (1 baris untuk 1 wallet).
 * user-agent.txt: Berisi daftar string User-Agent (bisa diisi beberapa baris untuk rotasi).
Contoh isi evm.txt:
0x1387ffb071dc2d160f1d1a92a8270ca8a1652a6f
0xb2dacc3fd4d98a79cb4b46f9aa0d0f9348a1b4e7
0x134db9e5d1b409c038f907da603666785927a03f

Contoh isi user-agent.txt:
Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36

4. Jalankan Script
Jika file-file di atas sudah disiapkan, jalankan bot melalui terminal dengan perintah:
python brokebookies_bot.py

📊 Indikator Status di Terminal
 * SUKSES (Status: 200): Wallet berhasil didaftarkan ke program Early Access.
 * GAGAL (Status: 429): Terkena pembatasan server karena terlalu cepat. Bot akan otomatis beristirahat selama 10 detik sebelum melanjutkan proses berikutnya.
⚠️ Catatan Penting
 * Jumlah Wallet yang Banyak (>1000): Jika Anda memproses ribuan wallet sekaligus, alamat IP internet Anda berpotensi terkena blokir sementara oleh sistem keamanan server (Cloudflare). Sangat disarankan menggunakan jaringan seluler (dengan mode pesawat dinyala-matikan untuk ganti IP) atau menggunakan tambahan Proxy jika diperlukan.
 * 
