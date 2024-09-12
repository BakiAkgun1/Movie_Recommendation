import pandas as pd
from mlxtend.frequent_patterns import fpgrowth, association_rules
from sklearn.feature_extraction.text import CountVectorizer
import streamlit as st # type: ignore

def modal1():
    data= pd.read_csv('clean_data.csv')
    result= pd.read_csv('movie_dataset.csv')

    data['keywords'] = data['keywords'].fillna('')
    data['overview'] = data['overview'].fillna('')
    result['overview'] = result['overview'].fillna('')
    result['keywords'] = result['keywords'].fillna('')
    result['genres'] = result['genres'].fillna('')

    data['combined_features'] = data['keywords']+ ' ' +  data['genres'] + ' ' + data['overview']

    #FP-Growth'a göre veriyi işleme
    vectorizer = CountVectorizer(tokenizer=lambda doc: doc.split(), binary=True)
    X = vectorizer.fit_transform(data['combined_features'])
    df_features = pd.DataFrame(X.toarray(), columns = vectorizer.get_feature_names_out())


    frequent_itemset = fpgrowth(df_features, min_support=0.02, use_colnames= True)

    rules= association_rules(frequent_itemset, metric="lift", min_threshold=1)

    st.markdown("""
        <style>
        .stSelectbox div {
            background-color: white; /* Arka plan rengini değiştirir */
            color: blue; /* Metin rengini değiştirir */
        }
        .stSelectbox div:hover {
            background-color: #e0e0e0; /* Hover arka plan rengi */
        }
        </style>
        """, unsafe_allow_html=True)

    st.image('images/movieee.png', use_column_width=True)
    st.header('Bir Film Arayın Veya Seçiniz:')
    selected_movie = st.selectbox('', data['title'].values)

    if selected_movie:
        # Seçilen filmin anahtar kelimelerini al
        selected_movie_row = data[data['title'] == selected_movie]
        
        if not selected_movie_row.empty:
            # Tek bir satır için tür bilgilerini als
            selected_movie_genres = selected_movie_row['genres'].values[0]

            # Benzer türdeki filmleri bul
            similar_movies = data[
                data['genres'] == selected_movie_genres  # Aynı türdeki filmleri seçer
            ].loc[
                data['title'] != selected_movie  # Seçilen filmi hariç tutar
            ].sort_values(by='title')  # Başka bir sıralama kriteri de ekleyebilirsiniz

            # Sonuçları Görüntüle
            if not similar_movies.empty:
                st.write(f"**{selected_movie}** filmi ile benzer öneriler:")
                st.dataframe(similar_movies[['title','genres','runtime','vote_average','vote_count','cast','director','homepage']].head(10))  # İlk 10 benzer filmi tablo olarak gösterir
            else:
                st.write(f"**{selected_movie}** filmi için benzer film bulunamadı.")
        else:
            st.write(f"**{selected_movie}** filmi veri setinde bulunamadı.")


