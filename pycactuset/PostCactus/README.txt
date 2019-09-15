==========
PostCactus
==========

This package contains modules to read and represent various CACTUS
data formats in Python, and some utilities for data analysis.
In detail,

* simdir is an abstraction of one or more CACTUS output directories,
  allowing access to data of various type by variable name, and 
  seamlessly combining data split over several directories.
* cactus_grid_h5 reads 1,2 and 3D data from CACTUS hdf5 datasets.
* cactus_grid_omni uses whatever data source it finds, e.g. cut 
  a 3D file to get xy plane data 
* grid_data represents simple and mesh refinened datsets, common
  arithmetic operations on them, as well as interpolation.
* cactus_scalars reads CACTUS 0D ASCII files representing timeseries.
* timeseries represents timeseries and provides resampling numerical
  differentiation.
* fourier_util performs FFT on timeseries and searches for peaks.
* unitconv performs unit conversion with focus on geometric units,
  including predefined CACTUS, PIZZA, and CGS systems.


