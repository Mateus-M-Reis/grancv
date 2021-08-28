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
        self.f_input = v.FileInput(show_progress=True)

        # Turn Histogram Up Switch
        self.flip_hist_btn = button(
                class_='ma-4',
                style_='width:35px; height: 35px',
                color='primary',
                size='small',
                fab=True,
                icon='mdi-chart-histogram',
                outlined=True,
                on_click=flip_func,
                )

        self.save_op_btn = button(
                class_='ma-4',
                style_='width:35px; height: 35px',
                color='primary',
                size='small',
                fab=True,
                icon='mdi-content-save',
                outlined=True,
                #on_click=flip_func,
                )

        self.github_btn = button(
                class_='ma-4',
                style_='width:35px; height: 35px',
                size='small',
                fab=True,
                color='primary',
                icon='mdi-source-repository',
                outlined=True,
                href='https://github.com/Mateus-M-Reis/grancv',
                target='_blank',
                )

        self.save_chart_btn = button(
                class_='ma-4',
                style_='width:35px; height: 35px',
                size='small',
                fab=True,
                color='secondary',
                icon='mdi-chart-histogram',
                #outlined=True,
                )

        self.save_img_btn = button(
                class_='ma-4',
                style_='width:35px; height: 35px',
                size='small',
                fab=True,
                color='secondary',
                icon='mdi-image-plus',
                #outlined=True,
                )

        self.show_console_btn = button(
                class_='ma-4',
                style_='width:35px; height: 35px',
                size='small',
                fab=True,
                color='secondary',
                icon='mdi-console-line',
                ##outlined=True,
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
        self.drawer = v.Card(
                children = [ 

                    v.NavigationDrawer(
                        width='425px',
                        dark=True,
                        color='#FF000000',
                        expand_on_hover=True,
                        mini_variant_width='75px',
                        fixed=True, # *
                        floating=True,
                        permanent=True,
                        #mini_variant=True,
                        #app=True,
                        #disable_route_watcher=True,
                        #disable_resize_watcher=True,
                        #v_model='drawer',
                        #hide_overlay=True,
                        #clipped=True,
                        #absolute=True,
                        #touchless=True,
                        children=[

                            v.List(children=[ 
                                v.ListItem(children=[
                                    self.upload_btn, 
                                    self.img_selector
                                    ],
                                    class_='d-flex align-stretch mb-6',
                                    style_='height: 40px;'
                                    ),
                                v.ListItem(children=[
                                    self.flip_hist_btn, 
                                    self.colorspace_sel
                                    ], 
                                    class_='d-flex align-stretch mb-6',
                                    style_='height: 40px;'
                                    ),
                                v.ListItem(
                                    children=[
                                        self.save_op_btn,
                                        self.save_img_btn,
                                        self.save_chart_btn,
                                        self.show_console_btn,
                                        ],
                                    class_='d-flex align-stretch mb-6',
                                    style_='\
                                            height: 40px; \
                                            '
                                    ),
                                v.ListItem(
                                    children=[
                                        self.github_btn,
                                        self.op_selector,
                                        ],
                                    class_='d-flex align-stretch mb-6',
                                        style_='\
                                            height: 100%; \
                                            '
                                    ),

                                ],
                                style_='background-color: #000000BF'
                                ),

                            v.Divider(),
                            v.List(
                                children=[

                                    v.ListItem(
                                        children=[
                                            self.op_panel,
                                            ],
                                            class_='d-flex align-stretch mb-6',
                                            style_='\
                                                width: 100%; \
                                                height: 100%; \
                                                '
                                        ),

                                ])

                            ]) 

                ], 
                class_='d-flex flex-column mb-12',
            ) 

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
                            f' \
                            display: block; \
                            order: {cur_opts.index(op)}; \
                            background-color: #000000BF \
                            '
                    pass
                elif op=='smoothing':
                    smooth_expp.style_=\
                            f' \
                            display: block; \
                            order: {cur_opts.index(op)}; \
                            background-color: #000000BF; \
                            '
                    pass
                elif op=='thresholding':
                    threshold_expp.style_=\
                            f' \
                            display: block; \
                            order: {cur_opts.index(op)}; \
                            background-color: #000000BF \
                            '
                    pass
                elif op=='morphologycal-operations':
                    morpho_expp.style_=\
                            f' \
                            display: block; \
                            order: {cur_opts.index(op)}; \
                            background-color: #000000BF \
                            '
                    pass

            else:

                if op=='neural-style-transfer':
                    nst_expp.style_=' \
                            display: none; \
                            background-color: #000000BF \
                            '
                    pass
                elif op=='smoothing':
                    smooth_expp.style_=' \
                            display: none; \
                            background-color: #000000BF \
                            '
                    pass
                elif op=='thresholding':
                    threshold_expp.style_=' \
                            display: none; \
                            background-color: #000000BF \
                            '
                    pass
                elif op=='morphologycal-operations':
                    morpho_expp.style_=' \
                            display: none; \
                            background-color: #000000BF \
                            '
                    pass
