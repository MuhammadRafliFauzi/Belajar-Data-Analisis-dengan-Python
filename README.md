
# Bike Sharing Dashboard

## Deskripsi Proyek
Ini adalah proyek analisis data untuk penyewaan sepeda menggunakan Dataset Bike Sharing. Proyek ini menampilkan dashboard sederhana yang dibangun menggunakan Streamlit. Dashboard ini berisi visualisasi tentang bagaimana cuaca, musim, dan hari dalam seminggu mempengaruhi penyewaan sepeda.

## Cara Menjalankan Dashboard

### 1. Menjalankan Secara Lokal
Ikuti langkah-langkah berikut untuk menjalankan dashboard secara lokal di komputer:

#### Prasyarat
Pastikan sudah memiliki **Python** dan **pip** yang sudah terinstal. Kemudian instal library yang diperlukan dengan menjalankan perintah berikut:

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
Jika ingin mencoba dashboard secara online tanpa menginstal apapun di komputer, dapat mengunjungi tautan berikut:

[**Dashboard Online**](https://2d3zctwjxbby3fhefvszvq.streamlit.app/)

Dashboard ini di-hosting menggunakan **Streamlit Cloud**, sehingga dapat langsung melihat visualisasi tanpa perlu melakukan setup lokal.

## Struktur Proyek
- `dashboard.py`: Script utama yang digunakan untuk menjalankan dashboard.
- `cleaned_day.csv`: Dataset harian penyewaan sepeda yang telah dibersihkan.
- `cleaned_hour.csv`: Dataset jam penyewaan sepeda yang telah dibersihkan.
- `Notebook_Proyek_Analisis_Data.ipynb`: File Google Collab untuk keperluan Data Wrangling, EDA dan Data Visualization
- `requirements.txt`: Daftar pustaka yang diperlukan untuk menjalankan aplikasi.
- `README.md`: Panduan cara menjalankan proyek ini.
- `url.txt`: Link akses dashboard secara cloud menggunakan stream app

## Informasi Pemilik
- **Nama**: Muhammad Rafli Fauzi
- **Email**: raplifauji@gmail.com
- **ID Dicoding**: raflifzi
