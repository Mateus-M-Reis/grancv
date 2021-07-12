import numpy as np
import cv2
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
from io import StringIO
import base64

#from . import app 

class Histogram():
    def __init__(self, img):

        self.fig = go.Figure()
        self.fig.update_layout(
                margin={"l": 45, "r": 5, "t": 0, "b": 0},
                showlegend=False,
                xaxis_showgrid=False, 
                yaxis_showgrid=False,
                template='plotly_dark',
                paper_bgcolor='rgba(25,25,25,0.6)',
                plot_bgcolor='rgba(25,25,25,0)',
                )

        self.color = ['red', 'green', 'blue']
        #self.hists = []
        for i, col in enumerate(self.color):
            hist = cv2.calcHist([img],[i],None,[256],[0,256])
            #self.hists.append(hist.flatten())

            self.fig.add_trace(
                    go.Scatter(
                        x=np.arange(1,256,1),
                        y=hist.flatten(),
                        mode='lines',
                        marker_color=self.color[i],
                        fill='tozeroy',
                        )
                    )

        self.graph = dcc.Graph(
                id='graph',
                figure = self.fig,
                responsive='auto',
                config={
                    'modeBarButtonsToRemove': [
                        'pan2d', 
                        #'lasso2d',
                        'zoomIn2d',
                        'zoomOut2d',
                        'autoScale2d',
                        'resetScale2d',
                        'hoverClosestCartesian',
                        'hoverCompareCartesian',
                        'toggleSpikelines',
                        ],
                    'displaylogo': False
                    },
                style={'width': '40%', 'display': 'none'},
                )

    def flip(self, up):
        if up == False:
            self.graph.style['display'] = 'none'
        else:
            self.graph.style['display']= 'flex'
        return self.graph.style

    def update(self, im):

        self.fig.data=[]

        for i, col in enumerate(self.color):
            hist = cv2.calcHist(im,[i],None,[256],[0,256])
            self.fig.add_trace(
                    go.Scatter(
                        x=np.arange(1,256,1),
                        y=hist,
                        mode='lines',
                        marker_color=self.color[i],
                        fill='tozeroy',
                        )
                    )

        print(type(self.fig['data']))
        return self.fig
