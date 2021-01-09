import plotly
from plotly.offline import plot,iplot,download_plotlyjs
import plotly.offline as pyo
import plotly.graph_objects as go
x_list = [2,6,7,43,65,87]
y_list = [0,16,7,43,95,67]



data = [go.Scatter(x = x_list,y = y_list ,mode = "lines" , name = "demo chart")]
layout = go.Layout(title = "X vs y" )
figure = go.Figure(data= data,layout=layout)
plotly.io.write_html(figure,full_html=False,file = "optimised_graph.html")

#plot([{"x":[1,2,3,4,5,6],"y":[1,2,3,4,5,6]}])