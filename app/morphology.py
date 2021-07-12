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

morpho_dropdown = dcc.Dropdown(
        id='morpho-op',
        options=cfg['options']['Thresholding'],
        style={'color': 'white'},
        )

morpho_value = dcc.Slider(
        id='morpho-value',
        min=0,
        max=255,
        step=1,
        value=127)

morpho_wid = dbc.Card([
    dbc.CardHeader(
        html.H6('Morphological Operations')
        ),
    dbc.CardBody([
        morpho_dropdown,
        html.Br(),

        morpho_value
        ],
        style={
            'display': 'flex',
            'flex-direction': 'column',
            'justify-content': 'space-between'
            }
        )
    ], className='inv')

def morphology(img, op_type, number):

    kernel = np.ones((5,5),np.uint8)

    if op_type == 'erosion':
        morpho = cv2.erode(img, kernel, iterations=number)
        return morpho
    elif op_type == 'dilatation':
        morpho = cv2.dilate(img, kernel, iterations=number)
        return morpho
    elif op_type == 'opening':
        morpho = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel,iterations=number)
        return morpho
    elif op_type == 'closing':
        morpho = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel,iterations=number)
        return morpho
    elif op_type == 'gradient':
        morpho = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel, iterations=number)
        return morpho
    elif op_type == 'top-hat':
        morpho = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel, iterations=number)
    elif op_type == 'top-hat':
        morpho = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel, iterations=number)
