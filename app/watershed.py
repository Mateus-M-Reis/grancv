# import ipyvuetify as v
from .vvapp.inputs import slider  # select
from .vvapp.outputs import row, column  # , container

import cv2 as cv
import numpy as np

op_iter_slider = slider(min=0, max=6, step=1, v_model=2)
dl_iter_slider = slider(min=0, max=6, step=1, v_model=3)
sf_factor_slider = slider(min=.1, max=.9, step=.1, v_model=.7)

watershed_expp = row(
        children=[
            column(children=[op_iter_slider], cols=12),
            column(children=[dl_iter_slider], cols=12),
            column(children=[sf_factor_slider], cols=12),
            ],
        style_='\
                display: none;\
                '
        )


def watershed_seg(img, op_iter, dl_iter, sf_factor):

    g_img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    ret, thresh = cv.threshold(
            g_img, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)

    # noise removal
    kernel = np.ones((3, 3), np.uint8)
    opening = cv.morphologyEx(
            thresh, cv.MORPH_OPEN, kernel, iterations=op_iter)

    # Finding sure background area
    sure_bg = cv.dilate(opening, kernel, iterations=dl_iter)

    # Finding sure foreground area
    dist_transform = cv.distanceTransform(opening, cv.DIST_L2, 5)
    ret, sure_fg = cv.threshold(
            dist_transform, sf_factor*dist_transform.max(), 255, 0)

    # Finding unknown region
    sure_fg = np.uint8(sure_fg)
    unknown = cv.subtract(sure_bg, sure_fg)

    # Marker labelling
    ret, markers = cv.connectedComponents(sure_fg)
    # Add one to all labels so that sure background is not 0, but 1
    markers = markers+1
    # Now, mark the region of unknown with zero
    markers[unknown == 255] = 0

    markers = cv.watershed(img, markers)
    img[markers == -1] = [255, 0, 0]

    return img
