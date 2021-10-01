import pandas as pd
import plotly.express as px

dataframe = pd.read_csv("Copy+of+data+-+data.csv")
graph = px.scatter(dataframe, x="date", y="cases", color="country", size_max=100)
graph.show()