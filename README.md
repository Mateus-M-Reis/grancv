# grancv

Computer vision web application with granulometry purpouses, built on top of [dash](https://github.com/plotly/dash), [plotly](https://github.com/plotly/plotly.py), [opencv](https://opencv.org/),  [dash-bootstrap-components](https://github.com/facultyai/dash-bootstrap-components) and [dash-extensions](https://github.com/thedirtyfew/dash-extensions).

![](demo/gifs/grancv_now.gif)

## Install

Create new conda environment:

`conda env create -f environment.yml`

Activate environment:

`source activate dash`

Install some more packages:

`python -m pip install -r requirements.txt`

Run the app:

`python index.py`

## Operations Available

You can use and tune combinations of the following operations:

- Neural Style Transfer

- - Select one of the available torch .t7 models available in the 'models' folder.
  
  - You can adjust the quality of the final result by changing the image width.

- Preprocessing
  
  - Filtering 
    
    - Simple
    
    - Bilateral Filtering
  
  - Blur
    
    - Simple
    
    - Median Blur 
    
    - Gaussian Blur

- Morphologycal Operations
  
  - Erosion
  
  - Dilatation
  
  - Opening
  
  - Closing
  
  - Gradient
  
  - Top Hat
  
  - Black Hat

- Thresholding
  
  - Simple
    
    - Binary
    
    - Binary Inverse
    
    - To-Zero
    
    - To-Zero Inverse
  
  - Adaptive
    
    - Adaptive mean c
    
    - Adaptive Gaussian c

## To do

This repo is is very initial stage. More operations will be added to the application gradually. Here are some I've thought about:

- Possibility of creating your own operation, from the combinations of wherever you want.

- Choose (and plot) the kernel. All kernel used in the operations are matrices of 1's of size 3 or 5. 

- Scripts to build the application.
