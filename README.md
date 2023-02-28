# Order-Delay-Predictionv2

#Step # 1
First extract the external features and merge internal and external features. For Extraction run following command. </br>
!python /content/drive/MyDrive/Final_Code1/Main_Extraction.py -d 'dataset1.csv' -m '/content/drive/MyDrive/Final_Code1'

Command takes two arguments
#First command line argument -d: It takes the directory of the dataset </br>
#Second command line argument -m: It takes the directory of the main folder of the code </br>

After running this commands, different lookback features will extracted and will merge with internal features. (Meging_encoding.py code is commented for just one set of lookback features 3 Months lookback) 
