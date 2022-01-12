import cv2
import ipyvuetify as v
from .vvapp.inputs import slider, select
from .vvapp.outputs import container, row, column

opening_slider = slider(
        min=0,
        max=6,
        step=1,
        v_model=0,
        ticks=False
        )

dilate_slider = slider(
        min=0,
        max=6,
        step=1,
        v_model=0,
        ticks=False
        )
