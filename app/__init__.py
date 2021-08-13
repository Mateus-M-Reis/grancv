import os
import json
import cv2
import imutils
import time

from IPython.core.display import HTML, display
from ipywidgets import AppLayout, Layout, Output, Box, HBox, VBox
from ipycanvas import Canvas, hold_canvas
import ipyvuetify as v
v.theme.dark = True
v.theme.themes.dark.primary = 'colors.cyan.accent2'
v.theme.themes.dark.secondary = 'colors.red.accent3'
v.theme.themes.dark.success = 'colors.green.accent3'
from .vvapp.inputs import button
from .vvapp.outputs import container, row, column

from .sidebar import Sidebar
from .paper import Paper
from .histogram import Histogram

from .smoothing import (
        smooth,
        smooth_dropd,
        smooth_slider,
        sigma1_slider,
        sigma2_slider,
        )
from .morphology import (
        morphology,
        morpho_dropd,
        morpho_slider,
        )
from .thresholding import (
        threshold,
        threshold_dropd,
        threshold_slider,
        threshold_bs_slider,
        threshold_C_slider,
        )
from .neural_style_transfer import (
        style_transfer,
        nst_style,
        nst_quality,
        )

class App():
    """
    Base Operation Class.
    """
    def __init__(self):

        f = open('app/config.json')
        self.cfg = json.load(f)

        self.img_list = []
        self.cur_img = 'desmonte.jpg'

        self.img_list.append(
                cv2.cvtColor(
                    cv2.imread(
                        os.path.join(
                            self.cfg['images']['path'],
                            self.cur_img
                            )
                        ),
                    cv2.COLOR_BGR2RGB
                    )
                )

        self.sidebar = Sidebar(self.flip_hist)

        self.paper = Paper(self.img_list[0])

        self.hist = Histogram(self.img_list[0])
        self.is_hist_up = True

        self.layout = row(children= [ 
            column(
                children=[self.sidebar.drawer], 
                cols=3
                ),
            column(
                children=[
                    self.paper.canvas, 
                    ], 
                cols=9
                ),
            self.hist.wid
            ],
            justify='end',
            style_='\
                    height: 100%; \
                    width: 100% \
                    '
                    )

    def read_img(self, *args):

        img = cv2.imread(
                os.path.join(
                    self.cfg['images']['path'],
                    self.sidebar.img_selector.v_model
                    )
                )
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        self.img_list = [img]
        self.paper.update(self.img_list[-1], self.sidebar.output)
        self.hist.update(self.img_list[-1])

    def flip_hist(self, *args):
        if self.is_hist_up==True:
            self.hist.wid.style_='\
                            display: none; \
                            position: absolute; \
                            background-color: #00000066; \
                            '
            self.is_hist_up=False
            self.sidebar.flip_hist_btn.color = 'grey'
        else:
            self.hist.wid.style_='\
                            display: block; \
                            position: absolute; \
                            background-color: #000000BF; \
                            '

            self.is_hist_up=True
            self.sidebar.flip_hist_btn.color = 'primary'

    def operate(self, *args):
        """
        Operate on current image.
        """
        op_opts = list(self.cfg['operations'].values())
        cur_ops = self.sidebar.op_selector.v_model
        self.img_list = [self.img_list[0]]

        for op in op_opts:

            if op in cur_ops:
                if op=='neural-style-transfer':
                    stylized = style_transfer(
                            self.img_list[-1],
                            nst_style.v_model,
                            nst_quality.v_model,
                            self.sidebar.output,
                            )
                    self.img_list.append(stylized)

                elif op=='smoothing':
                    smoothed = smooth(
                            self.img_list[-1],
                            smooth_dropd.v_model,
                            smooth_slider.v_model,
                            sigma1_slider.v_model,
                            sigma2_slider.v_model,
                            )
                    self.img_list.append(smoothed)

                elif op=='thresholding':
                    thresholded = threshold(
                            self.img_list[-1],
                            threshold_dropd.v_model,
                            threshold_slider.v_model,
                            threshold_bs_slider.v_model,
                            threshold_C_slider.v_model,
                            )
                    self.img_list.append(thresholded)

                elif op=='morphologycal-operations':
                    morpho = morphology(
                            self.img_list[-1],
                            morpho_dropd.v_model,
                            morpho_slider.v_model,
                            )
                    self.img_list.append(morpho)

            else:
                if op=='neural-style-transfer':
                    pass
                elif op=='smoothing':
                    pass
                elif op=='thresholding':
                    pass
                elif op=='morphologycal-operations':
                    pass
        
        self.paper.update(self.img_list[-1], self.sidebar.output)
        self.hist.update(self.img_list[-1])

app = App()

# Changing images
app.sidebar.img_selector.on_event('input', app.read_img)
# Hiding Showing Histogram
app.sidebar.flip_hist_btn.on_event('click', app.flip_hist)
# Smoothing
smooth_dropd.on_event('input', app.operate)
smooth_slider.on_event('input', app.operate)
sigma1_slider.on_event('input', app.operate)
sigma2_slider.on_event('input', app.operate)
# Morphology
morpho_dropd.on_event('input', app.operate)
morpho_slider.on_event('input', app.operate)
# Thresholding
threshold_dropd.on_event('input', app.operate)
threshold_slider.on_event('input', app.operate)
threshold_bs_slider.on_event('input', app.operate)
threshold_C_slider.on_event('input', app.operate)
# Neural Style Transfer
nst_style.on_event('input', app.operate)
nst_quality.on_event('input', app.operate)
