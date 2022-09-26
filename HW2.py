import streamlit as st
import seaborn as sns
import plotly.express as px

df_iris = sns.load_dataset("iris")
df_iris = px.data.iris()

plot = px.scatter_3d(df_iris, x="sepal_length", y="sepal_width", z="petal_length", size="petal_width", color="species")
plot.show()
