import cv2
import numpy as np
import json

from ipywidgets import HTMLMath, HTML
import ipyvuetify as v
from .vvapp.inputs import slider, select, checkbox
from .vvapp.outputs import container, row, column

f = open('app/config.json')
cfg = json.load(f)

apply_contours = checkbox(label='Apply contours?')

threshold_dropd = select(
        items=cfg['options']['Thresholding'],
        v_model='threshold-binary',
        )
threshold_slider = slider(
        #label='Threshold Value',
        min=0,
        max=255,
        step=1,
        v_model=127,
        ticks=False,
        )

threshold_bs_slider = slider(
        #label='Block Size',
        min=3,
        max=21,
        step=2,
        v_model=9,
        ticks=False,
        )
threshold_C_slider = slider(
        #label='C',
        min=-21,
        max=21,
        step=1,
        v_model=7,
        ticks=False,
        )
threshold_adapt_row = row(
                children=[ 
                    threshold_bs_slider, 
                    threshold_C_slider 
                    ],
                style_=' \
                        display: none; \
                        background-color: #000000BF; \
                        '
                )

threshold_expp = v.ExpansionPanel(children=[
    v.ExpansionPanelHeader(
        children=['Thresholding']
        ),
    v.ExpansionPanelContent(children=[

        apply_contours,

        threshold_dropd,

        threshold_slider,

        threshold_adapt_row,

        ],
        #style='\'
        )
    ], 
    style_='display: none;'
    )

def threshold(img, op_type, value, bs, Cbs):

    if op_type == 'threshold-binary':
        ret,thresh = cv2.threshold(img,value,255,cv2.THRESH_BINARY)
    elif op_type == 'threshold-binary-inverse':
        ret,thresh = cv2.threshold(img,value,255,cv2.THRESH_BINARY_INV)
    elif op_type == 'threshold-truncated':
        ret,thresh = cv2.threshold(img,value,255,cv2.THRESH_TRUNC)
    elif op_type == 'threshold-tozero':
        ret,thresh = cv2.threshold(img,value,255,cv2.THRESH_TOZERO)
    elif op_type == 'threshold-tozero-inverse':
        ret,thresh = cv2.threshold(img,value,255,cv2.THRESH_TOZERO_INV)
    elif op_type=='threshold-adaptive-mean-c':
        thresh = cv2.adaptiveThreshold( 
                img,
                255,
                cv2.ADAPTIVE_THRESH_MEAN_C, 
                cv2.THRESH_BINARY,
                bs,
                Cbs)
    elif op_type=='threshold-adaptive-gaussian-c':
        thresh = cv2.adaptiveThreshold(
                img,
                255,
                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                cv2.THRESH_BINARY,
                bs,
                Cbs)
    return thresh 

def update_adap_ts_items(*args): 
    if threshold_dropd.v_model not in \
            ['threshold-adaptive-gaussian-c','threshold-adaptive-mean-c']:
            threshold_adapt_row.style_='\
                    display: none; \
                    '
            threshold_slider.style_='display: block'
    else:
        threshold_adapt_row.style_='\
                display: block;\
                '
        threshold_slider.style_='display: none'
threshold_dropd.on_event('change', update_adap_ts_items)
