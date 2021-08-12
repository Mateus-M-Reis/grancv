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
from .neural_style_transfer import nst_expp
from .smoothing import smooth_expp
from .thresholding import threshold_expp
from .morphology import morpho_expp

class Sidebar():

    def __init__(self, flip_func):

        f = open('app/config.json')
        self.cfg = json.load(f)

        self.output = Output()

        # Colorspace Seletor
        self.colorspace_sel = select(
                items=['RGB', 'HSV', 'LAB', 'GRAY'],
                v_model='RGB',
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
                items= list(self.cfg['operations'].values()),
                v_model='neural-style-transfer',
                multiple=True,
                )
        self.op_selector.on_event(
                'change',
                self.update_expansion_panel
                )

        # Operations Panel
        self.op_panel = v.ExpansionPanels(
                children=[
                    smooth_expp,
                    morpho_expp,
                    threshold_expp,
                    nst_expp,
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
                                children=[self.flip_hist_btn],
                                cols=3,
                                ),
                            column(
                                children=[self.colorspace_sel],
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
                                    height: 100%; \
                                '
                            ),
                        row(children=[
                            column(
                                children=[self.op_panel],
                                cols=12,
                                )
                            ],
                            no_gutters=True,
                            style_='\
                                    width: 100%; \
                                    height: 100%; \
                                '
                            ),
                        row(children=[
                            column(
                                children=[self.output],
                                cols=12,
                                )
                            ],
                            no_gutters=True,
                            style_='\
                                    width: 100%; \
                                    height: 100%; \
                                '
                            ),


                        ],
                        #style_=''
                        )
                    ],
                )

    def return_layout(self):
        return self.layout

    def update_expansion_panel(self, *args):
        """
        Update expansion panel children.
        """
        op_opts = list(self.cfg['operations'].values())
        cur_opts = self.op_selector.v_model

        for op in op_opts:

            if op in cur_opts:

                if op=='neural-style-transfer':
                    nst_expp.style_=\
                            f'display: block; order: {cur_opts.index(op)}'
                    pass
                elif op=='smoothing':
                    smooth_expp.style_=\
                            f'display: block; order: {cur_opts.index(op)}'
                    pass
                elif op=='thresholding':
                    threshold_expp.style_=\
                            f'display: block; order: {cur_opts.index(op)}'
                    pass
                elif op=='morphologycal-operations':
                    morpho_expp.style_=\
                            f'display: block; order: {cur_opts.index(op)}'
                    pass

            else:

                if op=='neural-style-transfer':
                    nst_expp.style_='display: none;'
                    pass
                elif op=='smoothing':
                    smooth_expp.style_='display: none;'
                    pass
                elif op=='thresholding':
                    threshold_expp.style_='display: none;'
                    pass
                elif op=='morphologycal-operations':
                    morpho_expp.style_='display: none;'
                    pass
