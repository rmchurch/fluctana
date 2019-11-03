import sys, os
sys.path.append(os.pardir)
from fluctana import *

# HOW TO RUN
# ./python3 check_xspec.py 10186 [15,16] ECEI_L1303 ECEI_L1403

shot = 18431 
trange = [0,9]
clist = [['ECEI_L1102'], ['ECEI_L0906']]

# call fluctana
A = FluctAna()

# add data
A.add_data(KstarEcei(shot=shot, clist=clist[0], data_path='./'), trange=trange, norm=1)
A.add_data(KstarEcei(shot=shot, clist=clist[1], data_path='./'), trange=trange, norm=1)

# list data
A.list_data()

# xspec parameters 
# frequency resolution ~ sampling frequency / nfft
nfft = 2048
# temporal resolution 
overlap = 0.5 # finest overlap = (nfft-1.0)/nfft
# for full frequency range, full=1 (e.g. MIR). Else full=0.
A.fftbins(nfft=nfft, window='kaiser', overlap=overlap, detrend=0, full=0)

# calculate the cross power spectrogram using data sets done and dtwo; thres = threshold for significance
A.xspec(done=0,dtwo=1,thres=0.1)
