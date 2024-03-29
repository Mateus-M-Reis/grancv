import os
import json
import cv2
# import imutils
# import time

# from IPython.core.display import HTML, display
# from ipywidgets import AppLayout, Layout, Output, Box, HBox, VBox
# from ipycanvas import Canvas, hold_canvas
# import ipyvuetify as v
# v.theme.dark = True
# v.theme.themes.dark.primary = 'colors.cyan.accent2'
# v.theme.themes.dark.secondary = 'colors.red.accent3'
# v.theme.themes.dark.success = 'colors.green.accent3'
# from .vvapp.inputs import button
from .vvapp.outputs import row, column

from .sidebar import Sidebar
from .paper import Paper
from .histogram import Histogram

from .smoothing import (
        smooth,
        smooth_dropd,
        smooth_slider,
        sigma1_slider,
        sigma2_slider,
        sharp_cb,
        alpha_slider,
        beta_slider,
        gamma_slider)
from .morphology import (
        morphology,
        morpho_dropd,
        morpho_slider)
from .thresholding import (
        threshold,
        threshold_dropd,
        threshold_slider,
        threshold_bs_slider,
        threshold_C_slider,
        apply_contours)
from .neural_style_transfer import (
        style_transfer,
        nst_style,
        nst_quality)
from .watershed import (
        op_iter_slider,
        dl_iter_slider,
        sf_factor_slider,
        watershed_seg)


class App():
    """
    Base Operation Class.
    """

    def __init__(self):

        f = open('app/config.json')
        self.cfg = json.load(f)

        self.img_list = []
        self.cur_img = 'Dipping-Sun.jpg'

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

        self.layout = column(children=[
            self.sidebar.drawer,
            row([
                self.paper.canvas,
                self.hist.wid,
                ],
                justify='end',
                align_content='start',
                ),
            ],
            #justify='start',
            #align='center',
            #align_content='center',
            class_='d-flex flex-row mb12',
            style_='\
                    height: 90%; \
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

        if self.sidebar.colorspace_sel.v_model == 'RGB':
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        elif self.sidebar.colorspace_sel.v_model == 'HSV':
            img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        elif self.sidebar.colorspace_sel.v_model == 'LAB':
            img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        elif self.sidebar.colorspace_sel.v_model == 'GRAY':
            img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        self.img_list = [img]
        self.paper.update(self.img_list[-1], self.sidebar.output)
        self.hist.update(self.img_list[-1])

    def flip_hist(self, *args):
        if self.is_hist_up:
            self.hist.wid.style_ = '\
                            display: none; \
                            position: absolute; \
                            background-color: #00000066; \
                            '
            self.is_hist_up = False
            self.sidebar.flip_hist_btn.color = 'grey'
        else:
            self.hist.wid.style_ = '\
                            display: block; \
                            position: absolute; \
                            background-color: #000000BF; \
                            '

            self.is_hist_up = True
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
                if op == 'neural-style-transfer':
                    stylized = style_transfer(
                            self.img_list[-1],
                            nst_style.v_model,
                            nst_quality.v_model,
                            self.sidebar.output,
                            )
                    self.img_list.append(stylized)

                elif op == 'smoothing':
                    smoothed = smooth(
                            self.img_list[-1],
                            smooth_dropd.v_model,
                            smooth_slider.v_model,
                            sigma1_slider.v_model,
                            sigma2_slider.v_model,
                            sharp_cb.v_model,
                            alpha_slider.v_model,
                            beta_slider.v_model,
                            gamma_slider.v_model
                            )
                    self.img_list.append(smoothed)

                elif op == 'thresholding':
                    thresholded = threshold(
                            cv2.cvtColor(self.img_list[-1], cv2.COLOR_RGB2GRAY),
                            threshold_dropd.v_model,
                            threshold_slider.v_model,
                            threshold_bs_slider.v_model,
                            threshold_C_slider.v_model,
                            )
                    if apply_contours.v_model == True:
                        contours, hierarchy= cv2.findContours(
                                thresholded, 
                                cv2.RETR_TREE, 
                                cv2.CHAIN_APPROX_SIMPLE)
                        contoured=cv2.drawContours(
                                self.img_list[-1].copy(), 
                                contours, 
                                -1, 
                                (0, 255, 0))
                        self.img_list.append(contoured)
                    elif apply_contours.v_model == False:
                        self.img_list.append(thresholded)

                elif op == 'morphologycal-operations':
                    morpho = morphology(
                            self.img_list[-1],
                            morpho_dropd.v_model,
                            morpho_slider.v_model,
                            )
                    self.img_list.append(morpho)
                elif op == 'watershed':
                    watersheded = watershed_seg(
                            self.img_list[-1].copy(),
                            op_iter_slider.v_model,
                            dl_iter_slider.v_model,
                            sf_factor_slider.v_model
                            )
                    self.img_list.append(watersheded)

            else:
                if op=='neural-style-transfer':
                    pass
                elif op=='smoothing':
                    pass
                elif op=='thresholding':
                    pass
                elif op=='morphologycal-operations':
                    pass
                elif op=='watershed':
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
sharp_cb.on_event('input', app.operate)
alpha_slider.on_event('input', app.operate)
beta_slider.on_event('input', app.operate)
gamma_slider.on_event('input', app.operate)
# Morphology
morpho_dropd.on_event('input', app.operate)
morpho_slider.on_event('input', app.operate)
# Thresholding
threshold_dropd.on_event('input', app.operate)
threshold_slider.on_event('input', app.operate)
threshold_bs_slider.on_event('input', app.operate)
threshold_C_slider.on_event('input', app.operate)
apply_contours.on_event('input', app.operate)
# Neural Style Transfer
nst_style.on_event('input', app.operate)
nst_quality.on_event('input', app.operate)
# Watershed
op_iter_slider.on_event('input', app.operate)
dl_iter_slider.on_event('input', app.operate)
sf_factor_slider.on_event('input', app.operate)
