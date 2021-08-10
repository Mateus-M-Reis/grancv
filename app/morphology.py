import cv2
import numpy as np
import json

import ipyvuetify as v
from .vvapp.inputs import slider, select
from .vvapp.outputs import container, row, column

f = open('app/config.json')
cfg = json.load(f)

morpho_dropdown = select(
        v_model='erosion',
        items=cfg['options']['Morphological Operations'],
        )

morpho_slider = slider(
        label='Iterations',
        min=0,
        max=10,
        step=1,
        v_model=3
        )

morpho_expp = v.ExpansionPanel(children=[
    v.ExpansionPanelHeader(
        children=['Morphological Operations']
        ),
    v.ExpansionPanelContent(children=[

        morpho_dropdown,

        morpho_slider

        ],
        )
    ],
    style_='display: none;'
    )

#def morphology(img, op_type, number):
#
#    kernel = np.ones((5,5),np.uint8)
#
#    if op_type == 'erosion':
#        morpho = cv2.erode(img, kernel, iterations=number)
#        return morpho
#    elif op_type == 'dilatation':
#        morpho = cv2.dilate(img, kernel, iterations=number)
#        return morpho
#    elif op_type == 'opening':
#        morpho = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel,iterations=number)
#        return morpho
#    elif op_type == 'closing':
#        morpho = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel,iterations=number)
#        return morpho
#    elif op_type == 'gradient':
#        morpho = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel, iterations=number)
#        return morpho
#    elif op_type == 'top-hat':
#        morpho = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel, iterations=number)
#        return morpho
#    elif op_type == 'black-hat':
#        morpho = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel, iterations=number)
#        return morpho
