import cv2
import numpy as np
import json

import ipyvuetify as v
from .vvapp.inputs import slider, select
from .vvapp.outputs import container, row, column

f = open('app/config.json')
cfg = json.load(f)

threshold_dropd = select(
        v_model='threshold-binary',
        items=cfg['options']['Thresholding'],
        )
threshold_slider = slider(
        label='Threshold Value',
        min=0,
        max=255,
        step=1,
        v_model=127
        )

threshold_bs_slider = slider(
        label='Block Size',
        min=1,
        max=19,
        step=2,
        v_model=9,
        )
threshold_C_slider = slider(
        label='C',
        min=-21,
        max=21,
        step=1,
        v_model=7
        )
threshold_adapt_row = row(
                children=[ threshold_bs_slider, threshold_C_slider ],
                style_='display: none;'
                )

threshold_expp = v.ExpansionPanel(children=[
    v.ExpansionPanelHeader(
        children=['Thresholding']
        ),
    v.ExpansionPanelContent(children=[

        threshold_dropd,

        threshold_slider,

        threshold_adapt_row,

        ],
        #style='\'
        )
    ], 
    style_='display: none;'
    )

#def threshold(img, op_type, k_size):
#
#    k_size=np.intc(k_size)
#
#    if op_type == 'filter':
#        kernel = np.ones((k_size, k_size), np.float32)/25
#        dst = cv2.filter2D(img,-1,kernel)
#        return dst
#    elif op_type == 'blur':
#        blur = cv2.blur(img,(k_size,k_size))
#        return blur
#    elif op_type == 'gaussian-blur':
#        blur = cv2.GaussianBlur(img,(k_size,k_size),0)
#        return blur
#    elif op_type == 'median-blur':
#        median = cv2.medianBlur(img,k_size)
#        return median
#    elif op_type == 'bilateral-filter':
#        #blur = cv2.bilateralFilter(img,d,sigma1,sigma1)
#        return img
def update_adap_ts_items(*args):
    if threshold_dropd.v_model not in \
            ['threshold-adaptive-gauss', 'threshold-adaptive-mean-c']:
        threshold_adapt_row.style_='\
                display: none; \
                '
    else:
        threshold_adapt_row.style_='\
                display: block; \
                '
threshold_dropd.on_event('change', update_adap_ts_items)


