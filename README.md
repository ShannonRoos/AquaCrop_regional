# AquaCrop_regional
With this code you can excute AquaCrop (https://www.fao.org/aquacrop/en/) in parallel for regional applications 

_Code to run the spatial AquaCrop model:_

AC_exec.py: wrapper that executes AquaCrop in parrallel using the multiprocessing package

AC_PRM.py: code to create an AquaCrop Project Management File (.PRM) for successive years. This PRM file contains all the input data with their paths that AquaCrop requires.

_Supporting scripts:_

COORD_AC.py: contains functions to transform row/col numbers to lat/lon values (HWSDv1.2)

acout_filestructure.py: contains the header names and the row numbers that need to be skipped when reading in AquaCrop output as a dataframe in Python. Column length depends on the soil depth (deeper soils are divided into more layers, where each soil layer produces an extra column for water content and soil salinity)

_* Please note that the AquaCrop executable should be downloaded seperately from https://zenodo.org/record/4770738#.ZBrmqnbMKUk_
