import pandas as pd
import plotly_express as px
df = pd.read_csv("covidData.csv")
fig = px.scatter(df , x = "date" , y = "cases" , color = "country" )
fig.show()

# import pandas as pd
# import plotly_express as px
# df = pd.read_csv("covidData.csv")
# fig = px.scatter(df , x="date" , y="cases" , color = "country" , title = "Per Capita Income")
# fig.show()