# import all required libraries
import numpy as np
import plotly
import plotly.graph_objects as go
import plotly.offline as pyo



# countries on x-axis
countries=['India', 'canada',
           'Australia','Brazil',
           'Mexico','Russia',
           'Germany','Switzerland',
           'Texas']

# plotting corresponding y for each
# country in x
fig = go.Figure([go.Bar(x=countries,
                        y=[80,70,60,50,
                           40,50,60,70,80])])

pyo.plot(fig)
