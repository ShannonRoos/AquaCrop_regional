# !/usr/bin/env python
import os
import shutil
import numpy as np
from multiprocessing import Pool
from AC_PRM import run_ac_pro_yrs
from COORD_AC import AC_GEOreference
crds= AC_GEOreference()

''' --------------------------------------------------------------------------------------------------------------------------
Executable for AquaCrop, the regional version. With multiprocessing it can be run on the max available cores on a single node.
@ Shannon de Roos 2020
----------------------------------------------------------------------------------------------------------------------------'''


# ------------------------ parallel processing python ------------------------------------------------------------------------

def main():

    row_start = int(719)   # subsetEGU2020: 719-3000
    row_end = int(3600)     #max: 3600
    col_start = int(2400)   #subsetEGU2020: 2400-3540
    col_end = int(3540)     #max: 6660
    args = list()
    for row in np.arange(row_start, row_end + 1):
        for col in np.arange(col_start,col_end + 1):
            args.append((col, row))

    p = Pool(36)    #define number of cores
    p.map(wrapper, args)    #performs actual parallelization


def wrapper(coords):  # wraps all functions into one list of functions

    col, row = coords

    #filenames and directories
    dir_out = '/staging/leuven/stg_00024/OUTPUT/shannondr/AC_OUT/'
    dir_soil = '/staging/leuven/stg_00024/OUTPUT/shannondr/SOL253_vardepth/'
    fname = str(row) + '_' + str(col)
    pa = dir_out  + fname +'/'
    PRM = pa + 'LIST/' + fname + '.PRM'


    if os.path.exists(dir_soil + fname+'.SOL'):
        print('=========', row, col, '=========')

        # Make new local directory for each gridcell
        os.mkdir(pa)
        os.chdir(pa)

        # Place Aquacrop directories SIMUL and LIST in local directory
        shutil.copytree('/data/leuven/329/vsc32926/AC_INPUT_data/SIMUL', pa + 'SIMUL')
        os.mkdir(pa + 'OUTP')
        os.mkdir(pa + 'LIST')
        open(pa + 'LIST/ListProjects.txt', 'w')

        # Link Aquacrop model to current directory
        AC_loc = '/data/leuven/329/vsc32926/AC_Genius/ACsaBareV60'
        os.symlink(AC_loc, pa + 'ACsaBareV60')

        # Run AC Project script if it doesnt already exist
        if not os.path.isfile(PRM):
            run_ac_pro_yrs(row, col, dir, dir_soil)
            os.system('ACsaBareV60')

            #remove extra files and directories: only save PRM and output file
            shutil.copyfile(PRM, pa + fname + '.PRM')
            shutil.rmtree(pa + 'SIMUL')
            shutil.rmtree(pa + 'LIST')
            os.unlink(pa + 'ACsaBareV60')
            os.remove(pa + 'OUTP/AllDone.OUT')
            os.remove(pa + 'OUTP/ListProjectsLoaded.OUT')

main()
