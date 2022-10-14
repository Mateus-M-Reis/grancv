import numpy as np
import cv2
import bqplot.pyplot as plt
import ipyvuetify as v


class Histogram():
    """
    Base Histogram Class.
    Receives image, checks its dimensions and plot the apropriate histogram.
    """

    def __init__(self, img):

        self.colors = ['red', 'green', 'blue']

        self.ax_options = {
                'x': {
                    'label': 'Intensity',
                    'label_color': 'white',
                    'label_offset': '5ex',
                    'orientation': 'horizontal',
                    'color': 'white',
                    'grid_lines': 'none',
                    },
                'y': {
                    'label': 'Frequency',
                    'label_color': 'white',
                    'label_offset': '8ex',
                    'orientation': 'vertical',
                    'color': 'white',
                    'grid_lines': 'none',
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
                    'width': '550px'
                    },
                fig_margin={
                    'top': 25,
                    'bottom': 50,
                    'left': 75,
                    'right': 25
                    },
                 )

        if len(img.shape) == 3:
            for i, color in enumerate(self.colors):
                histr = cv2.calcHist([img], [i], None, [256], [0, 256])
                plt.plot(
                        x=np.arange(0, 257, 1),
                        y=histr.flatten(),
                        colors=[color],
                        stroke_width=1.2,
                        axes_options=self.ax_options,
                        fill='bottom',
                        fill_opacities=[0.2],
                        )

        elif len(img.shape) == 2:
            hist = cv2.calcHist([img], None, [256], [0, 256])
            plt.plot(
                    x=np.arange(0, 257, 1),
                    y=hist,
                    color='white',
                    stroke_width=1.2,
                    axes_options=self.ax_options,
                    fill='bottom',
                    fill_opacities=[0.2]
                    )
        self.wid = v.Card(children=[
                    self.fig],
                    style_='\
                            display: block; \
                            position: absolute; \
                            background-color: #000000BF; \
                            '
                    )

    def update(self, img):
        """
        Check image shape and update histogram accordingly.
        """

        if len(img.shape) == 3:
            for i, color in enumerate(self.colors):
                histr = cv2.calcHist([img], [i], None, [256], [0, 256])
                self.fig.marks[i].y = histr

        elif len(img.shape) == 2:
            hist = cv2.calcHist([img], [0], None, [256], [0, 256])
            for i in range(3):
                self.fig.marks[i].y = hist
