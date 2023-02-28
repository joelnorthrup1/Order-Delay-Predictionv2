# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 18:03:29 2022

@author: DELL
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.pipeline import Pipeline
import pickle
import numpy as np

class MultiColumnLabelEncoder:
    def __init__(self,columns = None):
        self.columns = columns
         # array of column names to encode

    def fit(self,X,y=None):
        return self # not relevant here

    def transform(self,X,training_set):
        '''
        Transforms columns of X specified in self.columns using
        LabelEncoder(). If no columns specified, transforms all
        columns in X.
        '''
        output = X.copy()
        if self.columns is not None and training_set is not False:
            en=[]
            feature_names=[]
            for col in self.columns:
                le = OneHotEncoder(handle_unknown='ignore')
                r=le.fit_transform(output[col].to_numpy().reshape(-1, 1)).toarray()
                output[list(le.get_feature_names())]=r
                feature_names.append(list(le.get_feature_names()))
                en.append(le)
            with open("./encoder.obj", 'wb') as f:  #  'w' replaced by 'wb' to avoid crashing
                pickle.dump(en, f)
            with open("./feature_names.obj", 'wb') as f:  #  'w' replaced by 'wb' to avoid crashing
                pickle.dump(feature_names, f)
        if self.columns is not None and training_set is False:
            print("Encoder is loaded")
            with open("./encoder.obj", 'rb') as f:
                cencoder = pickle.load(f)
            for i,col in enumerate(self.columns):     
                #print("i"+str(i))
                r= cencoder[i].transform(output[col].to_numpy().reshape(-1, 1)).toarray()
                output[list(cencoder[i].get_feature_names())]=r
        return output

    def fit_transform(self,X,training_set,y=None):
        return self.fit(X,y).transform(X,training_set)
    
    
    
# m=MultiColumnLabelEncoder(['Bridge_Types'])
# bridge_types = ('Arch','Beam','Truss','Cantilever','Tied Arch','Suspension','Cable')
# bridge_df = pd.DataFrame(bridge_types, columns=['Bridge_Types'])
# output=m.fit_transform(bridge_df, True)
# dataset=pd.read_csv("../../../Project3/dataset1.csv")
# dataset=dataset.drop(['Unnamed: 15','Unnamed: 12','CNCL_DT','PO_ID'],axis=1)
#         #dataset=dataset1[dataset1['FD Location']=='USA']
# col=['EM_ITEM_NUM','GNRC_NAME'] #'RCV_QTY',
        
# cencoder=MultiColumnLabelEncoder(columns = col)
# X=cencoder.fit_transform(dataset,True)
   
   
   
   
   