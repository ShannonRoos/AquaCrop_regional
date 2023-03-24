#!/usr/bin/env python

def ac_columns(len):
    if len == 95:
        ACout_cols = ['Day', 'Month', 'Year', 'DAP', 'Stage', 'WC(1.55)_a', 'Rain_a', 'Irri', 'surf', 'Infilt',
                      'RO', 'Drain', 'CR',
                      'Zgwt_a', 'Ex', 'E', 'E/Ex', 'Trx_a', 'Tr_a', 'Tr/Trx_a', 'ETx', 'ET', 'ET/ETx', 'GD',
                      'Z_a', 'StExp', 'StSto',
                      'StSen', 'StSalt', 'StWeed', 'CC', 'CCw', 'StTrc', 'Kc(Tr)', 'Trx', 'Tr', 'TrW',
                      'Tr/Trx', 'WP', 'Biomass',
                      'HI', 'YieldPart', 'Brelative', 'WPet', 'WC(x)', 'Wr(x)', 'Z_b', 'Wr', 'Wr(SAT)',
                      'Wr(FC)', 'Wr(exp)',
                      'Wr(sto)', 'Wr(sen)', 'Wr(PWP)', 'SaltIn', 'SaltOut', 'SaltUp', 'Salt(1.55)', 'Salt',
                      'Z_c', 'ECe', 'ECsw',
                      'StSalt', 'Zgwt', 'ECgwf', 'WC01', 'WC02', 'WC03', 'WC04', 'WC05', 'WC06', 'WC07', 'WC08',
                      'WC09', 'WC10', 'WC11', 'WC12', 'ECe01', 'ECe02', 'ECe03', 'ECe04', 'ECe05', 'ECe06', 'ECe07',
                      'ECe08', 'ECe09', 'ECe10', 'Ece11', 'Ece12', 'Rain', 'ETo', 'Tmin', 'Tavg', 'Tmax', 'CO2']

    elif len == 93:
        ACout_cols = ['Day', 'Month', 'Year', 'DAP', 'Stage', 'WC(1.55)_a', 'Rain_a', 'Irri', 'surf', 'Infilt',
                      'RO', 'Drain', 'CR',
                      'Zgwt_a', 'Ex', 'E', 'E/Ex', 'Trx_a', 'Tr_a', 'Tr/Trx_a', 'ETx', 'ET', 'ET/ETx', 'GD',
                      'Z_a', 'StExp', 'StSto',
                      'StSen', 'StSalt', 'StWeed', 'CC', 'CCw', 'StTrc', 'Kc(Tr)', 'Trx', 'Tr', 'TrW',
                      'Tr/Trx', 'WP', 'Biomass',
                      'HI', 'YieldPart', 'Brelative', 'WPet', 'WC(x)', 'Wr(x)', 'Z_b', 'Wr', 'Wr(SAT)',
                      'Wr(FC)', 'Wr(exp)',
                      'Wr(sto)', 'Wr(sen)', 'Wr(PWP)', 'SaltIn', 'SaltOut', 'SaltUp', 'Salt(1.55)', 'Salt',
                      'Z_c', 'ECe', 'ECsw',
                      'StSalt', 'Zgwt', 'ECgwf', 'WC01', 'WC02', 'WC03', 'WC04', 'WC05', 'WC06', 'WC07', 'WC08',
                      'WC09', 'WC10', 'WC11',
                      'ECe01', 'ECe02', 'ECe03', 'ECe04', 'ECe05', 'ECe06', 'ECe07',
                      'ECe08', 'ECe09', 'ECe10', 'Ece11',
                      'Rain', 'ETo', 'Tmin', 'Tavg', 'Tmax', 'CO2']
    elif len == 91:
        ACout_cols = ['Day', 'Month', 'Year', 'DAP', 'Stage', 'WC(1.55)_a', 'Rain_a', 'Irri', 'surf', 'Infilt',
                      'RO', 'Drain', 'CR',
                      'Zgwt_a', 'Ex', 'E', 'E/Ex', 'Trx_a', 'Tr_a', 'Tr/Trx_a', 'ETx', 'ET', 'ET/ETx', 'GD',
                      'Z_a', 'StExp', 'StSto',
                      'StSen', 'StSalt', 'StWeed', 'CC', 'CCw', 'StTrc', 'Kc(Tr)', 'Trx', 'Tr', 'TrW',
                      'Tr/Trx', 'WP', 'Biomass',
                      'HI', 'YieldPart', 'Brelative', 'WPet', 'WC(x)', 'Wr(x)', 'Z_b', 'Wr', 'Wr(SAT)',
                      'Wr(FC)', 'Wr(exp)',
                      'Wr(sto)', 'Wr(sen)', 'Wr(PWP)', 'SaltIn', 'SaltOut', 'SaltUp', 'Salt(1.55)', 'Salt',
                      'Z_c', 'ECe', 'ECsw',
                      'StSalt', 'Zgwt', 'ECgwf', 'WC01', 'WC02', 'WC03', 'WC04', 'WC05', 'WC06', 'WC07', 'WC08',
                      'WC09', 'WC10', 'ECe01', 'ECe02', 'ECe03', 'ECe04', 'ECe05', 'ECe06', 'ECe07',
                      'ECe08', 'ECe09', 'ECe10', 'Rain', 'ETo', 'Tmin', 'Tavg', 'Tmax', 'CO2']
    else:
        ACout_cols = print('check number of columns AC output', len)
    return(ACout_cols)
def ac_skiprows(yearstart, yearend):
    if yearstart ==2011 and yearend==2018:
        skiprows = [0, 1, 2, 3, 4, 370, 371, 372, 373, 740, 741, 742, 743, 1109, 1110, 1111, 1112, 1478,1479, 1480, 1481, 1847, 1848, 1849, 1850, 2217, 2218, 2219, 2220, 2586, 2587, 2588,2589]
    else:
        skiprows = print('check years AC output')
    return(skiprows)
