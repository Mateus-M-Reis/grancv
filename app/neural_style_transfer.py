from .vvapp.inputs import select, slider
# from .vvapp.outputs import container, row, column
import cv2
import imutils
import numpy as np
import json
import os
import ipyvuetify as v

v.theme.dark = True
f = open('app/config.json')
cfg = json.load(f)

nst_style = select(
        items=cfg['neural_style_transfer']['models'],
        v_model='candy.t7')

nst_quality = slider(
        min=300,
        max=1000,
        step=50,
        v_model=500,
        ticks=False)

nst_expp = v.ExpansionPanel(children=[
    v.ExpansionPanelHeader(
        children=['Neural Style Transfer']
        ),
    v.ExpansionPanelContent(children=[

        nst_style,

        nst_quality

        ])
    ],
    style_='\
            display: block; \
            background-color: #000000BF; \
            '
    )


def get_model_from_path(style_model_path):
    model = cv2.dnn.readNetFromTorch(style_model_path)
    return model


def style_transfer(img, model, quality, out):

    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    img = imutils.resize(img, width=quality)

    (h, w) = img.shape[:2]

    model = get_model_from_path(
            os.path.join(
                cfg['neural_style_transfer']['path'],
                model
                )
            )

    blob = cv2.dnn.blobFromImage(
            img, 1.0, (w, h), (103.939, 116.779, 123.680),
            swapRB=False, crop=False)
    model.setInput(blob)
    output = model.forward()

    output = output.reshape((3, output.shape[2], output.shape[3]))

    output[0] += 103.939
    output[1] += 116.779
    output[2] += 123.680

    output = output.transpose(1, 2, 0)
    output = np.clip(output, 0, 255)

    # output = imutils.resize(output, width=1900)

    output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)

    return output
