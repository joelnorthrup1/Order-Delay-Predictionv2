from MyApp.MultiColumnLabelEncoder import MultiColumnLabelEncoder
from sklearn import preprocessing
import pandas as pd
from sklearn import preprocessing
import os
from MyApp.feature_extractors.geo_political_risk import geo_political_risk
from MyApp.feature_extractors.amazon_trends import amazon_trends
from MyApp.feature_extractors.india_cpi import india_cpi
from MyApp.feature_extractors.pet_consumption import pet_consumption_fun
from MyApp.feature_extractors.railway_goods import railway_goods_fun
from MyApp.feature_extractors.rainfall_india import rainfall_india_fun
from MyApp.feature_extractors.air_quality import air_quality_fun
from MyApp.feature_extractors.date_specific_features import date_specific_features_fun
#os.chdir("../")
from MyApp.merge_for_economics import merge_for_economics
from MyApp.feature_extractors.other_numeric_features import merge_for_other_features

import pandas as pd
import numpy as np
# summarize class distribution
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from imblearn.pipeline import Pipeline
from MyApp.merging_encoding import merging_encoding
from MyApp.label_utils import create_days_delayed
import os
import torch
import pandas as pd
# Oversample with SMOTE and random undersample for imbalanced dataset
from collections import Counter
from sklearn.datasets import make_classification
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from imblearn.pipeline import Pipeline
from matplotlib import pyplot
from numpy import where
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from matplotlib import pyplot

import tensorflow.compat.v1.keras.backend as K
import tensorflow as tf
tf.compat.v1.disable_eager_execution()
tf.compat.v1.disable_v2_behavior()
import pandas as pd


import pandas as pd
import pandas as pd
import numpy as np
# summarize class distribution
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from imblearn.pipeline import Pipeline

from MyApp.label_utils import create_days_delayed
import os
import torch
import pandas as pd
# Oversample with SMOTE and random undersample for imbalanced dataset
from collections import Counter
from sklearn.datasets import make_classification
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from imblearn.pipeline import Pipeline
from matplotlib import pyplot
from numpy import where
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from matplotlib import pyplot

import tensorflow.compat.v1.keras.backend as K
import tensorflow as tf
tf.compat.v1.disable_eager_execution()
tf.compat.v1.disable_v2_behavior()
import pandas as pd
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM,Dropout,Embedding,Conv1D,MaxPooling1D,Flatten
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn import preprocessing
import random
import numpy as np
from sklearn.model_selection import train_test_split
from MyApp.cm import plot_confusion_matrix

from sklearn.metrics import confusion_matrix
import pandas as pd


import csv
import keras

def training(epochs,model_name):
    from tensorflow import keras
    ip = keras.Input(shape=(X_train.shape[1],X_train.shape[2]), name="input")
    x = keras.layers.Conv1D(64, kernel_size=1, activation="relu")(ip)
    x = keras.layers.Conv1D(32, kernel_size=1, activation="relu")(x)
    x = keras.layers.Conv1D(32, kernel_size=1, activation="relu")(x)
    #x = keras.layers.GlobalMaxPooling1D()(x)
    x = keras.layers.BatchNormalization()(x)
    x = keras.layers.Dropout(0.7)(x)

    out = keras.layers.Bidirectional(keras.layers.LSTM(64, return_sequences=True))(ip)
    out = keras.layers.Bidirectional(keras.layers.LSTM(32, return_sequences=True))(out)
    out = keras.layers.Bidirectional(keras.layers.LSTM(16, return_sequences=False))(out)
    out = keras.layers.BatchNormalization()(out)
    out = keras.layers.Dropout(0.7)(out)

    x = keras.layers.Flatten()(x)
    out = keras.layers.Flatten()(out)
    combined = keras.layers.concatenate([x,out])
    #combined = keras.layers.Dense(512, activation="relu")(out)
    #combined = keras.layers.Dropout(0.7)(combined)
    #combined = keras.layers.Dense(128, activation="relu")(combined)
    #combined = keras.layers.Dropout(0.7)(combined)
    out = keras.layers.Dense(1, activation="sigmoid")(combined)


    model = keras.Model(ip, out)

    from focal_loss import BinaryFocalLoss
    model.compile(
        optimizer=keras.optimizers.Adam(0.001),
        loss='binary_crossentropy',metrics=['accuracy']) # BinaryFocalLoss(gamma=2)

    H=model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=epochs, batch_size=128)
    model.save("./MyApp/"+model_name)
    tr_pred=model.predict(X_train)
    tr_pred=(tr_pred>0.5).astype(np.int8)

    pred=model.predict(X_test)
    pred=(pred>0.5).astype(np.int8)

    from MyApp.cm import plot_confusion_matrix

    from sklearn.metrics import confusion_matrix
    tr_cm = confusion_matrix(y_train,tr_pred)
    cm = confusion_matrix(y_test,pred)
    print(cm)
    plt.figure()
    plot_confusion_matrix(cm, classes=[],
                          title='Confusion matrix, without normalization')
    from sklearn.metrics import classification_report


    print(classification_report(y_test, pred))
    return model,X_train, X_test, y_train, y_test,tr_cm,cm
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
def preproces_data(X,days_delayed,pcs_components,training_set,with_label=True):
  if(training_set==True):
    X['air_quality_kolkata'].fillna((X['air_quality_kolkata'].mean()), inplace=True)
    X['air_quality_newdehli'].fillna((X['air_quality_newdehli'].mean()), inplace=True)
    X['rainfall_india_data'].fillna((X['rainfall_india_data'].mean()), inplace=True)
    X['trends'].fillna((X['trends'].mean()), inplace=True)
    y=(pd.read_csv("./y4_train_processed.csv",engine='python')['Days_Delayed']>days_delayed).astype(np.int8) #../dataset/Yprocessed.csv


    dataset=pd.concat([X,y],axis=1)
    X_=dataset.drop_duplicates().iloc[:,:-1]
    y_=dataset.drop_duplicates().iloc[:,-1:]
    sc = StandardScaler()
    X_train, X_test, y_train, y_test = train_test_split(
      np.array(X_), np.array(y_), test_size=0.10,shuffle=True, random_state=42)
    pca = PCA(n_components = pcs_components)
    X_train = sc.fit_transform(X_train)
    with open("./standardscaler.obj", 'wb') as f: 
      pickle.dump(sc, f)
    X_test = sc.transform(X_test)
    #X_train = pca.fit_transform(X_train)
    with open("./pca.obj", 'wb') as f:  
      pickle.dump(pca, f)
    #X_test = pca.transform(X_test)
    over = SMOTE(sampling_strategy=0.9) 
    under = RandomUnderSampler(sampling_strategy=0.2) 
    steps = [ ('u', under),('o', over)] #('o', over)
    pipeline = Pipeline(steps=steps)
    print("samples before augmentation"+str(len(X_train)))
    X_train, y_train = pipeline.fit_resample(X_train, y_train)
    print("samples before augmentation"+str(len(X_train)))
    X_train = np.reshape(np.array(X_train), (X_train.shape[0],1, X_train.shape[1]))
    X_test = np.reshape(np.array(X_test), (X_test.shape[0],1, X_test.shape[1]))
    return X_train, X_test, y_train, y_test
  else:
    X=pd.read_csv("./X_test_processed.csv")
    date=X['time']    
    X=X.iloc[:,:].drop('time',axis=1) #[['EM_ITEM_NUM','GNRC_NAME','THERAP_CLASS','FD Location','API Location','DC_NUM','SPLR_VENDOR_NUM','SPLR_NAME','SPLR_REGION','SPLR_POSTAL_CODE','SPLR_COUNTRY','risk','trends','india_cpi_data','railway_goods','rainfall_india_data','air_quality_kolkata','air_quality_newdehli']] #../dataset/Xprocessed.csv
    X=X.drop('Unnamed: 0',axis=1)
    #sc = StandardScaler()
    with open("./standardscaler.obj", 'rb') as f:
      sc = pickle.load(f)
      print("sc loaded")
    #pca = PCA(n_components = pcs_components)
    with open("./pca.obj", 'rb') as f:
      pca = pickle.load(f)
    X = sc.transform(X)
    X = pca.transform(X)
    if(with_label==True):
      y=(pd.read_csv("./y_test_processed.csv")['Days_Delayed']>days_delayed).astype(np.int8)
      return X,y,date
    else:
      return X,date



X=pd.read_csv("./X4_train_processed.csv")
X_train, X_test, y_train, y_test=preproces_data(X.iloc[:,21:],y,5,8000,training_set=True)

model,X_train, X_test, y_train, y_test,train_cm,test_cm=training(50)



    

