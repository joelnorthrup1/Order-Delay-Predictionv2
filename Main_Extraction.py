from argparse import ArgumentParser
if __name__ == "__main__":
    parser =ArgumentParser()
    parser.add_argument("-d", "--data", required=True, help="CSV file with quotes to run the model")
    parser.add_argument("-m", "--main", required=True, help="CSV file with quotes to run the model")

    args = parser.parse_args()
args = vars(args)

print(args['data'])

import os
os.chdir(args['main'])
print(os.listdir())

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






import csv
import keras

def merge_encode(file_dir,training_set):

        dataset=pd.read_csv(file_dir).reset_index() #,skiprows=lambda i: i>0 and random.random() > 1.0
        print("Dataset is loaded")
        X,y=preprocess(dataset,"X_test100","y_test100",training_set)
        return X,y


    



merge_encode(args['data'],training_set=True)

