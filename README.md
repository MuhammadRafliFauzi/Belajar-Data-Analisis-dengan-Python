
# Bike Sharing Dashboard

## Deskripsi Proyek
Ini adalah proyek analisis data untuk penyewaan sepeda menggunakan dataset Bike Sharing. Proyek ini menampilkan dashboard interaktif yang dibangun menggunakan Streamlit, dengan visualisasi tentang bagaimana cuaca, musim, dan hari dalam seminggu mempengaruhi penyewaan sepeda.

## Cara Menjalankan Dashboard

### 1. Menjalankan Secara Lokal
Ikuti langkah-langkah berikut untuk menjalankan dashboard secara lokal di komputer Anda:

#### Prasyarat
Pastikan Anda memiliki **Python** dan **pip** terinstal di sistem Anda. Kemudian instal pustaka yang diperlukan dengan menjalankan perintah berikut:

```bash
pip install -r requirements.txt
```

#### Langkah-langkah
1. Clone repository ini:
   ```bash
   git clone https://github.com/MuhammadRafliFauzi/Belajar-Data-Analisis-dengan-Python
   ```
2. Masuk ke direktori proyek:
   ```bash
   cd Belajar-Data-Analisis-dengan-Python/dashboard
   ```
3. Unduh file yang tersedia mulai dari file python dan dataset berupa file.csv yang telah bersih, jangan lupa untuk menyesuaikan kode program dan pathnya.
4. Jalankan aplikasi Streamlit pada terminal:
   ```bash
   streamlit run dashboard.py
   ```

### 2. Menjalankan di Streamlit Cloud
Jika Anda ingin mencoba dashboard secara online tanpa menginstal apapun di komputer Anda, Anda dapat mengunjungi tautan berikut:

[**Dashboard Online**](https://2d3zctwjxbby3fhefvszvq.streamlit.app/)

Dashboard ini di-hosting menggunakan **Streamlit Cloud**, sehingga Anda dapat langsung melihat visualisasi tanpa perlu melakukan setup lokal.

## Struktur Proyek
- `dashboard.py`: Script utama yang digunakan untuk menjalankan dashboard.
- `cleaned_day.csv`: Dataset harian penyewaan sepeda yang telah dibersihkan.
- `cleaned_hour.csv`: Dataset jam penyewaan sepeda yang telah dibersihkan.
- 'Notebook_Proyek_Analisis_Data.ipynb': File Google Collab untuk keperluan Data Wrangling, EDA dan Data Visualization
- `requirements.txt`: Daftar pustaka yang diperlukan untuk menjalankan aplikasi.
- `README.md`: Panduan cara menjalankan proyek ini.
- 'url.txt': Link akses dashboard secara cloud menggunakan stream app

## Informasi Kontak
- **Nama**: Muhammad Rafli Fauzi
- **Email**: raplifauji@gmail.com
- **ID Dicoding**: raflifzi
