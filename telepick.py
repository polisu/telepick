#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 10:41:22 2018

Author: Po-Li Su @ NCU
"""

import obspy
import numpy as np

events=np.genfromtxt('dir.lis',dtype='str')
com="HHZ"
filend=".decon.p"
for event in events:
    print(event)
    sac=obspy.read(event+"/*"+com+"*"+filend)
    year=sac[0].stats.sac.nzyear
    jday=sac[0].stats.sac.nzjday
    hour=sac[0].stats.sac.nzhour
    min=sac[0].stats.sac.nzmin
    sec=sac[0].stats.sac.nzsec
    msec=1000*sac[0].stats.sac.nzmsec
    origin=obspy.UTCDateTime(year=year,julday=jday,hour=hour,minute=min,second=sec,microsecond=msec)
    #predict
    #snr(each trace)
    #stack
    #pick(stack)
    #window(stack)
    #snr(stack)
    #xcorr
    #eval
    
    
    #origin=obspy.UTCDateTime(year=sac[0].sac, julday=299, hour=9, minute=9,second=42, microsecond=20)
    
    
#def 