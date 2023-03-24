#!/usr/bin/env python
from datetime import datetime

# Function to convert dates into AquaCrop numbers:
def date_to_number(list_dates):
    days = []
    for i in list_dates:
        strip = datetime.strptime(i, '%Y-%m-%d')
        month = [0, 0, 31, 59.25, 90.25, 120.25, 151.25, 181.25, 212.25, 243.25, 273.25, 304.25, 334.25]
        daynmr = int((strip.year - 1901) * 365.25 + month[strip.month] + strip.day)
        days.append(daynmr)
    return (days)


class parameters():
    def __init__(self):
        # ------------------------------------------PRM parameters----------------------------------------------------------#
        self.version = 6.1  # AquaCrop version
        self.ETdec = 4  # evaporation decline factor for stage II
        self.Kex = 1.10  # Ke(x) Soil evaporation coefficient (fully wet and non-shaded)
        self.CCHI = 5  # threshold for CC below HI can no longer increase (% cover)
        self.RZD = 70  # starting depth of root zone expansion curve (% of Zmin)
        self.RZexpmax = 5.00  # maximum allowable root zone expansion (fixed at 5 cm/day)
        self.shpRZ = -6  # shape factor for effect water stress on root zone expansion
        self.swcGer = 20  # required soil water content in soil for germination (% TAW)
        self.Fdepl = 1.0  # adjustment factor for soil water depletion (p) by ETo
        self.aerdays = 3  # number days after which deficient aeration is fully effective
        self.senesps = 1.00  # exponent of senescence adjusting photosynthetic activity
        self.Psendec = 12  # decrease of p(sen) once senescence is triggered (% of p(sen))
        self.deplDep = 10  # thickness top soil (cm) for determination of water depletion
        self.ETDep = 30  # depth [cm] of profile affected by soil evaporation
        self.CNDep = 0.30  # considered depth (m) for CN adjustment
        self.CNaSM = 1  # 1 CN is adjusted to Antecedent Moisture Class
        self.salDiff = 20  # salt diffusion factor [%]
        self.Salsol = 100  # salt solubility [g/liter]
        self.shpswcCR = 16  # shape factor for effect of soil water content on CR
        self.defMinT = 12.0  # default minimum temperature (°C) 28.0 : Default maximum temperature (°C)
        self.defMaxT = 28.0  # default minimum temperature (°C) 28.0 : Default maximum temperature (°C)
        self.defGDD = 3  # default method for the calculation of growing degree days Reference
