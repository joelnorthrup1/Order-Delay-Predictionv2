

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
from MyApp.preprocessing import preprocess
from sklearn.metrics import confusion_matrix
import pandas as pd



# performing preprocessing part
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from MyApp.MultiColumnLabelEncoder_Inv import inverse_encoded_data 
#X=X.drop('Unnamed: 0',axis=1)
def preproces_data(days_delayed,pcs_components,training_set,with_label=True):
  if(training_set==True):
    X=pd.read_csv("./X7_train_processed.csv")
    date=X['time']    
    X=X.iloc[:,:].drop('time',axis=1) #[['EM_ITEM_NUM','GNRC_NAME','THERAP_CLASS','FD Location','API Location','DC_NUM','SPLR_VENDOR_NUM','SPLR_NAME','SPLR_REGION','SPLR_POSTAL_CODE','SPLR_COUNTRY','risk','trends','india_cpi_data','railway_goods','rainfall_india_data','air_quality_kolkata','air_quality_newdehli']] #../dataset/Xprocessed.csv
    X=X.drop('Unnamed: 0',axis=1)
    X=X.drop(['EM_ITEM_NUM','GNRC_NAME','THERAP_CLASS','FD Location','API Location','DC_NUM','SPLR_VENDOR_NUM','SPLR_NAME','SPLR_REGION','SPLR_POSTAL_CODE','SPLR_COUNTRY'],axis=1)
    y=(pd.read_csv("./y7_train_processed.csv",engine='python')['Days_Delayed']>days_delayed).astype(np.int8) #../dataset/Yprocessed.csv
    sc = StandardScaler()
    X_train, X_test, y_train, y_test = train_test_split(
      np.array(X), np.array(y), test_size=0.10,shuffle=True, random_state=42)
    pca = PCA(n_components = pcs_components)
    X_train = sc.fit_transform(X_train)
    with open("./standardscaler.obj", 'wb') as f: 
      pickle.dump(sc, f)
    X_test = sc.transform(X_test)
    X_train = pca.fit_transform(X_train)
    with open("./pca.obj", 'wb') as f:  
      pickle.dump(pca, f)
    X_test = pca.transform(X_test)
    over = SMOTE(sampling_strategy=0.9) 
    under = RandomUnderSampler(sampling_strategy=0.2) 
    steps = [ ('u', under),('o', over)] #('o', over)
    pipeline = Pipeline(steps=steps)
    print("samples before augmentation"+str(len(X_train)))
    X_train, y_train = pipeline.fit_resample(X_train, y_train)
    print("samples before augmentation"+str(len(X_train)))
    X_train = np.reshape(np.array(X_train), (X_train.shape[0],1, X_train.shape[1]))
    X_test = np.reshape(np.array(X_test), (X_test.shape[0],1, X_test.shape[1]))
    return X_train, X_test, y_train, y_test,date
  else:
    X=pd.read_csv("./X_test_processed.csv")
    date=X['time']    
    X=X.iloc[:,:].drop('time',axis=1) #[['EM_ITEM_NUM','GNRC_NAME','THERAP_CLASS','FD Location','API Location','DC_NUM','SPLR_VENDOR_NUM','SPLR_NAME','SPLR_REGION','SPLR_POSTAL_CODE','SPLR_COUNTRY','risk','trends','india_cpi_data','railway_goods','rainfall_india_data','air_quality_kolkata','air_quality_newdehli']] #../dataset/Xprocessed.csv
    X=X.drop('Unnamed: 0',axis=1)
    X=X.drop(['EM_ITEM_NUM','GNRC_NAME','THERAP_CLASS','FD Location','API Location','DC_NUM','SPLR_VENDOR_NUM','SPLR_NAME','SPLR_REGION','SPLR_POSTAL_CODE','SPLR_COUNTRY'],axis=1)
    #sc = StandardScaler()
    with open("./standardscaler.obj", 'rb') as f:
      sc = pickle.load(f)
      print("sc loaded")
    #pca = PCA(n_components = pcs_components)
    with open("./pca.obj", 'rb') as f:
      pca = pickle.load(f)
      
    print("transforming")  
    X = sc.transform(np.array(X))
    X = pca.transform(np.array(X))
    print("transformed")
    if(with_label==True):
      y=(pd.read_csv("./y_test_processed.csv")['Days_Delayed']>days_delayed).astype(np.int8)
      return X,y,date
    else:
      return X,date
      


def training():
    days_delayed_thres=5
    X_train, X_test, y_train, y_test,date=preproces_data(days_delayed_thres,500,True,True)
    from tensorflow import keras
    ip = keras.Input(shape=(X_train.shape[1],X_train.shape[2]), name="input")
    x = keras.layers.Conv1D(64, kernel_size=1, activation="relu")(ip)
    x = keras.layers.Conv1D(32, kernel_size=1, activation="relu")(x)
    x = keras.layers.Conv1D(16, kernel_size=1, activation="relu")(x)
    x = keras.layers.GlobalMaxPooling1D()(x)
    x = keras.layers.Dropout(0.3)(x)

    out = keras.layers.Bidirectional(keras.layers.LSTM(64, return_sequences=True))(ip)
    out = keras.layers.Bidirectional(keras.layers.LSTM(32, return_sequences=True))(out)
    out = keras.layers.Bidirectional(keras.layers.LSTM(16, return_sequences=False))(out)
    out = keras.layers.Dropout(0.3)(out)
    combined = keras.layers.concatenate([x,out])
    out = keras.layers.Dense(1, activation="sigmoid")(combined)
    model = keras.Model(ip, out)
    import numpy as np
    from focal_loss import BinaryFocalLoss
    model.compile(
        optimizer=keras.optimizers.Adam(0.001),
        loss='binary_crossentropy',metrics=['accuracy']) # BinaryFocalLoss(gamma=2)

    H=model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=40, batch_size=128)
    model.save("./MyApp/model2.h5")
    pred=model.predict(X_test)
    pred=(pred>0.5).astype(np.int8)

    from MyApp.cm import plot_confusion_matrix

    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_test,pred)
    print(cm)
    from operator import truediv


    plt.figure()
    plot_confusion_matrix(cm, classes=[],normalize=True,
                          title='Confusion matrix, without normalization')
    r1=cm[0]/(cm.astype(np.float).sum(axis=1))[0]
    r2=cm[1]/(cm.astype(np.float).sum(axis=1))[1]
    cm=[list(r1),list(r2)]
    tp = np.diag(cm)
    prec = list(map(truediv, tp, np.sum(cm, axis=0)))
    rec = list(map(truediv, tp, np.sum(cm, axis=1)))
    print ('Precision: {}\nRecall: {}'.format(prec, rec))


    return model,X_train, X_test, y_train, y_test

import csv
import keras

def merge_encode(file_dir,training_set):

        dataset=pd.read_csv(file_dir).reset_index() #,skiprows=lambda i: i>0 and random.random() > 1.0
        print("Dataset is loaded")
        X,y=preprocess(dataset,"X_train","y_train",training_set)
        return X,y


    


# import os
# print(os.chdir("../../"))
# print(os.listdir())
merge_encode("dataset1.csv",training_set=True)
#training()
#inference()
#shap()
