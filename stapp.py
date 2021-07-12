import time 
import numpy as np
#from PIL import Image
import cv2
import json
import streamlit as st 
from streamlit_echarts import st_echarts, st_pyecharts
st.set_page_config(layout="wide")

from app.stsidebar import Sidebar
from app.histogram import Histogram
#from input_type import image_input, webcam_input

#style_model_name = st.sidebar.selectbox("Choose the style model: ", style_models_name)

class App():
	
	def __init__(self):
		# Local css
		def local_css(file_name):
			with open(file_name) as f:
				st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
		local_css('assets/style.css')

		f = open('app/config.json')
		self.cfg = json.load(f)

		self.center = st.beta_container()
		self.r_sidebar = st.beta_container()
		self.center, self.r_sidebar = st.beta_columns([3,1])

		self.root_img = cv2.cvtColor(
			cv2.imread('input/images/tubingen.jpg'),
			cv2.COLOR_BGR2RGB
			)
		self.cur_img = self.root_img
		self.final_img = self.root_img
		self.center.image(
				self.root_img,
				use_column_width=True
				)

		# Sidebar
		self.sidebar = Sidebar()

		# Right sidebar
		self.hist = Histogram(self.cur_img)
		import time
		with self.r_sidebar:
			st_echarts(self.hist.options)
			time.sleep(3)
			self.hist.options.data.shuffle()
			st_echarts(self.hist.options)


app = App()
