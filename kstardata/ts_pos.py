#
def get_ts_pos(shot):   
    if shot < 12273:
        TS_CORE_RPOS = [1807, 1830, 1851, 1874, 1897, 1920, 1943, 1968, 1993, 2018, 2043, 2070, 2096, 2124]
        TS_EDGE_RPOS = [2106, 2124, 2138, 2156, 2173, 2190, 2208, 2223, 2241, 2260, 2276, 2295, 2310]
        # print('YEAR 2014')
    elif (shot >= 12273) and (shot <= 14386):
        TS_CORE_RPOS = [1807, 1830, 1851, 1874, 1897, 1920, 1943, 1968, 1993, 2018, 2043, 2070, 2096, 2124]
        TS_EDGE_RPOS = [2106, 2124, 2138, 2156, 2173, 2190, 2208, 2223, 2241, 2260, 2276, 2295, 2310]
        # print('YEAR 2015')
    elif (shot > 14386) and (shot <= 17356):
        TS_CORE_RPOS = [1807, 1830, 1851, 1874, 1897, 1920, 1943, 1968, 1993, 2018, 2043, 2070, 2096, 2124]
        TS_EDGE_RPOS = [2106, 2124, 2138, 2156, 2173, 2190, 2208, 2223, 2241, 2260, 2276, 2295, 2310]
        # print('YEAR 2016')
    elif (shot > 17356) and (shot <= 19399):
        TS_CORE_RPOS = [1807, 1830, 1851, 1874, 1897, 1920, 1943, 1968, 1993, 2018, 2043, 2070, 2096, 2124]
        TS_EDGE_RPOS = [2106, 2124, 2138, 2156, 2173, 2190, 2208, 2223, 2241, 2260, 2276, 2295, 2310]
        # print('YEAR 2017')
    elif (shot >= 19400) and (shot <= 21778):
        TS_CORE_RPOS = [1807, 1830, 1851, 1874, 1897, 1920, 1943, 1968, 1993, 2018, 2043, 2070, 2096, 2124]
        TS_EDGE_RPOS = [2106, 2124, 2138, 2156, 2173, 2190, 2208, 2223, 2241, 2260, 2276, 2295, 2310]
        # print('YEAR 2018')
    elif shot >= 21779:
        TS_CORE_RPOS = [1806, 1826, 1848, 1871, 1894, 1917, 1942, 1966, 1991, 2016, 2041, 2068, 2093, 2119]
        TS_EDGE_RPOS = [2124, 2137, 2143, 2149, 2156, 2162, 2177, 2191, 2202, 2216, 2229, 2242, 2257, 2271, 2285, 2297, 2311]

    ts_rpos = {}

    for i in range(len(TS_CORE_RPOS)):
        chname = 'TS_CORE{:d}'.format(i+1)
        ts_rpos[chname] = TS_CORE_RPOS[i]

    for i in range(len(TS_EDGE_RPOS)):
        chname = 'TS_EDGE{:d}'.format(i+1)
        ts_rpos[chname] = TS_EDGE_RPOS[i]

    return ts_rpos
