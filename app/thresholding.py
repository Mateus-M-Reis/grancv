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

threshold_dropdown = dcc.Dropdown(
        id='threshold-op',
        options=cfg['options']['Thresholding'],
        style={'color': 'white'},
        )

threshold_value = dcc.Slider(
        id='threshold-value',
        min=0,
        max=255,
        step=1,
        value=127)

threshold_wid = dbc.Card([
    dbc.CardHeader(
        html.H6('Thresholding')
        ),
    dbc.CardBody([
        threshold_dropdown,
        html.Br(),

        threshold_value
        ],
        style={
            'display': 'flex',
            'flex-direction': 'column',
            'justify-content': 'space-between'
            }
        )
    ], className='inv')

def threshold(img, op_type, k_size):
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
        #blur = cv2.bilateralFilter(img,d,sigma1,sigma1)
        return img
