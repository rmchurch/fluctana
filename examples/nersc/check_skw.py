# coding: utf-8
import fluctana as fa

shot=18431
trange=[7.0,7.5]
clist = [['ECEI_L1203','ECEI_L1303','ECEI_L1403','ECEI_L1503'],
        ['ECEI_L1303','ECEI_L1403','ECEI_L1503','ECEI_L1603']]

A = fa.FluctAna()
A.add_data(fa.KstarEcei(shot=shot,clist=clist[0],data_path='./'),trange=trange,norm=1)
A.add_data(fa.KstarEcei(shot=shot,clist=clist[1],data_path='./'),trange=trange,norm=1)
A.list_data()
A.fftbins(nfft=512,window='hann',overlap=0.5,detrend=0)
A.skw(done=0, dtwo=1, kstep=0.01)
