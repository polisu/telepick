#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 10:41:22 2018

Author: Po-Li Su @ NCU
"""
import sys
sys.path.append("/home/peter/0_wrk/Code/PhasePApy")
from obspy.core import *
import numpy as np
#from phasepapy.phasepicker import aicdpicker
#from obspy.core import *



events=np.genfromtxt('dir.lis',dtype='str')
com="HHZ"
filend=".decon.p"
for event in events:
    print(event)
    st=read(event+"/*"+com+"*"+filend)
    year=st[0].stats.sac.nzyear
    jday=st[0].stats.sac.nzjday
    hour=st[0].stats.sac.nzhour
    min=st[0].stats.sac.nzmin
    sec=st[0].stats.sac.nzsec
    msec=1000*st[0].stats.sac.nzmsec
    origin=UTCDateTime(year=year,julday=jday,hour=hour,minute=min,second=sec,microsecond=msec)
    tr=st[0]
    tr.plot()
    tr.detrend(type='demean')
    tr.plot()
    
    
    #st.plot()
#pick(each trace)
#snr(each trace)
# for loop:
    #select(each trace)
    #stack
    #pick(stack)
    #window(stack)   find p wave window
    #cut(stack) (obspy trace method)
    #match(each trace)
    #uncertainty(stack trace and then each trace)
    #eval stopping criteria
    #if pass break
#else:



#def pick(self,:   
        
#    def snr(self,pick):
#        
#    def select:
#        
#    def window(self, phase):
#        
#    def match(self, stack_phase):
#        
#    def uncertainty:
        
        