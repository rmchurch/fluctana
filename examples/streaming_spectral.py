#!/usr/bin python

#perform spectral analysis on streaming KSTAR ECEi data

from fluctana import *

##do ADIOS streaming read setup
#TODO: Integrate with Ralph. For now assume cfg the adios2 object for initial, 
#one-off configuration read in, and fstream the adios2 object for data stream
#cfg will include BOTH attrs found in ECEi HDF5 files AND analysis config
cfg = read_cfg()
fstream = read_stream()

#TODO: Will stream metadata at beginning also? Or how will we pass? For now assume
#it has all parameters, accessible from cfg

#number of vertical and radial channels
NV = 24
NR = 8

#TODO: Need to read in METADATA file
A = FluctAna()
#TODO: Modify so it can take in a cfg set
dobjAll = KstarEcei(cfg=cfg,clist=['ECEI_L0101-2408'])

#TODO: Determine if for loops can be avoided (I dont think currecnt fluctana
#structure easily allows)
for i,chunk in enumerate(fstream):
    #TODO: what is the right adios2 calls for this? Look at Ralphs
    data = fstream.get_data()
    #TODO: Determine how to get time range of adios2 chunk
    trange = fstream.get_time()
    #TODO: Do we want norm here for all analyses?
    if i==0:
        A.add_data(dobjAll,trange=trange,norm=1)
    else:
        A.Dlist[0].data = data
        #TODO: Add new time info here so it is saved 

    A.fftbins(nfft=cfg['nfft'],window=cfg['window'],
              overlap=cfg['overlap'],detrend=cfg['detrend'],full=1)

    #perform the various spectral analyses from fluctana
    #TODO: Currently n^2, could be 2x more efficient by subsetting the dataset
    #TODO: Subsetting would avoid the 2nd datasset creation, FFT
    for iv in range(NV):
        for ir in range(NR):
            #TODO: Generalize clist input (should take ECEi L,H,G systems)
            #iclist = ['ECEI_L'+str(iv).zfill(2)+str(ir).zfill(2)]
            done_subset = [iv*NV + ir]
            dtwo_subset = range(done_subset[0],NV*NR)

            #1 cwt
            #TODO: Decide on cwt, need to remove autoplot
            #A.cwt()
            #save_spec(A)
            #2 cross_power
            A.cross_power(done=0,dtwo=0, done_subset=done_subset, dtwo_subset=dtwo_subset)
            save_spec(A) #TODO: determine how to save in aggregate
            #3 coherence
            A.coherence(done=0,dtwo=0, done_subset=done_subset, dtwo_subset=dtwo_subset)
            save_spec(A)
            #4 cross-phase
            A.cross_phase(done=0,dtwo=0, done_subset=done_subset, dtwo_subset=dtwo_subset)
            save_spec(A)
            #5 correlation
            A.correlation(done=0,dtwo=0, done_subset=done_subset, dtwo_subset=dtwo_subset)
            save_spec(A)
            #6 corr_coef
            A.corr_coef(done=0,dtwo=0, done_subset=done_subset, dtwo_subset=dtwo_subset)
            save_spec(A)
            #7 xspec
            #TODO xspec has rnum=cnum, so have to do one at a time, decide best way
            #A.xspec(done=0,dtwo=0, done_subset=done_subset, dtwo_subset=dtwo_subset, plot=False)
            #save_spec(A)
            #8 skw
            #TODO: not same ref/cmp channel setup, check
            A.skw(done=0,dtwo=0, done_subset=done_subset, dtwo_subset=dtwo_subset, plot=False)
            save_spec(A)
            #9 bicoherence
            A.bicoherence(done=0,dtwo=0, , done_subset=done_subset, dtwo_subset=dtwo_subset, plot=False)
            save_spec(A)

