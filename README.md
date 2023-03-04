# Order-Delay-Predictionv2

**#Step  1**
First extract the external features and merge internal and external features. For Extraction run following command. </br>
**!python /content/drive/MyDrive/Final_Code1/Main_Extraction.py -d 'dataset1.csv' -m '/content/drive/MyDrive/Final_Code1'**

**Command takes two arguments </br>**
**1.** First command line argument -d: It takes the directory of the dataset </br>
**2.** Second command line argument -m: It takes the directory of the main folder of the code </br>

After running this commands, different lookback features will extracted and will merge with internal features. (Meging_encoding.py code is commented for just one set of lookback features 3 Months lookback) 

Extracted data will stored as X_train and X_test in current directory



#Step 2
To train model, run following command. </br>
**!python /content/drive/MyDrive/Final_Code1/training.py -d 5 -m '/content/drive/MyDrive/Final_Code1' **
**Command takes two arguments </br>**
**1.** First command line argument -d: It takes the threshold for the days delay. It can be 5,10,15 or 28 </br>
**2.** Second command line argument -m: It takes the directory of the main folder of the code </br>

After running this commands, data will preprocessed and code will start training process.




To train model, set the path "https://drive.google.com/drive/folders/15dADrvanOm0QBDaYy6bktl15-ikeYJ2q?usp=share_link" in the following notebooks

Training Notebook **Order_delay_Project3_Modified5(Model_Traing_3_6_Lookback_Dataset8_Training).ipynb**


or 

you can use this colab notebook but please make a copy to run the code.
https://colab.research.google.com/drive/1_osIophTvGe-aKVLyV9mu1pCpp4vRuTk?usp=sharing



Notebook contains multiple functions </br>
1). spreproces_data: This function will performs prepocessing like replacing nans with mean values , standard scaling of the features, PCA and SMOTE for data augmentation, reshaping of the features.  </br>
2). training: This function will initialize the model, train the model and finally evaluates the model performance.
