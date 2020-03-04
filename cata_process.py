#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 10:12:55 2018

@author: peter
"""
from obspy import UTCDateTime
from obspy.geodetics import gps2dist_azimuth
class Event():
    def __init__(self, cata, num, ot, lon, lat, dep, mag):
        self.cata = cata
        self.num = num
        self.ot = ot
        self.lon = lon
        self.lat = lat
        self.dep = dep
        self.mag = mag
        self.it  = 0
        self.pair=[]

    def findpair(self,event2,radius=50,timelag=30,option=''):
        if option=='nosecond':
            timediff=self.dtimenosecond(event2)
        else:
            timediff=self.dtime(event2)

        if timediff < timelag or timelag <0:
            distance=self.dist(event2)
            if distance < radius or radius < 0:
                self.pair.append((event2.num,distance))
                self.pair.sort(key=lambda x:x[1])

    def dist(self,event2):
        #latd2km=110.76698
        #lond2km=101.27423
        #dlon=(self.lon-event2.lon)*lond2km
        #dlat=(self.lat-event2.lat)*latd2km
        distm, az ,baz = gps2dist_azimuth(self.lat,self.lon,event2.lat,event2.lon)
        dist=distm/1000.
        ddep=(self.dep-event2.dep)
        dist=(dist**2+ddep**2)**0.5
        return dist

    def dtime(self,event2):
        dtime=abs(self.ot-event2.ot)
        return dtime

    def dtimenosecond(self,event2):
        ot1=UTCDateTime(self.ot)
        ot2=UTCDateTime(event2.ot)
        ot1.second=0
        ot2.second=0
        dtime=abs(ot1-ot2)
        return dtime
    
    def ask(self,used,cata1):
        if ( len(self.pair) > self.it ):
            key=self.pair[self.it][0]               #key=cata2.num of current it
            value=(self.num,self.pair[self.it][1])  #first item=cata1.num, second item=distance
            if key in used:
                if value[1] < used[key][1] :  #if value < current stored distance
                    old=used[key][0]          #current stored cata1.num
                    cata1[old].it=cata1[old].it+1
                    cata1[old].ask(used,cata1)          #recursive ask
                    used[key]=value
                
                elif value[1] > used[key][1] :
                    self.it= self.it+1
                    self.ask(used,cata1)
            else:
                used[key]=value

    def output(self,cata2,option='compare'):
        if ( len(self.pair) > self.it ):
#            print(self.num,self.pair,self.pair[self.it])
            event2=cata2[self.pair[self.it][0]]
            if option=='compare':
                print(self.ot,self.lon,self.lat,self.dep,self.mag,event2.num,event2.ot,event2.lon,event2.lat,event2.dep,event2.mag)
            else:
                print(self.ot-event2.ot, self.lon-event2.lon, self.lat-event2.lat, self.dep-event2.dep)
        else:
#            print(self.num,self.pair,"NONE")
            if option=='compare':
                print(self.ot,self.lon,self.lat,self.dep,self.mag,"N")
