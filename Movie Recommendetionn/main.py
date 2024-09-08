import pandas as pd

import streamlit as st # type: ignore
from modal import modal1

st.sidebar.title("Movie Project")
selection = st.sidebar.radio("", ( "Film Öneri Sistemi", "IMDB TOP 100"))

# Seçilen sayfayı göster
if selection == "Film Öneri Sistemi":  
    modal1()
elif selection == "IMDB TOP 250":
    data = pd.read_csv("clean_data.csv")
    filtered_data = data[data['vote_count'] > 1000]
    data_sorted =filtered_data[['title', 'vote_average', 'vote_count','runtime','cast','director']].sort_values(by="vote_average", ascending=False).head(250)
    st.title("Top 250 Movies")
    st.dataframe(data_sorted)
    st.image('images/moviee.jpeg', use_column_width=True)


# elif selection == "Hakkında":
#     about_page()