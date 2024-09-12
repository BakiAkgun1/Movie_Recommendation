import pandas as pd
import streamlit as st # type: ignore
import matplotlib.pyplot as plt
import seaborn as sns # type: ignore


def visual1():

    data = pd.read_csv('clean_data.csv')

    st.title("Genel Filmler Analizi")
    st.markdown("### Film veritabanındaki `Puan` değerlerine göre dağılım")

    movies = pd.DataFrame(data)
    bins = [i for i in range(0, 11)]  # 0-1, 1-2, ..., 9-10 aralığı oluşturma
    movies['vote_average_bins'] = pd.cut(movies['vote_average'], bins=bins)
    bin_counts = movies['vote_average_bins'].value_counts().sort_index()
    # Bar grafiği oluşturma
    fig, ax = plt.subplots(figsize=(10, 6))
    bin_counts.plot(kind='bar', color='lightgreen', ax=ax)
    ax.set_title('Puan Dağılımı')
    ax.set_xlabel('Puan Aralıkları')
    ax.set_ylabel('Film Sayısı')
    plt.xticks(rotation=0)
    # Bar grafiğini Streamlit ile gösterme
    st.pyplot(fig)

#-------------------------------------------------------------

    all_genres = data['genres'].str.get_dummies(sep=' ')
    data = pd.concat([data, all_genres], axis=1)
    st.title("Film Türlerinin Dağılımı")
    st.write(data[['title'] + list(all_genres.columns)])
    data = pd.concat([data, all_genres], axis=1)
    genre_counts = all_genres.sum().sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    sns.barplot(x=genre_counts.index, y=genre_counts.values, palette="viridis")
    plt.xticks(rotation=90)
    plt.title("Film Türlerine Göre Dağılım", fontsize=16)
    plt.xlabel("Türler", fontsize=12)
    plt.ylabel("Film Sayısı", fontsize=12)
    # Streamlit üzerinde grafiği göster
    st.pyplot(plt)

#-------------------------------------------------------------
    df_filtered = data[data['director'] != 'unnamed']  # Boş olanları çıkar
    df_filtered = df_filtered[~df_filtered['director'].str.contains('Unnamed', na=False)]  # 'Unnamed' içeren satırları çıkar

    # 'director' sütunundaki yönetmenlere göre film sayısını hesapla (ilk 10)
    director_counts = df_filtered['director'].value_counts().sort_values(ascending=False).head(10)

    # Streamlit başlığı
    st.title("Yönetmenlerin Yönettiği Film Sayısı")
    plt.figure(figsize=(10, 6))
    sns.barplot(x=director_counts.index, y=director_counts.values, palette="viridis")
    plt.xticks(rotation=90)
    plt.title("Film Türlerine Göre Dağılım", fontsize=16)
    plt.xlabel("yönetmenler", fontsize=12)
    plt.ylabel("Film Sayısı", fontsize=12)

    # Streamlit üzerinde grafiği göster
    st.pyplot(plt)


#-------------------------------------------------------------