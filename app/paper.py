import cv2
from IPython.core.display import display
from ipywidgets import Output, Layout
from ipycanvas import Canvas, hold_canvas


class Paper():
    """
    Base paper class.
    """

    def __init__(self, img):

        self.img = img
        self.width = 1080
        self.height = 770
        self.canvas = Canvas(
                width=self.width,
                height=self.height,
                )
        self.output = Output(
                layout=Layout(
                    width='1170px',
                    height='770px',
                    min_height='90vh',
                    overflow='hidden hidden'
                    ),
                )
        with self.output:
            display(self.canvas)

        def put_image():
            resized = cv2.resize(
                    img,
                    (self.width, self.height), interpolation=cv2.INTER_AREA)
            self.canvas.put_image_data(resized, 0, 0)

        self.canvas.on_client_ready(put_image)

    def update(self, img, out):

        resized = cv2.resize(
                       img,
                       (self.width, self.height),
                       interpolation=cv2.INTER_AREA
                       )

        with hold_canvas(self.canvas):
            self.canvas.clear()
            self.canvas.put_image_data(resized, 0, 0)
