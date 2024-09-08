import pandas as pd
import streamlit as st

data = pd.read_csv("clean_data.csv")

df = data.groupby("vote_average").size().reset_index(name="Point")
df1 = df.sort_values(by="point", ascending=False)
df1