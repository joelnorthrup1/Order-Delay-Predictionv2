# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 17:49:55 2022

@author: DELL
"""

import pandas as pd
import numpy as np
import datetime
#wind=pd.read_csv("./ext_data/geo_political_risk.csv").reset_index(True)
#rsd=datetime.datetime.strptime(wind['ReportTime'][0][:10],'%Y-%m-%d')
# dataset1=pd.read_csv("../../../Project3/dataset1.csv")

# date1=[]
# for i in range(len(wind)):
#     rsd=datetime.datetime.strptime(wind['ReportTime'][i][:10],'%Y-%m-%d')
#     date1.append(rsd)
    
# date2=[]
# for i in range(len(wind)):
#     rsd=datetime.datetime.strptime(dataset1['XPCT_DLVRY_DT'][i],'%Y-%m-%d')
#     date2.append(rsd)


def indx_min_dif(date1,date2):
    print("hello")
    minimum=[]
    final=[]
    mini=0
    for i in range(len(date1)):
        print(i)
        for j in range(len(date2)):
            diff=np.abs((date1[i]-date2[j]).days)
            minimum.append(diff)
        index=minimum.index(min(minimum))

        final.append(index)
        minimum=[]
    print(len(final))
    return final
        
# indx_min_dif(date1,date2)