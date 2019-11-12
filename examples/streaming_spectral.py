#!/usr/bin python

#perform spectral analysis on streaming KSTAR ECEi data

from fluctana import *

##do ADIOS streaming read setup
#TODO: Integrate with Ralph. For now assume cfg the adios2 object for initial, 
#one-off configuration read in, and fstream the adios2 object for data stream
#cfg will include BOTH attrs found in ECEi HDF5 files AND analysis config
#TODO Split cfg so reading ECEi params from streaming data, FFT params from local config (?)
class read_stream(object):
    def __init__(self,shot,nchunk,data_path='./'):
        self.dobj = KstarEcei(shot=shot,data_path=filedir,clist=['ECEI_L0101-2408'])
        self.time = self.dobj.time_base()
        tstarts = self.time[::nchunk]
        tstops = self.time[nchunk-1::nchunk]
        if tstarts.size>tstops.size: tstarts = tstarts[:-1]
        self.timeiter = iter(zip(tstarts,tstops))

    def get_data(self):
        trange = next(self.timeiter)
        _,data = self.dobj.get_data(trange=trange,norm=1,verbose=0)
        return trange,data

debug = True
if debug:
    shot = 18431; nchunk=10000
    fstream = read_stream(shot=shot)
    cfg = {'shot':shot,'nfft':1000,'window':'hann','overlap':0.2,'detrend':1,
           'tt',fstream.dobj.tt,'toff',fstream.dobj.toff,'fs',fstream.dobj.fs,
           'itf',fstream.dobj.itf,'mode',fstream.dobj.mode,'hn`',fstream.dobj.hn,
           'lo',fstream.dobj.lo,'sf',fstream.dobj.sf,'sz',fstream.dobj.sz}
else:
    cfg = read_cfg()
    fstream = read_stream()

#TODO: Will stream metadata at beginning also? Or how will we pass? For now assume
#it has all parameters, accessible from cfg

#number of vertical and radial channels
NV = 24
NR = 8

A = FluctAna()
#TODO: Modify so it can take in a cfg set
dobjAll = KstarEcei(shot=cfg['shot'],cfg=cfg,clist=['ECEI_L0101-2408'])

#TODO: Placeholder for data saving
def save_spec(A):
    pass

#TODO: Determine if for loops can be avoided (I dont think currecnt fluctana
#structure easily allows)
for i,chunk in enumerate(fstream):
    #TODO: what is the right adios2 calls for this? Look at Ralphs
    trange,data = fstream.get_data()
    #TODO: Determine how to get time range of adios2 chunk
    #trange = fstream.get_trange()
    #TODO: Do we want norm here for all analyses?
    if i==0:
        A.Dlist.append(dobjAll)    
    A.Dlist[0].data = data
    #TODO: Add new time info here so it is saved 

    A.fftbins(nfft=cfg['nfft'],window=cfg['window'],
              overlap=cfg['overlap'],detrend=cfg['detrend'],full=1)

    #perform the various spectral analyses from fluctana
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

