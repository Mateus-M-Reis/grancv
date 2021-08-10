import numpy as np
import cv2
import bqplot as bq
import bqplot.pyplot as plt

from .vvapp.outputs import container, row, column

class Histogram():
    """
    Base Histogram Class.
    Receives image, verifys its dimensions and plot the apropriate histogram. 
    """
    def __init__(self, img):

        self.colors = ['magenta', 'green', 'cyan']

        xs = bq.LinearScale(min=0, max=256)
        ys = bq.LinearScale(min=0, max=256)

        self.ax_options = {
                'x': {
                    'label': 'Intensity',
                    'orientation': 'horizontal',
                    'color': 'white',
                    'grid_lines': 'none', 
                    #'grid_color': 'black',
                    }, 
                'y': {
                    'label': 'Frequency', 
                    'orientation': 'vertical', 
                    'color': 'white',
                    'grid_lines': 'none', 
                    #'grid_color': 'black',
                    }
                }

        self.fig = plt.figure(
                0, 
                title='Histogram', 
                title_style={'font-size': '16px'}, 
                legend_location='top-right',
                background_style={'fill': '#FF000000'},
                axes_options=self.ax_options,
                animation_duration=1000, 
                padding_y=0,
                layout={
                    'height': '400px', 
                    'width': '700px'
                    }, 
                fig_margin={
                    'top':30,
                    'bottom':40, 
                    'left':60, 
                    'right':30
                    },
                 )
        for i, color in enumerate(self.colors):
            histr = cv2.calcHist([img],[i],None,[256],[0,256])
            plt.plot(
                    x=np.arange(0, 257, 1), 
                    y=histr.flatten(), 
                    colors=[color],
                    stroke_width=1.2,
                    axes_options=self.ax_options,
                    fill='bottom',
                    fill_opacities=[0.2],
                    #scales=
                    #interpolation=
                    )

        self.wid = row(children=[
                    self.fig
                    ],
                    justify='end',
                    style_='\
                            display: block; \
                            position: absolute; \
                            background-color: #000000BF; \
                            '
                    )
