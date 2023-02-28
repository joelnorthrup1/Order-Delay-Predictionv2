# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 20:54:33 2022

@author: DELL
"""
import pandas as pd
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.pipeline import Pipeline
import pickle

def inverse_encoded_data(X):
        output = X.copy()
        with open("./feature_names.obj", 'rb') as f:
          columns = pickle.load(f)
        if columns is not None:
            print("Encoder is loaded")
            with open("./encoder.obj", 'rb') as f:
                cencoder = pickle.load(f)
            #print(len(cencoder))
            for i,col in enumerate(columns):     
                print(str(col))
                output["Decoded"+str(i)] = cencoder[i].inverse_transform(output[col])
        return output