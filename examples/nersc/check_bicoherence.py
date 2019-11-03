import sys, os
sys.path.append(os.pardir)
from fluctana import *

# HOW TO RUN
# ./python3 check_correlation.py 10186 [15.9,16] ECEI_L1303 ECEI_L1403

shot = 18431 
trange = [2,3]
clist = [['ECEI_L1102'], ['ECEI_L0906']]

# call fluctana
A = FluctAna()

# add data
A.add_data(KstarEcei(shot=shot, clist=clist[1], data_path='./'), trange=trange, norm=1)
A.add_data(KstarEcei(shot=shot, clist=clist[1], data_path='./'), trange=trange, norm=1)

# list data
A.list_data()

# do fft; full = 1 
A.fftbins(nfft=512,window='hann',overlap=0.5,detrend=0,full=1)

# calculate correlation using data sets done and dtwo. results are saved in A.Dlist[dtwo].val
A.bicoherence(done=0, dtwo=1)
