import cv2
import numpy as np
import json

from ipywidgets import HTMLMath, HTML, Layout
import ipyvuetify as v
from .vvapp.inputs import slider, select, checkbox
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

    if sharp_cb.v_model == False:
        sharp_row.style_='\
                display: none; \
                '
    else:
        sharp_row.style_='\
                display: block; \
                '

smooth_dropd = select(
        items=cfg['options']['Smoothing'],
        v_model=['filter'],
        )
smooth_dropd.on_event('change', update_sigma_items)

smooth_slider = slider(
        #label='Iterations',
        min=1,
        max=19,
        step=2,
        v_model=7,
        ticks=False,
        )

sigma1_slider = slider(
        #label='\sigma_1',
        min=55,
        max=95,
        step=5,
        v_model=75,
        ticks=False,
        )

sigma2_slider = slider(
        #label='\sigma_2',
        min=55,
        max=95,
        step=5,
        v_model=75,
        ticks=False,
        )

sigma_container = row(
                children=[ 
                    column([sigma1_slider], cols=12),
                    column([sigma2_slider], cols=12),
                    ],
                style_='\
                        display: none; \
                        '
                )

sharp_cb = checkbox(label='Sharp / Unsharp')

sharp_cb.on_event('change', update_sigma_items)

alpha_slider = slider(
        #label='\alpha',
        min=-2,
        max=2,
        step=0.1,
        v_model=0.5,
        ticks=False,
        )

beta_slider = slider(
        #label='\alpha',
        min=-2,
        max=2,
        step=0.1,
        v_model=0.5,
        ticks=False,
        )

gamma_slider = slider(
        #label='\gamma',
        min=-2,
        max=2,
        step=0.1,
        v_model=0.0,
        ticks=False,
        )

sharp_row = row(
        children=[
            column([alpha_slider], cols=12),
            column([beta_slider], cols=12),
            column([gamma_slider], cols=12),
            ],
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

        column([smooth_slider], cols=12),

        sigma_container,

        sharp_cb,

        sharp_row,

        ],
        ),
    ],
    style_=' \
            display: none; \
            background-color: #000000BF; \
            '
    )

def smooth(img, op_type, k_size, sigma1, sigma2, \
        apply_sharp=False, alpha=0.5, beta=0.5, gamma=0.0): 

    k_size=np.intc(k_size)

    if op_type == 'filter':
        kernel = np.ones((k_size, k_size), np.float32)/25
        smoothed = cv2.filter2D(img,-1,kernel)
    elif op_type == 'blur':
        smoothed = cv2.blur(img,(k_size,k_size))
    elif op_type == 'gaussian-blur':
        smoothed = cv2.GaussianBlur(img,(k_size,k_size),0)
    elif op_type == 'median-blur':
        smoothed = cv2.medianBlur(img,k_size)
    elif op_type == 'bilateral-filter':
        smoothed = cv2.bilateralFilter(img,k_size,sigma1,sigma1)

    if apply_sharp == False:
        return smoothed
    else:
        img = cv2.addWeighted(img, alpha, smoothed, beta, gamma)
        return img

