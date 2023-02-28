
import pandas as pd
import random



def date_cor(row):
    row=str(row)[:19]
    return row
    
def date_specific(dataset1,risk,feature_name,look_back,direction):
  #print(risk.columns)
  #print(risk)
  #risk.rename({'DateTime': 'time'}, axis=1, inplace=True)
  dataset1=pd.DataFrame(dataset1)
  risk['time']=pd.to_datetime(risk['time'].apply(date_cor))
  #print(risk['time'])
  try:
    merged_dataframe = pd.merge_asof(dataset1.sort_values('time'),risk[['time','Value']].sort_values('time'),on='time',direction=direction,tolerance=pd.Timedelta(look_back))
    merged_dataframe.rename({'Value': feature_name}, axis=1, inplace=True)
  except:
    merged_dataframe = pd.merge_asof(dataset1.sort_values('time'),risk[['time','GPRHC_IND']].sort_values('time'),on='time',direction=direction,tolerance=pd.Timedelta(look_back))
    merged_dataframe.rename({'GPRHC_IND': feature_name}, axis=1, inplace=True)      
  return merged_dataframe





from sklearn import preprocessing

def merge_for_other_features(dataset,risk,feature_name,look_back,direction):
    #print(risk['ReportTime'])
    dataset.rename({'XPCT_DLVRY_DT': 'time'}, axis=1, inplace=True)
    try:
      risk.rename({'DateTime': 'time'}, axis=1, inplace=True)
    except:
      risk.rename({'ReportTime': 'time'}, axis=1, inplace=True)   
    dataset["time"] = pd.to_datetime(dataset["time"])
    risk.rename({'ReportTime': 'time'}, axis=1, inplace=True)
    dataset=dataset.dropna(axis=1)
    processing_data=dataset
    processing_data=date_specific(processing_data,risk,feature_name,look_back,direction)

    return processing_data





# import pandas as pd
# d2=pd.read_csv("G:/My Drive/Upwork_Projects/SirJoelWork/Project3_Modified/scratch/ext_data/amazon_trends.csv").reset_index()
# d1=pd.read_csv("G:/My Drive/Upwork_Projects/SirJoelWork/Project3//dataset1.csv").reset_index()
# d1=d1.drop(['Unnamed: 15','Unnamed: 12','CNCL_DT','PO_ID'],axis=1)
# d1=d1[d1['FD Location']=='INDIA']
# col=['XPCT_DLVRY_DT','EM_ITEM_NUM','GNRC_NAME','THERAP_CLASS','FD Location','API Location','DC_NUM','SPLR_VENDOR_NUM','SPLR_NAME','SPLR_REGION','SPLR_POSTAL_CODE','SPLR_COUNTRY','Days_Delayed'] #'RCV_QTY',

# d1=d1[col].dropna()
# #processing_data=merge_for_other_features(d1,d2,"lll")






