import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
from flask_caching import Cache
import plotly.graph_objects as go
import plotly.express as px
import os
import json
import cv2
import imutils
import time

FA = "https://use.fontawesome.com/releases/v5.15.1/css/all.css"
app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY, FA])

cache = Cache( 
        app.server, 
        config={
            'CACHE_TYPE': 'filesystem',
            'CACHE_DIR': 'cache-directory'
            }
        )
app.config.suppress_callback_exceptions = True

from .paper import paper
from .sidebar import sidebar
from .histogram import Histogram

from .neural_style_transfer import style_transfer 
from .preprocessing import preprocess#, update_preproc_items
from .morphology import morphology

class Operations():
    """
    Base Operation Class.
    """
    def __init__(self):

        f = open('app/config.json')
        self.cfg = json.load(f)
       
        self.img_list = []
        self.img_list.append(
                #cv2.cvtColor(
                    cv2.imread(
                        os.path.join(
                            self.cfg['images']['path'],
                            'Alan.jpg'
                            )
                        #),
                    #cv2.COLOR_BGR2RGB
                    )
                )

        self.cur_path = 'Alan.jpg'

        self.sidebar=sidebar
        self.paper=paper
        self.histogram = Histogram(self.img_list[-1])

        self.layout = html.Div([
            dcc.Location(id="url"),
            dbc.Row([

                self.sidebar.return_layout(),

                dbc.Col(
                    [ 
                        self.paper, 
                        dbc.Row(
                            [self.histogram.graph],
                            justify='end',
                            style={
                                'margin-right': '10px',
                                'margin-top': '10px',
                                })
                        ], 
                    width={'size': 10},
                    className='col-graph')
                ], 
                no_gutters=True, 
                style={'width': '100%', 'height': '100%'},
                )
            ], 
            className='paper',
            style={ 
                'height': '100vh', 
                'overflow': 'hidden', 
                }
            )

    @cache.memoize(timeout=20)
    def read_img(self, path, width):

        self.cur_path = path
        self.img_list = []

        img = cv2.imread(
                os.path.join(
                    self.cfg['images']['path'],
                    self.cur_path)
                )

        img = imutils.resize(img, width=width)
        self.img_list.append(img)

    def return_figure(self, im, rev=False):

        if rev==True:
            pass
        else:
            im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

        fig = px.imshow(im, template='plotly_dark')
        fig.update_layout(
                margin={"l": 0, "r": 0, "t": 0, "b": 0},
                showlegend=False,
                xaxis_showgrid=False, 
                yaxis_showgrid=False)
        fig.update_xaxes(showticklabels=False)
        fig.update_yaxes(showticklabels=False)

        return fig

operations = Operations()
app.layout = operations.layout

@app.callback( 
        Output(component_id='paper', component_property='figure'),
        [
            Input(component_id='image', component_property='value'),
            Input(component_id='op_selector', component_property='value'),
            Input(component_id='reverse-colorspace', component_property='on'),
            Input(component_id='transfer-style', component_property='value'),
            Input(component_id='transfer-quality', component_property='value'),
            Input(component_id='preproc-op', component_property='value'),
            Input(component_id='preproc-value', component_property='value'),
            Input(component_id='median_sigma1', component_property='value'),
            Input(component_id='median_sigma2', component_property='value'),
            Input(component_id='morpho-op', component_property='value'),
            Input(component_id='morpho-value', component_property='value'),
            ],
        prevent_initial_call=True,
        supress_callback_exceptions=True)
def operate(
        img_path, operation, rev_col,
        nst_model, quality,       # Neural Style Transfer Variables
        preproc_op, preproc_value, sigma_1, sigma_2, # Preprocessing
        morpho_op, morpho_iter, # Morphological Operations
         ):

    operations.read_img(img_path, width=quality)

    for i, op in enumerate(operation):
        if op == 'neural-style-transfer':
            out = style_transfer(operations.img_list[-1], nst_model)
            operations.img_list.append(out)
        elif op == 'preprocessing':
            out = preprocess(
                    operations.img_list[-1],
                    preproc_op, 
                    preproc_value,
                    sigma_1, sigma_2,)
            operations.img_list.append(out)
        elif op == 'morphologycal-operations':
            out = morphology(
                    operations.img_list[-1],
                    morpho_op,
                    morpho_iter,)
            operations.img_list.append(out)
        else:
            pass

    return operations.return_figure(operations.img_list[-1], rev_col)

# Show/Hide Histogram
@app.callback(
        Output(component_id='graph', component_property='style'),
        [Input(component_id='is-up', component_property='on')],
        prevent_initial_call=True,
        )
def flip_histogram(is_up):
    return operations.histogram.flip(is_up)

## Update Histogram
#@app.callback(
#        Output(component_id='graph', component_property='figure'),
#        [Input(component_id='paper', component_property='figure')],
#        prevent_initial_call=False,
#        )
#def update_histogram(fig):
#    return operations.histogram.update(operations.img_list[-1])
