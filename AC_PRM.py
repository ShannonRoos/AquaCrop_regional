#!/usr/bin/env python
import pandas as pd
import numpy as np
import os
from datetime import datetime
from netCDF4 import Dataset
from defParam import parameters
par = parameters()
from COORD_AC import AC_GEOreference, mindist, MERRA2_GEOreference
crds = AC_GEOreference()
Mcrds = MERRA2_GEOreference()

'''---------------------------------------------------------------------------------------------------------------------
This script creates a Project Management File as input for AquaCrop, containing the information of CLI, SOL, CRO & MAN.
 It has to be executed before AquaCrop is executed.
 -----------------------------------------------------------------------------------------------------------------------'''

def run_ac_pro_yrs(row,col,dir_out, DirSoil):
    locs = str(row) + '_' + str(col)
    fsoil = locs
    MANfile = 'SFR30'
    Dirsupfiles = '   ' + '/data/leuven/329/vsc32926/AC_INPUT_data/input_files/\n'
    DirCrop = '   ' + '/data/leuven/329/vsc32926/AC_INPUT_data/input_files/\n'
    crop= 'Gen365_Tb8_sen232'
    fname_default = locs
    fname = fname_default
    Dirnew = dir_out + fname +'/'

    # Define lat lon pixel
    lat = crds.row_to_lat(row) # FILL in ISIMIP_lat
    lon = crds.col_to_lon(col)  # FILL in ISIMIP_lon

    if os.path.exists(DirSoil + fsoil +'.SOL'):
        print(locs, 'agriculture Dominant')

        # Find correct climate file:
        lat_id, lon_id = mindist(lat, Mcrds.CLI_latrange), mindist(lon, Mcrds.CLI_lonrange)
        cliname= str(lat_id) + '_'+ str(lon_id)
        Dir_cli = '/staging/leuven/stg_00024/OUTPUT/shannondr/CLI_files/' + cliname + '_EU36km/'

        '''------------------------------------------PROJECT FILE-------------------------------------------------------'''

        fid = open(Dirnew + 'LIST/'+ fname +'.PRM','w')

        #------------------------------years cropping and simulation periods---------------------------------------------------------------#
        # Start at 1 Jan
        sim_s = ['2011-01-01','2012-01-01','2013-01-01','2014-01-01','2015-01-01','2016-01-01','2017-01-01','2018-01-01' ]
        sim_e = ['2011-12-31','2012-12-31','2013-12-31','2014-12-31','2015-12-31','2016-12-31','2017-12-31','2018-12-31']
        crop_s = ['2011-01-01','2012-01-01','2013-01-01','2014-01-01','2015-01-01','2016-01-01','2017-01-01','2018-01-01']
        crop_e = ['2011-12-31','2012-12-30','2013-12-31','2014-12-31','2015-12-31','2016-12-30','2017-12-31','2018-12-31']

        years= len(sim_s)       #How many annual simulation runs?
        print(years)

        #--------------------------------------------------file-input--------------------------------------------------------------#
        syears = len(sim_s)
        print(syears)
        nan= 'nan'

        '''file for each year in successive order'''
        name_crop = [crop, crop, crop,crop, crop, crop, crop, crop]
        name_irr = [nan, nan, nan, nan, nan, nan, nan, nan]
        name_man = [MANfile, MANfile, MANfile,MANfile, MANfile, MANfile,MANfile, MANfile]
        name_gwt = [nan, nan, nan, nan, nan, nan, nan, nan]
        name_sw0 = [nan, nan, nan, nan, nan, nan, nan, nan]
        name_off = [nan, nan, nan, nan, nan, nan, nan, nan]

        #-------------------------------------------------------------------------------------------------------------------------#

        fid.write(fname+ ' Lon_Lat Project file\n')
        fid.write('\t %3.1f\t'%par.version + '\t: AquaCrop Version (march 2017)\n')

        #------------------------------convert dates to day numbers---------------------------------------------------------------#
        list = [sim_s[0], sim_e[0], crop_s[0], crop_e[0]]
        day = []
        for i in list:
            strip = datetime.strptime(i, '%Y-%m-%d')
            month = [0, 0, 31, 59.25, 90.25, 120.25, 151.25, 181.25, 212.25, 243.25, 273.25, 304.25, 334.25]
            daynmr = int((strip.year - 1901) * 365.25 + month[strip.month] + strip.day)
            day.append(daynmr)

        SDsim = day[0]#42004            #first day of simulation period
        EDsim = day[1] #42369            #last day of simulation period
        SDcrop = day[2] #42095              #first day of cropping period
        EDcrop = day[3] #42277             #last day of cropping period


        #---------------------------------------write Project file-------------------------------------------------------------------------#
        fid.write('\t %d\t'%SDsim + '\t: First day of simulation period  - ' + sim_s[0] + '\n')
        fid.write('\t %d\t'%EDsim + '\t: Last day of simulation period  - ' + sim_e[0] + '\n')
        fid.write('\t %d\t'%SDcrop + '\t: First day of cropping period  - ' + crop_s[0] + '\n')
        fid.write('\t %d\t'%EDcrop + '\t: Last day of cropping period  - ' + crop_e[0] + '\n')
        fid.write('\t %d\t'%par.ETdec + '\t: Evaporation decline factor for stage II \n')
        fid.write('\t %4.2f\t'%par.Kex + '\t: Ke(x) Soil evaporation coefficient (fully wet and non-shaded)\n')
        fid.write('\t %d\t'%par.CCHI + '\t: Threshold for CC below HI can no longer increase (% cover)\n')
        fid.write('\t %d\t'%par.RZD + '\t: Starting depth of root zone expansion curve (% of Zmin)\n')
        fid.write('\t %4.2f\t'%par.RZexpmax + '\t: Maximum allowable root zone expansion (fixed at 5 cm/day)\n')
        fid.write('\t %d\t'%par.shpRZ + '\t: Shape factor for effect water stress on root zone expansion\n')
        fid.write('\t %d\t'%par.swcGer + '\t: Required soil water content in soil for germination (% TAW)\n')
        fid.write('\t %3.1f\t'%par.Fdepl + '\t: Adjustment factor for soil water depletion (p) by ETo\n')
        fid.write('\t %d\t'%par.aerdays + '\t: Number days after which deficient aeration is fully effective\n')
        fid.write('\t %4.2f\t'%par.senesps + '\t: Exponent of senescence adjusting photosynthetic activity\n')
        fid.write('\t %d\t'%par.Psendec + '\t: Decrease of p(sen) once senescence is triggered (% of p(sen))\n')
        fid.write('\t %d\t'%par.deplDep + '\t: Thickness top soil (cm) for determination of water depletion\n')
        fid.write('\t %d\t'%par.ETDep + '\t: Depth [cm] of profile affected by soil evaporation\n')
        fid.write('\t %4.2f\t'%par.CNDep + '\t: Considered depth (m) for CN adjustment\n')
        fid.write('\t %d\t'%par.CNaSM + '\t: CN is adjusted to Antecedent Moisture Class\n')
        fid.write('\t %d\t'%par.salDiff + '\t: salt diffusion factor [%]\n')
        fid.write('\t %d\t'%par.Salsol + '\t: salt solubility [g/liter]\n')
        fid.write('\t %d\t'%par.shpswcCR + '\t: shape factor for effect of soil water content on CR\n')
        fid.write('\t %3.1f\t'%par.defMinT + '\t: Default minimum temperature (°C)\n')
        fid.write('\t %3.1f\t'%par.defMaxT + '\t: Default maximum temperature (°C)\n')
        fid.write('\t %d\t'%par.defGDD + '\t: Default method for the calculation of growing degree days Reference\n')

        CLI= ['-- 1. Climate (CLI) file\n',
             '   ' + cliname + '_.CLI\n'
             '   ' + Dir_cli +  '\n'
             '   1.1 Temperature (TNx or TMP) file\n'
             '   ' + cliname + '_.Tnx\n'
             '   ' + Dir_cli + '\n'
             '   1.2 Reference ET (ETo) file\n'
             '   ' + cliname + '_.ETo\n'
             '   ' + Dir_cli + '\n'
             '   1.3 Rain (PLU) file\n'
             '   ' + cliname + '_.PLU\n'
             '   ' + Dir_cli +'\n'
             '   1.4 Atmospheric CO2 concentration (CO2) file\n'
             '   MaunaLoa.CO2\n'
             '   ' + Dirnew + 'SIMUL/\n' ]
        fid.writelines(CLI)

        CROP= ['-- 2. CROP (CRO) file\n',
              '   ' + name_crop[0] + '.CRO\n',
               DirCrop]
        fid.writelines(CROP)

        if name_irr[0] == nan:
            irrfile = '   (None)\n'
            irrdir = '   (None)\n'
        else:
            irrfile = '   ' + name_irr[0] + '.IRR\n'
            irrdir =Dirsupfiles
        IRR= ['-- 3. Irrigation management (IRR) file\n',
              irrfile,
              irrdir]
        fid.writelines(IRR)

        if name_man[0] == nan:
            manfile = '   (None)\n'
            mandir = '   (None)\n'
        else:
            print('MAN in PRM')
            manfile = '   ' + name_man[0] + '.MAN\n'
            mandir = Dirsupfiles
        MAN= ['-- 4. Field management (MAN) file\n',
              manfile,
              mandir]
        fid.writelines(MAN)

        SOL= ['-- 5. Soil profile (SOL) file\n',
              '   ' + fsoil + '.SOL\n',
              '   ' + DirSoil + '\n']
        fid.writelines(SOL)

        if name_gwt[0] == nan:
            gwtfile = '   (None)\n'
            gwtdir = '   (None)\n'
        else:
            gwtfile = '   '+ name_gwt[0] + '.GWT\n'
            gwtdir = Dirsupfiles
        GWT= ['-- 6. Groundwater table (GWT) file\n',
              gwtfile,
              gwtdir]
        fid.writelines(GWT)

        if name_sw0[0] == nan:
            inifile = '   (None)\n'
            inidir = '   (None)\n'
        else:
            inifile = '   '+ name_sw0[0] + '.SW0\n'
            inidir = Dirsupfiles
        INI= ['-- 7. Initial conditions (SW0) file\n',
              inifile,
              inidir]
        fid.writelines(INI)

        if name_off[0] == nan:
            offfile = '   (None)\n'
            offdir = '   (None)\n'
        else:
            offfile = '   '+ name_off[0] + '.OFF\n'
            offdir = Dirsupfiles
        OFF= ['-- 8. Off-season conditions (OFF) file\n',
              offfile,
              offdir]
        fid.writelines(OFF)
        # print('first year done')

        ''' =====================================
        ============= Successive years ==========
        ========================================='''
        if years > 0:
            for syear in range(syears):
                if syear>0:
                    n = syear
                    list = [sim_s[n], sim_e[n], crop_s[n], crop_e[n]]
                    day = []
                    for i in list:
                        strip = datetime.strptime(i, '%Y-%m-%d')
                        month = [0, 0, 31, 59.25, 90.25, 120.25, 151.25, 181.25, 212.25, 243.25, 273.25, 304.25, 334.25]
                        daynmr = int((strip.year - 1901) * 365.25 + month[strip.month] + strip.day)
                        day.append(daynmr)

                    SDsim = day[0]  # 42004            #first day of simulation period
                    EDsim = day[1]  # 42369            #last day of simulation period'
                    SDcrop = day[2]  # 42095              #first day of cropping period
                    EDcrop = day[3]  # 42277             #last day of cropping period


                    simul=['  %d  '%SDsim + '         : First day of simulation period  - '+sim_s[n]+ '\n',
                    '  %d  '%EDsim + '         : Last day of simulation period  - '+sim_e[n]+ '\n',
                    '  %d  '%SDcrop + '         : First day of cropping period  - '+crop_s[n]+ '\n',
                    '  %d  '%EDcrop + '         : Last day of cropping period  - '+crop_e[n]+ '\n']
                    fid.writelines(simul)
                    fid.writelines(CLI)
                    CROP = ['-- 2. CROP (CRO) file\n',
                            '   ' + name_crop[n] + '.CRO\n',
                            Dirsupfiles]
                    fid.writelines(CROP)

                    if name_irr[n] == nan:
                        irrfile = '   (None)\n'
                        irrdir = '   (None)\n'
                    else:
                        irrfile = '   ' + name_irr[n] + '.IRR\n'
                        irrdir = Dirsupfiles
                    IRR = ['-- 3. Irrigation management (IRR) file\n',
                           irrfile,
                           irrdir]
                    fid.writelines(IRR)

                    if name_man[n] == nan:
                        manfile = '   (None)\n'
                        mandir = '   (None)\n'
                    else:
                        manfile = '   ' + name_man[n] + '.MAN\n'
                        mandir = Dirsupfiles
                    MAN = ['-- 4. Field management (MAN) file\n',
                           manfile,
                           mandir]
                    fid.writelines(MAN)

                    SOL = ['-- 5. Soil profile (SOL) file\n',
                           '   ' + fsoil + '.SOL\n',
                           '   ' + DirSoil + '\n']
                    fid.writelines(SOL)

                    if name_gwt[n] == nan:
                        gwtfile = '   (None)\n'
                        gwtdir = '   (None)\n'
                    else:
                        gwtfile = '   ' + name_gwt[n] + '.GWT\n'
                        gwtdir = Dirsupfiles
                    GWT = ['-- 6. Groundwater table (GWT) file\n',
                           gwtfile,
                           gwtdir]
                    fid.writelines(GWT)

                    INI = ['-- 7. Initial conditions (SW0) file\n',
                           '   KeepSWC\n'
                           '   Keep soil water profile of previous run\n']
                    fid.writelines(INI)

                    if name_off[n] == nan:
                        offfile = '   (None)\n'
                        offdir = '   (None)\n'
                    else:
                        offfile = '   ' + name_off[n] + '.OFF\n'
                        offdir = Dirsupfiles
                    OFF = ['-- 8. Off-season conditions (OFF) file\n',
                           offfile,
                           offdir]
                    fid.writelines(OFF)
            fid.writelines('\n')

        fid.close()

        with open(Dirnew +'LIST/ListProjects.txt', 'a') as file:
            file.write(fname+'.PRM\n')
    else:
        print('no dominant rainfed agriculture')
        pass
