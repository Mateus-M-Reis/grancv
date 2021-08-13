import cv2
import numpy as np
import json

from ipywidgets import interact
import ipyvuetify as v
from .vvapp.inputs import slider, select
from .vvapp.outputs import container, row, column

f = open('app/config.json')
cfg = json.load(f)

def update_sigma_items(*args):

    if smooth_dropd.v_model != 'bilateral-filter':
        sigma_container.style_='\
                display: none; \
                '
    else:
        sigma_container.style_='\
                display: block; \
                '

smooth_dropd = select(
        items=cfg['options']['Smoothing'],
        v_model=['filter'],
        )
smooth_dropd.on_event('change', update_sigma_items)

smooth_slider = slider(
        label='Iterations',
        min=1,
        max=19,
        step=2,
        v_model=7
        )

sigma1_slider = slider(
        label='\sigma_1',
        min=55,
        max=95,
        step=5,
        v_model=75,
        )

sigma2_slider = slider(
        label='\sigma_2',
        min=55,
        max=95,
        step=5,
        v_model=75,
        )

sigma_container = row(
                children=[ sigma1_slider, sigma2_slider ],
                style_='\
                        display: none; \
                        '
                )

smooth_expp = v.ExpansionPanel(children=[
    v.ExpansionPanelHeader(
        children=['Smoothing']
        ),
    v.ExpansionPanelContent(children=[

        smooth_dropd,

        smooth_slider,

        sigma_container,

        ],
        ),
    ],
    style_='display: none;'
    )

def smooth(img, op_type, k_size, sigma1, sigma2): 

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
