#import cv2
import os
import json

from IPython.core.display import HTML, display
import ipyvuetify as v
from ipywidgets import Output, Layout
from .vvapp.inputs import (
        button, 
        select_or_create, 
        select,
        radio_buttons,
        )
from .vvapp.outputs import container, row, column

#from . import app
#from .neural_style_transfer import nst_wid, transfer_style
from .smoothing import smooth_expp
#from .thresholding import threshold_wid
from .morphology import morpho_expp

class Sidebar():

    def __init__(self, flip_func):

        f = open('app/config.json')
        self.cfg = json.load(f)

        # Colorspace Seletor
        self.colorspace_btn = button(
                class_='ma-4',
                size='small',
                fab=True,
                color='primary',
                icon='mdi-rotate-orbit',
                outlined=True,
                style_='width:35px; height: 35px'
                )
        self.colorspace_btns = radio_buttons(
                row=True,
                choices=['RGB', 'HSV', 'LAB', 'GRAY'],
                v_model='RGB',
                style_='font-size=12px',
                )

        # Image Selector
        self.img_selector = select(
                items=self.cfg['images']['content_images_file'],
                v_model='desmonte.jpg',
                style_='height: 15px',
                )
        
        # Upload button
        self.upload_btn = button(
                class_='ma-4',
                style_='width:35px; height: 35px',
                size='small',
                fab=True,
                color='primary',
                icon='mdi-upload',
                outlined=True,
                )
        
        # Turn Histogram Up Switch
        self.flip_hist_btn = button(
                class_='ma-4',
                style_='width:35px; height: 35px',
                color='blue',
                size='small',
                fab=True,
                icon='mdi-chart-histogram',
                outlined=True,
                on_click=flip_func,
                )

        self.save_op_btn = button(
                class_='ma-4',
                style_='width:35px; height: 35px',
                color='blue',
                size='small',
                fab=True,
                icon='mdi-content-save',
                outlined=True,
                #on_click=flip_func,
                )

        # Operations Selector
        self.op_selector = select_or_create(
                items= self.cfg['operations'],
                v_model='smoothing',
                multiple=True,
                )

        # Operations Panel
        self.op_panel = v.ExpansionPanels(
                children=[
                    smooth_expp,
                    morpho_expp
                    ],
                )
        
        # Sidebar Layout
        self.drawer = v.NavigationDrawer(
                class_='ma-2',
                v_model=True,
                #expand_on_hover=True,
                #absolute=True,
                fixed=True,
                dark=True,
                #permanent=True,
                color='#111111',
                width='400px',
                children=[
                    row(dense=True, children=[

                        row(children=[
                            column(
                                children=[self.upload_btn],
                                cols=3,
                                ),
                            column(
                                children=[self.img_selector],
                                cols=9,
                                ),
                            ],
                            no_gutters=True,
                            style_='\
                                    height: 50px; \
                                '
                            ),
                        row(children=[
                            column(
                                children=[self.colorspace_btn],
                                cols=3,
                                ),
                            column(
                                children=[self.colorspace_btns],
                                cols=9,
                                ),
                            ],
                            no_gutters=True,
                            style_='\
                                    height: 50px; \
                                '
                            ),
                        row(children=[
                            column(
                                children=[self.flip_hist_btn],
                                cols=3,
                                ),
                            column(
                                children=[],
                                cols=9,
                                ),
                            ],
                            no_gutters=True,
                            style_='\
                                    height: 50px; \
                                '
                            ),
                        row(children=[
                            column(
                                children=[self.save_op_btn],
                                cols=3,
                                ),
                            column(
                                children=[self.op_selector],
                                cols=9,
                                )
                            ],
                            no_gutters=True,
                            style_='\
                                    height: 50px; \
                                '
                            ),
                        row(children=[
                            self.op_panel,
                            ],
                            no_gutters=True,
                            style_='\
                                    width: 100%; \
                                    height: 100%; \
                                    border: 1px solid red; \
                                '
                            ),

                        ])
                    ],
                )

    def return_layout(self):
        return self.layout

#@app.callback(
#        Output(component_id='op-panel',component_property='children'),
#        [Input(component_id='op_selector',component_property='value')],
#        prevent_initial_call=True)
#def update_content(operation):
#
#    print(operation, '\n')
#    for i, op in enumerate(sidebar.ops.keys()):
#
#        if op not in operation:
#            sidebar.op_panel.children.remove(sidebar.ops[op])
#            sidebar.op_panel.children.append(sidebar.ops[op])
#
#            sidebar.op_panel.children[
#                    len(sidebar.op_panel.children)-1
#                    ].className='inv'
#
#        else:
#            sidebar.op_panel.children.remove(sidebar.ops[op])
#            sidebar.op_panel.children.append(sidebar.ops[op])
#
#            sidebar.op_panel.children[
#                    len(sidebar.op_panel.children)-1
#                    ].className='appear'
#
#    return sidebar.op_panel.children
