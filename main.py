import pandas as pd
from visual import visual1
import streamlit as st # type: ignore
from modal import modal1

st.sidebar.title("Movie Project")
selection = st.sidebar.radio("", ( "Film Öneri Sistemi", "IMDB TOP 250", "Analiz"))

# Seçilen sayfayı göster
if selection == "Film Öneri Sistemi":  
    modal1()
elif selection == "IMDB TOP 250":
    st.image('images/movie1.png', use_column_width=True)

    data = pd.read_csv("clean_data.csv")
    filtered_data = data[data['vote_count'] > 1000]
    data_sorted =filtered_data[['title', 'vote_average', 'vote_count','runtime','cast','director']].sort_values(by="vote_average", ascending=False).head(250)

    # Veri çerçevesini stilize et ve göster
    st.dataframe(data_sorted, height=1000 )
    st.image('images/123.jpeg', use_column_width=True)


elif selection == "Analiz":
    visual1()