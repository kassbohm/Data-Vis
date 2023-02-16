from sympy.physics.units import *
from sympy import *

# Units:
(mm, cm)  =  ( m/1000, m/100 )
Newton    =  kg*m/s**2
kN        =  10**3*Newton
Pa        =  Newton/m**2
MPa       =  10**6*Pa
GPa       =  10**9*Pa
deg       =  pi/180
half      =  S(1)/2

a = 3 *m
q = 3 *kN/m
F = 10 *kN
E = 200 *GPa
I = 65*10**6 *mm**4

EI = E*I

f1 = a*a*a/6/EI * F / mm
f2 = a*a*a*a/24/EI * q / mm

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

x = np.linspace(0,1,101, endpoint=True)
y1 = 2 - 3*x + x**3
y2 = 3 - 4*x + x**4
# Create figure
fig = go.Figure()

# Add traces, one for each slider step
for i in range(11):
   fig.add_trace(
      go.Scatter(
         visible=False,
         name="i:" + str(i),
         x = x,
         y = i*float(f1)*y1/10,
         )
      )
# Make 10th trace visible
fig.data[10].visible = True

# Create and add slider
steps = []
for i in range(11):
   step = dict(
      method="restyle",
      # "update": modify data and layout attributes (as above)
      # "restyle": modify data attributes
      # "relayout": modify layout attributes         
      # "animate": start or pause an animation
      args=[
         {"visible": [False] * 11},
         ],
      label=str(i/10)
      )
   step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
   steps.append(step)

sliders = [
   dict(
   active=10, # slider position
   currentvalue={"prefix": "α: ", "suffix": ""},
   # pad={"t": 40},
   steps = steps,
   ),
   dict(
   y = -0.1,
   active=10, # slider position
   currentvalue={"prefix": "α: ", "suffix": ""},
   # pad={"t": 40},
   steps = steps,
   ),   
   ]

fig.update_layout(
   sliders=sliders,
   paper_bgcolor="rgba(0,0,0,0)",
   plot_bgcolor="rgba(243,246,246,1)", # table background
   xaxis = dict(fixedrange=True),
   yaxis = dict(range=[10, -0.2], fixedrange=True),
   hoverlabel_align = 'right',
   xaxis_title="x / m",
   yaxis_title="w / mm",
)

fig.update_traces(
   hovertemplate = 'x / m: %{x:.2f}</b><br>w / mm: %{y:.2f}',
   line_color = "rgba(191,0,191,0.6)",
   line_width = 2,
   # mode="markers+lines",
   )

fig.show(
   config= dict(displayModeBar = False),
   )
