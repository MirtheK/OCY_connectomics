# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 10:45:15 2023

@author: Mirthe
"""

# import matlab.engine
from mayavi import mlab
import numpy as np

data = np.random.random((100,100,100))

mlab.pipeline.volume(mlab.pipeline.scalar_field(data))
mlab.show()

# eng = matlab.engine.start_matlab()

# # eng = matlab.engine.start_matlab("Users\Mirthe\Docments\GiHub\OCY_connectomics\OCY_main")

# eng.Skel2Graph3D(nargout=0)
# eng.quit()

