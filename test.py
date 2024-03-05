import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

all_data = pd.read_csv("main_data.csv")
all_data['season_day'] = all_data['season_day'].replace({1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'})
all_data['yr_day'] = all_data['yr_day'].replace({0: 2011, 1: 2012})
all_data['weathersit_day'] = all_data['weathersit_day'].replace({1: 'Clear', 2: 'Misty', 3: 'Light Rain / Snow', 4: 'Heavy Rain'})
all_data['workingday_day'] = all_data['workingday_day'].replace({0: False, 1: True})

all_data['season_hour'] = all_data['season_hour'].replace({1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'})
all_data['yr_hour'] = all_data['yr_hour'].replace({0: 2011, 1: 2012})
all_data['weathersit_hour'] = all_data['weathersit_hour'].replace({1: 'Clear', 2: 'Misty', 3: 'Light Rain / Snow', 4: 'Heavy Rain'})
all_data['workingday_hour'] = all_data['workingday_hour'].replace({0: False, 1: True})

st.header('Bike Sharing Datasets Dashboard :sparkles:')
st.header('By Rama Aulia Gemilang')
selected_page = st.sidebar.selectbox("Pilih Opsi Visualisasi", ["Persebaran Banyaknya Penyewaan Sepeda per Bulan", "Pengaruh Musim terhadap Penyewaan Sepeda", "Penyewaan Sepeda di Setiap Cuaca", "Rata-rata Penyewaan Sepeda Setiap Jam"])
if selected_page == "Persebaran Banyaknya Penyewaan Sepeda per Bulan":
    # Visualisasi pertama
    st.subheader("Persebaran Banyaknya Penyewaan Sepeda per Bulan")
    total_rentals_per_month = all_data.groupby('mnth_hour')['cnt_hour'].sum()

    max_month = total_rentals_per_month.idxmax()
    min_month = total_rentals_per_month.idxmin()
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"Total Penyewaan Terbanyak di Bulan ke-{max_month}")
        st.write(f"Total: {total_rentals_per_month[max_month]}")
    with col2:
        st.markdown(f"Total Penyewaan Tersedikit di Bulan ke-{min_month}")
        st.write(f"Total: {total_rentals_per_month[min_month]}")
        
    sns.lineplot(x='mnth_hour', y='cnt_hour', color="maroon", marker="o", data=all_data)
    plt.xticks(range(1, 13))
    plt.title('Persebaran Banyaknya Penyewaan Sepeda per Bulan')
    plt.xlabel('Bulan')
    plt.ylabel('Banyaknya Persewaan Sepeda')
    st.pyplot(plt)
    st.markdown("Berdasarkan grafik lineplot dapat ditarik kesimpulan bahwa sepeda yang disewa paling besar terdapat di bulan 6 (Juni), 8 (Agustus), dan bulan 9 (September) serta mengalami tren kenaikan mulai bulan 1 (Januari) sampai bulan 6 (Juni) serta mengalami tren penurunan mulai bulan 9 (September) sampai bulan 12 (Desember).")
    plt.close()
elif selected_page == "Pengaruh Musim terhadap Penyewaan Sepeda":# Visualisasi kedua
    st.subheader("Pengaruh Musim terhadap Penyewaan Sepeda")
    total_rentals_per_season = all_data.groupby('season_hour')['cnt_hour'].sum()
    max_season = total_rentals_per_season.idxmax()
    min_season = total_rentals_per_season.idxmin()
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"Total Penyewaan Terbanyak di Musim {max_season}")
        st.write(f"Total: {total_rentals_per_season[max_season]}")
    with col2:
        st.markdown(f"Total Penyewaan Tersedikit di Musim {min_season}")
        st.write(f"Total: {total_rentals_per_season[min_season]}")
    plt.figure(figsize=(12, 6))
    sns.barplot(x='cnt_hour', y='season_hour', hue="season_hour", palette='dark', data=all_data)
    plt.title('Pengaruh Musim terhadap Penyewaan Sepeda')
    plt.xlabel('Banyaknya Penyewaan Sepeda')
    plt.ylabel('Musim')
    st.pyplot(plt)
    plt.close()
    st.markdown("Berdasarkan grafik barplot dapat ditarik kesimpulan bahwa sepeda yang disewa paling banyak saat musim summer dan paling sedikit saat musim winter. Hal ini berkaitan dengan visualisasi pada grafik 1 dimana pada grafik tersebut mengalami tren kenaikan mulai bulan 1 (Januari) sampai bulan 6 (Juni) dimana pada bulan tersebut merupakan musim summer dan mengalami tren penurunan mulai bulan 9 (September) sampai bulan 12 (Desember) dimana pada bulan tersebut merupakan musim winter.")

elif selected_page == "Penyewaan Sepeda di Setiap Cuaca":# Visualisasi ketiga
    st.subheader("Penyewaan Sepeda di Setiap Cuaca")
    total_rentals_per_weather = all_data.groupby('weathersit_day')['cnt_hour'].sum()
    max_weather = total_rentals_per_weather.idxmax()
    min_weather = total_rentals_per_weather.idxmin()
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"Total Penyewaan Terbanyak di Cuaca {max_weather}")
        st.write(f"Total: {total_rentals_per_weather[max_weather]}")
    with col2:
        st.markdown(f"Total Penyewaan Tersedikit di Cuaca {min_weather}")
        st.write(f"Total: {total_rentals_per_weather[min_weather]}")
    plt.figure(figsize=(10, 6))
    sns.barplot(x='weathersit_day', y='cnt_hour', hue="weathersit_day", palette="viridis", data=all_data)
    plt.title('Penyewaan Sepeda di Setiap Cuaca')
    plt.xlabel('Cuaca')
    plt.ylabel('Jumlah Penyewaan Sepeda')
    st.pyplot(plt)
    plt.close()
    st.markdown("Berdasarkan grafik barplot dapat ditarik kesimpulan bahwa sepeda yang disewa paling banyak saat cuaca clear dan paling sedikit saat light rain / snow serta saat cuaca heavy rain tidak ada persewaan sama sekali (karena pada barplot tidak tertera cuaca ini). Hal ini disebabkan karena pada cuaca clear tentunya lebih mudah untuk menggunakan sepeda sehingga orang-orang lebih banyak menyewanya sedangkan pada cuaca light rain / snow dan cuaca lainnya mungkin orang-orang lebih memilih transportasi lain yang lebih aman untuk memudahkan perjalanan.")

elif selected_page == "Rata-rata Penyewaan Sepeda Setiap Jam":# Visualisasi keempat
    st.subheader("Rata-rata Penyewaan Sepeda Setiap Jam")
    total_rentals_per_hour = all_data.groupby('hr')['cnt_hour'].sum()
    max_hour = total_rentals_per_hour.idxmax()
    min_hour = total_rentals_per_hour.idxmin()
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"Total Penyewaan Terbanyak di Jam {max_hour}")
        st.write(f"Total: {total_rentals_per_hour[max_hour]}")
    with col2:
        st.markdown(f"Total Penyewaan Tersedikit di Jam {min_hour}")
        st.write(f"Total: {total_rentals_per_hour[min_hour]}")
    ratarata = all_data.groupby('hr')['cnt_hour'].mean()
    plt.figure(figsize=(10, 6))
    plt.bar(ratarata.index, ratarata.values, color='tomato')
    plt.xlabel('Jam (hr)')
    plt.ylabel('Jumlah Sepeda yang Disewa (cnt)')
    plt.xticks(range(0,24))
    plt.title('Distribusi Jumlah Sepeda yang Disewa Berdasarkan Jam')
    st.pyplot(plt)
    plt.close()
    st.markdown("Berdasarkan grafik barplot dapat ditarik kesimpulan bahwa sepeda yang disewa paling banyak saat cuaca clear dan paling sedikit saat light rain / snow serta saat cuaca heavy rain tidak ada persewaan sama sekali (karena pada barplot tidak tertera cuaca ini). Hal ini disebabkan karena pada cuaca clear tentunya lebih mudah untuk menggunakan sepeda sehingga orang-orang lebih banyak menyewanya sedangkan pada cuaca light rain / snow dan cuaca lainnya mungkin orang-orang lebih memilih transportasi lain yang lebih aman untuk memudahkan perjalanan.")