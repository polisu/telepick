#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mar 4 16:44:0 2020

Author: Po-Li Su @ NCU
"""

import sys
from obspy.core import *
#import numpy as np

#Main
###  Initiate
directory=sys.argv[1]
com="HHZ"
filend=".decon.p"
st=read(directory+"/*"+com+"*"+filend)
#origin=UTCDateTime(year=year,julday=jday,hour=hour,minute=min,second=sec,microsecond=msec)
nfile=len(st)
#tp=[origin+st[i].stats.sac.t0 for i in range(0,nfile)]
st.plot()
st.detrend(type='demean')
st.detrend(type='linear')
st.filter('bandpass',freqmin=0.1, freqmax=1.0)
st.taper(max_percentage=0.1)
st.detrend(type='demean')
st.detrend(type='linear')


st.plot()

#groups[0]=Group()
#for tr in st:
#        groups[0].newmember(tr)
#
##***PARALLEL
#groups[0].members[0].arrival, uncertainty=aicpicker(groups[0].member[i].trace)
#
#### Group Loop
#it=0
#while len(groups[0].members) > 0:
#    it += 1
#    groups[0].members.sort(key=uncertainty)
#    groups[it]=Group()
#    Move(groups[0].members[0],groups[it])
#### Member Loop
#    while true:
#        Xcorr(groups[it])
#        groups[0].members.sort(key=ccc)
#        if (groups[0].members[0].ccc >= 0.85) then
#            Move(groups[0].members[0],groups[it])
#        else
#            exit
#
#        
