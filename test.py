# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 10:45:15 2023

@author: Mirthe
"""

import glob
import os
import numpy as np
import cv2
from scipy.ndimage import gaussian_filter
from skimage import color, morphology
import skimage
from functions import * 
# from skimage.morphology import skeletonize
from skimage import data
import matplotlib.pyplot as plt
from skimage.util import invert
from tifffile import imwrite
import numpy as np

# def main_func(path, string='*ch00*.tif'):
datapath = "Data/mouse_cs/1/"
# datapath = "/home/mkamphuis/public/10 Students/2022/Mirthe Kamphuis/Master Thesis/04_Raw Data/Data/mouse_cs/1/"
# datapath = "/home/mkamphuis/public/10 Students/2022/Mirthe Kamphuis/Master Thesis/05_Processed Data/5/"
# datapath = "/home/mkamphuis/public/10 Students/2022/Mirthe Kamphuis/Master Thesis/08_from XH/other data for PoC/"

os.chdir(datapath)
dirlist = os.listdir()
N = 51
THR = 0.13
dirlist
S = 10
string = '*ch00.tif'
# cel_string = '*C1*.tif'

if(dirlist != 0):
    img = OCY_read_stack(string)

    # use only first N images
    if(img.shape[2]>N):
        img=img[:,:,1:N]

    # Gaussian filter
    img1 = skimage.filters.gaussian(img, sigma=0.65)

    # apply threshold and save initial binary volume
    bin_thr = OCY_thr_stack(img1, THR)

    # morphological filtering, then save processed binary 
    bins = OCY_fill_voids(bin_thr, 10) 

    # detect cells
    cells = OCY_extract_cells(bins)
    cells_wrong = OCY_get_cells(bins)
    # imwrite(datapath+path+'/'+'cells.tif', cells_wrong)
    # nucl = OCY_read_stack(cel_string)
    # cells_thr = OCY_thr_stack(nucl, THR)
    # kernel = np.ones([3,3,3])
    # cells = skimage.morphology.closing(cells_thr, kernel)
    # #calculate initia skeleton 
    skeleton = OCY_skeletonize(bins, cells)
    # imwrite(datapath+path+'/'+'skeleton.tif', skeleton)

    # graph = skel2Graph(skeleton, cells_wrong)

    # return graph


#%%

os.chdir('C:/Users/Mirthe/Documents/GitHub/OCY_connectomics/skel2graph3d-matlab-master')
import matlab.engine
eng = matlab.engine.start_matlab()
eng.OCY_run_Skel2Graph3D(skeleton.astype(bool), cells, 5, nargout=0)
eng.quit()