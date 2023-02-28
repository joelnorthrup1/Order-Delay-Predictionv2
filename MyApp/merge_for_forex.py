# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 08:26:16 2022

@author: DELL
"""

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




def country_specific(dataset1,risk,country_name):
  dataset1=pd.DataFrame(dataset1)
  merged_dataframe = pd.merge_asof(dataset1.sort_values('time'),risk[['time','Open','High','Low','Close','Volume']].sort_values('time'),on='time',direction='nearest',tolerance=pd.Timedelta('1y'))
  merged_dataframe.rename({'Open': 'open_'+country_name}, axis=1, inplace=True)
  merged_dataframe.rename({'High': 'high_'+country_name}, axis=1, inplace=True)
  merged_dataframe.rename({'Low': 'low_'+country_name}, axis=1, inplace=True)
  merged_dataframe.rename({'Close': 'close_'+country_name}, axis=1, inplace=True)
  merged_dataframe.rename({'Volume': 'volume_'+country_name}, axis=1, inplace=True)
  return merged_dataframe[['time','open_'+country_name,'high_'+country_name,'low_'+country_name,'close_'+country_name,'volume_'+country_name]]





from sklearn import preprocessing

def merge_for_forex(dataset,risk):
    dataset.rename({'XPCT_DLVRY_DT': 'time'}, axis=1, inplace=True)
    risk.rename({'Date': 'time'}, axis=1, inplace=True)
    dataset["time"] = pd.to_datetime(dataset["time"])
    #dataset=dataset.dropna()
    processing_data=dataset
    all_countries_features=[]
    for i in range(len(risk['Symbol'].unique())):
        print(risk['Symbol'].unique()[i])
        country_name=risk['Symbol'].unique()[i]
        country_4_export=risk['Symbol'].unique()[i]
        country_data=risk.loc[risk['Symbol']==country_4_export]
        country_data=country_data.dropna()
        country_data["time"] = pd.to_datetime(country_data["time"])
        processing_data=country_specific(processing_data['time'],country_data,country_name)
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
