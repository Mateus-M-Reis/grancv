import os
import json
import cv2
import imutils
import time

from IPython.core.display import HTML, display
from ipywidgets import AppLayout, Layout, Output, Box, HBox, VBox
from ipycanvas import Canvas, hold_canvas
import ipyvuetify as v
from .vvapp.inputs import button
from .vvapp.outputs import container, row, column
v.theme.dark = True

from .sidebar import Sidebar
from .paper import Paper
from .histogram import Histogram

#from .smoothing import smooth
from .smoothing import (
        smooth,
        smooth_dropd,
        smooth_slider,
        sigma1_slider,
        sigma2_slider,
        )
#from .morphology import morphology
#from .neural_style_transfer import style_transfer 

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
                    self.paper.output, 
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

    def read_img(self, path, width):
        self.cur_path = path
        self.img_list = []

        img = cv2.imread(
                os.path.join(
                    self.cfg['images']['path'],
                    self.cur_img)
                )

        img = imutils.resize(img, width=width)
        self.img_list.append(img)

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
            self.sidebar.flip_hist_btn.color = 'blue'

    def operate(self, *args):
        """
        Operate on current image.
        """
        with self.sidebar.output:
            print('\nStarting Function')

        op_opts = list(self.cfg['operations'].values())
        cur_ops = self.sidebar.op_selector.v_model
        #self.img_list = self.img_list[0]

        for op in op_opts:

            if op in cur_ops:
                if op=='neural-style-transfer':
                    pass

                elif op=='smoothing':
                    with self.sidebar.output:
                        print('smoothing', len(self.img_list))
                    smoothed = smooth(self.img_list[-1])
                    self.img_list.append(smoothed)
                    with self.sidebar.output:
                        print('smoothed!!!', len(self.img_list))
                elif op=='thresholding':
                    pass

                elif op=='morphologycal-operations':
                    pass

            else:
                if op=='neural-style-transfer':
                    pass
                elif op=='smoothing':
                    pass
                elif op=='thresholding':
                    pass
                elif op=='morphologycal-operations':
                    pass
        
        with self.sidebar.output:
            print('displaying', len(self.img_list))
        self.paper.update(self.img_list[-1])
