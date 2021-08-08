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

from .paper import Paper
from .sidebar import Sidebar
from .histogram import Histogram
#from .neural_style_transfer import style_transfer 
#from .preprocessing import preprocess#, update_preproc_items
#from .morphology import morphology

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

        #flip_btn = self.sidebar.flip_hist_btn
        #flip_btn.on_click = self.flip_hist

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
                            background-color: #00000066; \
                            '

            self.is_hist_up=True
            self.sidebar.flip_hist_btn.color = 'blue'

#@app.callback( 
#        Output(component_id='paper', component_property='figure'),
#        [
#            Input(component_id='image', component_property='value'),
#            Input(component_id='op_selector', component_property='value'),
#            Input(component_id='reverse-colorspace', component_property='on'),
#            Input(component_id='transfer-style', component_property='value'),
#            Input(component_id='transfer-quality', component_property='value'),
#            Input(component_id='preproc-op', component_property='value'),
#            Input(component_id='preproc-value', component_property='value'),
#            Input(component_id='median_sigma1', component_property='value'),
#            Input(component_id='median_sigma2', component_property='value'),
#            Input(component_id='morpho-op', component_property='value'),
#            Input(component_id='morpho-value', component_property='value'),
#            ],
#        prevent_initial_call=True,
#        supress_callback_exceptions=True)
#def operate(
#        img_path, operation, rev_col,
#        nst_model, quality,       # Neural Style Transfer Variables
#        preproc_op, preproc_value, sigma_1, sigma_2, # Preprocessing
#        morpho_op, morpho_iter, # Morphological Operations
#         ):
#
#    operations.read_img(img_path, width=quality)
#
#    for i, op in enumerate(operation):
#        if op == 'neural-style-transfer':
#            out = style_transfer(operations.img_list[-1], nst_model)
#            operations.img_list.append(out)
#        elif op == 'preprocessing':
#            out = preprocess(
#                    operations.img_list[-1],
#                    preproc_op, 
#                    preproc_value,
#                    sigma_1, sigma_2,)
#            operations.img_list.append(out)
#        elif op == 'morphologycal-operations':
#            out = morphology(
#                    operations.img_list[-1],
#                    morpho_op,
#                    morpho_iter,)
#            operations.img_list.append(out)
#        else:
#            pass
#
#    return operations.return_figure(operations.img_list[-1], rev_col)
#
