import cv2
import bqplot.pyplot as plt
import imutils
import numpy as np
import json
import os

from IPython.core.display import HTML, display
from ipywidgets import AppLayout, Layout
from ipycanvas import Canvas, hold_canvas
import ipyvuetify as v
v.theme.dark = True
from .vvapp.inputs import button, select, slider
from .vvapp.outputs import container, row, column

f = open('app/config.json')
cfg = json.load(f)

nst_style = select(
        items=cfg['neural_style_transfer']['models'],
        v_model='candy.t7',
        )

nst_quality = slider(
        label='Transfer Quality',
        min=300,
        max=1001,
        step=50,
        v_model=500,
        )

nst_expp = v.ExpansionPanel(children=[
    v.ExpansionPanelHeader(
        children=['Neural Style Transfer']
        ),
    v.ExpansionPanelContent(children=[

        nst_style,

        nst_quality

        ],
        )
    ], 
    )

def get_model_from_path(style_model_path):
    model = cv2.dnn.readNetFromTorch(style_model_path)
    return model

def style_transfer(img, model):

    (h, w) = img.shape[:2]

    model = get_model_from_path(
            os.path.join(
                cfg['neural_style_transfer']['path'], 
                model)
            )
            
    blob = cv2.dnn.blobFromImage(img, 1.0, (w, h), (103.939, 116.779, 123.680), swapRB=False, crop=False)
    model.setInput(blob)
    output = model.forward()

    output = output.reshape((3, output.shape[2], output.shape[3]))
    output[0] += 103.939
    output[1] += 116.779
    output[2] += 123.680
    output /= 255.0
    output = output.transpose(1, 2, 0)
    output = np.clip(output, 0.0, 1.0)
    output = imutils.resize(output, width=1900) 

    return output
