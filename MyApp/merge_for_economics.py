# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 17:30:18 2022

@author: DELL
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 08:39:01 2022

@author: DELL
"""
import pandas as pd
import random




def country_specific(duration,direction,dataset1,risk,column_name,country_name):
  dataset1=pd.DataFrame(dataset1)
  print("Direction: "+str(direction)+"Duration: ",str(duration))
  if(direction=='backward'):
    print("Date Before: "+str(dataset1.time[0]))
    dataset1['ntime']=pd.DatetimeIndex(dataset1.time) - pd.DateOffset(int(duration[:-1]))
    print("Date After: "+str(dataset1.ntime[0]))
    print(int(duration[:-1]))
  merged_dataframe = pd.merge_asof(dataset1.sort_values('ntime'),risk[['ntime','Value']].sort_values('ntime'),on='ntime',direction=direction,tolerance=pd.Timedelta("1y"))
  merged_dataframe.rename({'Value': column_name+'_'+country_name}, axis=1, inplace=True)
  return merged_dataframe[['time',column_name+'_'+country_name]]





from sklearn import preprocessing

def merge_for_economics(duration,direction,dataset,risk,column_name):
    dataset.rename({'XPCT_DLVRY_DT': 'time'}, axis=1, inplace=True)
    risk.rename({'DateTime': 'ntime'}, axis=1, inplace=True)
    dataset["time"] = pd.to_datetime(dataset["time"])
    #dataset=dataset.dropna(axis=1)
    processing_data=dataset
    all_countries_features=[]
    for i in range(len(risk['HistoricalDataSymbol'].unique())):
        print(risk['HistoricalDataSymbol'].unique()[i])
        country_name=risk['HistoricalDataSymbol'].unique()[i]
        country_4_export=risk['HistoricalDataSymbol'].unique()[i]
        country_data=risk.loc[risk['HistoricalDataSymbol']==country_4_export]
        country_data=country_data.dropna()
        country_data["ntime"] = pd.to_datetime(country_data["ntime"])
        processing_data=country_specific(duration,direction,processing_data['time'],country_data,column_name,country_name)
        all_countries_features=pd.concat([pd.DataFrame(all_countries_features),processing_data],axis=1)
        if(i==0):

            all_countries_features.rename({'time': 'date'}, axis=1, inplace=True)
        if(i>2):
            all_countries_features=all_countries_features.drop(['time'],axis=1)
    dataset=dataset.sort_values(by='time')
    all_countries_features.rename({'date': 'time'}, axis=1, inplace=True)
    all_countries_features=pd.DataFrame(all_countries_features).dropna(axis=1)
    columns_list=list(all_countries_features.columns)
    #print(columns_list)
    columns_list.remove('time')
    all_countries_features=pd.DataFrame(all_countries_features.drop('time',axis=1)) #preprocessing.normalize(all_countries_features.drop('time',axis=1))
    #print(columns_list,all_countries_features.columns)
    all_countries_features.columns=columns_list
    try:
      all_countries_features=all_countries_features.drop(["level_0"],axis=1)
    except:
      print("ok")
    try:
      dataset=dataset.drop(["level_0"],axis=1)
    except:
      print("ok")
    final=pd.concat([dataset.reset_index(),all_countries_features.reset_index()],axis=1)

    try:
      final=final.drop(["level_0"],axis=1)
    except:
      print("ok")
    
    return final
