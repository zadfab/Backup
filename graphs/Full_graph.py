import plotly
from plotly.offline import plot,download_plotlyjs
import plotly.offline as pyo
import plotly.graph_objects as go
x_list = [2,6,7,43,65,87]
y_list = [0,16,7,43,95,67]



data = [go.Scatter(x = x_list,y = y_list ,mode = "lines" , name = "demo chart")]


layout = go.Layout(title = "X vs y" ,xaxis_title="X-axis",
                   yaxis_title="Y-axis")
figure = go.Figure(data= data,layout=layout)
plotly.io.write_html(figure,full_html=False,file = "Template/optimised_graph.html",config={"displayModeBar": False, "showTips": False})