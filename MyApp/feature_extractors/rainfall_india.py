# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 20:53:55 2022

@author: DELL
"""



import numpy as np
import pandas as pd
import datetime
import os
from MyApp.feature_extractors.date_diff import indx_min_dif
#from lib.constants import PATH_TO_REPO
PATH_TO_REPO='../'


def rainfall_india_fun(df,risk):
    date1=[]
    #df['XPCT_DLVRY_DT'].apply(date_string)
    #df=df.dropna()
    for i in range(len(risk)):
        rsd=datetime.datetime.strptime(risk['DateTime'][i][:10],'%Y-%m-%d')
        date1.append(rsd)
    date2=[]
    for i in range(len(df)):
        print(i)
        #print(df['XPCT_DLVRY_DT'][i])
        rsd=datetime.datetime.strptime(list(df['XPCT_DLVRY_DT'])[i],'%Y-%m-%d')
        date2.append(rsd)
    indices=indx_min_dif(date2,date1)

    #risk_values=risk[indices]['GPRHC_IND']
    print(indices)
    indices=pd.DataFrame(indices)
    indices.columns=['indices']
    merged=pd.concat([pd.DataFrame(df).reset_index(drop=True),risk.loc[indices['indices'],:]['Value'].reset_index(drop=True)],axis=1)
    #merged=merged.drop(["level_0"],axis=1)
    #risk_scores_indices=risk.loc[indices['indices'],:]['GPRHC_IND']
    #merged=pd.concat([df,indices],axis=1)
    #merged['risk']=merged['indices'].apply(replace)
    
    


    return merged
    


if __name__ == '__main__':
    sup = 'EXELAN PHARMACEUTICALS'
    dataset=pd.read_csv("../../../Project3/dataset1.csv")
    joined = dataset[dataset['SPLR_NAME'] == sup]
    
    
    # Correlation analysis of time shifts - compare the collected signal to the days_delayed label
    df = pd.DataFrame()
    shifts = np.arange(24, 24*10, 24)
    compare = joined['Days_Delayed']
    compare_norm = (compare - compare.mean()) / compare.std()
    corrs = {}

    for s in shifts:
        test = joined.apply(get_accumulation_fn(s, 1), axis='columns')

        c, t = compare_norm[test > 0], test[test > 0]
        df[s] = t

        t = (t - t.mean()) / t.std()
        corrs[s] = np.corrcoef(t.to_numpy(), c.to_numpy())[0][1]
        print(s, corrs[s])

    maxcoef = max(corrs.keys(), key = lambda x: abs(corrs[x]))
    print(f'Max Correlation Coefficient:  {maxcoef, corrs[maxcoef]}')