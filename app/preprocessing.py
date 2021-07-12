import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import imutils
import cv2
import numpy as np
import json

from . import app
f = open('app/config.json')
cfg = json.load(f)

preproc_dropdown = dcc.Dropdown(
        id='preproc-op',
        options=cfg['options']['Preprocessing'],
        style={'color': 'white'},
        value='filter'
        )

preproc_value = dcc.Slider(
        id='preproc-value',
        min=3,
        max=9,
        step=1,
        value=7)

median_sigma1 = dcc.Slider(
        id='median_sigma1',
        min=55,
        max=95,
        step=5,
        value=75,
        )

median_sigma2 = dcc.Slider(
        id='median_sigma2',
        min=55,
        max=95,
        step=5,
        value=75,
        )

sigma_div = html.Div(
                id='sigma-div',
                children=[ median_sigma1, median_sigma2 ],
                className='inv'
                )

preproc_wid = dbc.Card([
    dbc.CardHeader(
        html.H6('Preprocessing')
        ),
    dbc.CardBody([

        preproc_dropdown,
        html.Br(),

        preproc_value,
        html.Br(),

        sigma_div,

        ],
        style={
            'display': 'flex',
            'flex-direction': 'column',
            'justify-content': 'space-between'
            }
        )
    ], className='appear')

def preprocess(img, op_type, k_size, sigma1, sigma):
    k_size=np.intc(k_size)
    if op_type == 'filter':
        kernel = np.ones((k_size, k_size), np.float32)/25
        dst = cv2.filter2D(img,-1,kernel)
        return dst
    elif op_type == 'blur':
        blur = cv2.blur(img,(k_size,k_size))
        return blur
    elif op_type == 'gaussian-blur':
        blur = cv2.GaussianBlur(img,(k_size,k_size),0)
        return blur
    elif op_type == 'median-blur':
        median = cv2.medianBlur(img,k_size)
        return median
    elif op_type == 'bilateral-filter':
        blur = cv2.bilateralFilter(img,k_size,sigma1,sigma1)
        return blur

@app.callback(
        Output(component_id='sigma-div', component_property='className'),
        [Input(component_id='preproc-op', component_property='value')])
def update_preproc_items(op):

    if op != 'bilateral-filter':
        return 'inv'
    else:
        return 'appear'

@app.callback(
        Output(component_id='preproc-value', component_property='max'),
        [Input(component_id='preproc-op', component_property='value')])
def update_preproc_max(op):

    if op != 'bilateral-filter':
        return 9
    else:
        return 15
