from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_daq as daq
import plotly.express as px
import cv2
import os
import json

from . import app
from .neural_style_transfer import nst_wid, transfer_style
from .preprocessing import preproc_wid
from .thresholding import threshold_wid
from .morphology import morpho_wid

class Sidebar():

    def __init__(self):

        f = open('app/config.json')
        self.cfg = json.load(f)
        self.cur_ops={'preprocessing': preproc_wid}
        self.ops={
                'neural-style-transfer': nst_wid,
                'preprocessing': preproc_wid,
                'thresholding': threshold_wid,
                'morphologycal-operations': morpho_wid,
                }

        # Image Selector
        self.img_selector = dcc.Dropdown(
                id='image',
                options=[],
                style={'color': 'white'},
                )
        for i, content in enumerate(self.cfg['images']['content_images_file']):
            self.img_selector.options.append({
                'label': content,
                'value': content })
            self.img_selector.value = 'Alan.jpg'
        
        # Upload button
        self.upload_btn = dbc.Button(
                html.Span([
                    html.I(className="fas fa-upload" )
                    ]), style={'width': '100%', 'height':'100%'}
                )
        
        # Reverse Colorspace Switch
        self.rev_colorspace = daq.BooleanSwitch(
                id='reverse-colorspace',
                on=False,
                style={'height': '8px'},
                label='Reverse Colorspace',
                labelPosition='left',
                )

        # Turn Histogram Up Switch
        self.is_up = daq.BooleanSwitch(
                id='is-up',
                on=False,
                label='Show Histogram',
                labelPosition='left',
                )

        # Operations Selector
        self.op_selector = dcc.Dropdown(
                id='op_selector',
                options=self.cfg['operations'],
                multi=True,
                value=[
                    'preprocessing',
                    ],
                style={'color': 'white'},
                )

        # Operations Panel
        self.op_panel = html.Div(
                id='op-panel',
                children=[
                    nst_wid, 
                    preproc_wid,
                    threshold_wid,
                    morpho_wid,
                    ])
        
        # Sidebar Layout
        self.layout = dbc.Col([

            dbc.Row([
                dbc.Col([self.img_selector], width=9), 
                dbc.Col([self.upload_btn], width=3), 
                ]),
            html.Br(),
            
            dbc.Row([
                dbc.Col(
                    [ self.rev_colorspace ], width=6,
                    #style={ 'border': '1px solid red'}
                    ), 
                dbc.Col([ self.is_up ], width=6,
                    #style={ 'border': '1px solid red' }
                    ), 
                ],
                style={
                    'height': '40px', 
                    #'border': '1px solid white',
                    'justify-content': 'space-between',
                    }),
            html.Br(),

            self.op_selector,
            html.Br(),

            self.op_panel,

            ], 
            className='sidebar', width=10)

    def return_layout(self):
        return self.layout

sidebar = Sidebar()

@app.callback(
        Output(component_id='op-panel',component_property='children'),
        [Input(component_id='op_selector',component_property='value')],
        prevent_initial_call=True)
def update_content(operation):

    print(operation, '\n')
    for i, op in enumerate(sidebar.ops.keys()):

        if op not in operation:
            sidebar.op_panel.children.remove(sidebar.ops[op])
            sidebar.op_panel.children.append(sidebar.ops[op])

            sidebar.op_panel.children[
                    len(sidebar.op_panel.children)-1
                    ].className='inv'

        else:
            sidebar.op_panel.children.remove(sidebar.ops[op])
            sidebar.op_panel.children.append(sidebar.ops[op])

            sidebar.op_panel.children[
                    len(sidebar.op_panel.children)-1
                    ].className='appear'

    return sidebar.op_panel.children
