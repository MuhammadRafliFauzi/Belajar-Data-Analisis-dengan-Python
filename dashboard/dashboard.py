import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
day_df_clean = pd.read_csv('dashboard/cleaned_day.csv')
#hour_df_clean = pd.read_csv('cleaned_hour.csv')

# Dashboard Title
st.title("Dashboard Analisis Bike Sharing")
st.markdown("**Proyek Analisis Data**: Bike Sharing Dataset")
st.markdown("**Dibuat oleh**: Muhammad Rafli Fauzi")
st.markdown("**Email**: raplifauji@gmail.com | **ID Dicoding**: raflifzi")

# Sidebar untuk navigasi
st.sidebar.title("Navigasi")
section = st.sidebar.radio("Pilih Analisis", ("Pertanyaan 1", "Pertanyaan 2", "Pertanyaan 3"))

# Pertanyaan 1: Bagaimana kondisi cuaca mempengaruhi penyewaan sepeda?
if section == "Pertanyaan 1":
    st.header("Bagaimana kondisi cuaca semisal suhu, kelembapan dan kecepatan angin dapat memengaruhi penyewaan sepeda?")
    
    # Menghitung korelasi
    corr = day_df_clean[['temp', 'hum', 'windspeed', 'cnt']].corr()
    
    # Plot heatmap korelasi
    st.subheader("Matriks Korelasi")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)
    
    st.markdown("""
    **Kesimpulan**:
    1. Suhu memiliki hubungan positif dengan jumlah penyewaan yang menandakan ketika suhu meningkat, jumlah penyewaan sepeda juga cenderung meningkat. 
    2. Kelembapan memiliki hubungan negatif dengan penyewaan sepeda yang menandakan ketika kelembapan meningkat, jumlah penyewaan cenderung sedikit menurun.
    3. Kecepatan angin memiliki hubungan negatif dengan penyewaan sepeda yang menandakan ketika kecepatan angin meningkat, penyewaan sepeda cenderung lebih menurun.
    """)

# Pertanyaan 2: Bagaimana tren penyewaan sepeda di berbagai musim?
elif section == "Pertanyaan 2":
    st.header("Bagaimana tren penyewaan sepeda di berbagai musim?")
    
    # Mapping nama musim
    season_mapping = {1: 'Musim Semi', 2: 'Musim Panas', 3: 'Musim Gugur', 4: 'Musim Dingin'}
    day_df_clean['season_name'] = day_df_clean['season'].map(season_mapping)
    
    # Menghitung rata-rata penyewaan per musim
    season_counts = day_df_clean.groupby('season_name')['cnt'].mean().reset_index()
    
    # Plot bar chart
    st.subheader("Rata-rata Penyewaan per Musim")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(data=season_counts, x='season_name', y='cnt', hue='season_name', palette='viridis', ax=ax, legend=False)
    ax.set_xlabel('Musim')
    ax.set_ylabel('Jumlah Penyewaan Rata-rata')
    st.pyplot(fig)
    
    st.markdown("""
    **Kesimpulan**:
    1. Musim gugur menunjukkan rata-rata penyewaan sepeda tertinggi dibandingkan dengan musim lainnya.
    2. Musim panas dan musim dingin memiliki rata-rata penyewaan yang cukup baik, meskipun musim panas lebih tinggi dibanding musim dingin.
    3. Musim semi menunjukkan rata-rata penyewaan terendah dibandingkan musim lainnya.
    """)

# Pertanyaan 3: Bagaimana intensitas penyewaan dari Senin hingga Minggu?
else:
    st.header("Bagaimana intensitas penyewaan sepeda dari Hari Senin hingga Hari Minggu?")
    
    # Mapping nama hari
    weekday_mapping = {0: 'Minggu', 1: 'Senin', 2: 'Selasa', 3: 'Rabu', 4: 'Kamis', 5: 'Jumat', 6: 'Sabtu'}
    day_df_clean['weekday_name'] = day_df_clean['weekday'].map(weekday_mapping)
    
    # Mengurutkan hari sesuai urutan minggu
    order = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
    weekday_counts = day_df_clean.groupby('weekday_name')['cnt'].mean().reset_index()
    weekday_counts['weekday_name'] = pd.Categorical(weekday_counts['weekday_name'], categories=order, ordered=True)
    weekday_counts = weekday_counts.sort_values('weekday_name')
    
    # Plot line chart
    st.subheader("Rata-rata Penyewaan per Hari")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=weekday_counts, x='weekday_name', y='cnt', marker='o', ax=ax)
    ax.set_xlabel('Hari')
    ax.set_ylabel('Jumlah Penyewaan Rata-rata')
    st.pyplot(fig)
    
    st.markdown("""
    **Kesimpulan**:
    1. Grafik tersebut menunjukan intensitas menunjukkan bahwa penyewaan sepeda lebih tinggi selama hari kerja, dengan puncaknya pada Kamis dan Jumat, 
       sedangkan akhir pekan yaitu Sabtu dan khususnya Minggu mengalami penurunan drastis.
    """)
