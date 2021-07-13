import cv2
from PIL import Image
import os

import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import plotly.express as px

img_path = 'input/images/desmonte.jpg'
img = cv2.imread(img_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

fig = px.imshow(img, template='plotly_dark')

fig.update_layout(
		margin={"l": 0, "r": 0, "t": 0, "b": 0},
		showlegend=False,
		xaxis_showgrid=False, 
		yaxis_showgrid=False
		)
fig.update_xaxes(showticklabels=False)
fig.update_yaxes(showticklabels=False)

paper = dcc.Graph(
		id='paper',
		figure = fig,
		responsive='auto',
		style={
			'width': '100%',
			'height': '100%',
                        'position': 'absolute'
			},
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
			}
		)


