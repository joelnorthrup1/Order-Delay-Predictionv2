from MyApp.MultiColumnLabelEncoder import MultiColumnLabelEncoder
from sklearn import preprocessing
import pandas as pd
from sklearn import preprocessing
import pickle
import os
from MyApp.feature_extractors.geo_political_risk import geo_political_risk
from MyApp.merge_for_economics import merge_for_economics
from MyApp.feature_extractors.other_numeric_features import merge_for_other_features
from MyApp.merge_for_forex import merge_for_forex


def categorical_enc(x,name):

  label_encoder = preprocessing.LabelEncoder()
  encoded= label_encoder.fit_transform(x)
  encoded=pd.DataFrame(encoded)
  encoded.columns=[name]
  return encoded,label_encoder
    
def merging_encoding(df,forex,risk,trends,india_cpi_data,pet_consumption,railway_goods,rainfall_india_data,air_quality_kolkata,air_quality_newdehli,gasoline_price_data,motor_vehicles_data,motor_vehicles_class_type_data,economics_export_data,balance_of_trade_data,bank_lending_rate_data,banks_balance_sheet_data,economics_bonds_data,cash_reserve_ratio_data,building_permit_data,capital_flows_data,economics_consumer_confidence_data,economics_consumer_credit_data,consumer_price_index_cpi_data,consumer_spending_data,core_inflation_rate_data,economics_currencies_data,food_inflation,foreign_direct_investment,foreign_exchange_reserves,economics_unemployment_rate,full_time_employment,economics_gasoline_prices,gdp_deflator,debt_to_gdp,harmonised_consumer_prices,home_ownership_rate,households_debt_to_gdp,debt_to_income,housing_index,housing_starts,import_prices,economics_imports,lending_rate,labour_costs,inflation_rate,inflation_expectations,jobless_claims,inflation_rate_mom,loans_to_private_sector,loan_growth,minimum_wages,long_term_unemployment_rate,money_supply_m1,natural_gas_imports,economics_money_supply_m3,part_time_employment,personal_savings,personal_spending,price_to_rent_ratio,private_debt_to_gdp,private_sector_credit,producer_prices,producer_prices_change,productivity,remittances,retail_sales_mom,retail_sales_yoy,retirement_age_men,retirement_age_women,stock_market_indexes,interest_rate,terms_of_trade,terrorism_index,tourism_revenues,tourist_arrivals,unemployed_persons,unemployment_rate,wage_growth,economics_wages,weapons_sales,wages_in_manufacturing,youth_unemployment_rate,col,training_set):
    col2=['EM_ITEM_NUM','GNRC_NAME','THERAP_CLASS','FD Location','API Location','DC_NUM','SPLR_VENDOR_NUM','SPLR_NAME','SPLR_REGION','SPLR_POSTAL_CODE','SPLR_COUNTRY']   
    cencoder=MultiColumnLabelEncoder(columns = col2)
    df=cencoder.fit_transform(df,training_set)
    df = merge_for_other_features(df,risk,"risk_one_year",'1y','nearest') #df2.join(
    df = merge_for_other_features(df,risk,"risk_30days_backward",'60d','backward')
    df = merge_for_other_features(df,risk,"risk_30days_forward",'60d','forward')
    df = merge_for_other_features(df,risk,"risk_60days_backward",'60d','backward')
    df = merge_for_other_features(df,risk,"risk_60days_backward",'60d','forward')
    print("data length"+str(len(df)))
    print("mmmmmmmmmmmmmmmmmmmmm")

    print("data length"+str(len(df)))
    df = merge_for_other_features(df,india_cpi_data,"india_cpi_data_one_year",'1y','nearest')
    df = merge_for_other_features(df,india_cpi_data,"india_cpi_data_30days_backward",'60d','backward')
    df = merge_for_other_features(df,india_cpi_data,"india_cpi_data_30days_forward",'60d','forward')
    df = merge_for_other_features(df,india_cpi_data,"india_cpi_data_60days_backward",'60d','backward')
    df = merge_for_other_features(df,india_cpi_data,"india_cpi_data_60days_forward",'60d','forward')
    print("data length"+str(len(df)))
    # #df = pet_consumption_fun(df,pet_consumption) #problem1 need to normalize
    df= merge_for_other_features(df,railway_goods,"railway_goods_one_year",'1y','nearest')
    df= merge_for_other_features(df,railway_goods,"railway_goods_30days_backward",'60d','backward')
    df= merge_for_other_features(df,railway_goods,"railway_goods_30days_forward",'60d','forward')
    df= merge_for_other_features(df,railway_goods,"railway_goods_60days_backward",'60d','backward')
    df= merge_for_other_features(df,railway_goods,"railway_goods_60days_forward",'60d','forward')
    print("data length"+str(len(df)))
    df= merge_for_other_features(df,rainfall_india_data,"rainfall_india_data_one_year",'1y','nearest') #problem
    df= merge_for_other_features(df,rainfall_india_data,"rainfall_india_data_30days_backward",'60d','backward')
    df= merge_for_other_features(df,rainfall_india_data,"rainfall_india_data_30days_forward",'60d','forward')
    df= merge_for_other_features(df,rainfall_india_data,"rainfall_india_data_60days_backward",'60d','backward')
    df= merge_for_other_features(df,rainfall_india_data,"rainfall_india_data_60days_forward",'60d','forward')

    print("data length"+str(len(df)))
    #print("kolkata data")
    #df= merge_for_other_features(df,air_quality_kolkata,"air_quality_kolkata") 
    print("length"+str(len(df)))
    df= merge_for_other_features(df,air_quality_newdehli,"air_quality_newdehli_one_year",'1y','nearest') 
    df= merge_for_other_features(df,air_quality_newdehli,"air_quality_newdehli_30days_backward",'60d','backward') 
    df= merge_for_other_features(df,air_quality_newdehli,"air_quality_newdehli_30days_forward",'60d','forward') 
    df= merge_for_other_features(df,air_quality_newdehli,"air_quality_newdehli_60days_backward",'60d','backward') 
    df= merge_for_other_features(df,air_quality_newdehli,"air_quality_newdehli_60days_forward",'60d','forward') 
    print("length"+str(len(df)))
  # #df= date_specific_features_fun(df,gasoline_price_data) #problem
  ##df= date_specific_features_fun(df,motor_vehicles_data) #problem
   #df= date_specific_features_fun(df,motor_vehicles_class_type_data)

    print("kolkata data")
    df= merge_for_other_features(df,air_quality_kolkata,"air_quality_kolkata_one_year",'1y','nearest') 
    df= merge_for_other_features(df,air_quality_kolkata,"air_quality_kolkata_30days_backward",'60d','backward')
    df= merge_for_other_features(df,air_quality_kolkata,"air_quality_kolkata_30days_forward",'60d','forward')
    df= merge_for_other_features(df,air_quality_kolkata,"air_quality_kolkata_60days_backward",'60d','backward')
    df= merge_for_other_features(df,air_quality_kolkata,"air_quality_kolkata_60days_forward",'60d','forward')
    
    df = merge_for_other_features(df,trends,"trends",'1y','nearest')     
    
    df=merge_for_forex(df,forex)     
    df=merge_for_economics(df,foreign_direct_investment,'foreign_direct_investment')
    df=merge_for_economics(df,foreign_exchange_reserves,'foreign_exchange_reserves')
    df=merge_for_economics(df,economics_unemployment_rate,'economics_unemployment_rate')
    df=merge_for_economics(df,full_time_employment,'full_time_employment')
    print("data length"+str(len(df)))
    df=merge_for_economics(df,economics_gasoline_prices,'economics_gasoline_prices')
    print("data length"+str(len(df)))
    df=merge_for_economics(df,gdp_deflator,'gdp_deflator')
    df=merge_for_economics(df,debt_to_gdp,'debt_to_gdp')
    df=merge_for_economics(df,harmonised_consumer_prices,'harmonised_consumer_prices')
    print("data length"+str(len(df)))
      
    df=merge_for_economics(df,home_ownership_rate,'home_ownership_rate')
    df=merge_for_economics(df,households_debt_to_gdp,'households_debt_to_gdp')
    df=merge_for_economics(df,debt_to_income,'debt_to_income')
    df=merge_for_economics(df,housing_index,'housing_index')
    print("data length"+str(len(df)))
    df=merge_for_economics(df,housing_starts,'housing_starts')
    df=merge_for_economics(df,import_prices,'import_prices')
    df=merge_for_economics(df,economics_imports,'economics_imports')
    df=merge_for_economics(df,lending_rate,'lending_rate')
    print("data length"+str(len(df)))
    df=merge_for_economics(df,labour_costs,'labour_costs')
    df=merge_for_economics(df,inflation_rate,'inflation_rate')
    df=merge_for_economics(df,inflation_expectations,'inflation_expectations')
    #df=merge_for_economics(df,jobless_claims,'jobless_claims')
    print("data length"+str(len(df)))
    df=merge_for_economics(df,inflation_rate_mom,'inflation_rate_mom')
    df=merge_for_economics(df,loans_to_private_sector,'loans_to_private_sector')
    df=merge_for_economics(df,loan_growth,'loan_growth')
    df=merge_for_economics(df,minimum_wages,'minimum_wages')
      
    df=merge_for_economics(df,long_term_unemployment_rate,'long_term_unemployment_rate')
    df=merge_for_economics(df,money_supply_m1,'money_supply_m1')
    df=merge_for_economics(df,natural_gas_imports,'natural_gas_imports')
    df=merge_for_economics(df,economics_money_supply_m3,'economics_money_supply_m3')
    
    df=merge_for_economics(df,part_time_employment,'part_time_employment')
    df=merge_for_economics(df,personal_savings,'personal_savings')
    df=merge_for_economics(df,personal_spending,'personal_spending')
    df=merge_for_economics(df,price_to_rent_ratio,'price_to_rent_ratio')
    
    df=merge_for_economics(df,private_debt_to_gdp,'private_debt_to_gdp')
    df=merge_for_economics(df,private_sector_credit,'private_sector_credit')
    df=merge_for_economics(df,producer_prices,'producer_prices')
    df=merge_for_economics(df,producer_prices_change,'producer_prices_change')
    print("data length"+str(len(df)))
      
    df=merge_for_economics(df,productivity,'productivity')
    df=merge_for_economics(df,remittances,'remittances')
    df=merge_for_economics(df,retail_sales_mom,'retail_sales_mom')
    df=merge_for_economics(df,retail_sales_yoy,'retail_sales_yoy')
      
    df=merge_for_economics(df,retirement_age_men,'retirement_age_men')
    df=merge_for_economics(df,retirement_age_women,'retirement_age_women')
    #df=merge_for_economics(df,stock_market_indexes,'stock_market_indexes')
    df=merge_for_economics(df,interest_rate,'interest_rate')
    print("data length"+str(len(df)))
    df=merge_for_economics(df,terms_of_trade,'terms_of_trade')
    df=merge_for_economics(df,terrorism_index,'terrorism_index')
    df=merge_for_economics(df,tourism_revenues,'tourism_revenues')
    df=merge_for_economics(df,tourist_arrivals,'tourist_arrivals')
      
    df=merge_for_economics(df,unemployed_persons,'unemployed_persons')
    df=merge_for_economics(df,unemployment_rate,'unemployment_rate')
    df=merge_for_economics(df,wage_growth,'wage_growth')
    df=merge_for_economics(df,economics_wages,'economics_wages')
      
    df=merge_for_economics(df,weapons_sales,'weapons_sales')
    df=merge_for_economics(df,wages_in_manufacturing,'wages_in_manufacturing')
    df=merge_for_economics(df,youth_unemployment_rate,'youth_unemployment_rate')
    print("data length"+str(len(df)))
      
      
      
    
      
    
    df=merge_for_economics(df,food_inflation,'food_inflation')
    df=merge_for_economics(df,economics_export_data,'economics_export_data')
    df=merge_for_economics(df,balance_of_trade_data,'balance_of_trade_data')
    df=merge_for_economics(df,bank_lending_rate_data,'bank_lending_rate_data')
    df=merge_for_economics(df,banks_balance_sheet_data,'banks_balance_sheet_data')  
    #df=merge_for_economics(df,economics_bonds_data,'economics_bonds_data')
    df=merge_for_economics(df,cash_reserve_ratio_data,'cash_reserve_ratio_data')  
    df=merge_for_economics(df,building_permit_data,'building_permit_data')  
    df=merge_for_economics(df,capital_flows_data,'capital_flows_data')  
    print("data length"+str(len(df)))
    df=merge_for_economics(df,economics_consumer_confidence_data,'economics_consumer_confidence_data')  
    df=merge_for_economics(df,economics_consumer_credit_data,'economics_consumer_credit_data')   
    df=merge_for_economics(df,consumer_price_index_cpi_data,'consumer_price_index_cpi_data')   
    df=merge_for_economics(df,consumer_spending_data,'consumer_spending_data')   
    df=merge_for_economics(df,core_inflation_rate_data,'core_inflation_rate_data')  
    print("data length"+str(len(df)))
    #df=merge_for_economics(df,economics_currencies_data,'economics_currencies_data')    
  

  

  
    col.remove("XPCT_DLVRY_DT")
    col.remove("Days_Delayed")
   #if(training_set==True):


    
    numeric_features = [ ] #'Order Entry Date' 'Ordered Value'
    numeric_bin = []
    
    print("Encoding completed")
      
    
    return df
from MyApp.MultiColumnLabelEncoder import MultiColumnLabelEncoder
from sklearn import preprocessing
import pandas as pd
from sklearn import preprocessing
import pickle
import os
#print(os.getcwd())
#os.chdir("./MyApp")
from MyApp.feature_extractors.geo_political_risk import geo_political_risk
#from MyApp.feature_extractors.amazon_trends import amazon_trends
#from MyApp.feature_extractors.india_cpi import india_cpi
#from MyApp.feature_extractors.pet_consumption import pet_consumption_fun
#from MyApp.feature_extractors.railway_goods import railway_goods_fun
#from MyApp.feature_extractors.rainfall_india import rainfall_india_fun
#from MyApp.feature_extractors.air_quality import air_quality_fun
#from MyApp.feature_extractors.date_specific_features import date_specific_features_fun
#os.chdir("../")
from MyApp.merge_for_economics import merge_for_economics
from MyApp.feature_extractors.other_numeric_features import merge_for_other_features
from MyApp.merge_for_forex import merge_for_forex


def categorical_enc(x,name):

  
# label_encoder object knows how to understand word labels.
  label_encoder = preprocessing.LabelEncoder()
  
# Encode labels in column 'species'.
  encoded= label_encoder.fit_transform(x)
  #encoded=pd.Categorical(x).codes
  encoded=pd.DataFrame(encoded)
  encoded.columns=[name]
  return encoded,label_encoder
    
def merging_encoding(df,forex,risk,trends,india_cpi_data,pet_consumption,railway_goods,rainfall_india_data,air_quality_kolkata,air_quality_newdehli,gasoline_price_data,motor_vehicles_data,motor_vehicles_class_type_data,economics_export_data,balance_of_trade_data,bank_lending_rate_data,banks_balance_sheet_data,economics_bonds_data,cash_reserve_ratio_data,building_permit_data,capital_flows_data,economics_consumer_confidence_data,economics_consumer_credit_data,consumer_price_index_cpi_data,consumer_spending_data,core_inflation_rate_data,economics_currencies_data,food_inflation,foreign_direct_investment,foreign_exchange_reserves,economics_unemployment_rate,full_time_employment,economics_gasoline_prices,gdp_deflator,debt_to_gdp,harmonised_consumer_prices,home_ownership_rate,households_debt_to_gdp,debt_to_income,housing_index,housing_starts,import_prices,economics_imports,lending_rate,labour_costs,inflation_rate,inflation_expectations,jobless_claims,inflation_rate_mom,loans_to_private_sector,loan_growth,minimum_wages,long_term_unemployment_rate,money_supply_m1,natural_gas_imports,economics_money_supply_m3,part_time_employment,personal_savings,personal_spending,price_to_rent_ratio,private_debt_to_gdp,private_sector_credit,producer_prices,producer_prices_change,productivity,remittances,retail_sales_mom,retail_sales_yoy,retirement_age_men,retirement_age_women,stock_market_indexes,interest_rate,terms_of_trade,terrorism_index,tourism_revenues,tourist_arrivals,unemployed_persons,unemployment_rate,wage_growth,economics_wages,weapons_sales,wages_in_manufacturing,youth_unemployment_rate,col,training_set):
    col2=['EM_ITEM_NUM','GNRC_NAME','THERAP_CLASS','FD Location','API Location','DC_NUM','SPLR_VENDOR_NUM','SPLR_NAME','SPLR_REGION','SPLR_POSTAL_CODE','SPLR_COUNTRY']   
    cencoder=MultiColumnLabelEncoder(columns = col2)
    df=cencoder.fit_transform(df,training_set)
     
    df = merge_for_other_features(df,risk,"risk") #df2.join(
    print("data length"+str(len(df)))
    print("trends data")

    print("data length"+str(len(df)))
    df = merge_for_other_features(df,india_cpi_data,"india_cpi_data")
    print("data length"+str(len(df)))
    # #df = pet_consumption_fun(df,pet_consumption) #problem1 need to normalize
    df= merge_for_other_features(df,railway_goods,"railway_goods")
    print("data length"+str(len(df)))
    df= merge_for_other_features(df,rainfall_india_data,"rainfall_india_data") #problem
    print("data length"+str(len(df)))
    #print("kolkata data")
    #df= merge_for_other_features(df,air_quality_kolkata,"air_quality_kolkata") 
    print("data length"+str(len(df)))
    df= merge_for_other_features(df,air_quality_newdehli,"air_quality_newdehli") 
    print("data length"+str(len(df)))
  # #df= date_specific_features_fun(df,gasoline_price_data) #problem
  ##df= date_specific_features_fun(df,motor_vehicles_data) #problem
   #df= date_specific_features_fun(df,motor_vehicles_class_type_data)

    df=merge_for_forex(df,forex)
    print("kolkata data")
    duration="30d"
    direction1="backward"
    df= merge_for_other_features(df,air_quality_kolkata,"air_quality_kolkata") 
    df = merge_for_other_features(df,trends,"trends")
    df=merge_for_economics(duration,direction1,df,foreign_direct_investment,'foreign_direct_investment_30days_backward')
    #print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,foreign_exchange_reserves,'foreign_exchange_reserves_30days_backward')
    #print("data length"+str(len(df)))
    #df=merge_for_economics(duration,direction1,df,economics_unemployment_rate,'economics_unemployment_rate_30days_backward')
    print("data length"+str(len(df)))
    #df=merge_for_economics(duration,direction1,df,full_time_employment,'full_time_employment_30days_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,economics_gasoline_prices,'economics_gasoline_prices_30days_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,gdp_deflator,'gdp_deflator_30days_backward')
    df=merge_for_economics(duration,direction1,df,debt_to_gdp,'debt_to_gdp_30days_backward')
    #df=merge_for_economics(duration,direction1,df,harmonised_consumer_prices,'harmonised_consumer_prices_30days_backward')
    #print("data length"+str(len(df)))
      
    #df=merge_for_economics(duration,direction1,df,home_ownership_rate,'home_ownership_rate_30days_backward')
    df=merge_for_economics(duration,direction1,df,households_debt_to_gdp,'households_debt_to_gdp_30days_backward')
    #df=merge_for_economics(duration,direction1,df,debt_to_income,'debt_to_income_30days_backward')
    df=merge_for_economics(duration,direction1,df,housing_index,'housing_index_30days_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,housing_starts,'housing_starts_30days_backward')
    df=merge_for_economics(duration,direction1,df,import_prices,'import_prices_30days_backward')
    df=merge_for_economics(duration,direction1,df,economics_imports,'economics_imports_30days_backward')
    df=merge_for_economics(duration,direction1,df,lending_rate,'lending_rate_30days_backward')
    #print("data length"+str(len(df)))
    #df=merge_for_economics(duration,direction1,df,labour_costs,'labour_costs_30days_backward')
    df=merge_for_economics(duration,direction1,df,inflation_rate,'inflation_rate_30days_backward')
    df=merge_for_economics(duration,direction1,df,inflation_expectations,'inflation_expectations_30days_backward')
    #df=merge_for_economics(duration,direction1,df,jobless_claims,'jobless_claims_30days_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,inflation_rate_mom,'inflation_rate_mom_30days_backward')
    #df=merge_for_economics(duration,direction1,df,loans_to_private_sector,'loans_to_private_sector_30days_backward')
    df=merge_for_economics(duration,direction1,df,loan_growth,'loan_growth_30days_backward')
    df=merge_for_economics(duration,direction1,df,minimum_wages,'minimum_wages_30days_backward')
      
    #df=merge_for_economics(duration,direction1,df,long_term_unemployment_rate,'long_term_unemployment_rate_30days_backward')
    #df=merge_for_economics(duration,direction1,df,money_supply_m1,'money_supply_m1_30days_backward')
    #df=merge_for_economics(duration,direction1,df,natural_gas_imports,'natural_gas_imports_30days_backward')
    #df=merge_for_economics(duration,direction1,df,economics_money_supply_m3,'economics_money_supply_m3_30days_backward')
    
    #df=merge_for_economics(duration,direction1,df,part_time_employment,'part_time_employment_30days_backward')
    df=merge_for_economics(duration,direction1,df,personal_savings,'personal_savings_30days_backward')
    df=merge_for_economics(duration,direction1,df,personal_spending,'personal_spending_30days_backward')
    #df=merge_for_economics(duration,direction1,df,price_to_rent_ratio,'price_to_rent_ratio_30days_backward')
    
    df=merge_for_economics(duration,direction1,df,private_debt_to_gdp,'private_debt_to_gdp_30days_backward')
    #df=merge_for_economics(duration,direction1,df,private_sector_credit,'private_sector_credit_30days_backward')
    df=merge_for_economics(duration,direction1,df,producer_prices,'producer_prices_30days_backward')
    df=merge_for_economics(duration,direction1,df,producer_prices_change,'producer_prices_change_30days_backward')
    #print("data length"+str(len(df)))
      
    df=merge_for_economics(duration,direction1,df,productivity,'productivity_30days_backward')
    #df=merge_for_economics(duration,direction1,df,remittances,'remittances_30days_backward')
    df=merge_for_economics(duration,direction1,df,retail_sales_mom,'retail_sales_mom_30days_backward')
    df=merge_for_economics(duration,direction1,df,retail_sales_yoy,'retail_sales_yoy_30days_backward')
      
    #df=merge_for_economics(duration,direction1,df,retirement_age_men,'retirement_age_men_30days_backward')
    #df=merge_for_economics(duration,direction1,df,retirement_age_women,'retirement_age_women_30days_backward')
    #df=merge_for_economics(duration,direction1,df,stock_market_indexes,'stock_market_indexes_30days_backward')
    df=merge_for_economics(duration,direction1,df,interest_rate,'interest_rate_30days_backward')
    #print("data length"+str(len(df)))
    #df=merge_for_economics(duration,direction1,df,terms_of_trade,'terms_of_trade_30days_backward')
    #df=merge_for_economics(duration,direction1,df,terrorism_index,'terrorism_index_30days_backward')
    df=merge_for_economics(duration,direction1,df,tourism_revenues,'tourism_revenues_30days_backward')
    df=merge_for_economics(duration,direction1,df,tourist_arrivals,'tourist_arrivals_30days_backward')
      
    df=merge_for_economics(duration,direction1,df,unemployed_persons,'unemployed_persons_30days_backward')
    df=merge_for_economics(duration,direction1,df,unemployment_rate,'unemployment_rate_30days_backward')
    df=merge_for_economics(duration,direction1,df,wage_growth,'wage_growth_30days_backward')
    df=merge_for_economics(duration,direction1,df,economics_wages,'economics_wages_30days_backward')
      
    #df=merge_for_economics(duration,direction1,df,weapons_sales,'weapons_sales_30days_backward')
    #df=merge_for_economics(duration,direction1,df,wages_in_manufacturing,'wages_in_manufacturing_30days_backward')
    #df=merge_for_economics(duration,direction1,df,youth_unemployment_rate,'youth_unemployment_rate_30days_backward')
    #print("data length"+str(len(df)))
      




    duration="90d"
    direction1="backward"
    df=merge_for_economics(duration,direction1,df,foreign_direct_investment,'foreign_direct_investment_90days_backward')
    #print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,foreign_exchange_reserves,'foreign_exchange_reserves_90days_backward')
    #print("data length"+str(len(df)))
    #df=merge_for_economics(duration,direction1,df,economics_unemployment_rate,'economics_unemployment_rate_90days_backward')
    print("data length"+str(len(df)))
    #df=merge_for_economics(duration,direction1,df,full_time_employment,'full_time_employment_90days_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,economics_gasoline_prices,'economics_gasoline_prices_90days_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,gdp_deflator,'gdp_deflator_90days_backward')
    df=merge_for_economics(duration,direction1,df,debt_to_gdp,'debt_to_gdp_90days_backward')
    #df=merge_for_economics(duration,direction1,df,harmonised_consumer_prices,'harmonised_consumer_prices_90days_backward')
    #print("data length"+str(len(df)))
      
    #df=merge_for_economics(duration,direction1,df,home_ownership_rate,'home_ownership_rate_90days_backward')
    df=merge_for_economics(duration,direction1,df,households_debt_to_gdp,'households_debt_to_gdp_90days_backward')
    #df=merge_for_economics(duration,direction1,df,debt_to_income,'debt_to_income_90days_backward')
    df=merge_for_economics(duration,direction1,df,housing_index,'housing_index_90days_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,housing_starts,'housing_starts_90days_backward')
    df=merge_for_economics(duration,direction1,df,import_prices,'import_prices_90days_backward')
    df=merge_for_economics(duration,direction1,df,economics_imports,'economics_imports_90days_backward')
    df=merge_for_economics(duration,direction1,df,lending_rate,'lending_rate_90days_backward')
    #print("data length"+str(len(df)))
    #df=merge_for_economics(duration,direction1,df,labour_costs,'labour_costs_90days_backward')
    df=merge_for_economics(duration,direction1,df,inflation_rate,'inflation_rate_90days_backward')
    df=merge_for_economics(duration,direction1,df,inflation_expectations,'inflation_expectations_90days_backward')
    #df=merge_for_economics(duration,direction1,df,jobless_claims,'jobless_claims_90days_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,inflation_rate_mom,'inflation_rate_mom_90days_backward')
    #df=merge_for_economics(duration,direction1,df,loans_to_private_sector,'loans_to_private_sector_90days_backward')
    df=merge_for_economics(duration,direction1,df,loan_growth,'loan_growth_90days_backward')
    df=merge_for_economics(duration,direction1,df,minimum_wages,'minimum_wages_90days_backward')
      
    #df=merge_for_economics(duration,direction1,df,long_term_unemployment_rate,'long_term_unemployment_rate_90days_backward')
    #df=merge_for_economics(duration,direction1,df,money_supply_m1,'money_supply_m1_90days_backward')
    #df=merge_for_economics(duration,direction1,df,natural_gas_imports,'natural_gas_imports_90days_backward')
    #df=merge_for_economics(duration,direction1,df,economics_money_supply_m3,'economics_money_supply_m3_90days_backward')
    
    #df=merge_for_economics(duration,direction1,df,part_time_employment,'part_time_employment_90days_backward')
    df=merge_for_economics(duration,direction1,df,personal_savings,'personal_savings_90days_backward')
    df=merge_for_economics(duration,direction1,df,personal_spending,'personal_spending_90days_backward')
    #df=merge_for_economics(duration,direction1,df,price_to_rent_ratio,'price_to_rent_ratio_90days_backward')
    
    df=merge_for_economics(duration,direction1,df,private_debt_to_gdp,'private_debt_to_gdp_90days_backward')
    #df=merge_for_economics(duration,direction1,df,private_sector_credit,'private_sector_credit_90days_backward')
    df=merge_for_economics(duration,direction1,df,producer_prices,'producer_prices_90days_backward')
    df=merge_for_economics(duration,direction1,df,producer_prices_change,'producer_prices_change_90days_backward')
    #print("data length"+str(len(df)))
      
    df=merge_for_economics(duration,direction1,df,productivity,'productivity_90days_backward')
    #df=merge_for_economics(duration,direction1,df,remittances,'remittances_90days_backward')
    df=merge_for_economics(duration,direction1,df,retail_sales_mom,'retail_sales_mom_90days_backward')
    df=merge_for_economics(duration,direction1,df,retail_sales_yoy,'retail_sales_yoy_90days_backward')
      
    #df=merge_for_economics(duration,direction1,df,retirement_age_men,'retirement_age_men_90days_backward')
    #df=merge_for_economics(duration,direction1,df,retirement_age_women,'retirement_age_women_90days_backward')
    #df=merge_for_economics(duration,direction1,df,stock_market_indexes,'stock_market_indexes_90days_backward')
    df=merge_for_economics(duration,direction1,df,interest_rate,'interest_rate_90days_backward')
    #print("data length"+str(len(df)))
    #df=merge_for_economics(duration,direction1,df,terms_of_trade,'terms_of_trade_90days_backward')
    #df=merge_for_economics(duration,direction1,df,terrorism_index,'terrorism_index_90days_backward')
    df=merge_for_economics(duration,direction1,df,tourism_revenues,'tourism_revenues_90days_backward')
    df=merge_for_economics(duration,direction1,df,tourist_arrivals,'tourist_arrivals_90days_backward')
      
    df=merge_for_economics(duration,direction1,df,unemployed_persons,'unemployed_persons_90days_backward')
    df=merge_for_economics(duration,direction1,df,unemployment_rate,'unemployment_rate_90days_backward')
    df=merge_for_economics(duration,direction1,df,wage_growth,'wage_growth_90days_backward')
    df=merge_for_economics(duration,direction1,df,economics_wages,'economics_wages_90days_backward')
      
    #df=merge_for_economics(duration,direction1,df,weapons_sales,'weapons_sales_90days_backward')
    #df=merge_for_economics(duration,direction1,df,wages_in_manufacturing,'wages_in_manufacturing_90days_backward')
    #df=merge_for_economics(duration,direction1,df,youth_unemployment_rate,'youth_unemployment_rate_90days_backward')
    #print("data length"+str(len(df)))
      
      
    
      
    duration2="1y"
    direction2="nearest"
    df=merge_for_economics(duration,direction1,df,food_inflation,'food_inflation')
    df=merge_for_economics(duration,direction1,df,economics_export_data,'economics_export_data')
    df=merge_for_economics(duration,direction1,df,balance_of_trade_data,'balance_of_trade_data')
    df=merge_for_economics(duration,direction1,df,bank_lending_rate_data,'bank_lending_rate_data')
    df=merge_for_economics(duration,direction1,df,banks_balance_sheet_data,'banks_balance_sheet_data')  
    #df=merge_for_economics(duration,direction1,df,economics_bonds_data,'economics_bonds_data')
    df=merge_for_economics(duration,direction1,df,cash_reserve_ratio_data,'cash_reserve_ratio_data')  
    df=merge_for_economics(duration,direction1,df,building_permit_data,'building_permit_data')  
    df=merge_for_economics(duration,direction1,df,capital_flows_data,'capital_flows_data')  
    print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,economics_consumer_confidence_data,'economics_consumer_confidence_data')  
    df=merge_for_economics(duration,direction1,df,economics_consumer_credit_data,'economics_consumer_credit_data')   
    df=merge_for_economics(duration,direction1,df,consumer_price_index_cpi_data,'consumer_price_index_cpi_data')   
    df=merge_for_economics(duration,direction1,df,consumer_spending_data,'consumer_spending_data')   
    df=merge_for_economics(duration,direction1,df,core_inflation_rate_data,'core_inflation_rate_data')  
    print("data length"+str(len(df)))
    #df=merge_for_economics(duration,direction1,df,economics_currencies_data,'economics_currencies_data')    
      
    df=merge_for_economics(duration2,direction2,df,home_ownership_rate,'home_ownership_rate')
    df=merge_for_economics(duration2,direction2,df,households_debt_to_gdp,'households_debt_to_gdp')
    df=merge_for_economics(duration2,direction2,df,debt_to_income,'debt_to_income')
    df=merge_for_economics(duration2,direction2,df,housing_index,'housing_index')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,housing_starts,'housing_starts')
    df=merge_for_economics(duration2,direction2,df,import_prices,'import_prices')
    df=merge_for_economics(duration2,direction2,df,economics_imports,'economics_imports')
    df=merge_for_economics(duration2,direction2,df,lending_rate,'lending_rate')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,labour_costs,'labour_costs')
    df=merge_for_economics(duration2,direction2,df,inflation_rate,'inflation_rate')
    df=merge_for_economics(duration2,direction2,df,inflation_expectations,'inflation_expectations')
    #df=merge_for_economics(duration2,direction2,df,jobless_claims,'jobless_claims')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,inflation_rate_mom,'inflation_rate_mom')
    df=merge_for_economics(duration2,direction2,df,loans_to_private_sector,'loans_to_private_sector')
    df=merge_for_economics(duration2,direction2,df,loan_growth,'loan_growth')
    df=merge_for_economics(duration2,direction2,df,minimum_wages,'minimum_wages')
      
    df=merge_for_economics(duration2,direction2,df,long_term_unemployment_rate,'long_term_unemployment_rate')
    df=merge_for_economics(duration2,direction2,df,money_supply_m1,'money_supply_m1')
    df=merge_for_economics(duration2,direction2,df,natural_gas_imports,'natural_gas_imports')
    df=merge_for_economics(duration2,direction2,df,economics_money_supply_m3,'economics_money_supply_m3')
    
    df=merge_for_economics(duration2,direction2,df,part_time_employment,'part_time_employment')
    df=merge_for_economics(duration2,direction2,df,personal_savings,'personal_savings')
    df=merge_for_economics(duration2,direction2,df,personal_spending,'personal_spending')
    df=merge_for_economics(duration2,direction2,df,price_to_rent_ratio,'price_to_rent_ratio')
    
    df=merge_for_economics(duration2,direction2,df,private_debt_to_gdp,'private_debt_to_gdp')
    df=merge_for_economics(duration2,direction2,df,private_sector_credit,'private_sector_credit')
    df=merge_for_economics(duration2,direction2,df,producer_prices,'producer_prices')
    df=merge_for_economics(duration2,direction2,df,producer_prices_change,'producer_prices_change')
    print("data length"+str(len(df)))
      
    df=merge_for_economics(duration2,direction2,df,productivity,'productivity')
    df=merge_for_economics(duration2,direction2,df,remittances,'remittances')
    df=merge_for_economics(duration2,direction2,df,retail_sales_mom,'retail_sales_mom')
    df=merge_for_economics(duration2,direction2,df,retail_sales_yoy,'retail_sales_yoy')
      
    df=merge_for_economics(duration2,direction2,df,retirement_age_men,'retirement_age_men')
    df=merge_for_economics(duration2,direction2,df,retirement_age_women,'retirement_age_women')
    #df=merge_for_economics(duration2,direction2,df,stock_market_indexes,'stock_market_indexes')
    df=merge_for_economics(duration2,direction2,df,interest_rate,'interest_rate')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,terms_of_trade,'terms_of_trade')
    df=merge_for_economics(duration2,direction2,df,terrorism_index,'terrorism_index')
    df=merge_for_economics(duration2,direction2,df,tourism_revenues,'tourism_revenues')
    df=merge_for_economics(duration2,direction2,df,tourist_arrivals,'tourist_arrivals')
      
    df=merge_for_economics(duration2,direction2,df,unemployed_persons,'unemployed_persons')
    df=merge_for_economics(duration2,direction2,df,unemployment_rate,'unemployment_rate')
    df=merge_for_economics(duration2,direction2,df,wage_growth,'wage_growth')
    df=merge_for_economics(duration2,direction2,df,economics_wages,'economics_wages')
      
    df=merge_for_economics(duration2,direction2,df,weapons_sales,'weapons_sales')
    df=merge_for_economics(duration2,direction2,df,wages_in_manufacturing,'wages_in_manufacturing')
    df=merge_for_economics(duration2,direction2,df,youth_unemployment_rate,'youth_unemployment_rate')
    print("data length"+str(len(df)))
      
      
      
    
      
    
    df=merge_for_economics(duration2,direction2,df,food_inflation,'food_inflation')
    df=merge_for_economics(duration2,direction2,df,economics_export_data,'economics_export_data')
    df=merge_for_economics(duration2,direction2,df,balance_of_trade_data,'balance_of_trade_data')
    df=merge_for_economics(duration2,direction2,df,bank_lending_rate_data,'bank_lending_rate_data')
    df=merge_for_economics(duration2,direction2,df,banks_balance_sheet_data,'banks_balance_sheet_data')  
    #df=merge_for_economics(duration2,direction2,df,economics_bonds_data,'economics_bonds_data')
    df=merge_for_economics(duration2,direction2,df,cash_reserve_ratio_data,'cash_reserve_ratio_data')  
    df=merge_for_economics(duration2,direction2,df,building_permit_data,'building_permit_data')  
    df=merge_for_economics(duration2,direction2,df,capital_flows_data,'capital_flows_data')  
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,economics_consumer_confidence_data,'economics_consumer_confidence_data')  
    df=merge_for_economics(duration2,direction2,df,economics_consumer_credit_data,'economics_consumer_credit_data')   
    df=merge_for_economics(duration2,direction2,df,consumer_price_index_cpi_data,'consumer_price_index_cpi_data')   
    df=merge_for_economics(duration2,direction2,df,consumer_spending_data,'consumer_spending_data')   
    df=merge_for_economics(duration2,direction2,df,core_inflation_rate_data,'core_inflation_rate_data')  
    print("data length"+str(len(df)))    
  

  
    col.remove("XPCT_DLVRY_DT")
    col.remove("Days_Delayed")
   #if(training_set==True):


    
    numeric_features = [ ] #'Order Entry Date' 'Ordered Value'
    numeric_bin = []
    
    print("Encoding completed")
      
    
    return df

from MyApp.MultiColumnLabelEncoder import MultiColumnLabelEncoder
from sklearn import preprocessing
import pandas as pd
from sklearn import preprocessing
import pickle
import os

from MyApp.feature_extractors.geo_political_risk import geo_political_risk

from MyApp.merge_for_economics import merge_for_economics
from MyApp.feature_extractors.other_numeric_features import merge_for_other_features
from MyApp.merge_for_forex import merge_for_forex


def categorical_enc(x,name):

  
# label_encoder object knows how to understand word labels.
  label_encoder = preprocessing.LabelEncoder()
  
# Encode labels in column 'species'.
  encoded= label_encoder.fit_transform(x)
  #encoded=pd.Categorical(x).codes
  encoded=pd.DataFrame(encoded)
  encoded.columns=[name]
  return encoded,label_encoder
    
def merging_encoding(df,forex,risk,trends,india_cpi_data,pet_consumption,railway_goods,rainfall_india_data,air_quality_kolkata,air_quality_newdehli,gasoline_price_data,motor_vehicles_data,motor_vehicles_class_type_data,economics_export_data,balance_of_trade_data,bank_lending_rate_data,banks_balance_sheet_data,economics_bonds_data,cash_reserve_ratio_data,building_permit_data,capital_flows_data,economics_consumer_confidence_data,economics_consumer_credit_data,consumer_price_index_cpi_data,consumer_spending_data,core_inflation_rate_data,economics_currencies_data,food_inflation,foreign_direct_investment,foreign_exchange_reserves,economics_unemployment_rate,full_time_employment,economics_gasoline_prices,gdp_deflator,debt_to_gdp,harmonised_consumer_prices,home_ownership_rate,households_debt_to_gdp,debt_to_income,housing_index,housing_starts,import_prices,economics_imports,lending_rate,labour_costs,inflation_rate,inflation_expectations,jobless_claims,inflation_rate_mom,loans_to_private_sector,loan_growth,minimum_wages,long_term_unemployment_rate,money_supply_m1,natural_gas_imports,economics_money_supply_m3,part_time_employment,personal_savings,personal_spending,price_to_rent_ratio,private_debt_to_gdp,private_sector_credit,producer_prices,producer_prices_change,productivity,remittances,retail_sales_mom,retail_sales_yoy,retirement_age_men,retirement_age_women,stock_market_indexes,interest_rate,terms_of_trade,terrorism_index,tourism_revenues,tourist_arrivals,unemployed_persons,unemployment_rate,wage_growth,economics_wages,weapons_sales,wages_in_manufacturing,youth_unemployment_rate,col,training_set):
    col2=['EM_ITEM_NUM','GNRC_NAME','THERAP_CLASS','FD Location','API Location','DC_NUM','SPLR_VENDOR_NUM','SPLR_NAME','SPLR_REGION','SPLR_POSTAL_CODE','SPLR_COUNTRY']   
    cencoder=MultiColumnLabelEncoder(columns = col2)
    df=cencoder.fit_transform(df,training_set)
     
    df = merge_for_other_features(df,risk,"risk") #df2.join(
    print("data length"+str(len(df)))
    print("trends data")

    print("data length"+str(len(df)))
    df = merge_for_other_features(df,india_cpi_data,"india_cpi_data")
    print("data length"+str(len(df)))
    # #df = pet_consumption_fun(df,pet_consumption) #problem1 need to normalize
    df= merge_for_other_features(df,railway_goods,"railway_goods")
    print("data length"+str(len(df)))
    df= merge_for_other_features(df,rainfall_india_data,"rainfall_india_data") #problem
    print("data length"+str(len(df)))
    #print("kolkata data")
    #df= merge_for_other_features(df,air_quality_kolkata,"air_quality_kolkata") 
    print("data length"+str(len(df)))
    df= merge_for_other_features(df,air_quality_newdehli,"air_quality_newdehli") 
    print("data length"+str(len(df)))
  # #df= date_specific_features_fun(df,gasoline_price_data) #problem
  ##df= date_specific_features_fun(df,motor_vehicles_data) #problem
   #df= date_specific_features_fun(df,motor_vehicles_class_type_data)

    df=merge_for_forex(df,forex)
    print("kolkata data")
    duration="30d"
    direction1="backward"
    df= merge_for_other_features(df,air_quality_kolkata,"air_quality_kolkata") 
    df = merge_for_other_features(df,trends,"trends")
    df=merge_for_economics(duration,direction1,df,foreign_direct_investment,'foreign_direct_investment_30days_backward')
    #print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,foreign_exchange_reserves,'foreign_exchange_reserves_30days_backward')
    #print("data length"+str(len(df)))
    #df=merge_for_economics(duration,direction1,df,economics_unemployment_rate,'economics_unemployment_rate_30days_backward')
    print("data length"+str(len(df)))
    #df=merge_for_economics(duration,direction1,df,full_time_employment,'full_time_employment_30days_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,economics_gasoline_prices,'economics_gasoline_prices_30days_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,gdp_deflator,'gdp_deflator_30days_backward')
    df=merge_for_economics(duration,direction1,df,debt_to_gdp,'debt_to_gdp_30days_backward')
    #df=merge_for_economics(duration,direction1,df,harmonised_consumer_prices,'harmonised_consumer_prices_30days_backward')
    #print("data length"+str(len(df)))
      
    #df=merge_for_economics(duration,direction1,df,home_ownership_rate,'home_ownership_rate_30days_backward')
    df=merge_for_economics(duration,direction1,df,households_debt_to_gdp,'households_debt_to_gdp_30days_backward')
    #df=merge_for_economics(duration,direction1,df,debt_to_income,'debt_to_income_30days_backward')
    df=merge_for_economics(duration,direction1,df,housing_index,'housing_index_30days_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,housing_starts,'housing_starts_30days_backward')
    df=merge_for_economics(duration,direction1,df,import_prices,'import_prices_30days_backward')
    df=merge_for_economics(duration,direction1,df,economics_imports,'economics_imports_30days_backward')
    df=merge_for_economics(duration,direction1,df,lending_rate,'lending_rate_30days_backward')
    #print("data length"+str(len(df)))
    #df=merge_for_economics(duration,direction1,df,labour_costs,'labour_costs_30days_backward')
    df=merge_for_economics(duration,direction1,df,inflation_rate,'inflation_rate_30days_backward')
    df=merge_for_economics(duration,direction1,df,inflation_expectations,'inflation_expectations_30days_backward')
    #df=merge_for_economics(duration,direction1,df,jobless_claims,'jobless_claims_30days_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,inflation_rate_mom,'inflation_rate_mom_30days_backward')
    #df=merge_for_economics(duration,direction1,df,loans_to_private_sector,'loans_to_private_sector_30days_backward')
    df=merge_for_economics(duration,direction1,df,loan_growth,'loan_growth_30days_backward')
    df=merge_for_economics(duration,direction1,df,minimum_wages,'minimum_wages_30days_backward')
      
    #df=merge_for_economics(duration,direction1,df,long_term_unemployment_rate,'long_term_unemployment_rate_30days_backward')
    #df=merge_for_economics(duration,direction1,df,money_supply_m1,'money_supply_m1_30days_backward')
    #df=merge_for_economics(duration,direction1,df,natural_gas_imports,'natural_gas_imports_30days_backward')
    #df=merge_for_economics(duration,direction1,df,economics_money_supply_m3,'economics_money_supply_m3_30days_backward')
    
    #df=merge_for_economics(duration,direction1,df,part_time_employment,'part_time_employment_30days_backward')
    df=merge_for_economics(duration,direction1,df,personal_savings,'personal_savings_30days_backward')
    df=merge_for_economics(duration,direction1,df,personal_spending,'personal_spending_30days_backward')
    #df=merge_for_economics(duration,direction1,df,price_to_rent_ratio,'price_to_rent_ratio_30days_backward')
    
    df=merge_for_economics(duration,direction1,df,private_debt_to_gdp,'private_debt_to_gdp_30days_backward')
    #df=merge_for_economics(duration,direction1,df,private_sector_credit,'private_sector_credit_30days_backward')
    df=merge_for_economics(duration,direction1,df,producer_prices,'producer_prices_30days_backward')
    df=merge_for_economics(duration,direction1,df,producer_prices_change,'producer_prices_change_30days_backward')
    #print("data length"+str(len(df)))
      
    df=merge_for_economics(duration,direction1,df,productivity,'productivity_30days_backward')
    #df=merge_for_economics(duration,direction1,df,remittances,'remittances_30days_backward')
    df=merge_for_economics(duration,direction1,df,retail_sales_mom,'retail_sales_mom_30days_backward')
    df=merge_for_economics(duration,direction1,df,retail_sales_yoy,'retail_sales_yoy_30days_backward')
      
    #df=merge_for_economics(duration,direction1,df,retirement_age_men,'retirement_age_men_30days_backward')
    #df=merge_for_economics(duration,direction1,df,retirement_age_women,'retirement_age_women_30days_backward')
    #df=merge_for_economics(duration,direction1,df,stock_market_indexes,'stock_market_indexes_30days_backward')
    df=merge_for_economics(duration,direction1,df,interest_rate,'interest_rate_30days_backward')
    #print("data length"+str(len(df)))
    #df=merge_for_economics(duration,direction1,df,terms_of_trade,'terms_of_trade_30days_backward')
    #df=merge_for_economics(duration,direction1,df,terrorism_index,'terrorism_index_30days_backward')
    df=merge_for_economics(duration,direction1,df,tourism_revenues,'tourism_revenues_30days_backward')
    df=merge_for_economics(duration,direction1,df,tourist_arrivals,'tourist_arrivals_30days_backward')
      
    df=merge_for_economics(duration,direction1,df,unemployed_persons,'unemployed_persons_30days_backward')
    df=merge_for_economics(duration,direction1,df,unemployment_rate,'unemployment_rate_30days_backward')
    df=merge_for_economics(duration,direction1,df,wage_growth,'wage_growth_30days_backward')
    df=merge_for_economics(duration,direction1,df,economics_wages,'economics_wages_30days_backward')
      
    #df=merge_for_economics(duration,direction1,df,weapons_sales,'weapons_sales_30days_backward')
    #df=merge_for_economics(duration,direction1,df,wages_in_manufacturing,'wages_in_manufacturing_30days_backward')
    #df=merge_for_economics(duration,direction1,df,youth_unemployment_rate,'youth_unemployment_rate_30days_backward')
    #print("data length"+str(len(df)))
      




    duration="90d"
    direction1="backward"
    df=merge_for_economics(duration,direction1,df,foreign_direct_investment,'foreign_direct_investment_90days_backward')
    #print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,foreign_exchange_reserves,'foreign_exchange_reserves_90days_backward')
    #print("data length"+str(len(df)))
    #df=merge_for_economics(duration,direction1,df,economics_unemployment_rate,'economics_unemployment_rate_90days_backward')
    print("data length"+str(len(df)))
    #df=merge_for_economics(duration,direction1,df,full_time_employment,'full_time_employment_90days_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,economics_gasoline_prices,'economics_gasoline_prices_90days_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,gdp_deflator,'gdp_deflator_90days_backward')
    df=merge_for_economics(duration,direction1,df,debt_to_gdp,'debt_to_gdp_90days_backward')
    #df=merge_for_economics(duration,direction1,df,harmonised_consumer_prices,'harmonised_consumer_prices_90days_backward')
    #print("data length"+str(len(df)))
      
    #df=merge_for_economics(duration,direction1,df,home_ownership_rate,'home_ownership_rate_90days_backward')
    df=merge_for_economics(duration,direction1,df,households_debt_to_gdp,'households_debt_to_gdp_90days_backward')
    #df=merge_for_economics(duration,direction1,df,debt_to_income,'debt_to_income_90days_backward')
    df=merge_for_economics(duration,direction1,df,housing_index,'housing_index_90days_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,housing_starts,'housing_starts_90days_backward')
    df=merge_for_economics(duration,direction1,df,import_prices,'import_prices_90days_backward')
    df=merge_for_economics(duration,direction1,df,economics_imports,'economics_imports_90days_backward')
    df=merge_for_economics(duration,direction1,df,lending_rate,'lending_rate_90days_backward')
    #print("data length"+str(len(df)))
    #df=merge_for_economics(duration,direction1,df,labour_costs,'labour_costs_90days_backward')
    df=merge_for_economics(duration,direction1,df,inflation_rate,'inflation_rate_90days_backward')
    df=merge_for_economics(duration,direction1,df,inflation_expectations,'inflation_expectations_90days_backward')
    #df=merge_for_economics(duration,direction1,df,jobless_claims,'jobless_claims_90days_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,inflation_rate_mom,'inflation_rate_mom_90days_backward')
    #df=merge_for_economics(duration,direction1,df,loans_to_private_sector,'loans_to_private_sector_90days_backward')
    df=merge_for_economics(duration,direction1,df,loan_growth,'loan_growth_90days_backward')
    df=merge_for_economics(duration,direction1,df,minimum_wages,'minimum_wages_90days_backward')
      
    #df=merge_for_economics(duration,direction1,df,long_term_unemployment_rate,'long_term_unemployment_rate_90days_backward')
    #df=merge_for_economics(duration,direction1,df,money_supply_m1,'money_supply_m1_90days_backward')
    #df=merge_for_economics(duration,direction1,df,natural_gas_imports,'natural_gas_imports_90days_backward')
    #df=merge_for_economics(duration,direction1,df,economics_money_supply_m3,'economics_money_supply_m3_90days_backward')
    
    #df=merge_for_economics(duration,direction1,df,part_time_employment,'part_time_employment_90days_backward')
    df=merge_for_economics(duration,direction1,df,personal_savings,'personal_savings_90days_backward')
    df=merge_for_economics(duration,direction1,df,personal_spending,'personal_spending_90days_backward')
    #df=merge_for_economics(duration,direction1,df,price_to_rent_ratio,'price_to_rent_ratio_90days_backward')
    
    df=merge_for_economics(duration,direction1,df,private_debt_to_gdp,'private_debt_to_gdp_90days_backward')
    #df=merge_for_economics(duration,direction1,df,private_sector_credit,'private_sector_credit_90days_backward')
    df=merge_for_economics(duration,direction1,df,producer_prices,'producer_prices_90days_backward')
    df=merge_for_economics(duration,direction1,df,producer_prices_change,'producer_prices_change_90days_backward')
    #print("data length"+str(len(df)))
      
    df=merge_for_economics(duration,direction1,df,productivity,'productivity_90days_backward')
    #df=merge_for_economics(duration,direction1,df,remittances,'remittances_90days_backward')
    df=merge_for_economics(duration,direction1,df,retail_sales_mom,'retail_sales_mom_90days_backward')
    df=merge_for_economics(duration,direction1,df,retail_sales_yoy,'retail_sales_yoy_90days_backward')
      
    #df=merge_for_economics(duration,direction1,df,retirement_age_men,'retirement_age_men_90days_backward')
    #df=merge_for_economics(duration,direction1,df,retirement_age_women,'retirement_age_women_90days_backward')
    #df=merge_for_economics(duration,direction1,df,stock_market_indexes,'stock_market_indexes_90days_backward')
    df=merge_for_economics(duration,direction1,df,interest_rate,'interest_rate_90days_backward')
    #print("data length"+str(len(df)))
    #df=merge_for_economics(duration,direction1,df,terms_of_trade,'terms_of_trade_90days_backward')
    #df=merge_for_economics(duration,direction1,df,terrorism_index,'terrorism_index_90days_backward')
    df=merge_for_economics(duration,direction1,df,tourism_revenues,'tourism_revenues_90days_backward')
    df=merge_for_economics(duration,direction1,df,tourist_arrivals,'tourist_arrivals_90days_backward')
      
    df=merge_for_economics(duration,direction1,df,unemployed_persons,'unemployed_persons_90days_backward')
    df=merge_for_economics(duration,direction1,df,unemployment_rate,'unemployment_rate_90days_backward')
    df=merge_for_economics(duration,direction1,df,wage_growth,'wage_growth_90days_backward')
    df=merge_for_economics(duration,direction1,df,economics_wages,'economics_wages_90days_backward')
      
    #df=merge_for_economics(duration,direction1,df,weapons_sales,'weapons_sales_90days_backward')
    #df=merge_for_economics(duration,direction1,df,wages_in_manufacturing,'wages_in_manufacturing_90days_backward')
    #df=merge_for_economics(duration,direction1,df,youth_unemployment_rate,'youth_unemployment_rate_90days_backward')
    #print("data length"+str(len(df)))
    duration2="180d"
    direction2="backward"
    df=merge_for_economics(duration,direction1,df,food_inflation,'food_inflation_180days_backward')
    df=merge_for_economics(duration,direction1,df,economics_export_data,'economics_export_data_180days_backward')
    df=merge_for_economics(duration,direction1,df,balance_of_trade_data,'balance_of_trade_data_180days_backward')
    df=merge_for_economics(duration,direction1,df,bank_lending_rate_data,'bank_lending_rate_data_180days_backward')
    df=merge_for_economics(duration,direction1,df,banks_balance_sheet_data,'banks_balance_sheet_data_180days_backward')  
    #df=merge_for_economics(duration,direction1,df,economics_bonds_data,'economics_bonds_data_180days_backward')
    df=merge_for_economics(duration,direction1,df,cash_reserve_ratio_data,'cash_reserve_ratio_data_180days_backward')  
    df=merge_for_economics(duration,direction1,df,building_permit_data,'building_permit_data_180days_backward')  
    df=merge_for_economics(duration,direction1,df,capital_flows_data,'capital_flows_data_180days_backward')  
    print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,economics_consumer_confidence_data,'economics_consumer_confidence_data_180days_backward')  
    df=merge_for_economics(duration,direction1,df,economics_consumer_credit_data,'economics_consumer_credit_data_180days_backward')   
    df=merge_for_economics(duration,direction1,df,consumer_price_index_cpi_data,'consumer_price_index_cpi_data_180days_backward')   
    df=merge_for_economics(duration,direction1,df,consumer_spending_data,'consumer_spending_data_180days_backward')   
    df=merge_for_economics(duration,direction1,df,core_inflation_rate_data,'core_inflation_rate_data_180days_backward')  
    print("data length"+str(len(df)))
    #df=merge_for_economics(duration,direction1,df,economics_currencies_data,'economics_currencies_data_180days_backward')    
      
    df=merge_for_economics(duration2,direction2,df,home_ownership_rate,'home_ownership_rate_180days_backward')
    df=merge_for_economics(duration2,direction2,df,households_debt_to_gdp,'households_debt_to_gdp_180days_backward')
    df=merge_for_economics(duration2,direction2,df,debt_to_income,'debt_to_income_180days_backward')
    df=merge_for_economics(duration2,direction2,df,housing_index,'housing_index_180days_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,housing_starts,'housing_starts_180days_backward')
    df=merge_for_economics(duration2,direction2,df,import_prices,'import_prices_180days_backward')
    df=merge_for_economics(duration2,direction2,df,economics_imports,'economics_imports_180days_backward')
    df=merge_for_economics(duration2,direction2,df,lending_rate,'lending_rate_180days_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,labour_costs,'labour_costs_180days_backward')
    df=merge_for_economics(duration2,direction2,df,inflation_rate,'inflation_rate_180days_backward')
    df=merge_for_economics(duration2,direction2,df,inflation_expectations,'inflation_expectations_180days_backward')
    #df=merge_for_economics(duration2,direction2,df,jobless_claims,'jobless_claims_180days_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,inflation_rate_mom,'inflation_rate_mom_180days_backward')
    df=merge_for_economics(duration2,direction2,df,loans_to_private_sector,'loans_to_private_sector_180days_backward')
    df=merge_for_economics(duration2,direction2,df,loan_growth,'loan_growth_180days_backward')
    df=merge_for_economics(duration2,direction2,df,minimum_wages,'minimum_wages_180days_backward')
      
    df=merge_for_economics(duration2,direction2,df,long_term_unemployment_rate,'long_term_unemployment_rate_180days_backward')
    df=merge_for_economics(duration2,direction2,df,money_supply_m1,'money_supply_m1_180days_backward')
    df=merge_for_economics(duration2,direction2,df,natural_gas_imports,'natural_gas_imports_180days_backward')
    df=merge_for_economics(duration2,direction2,df,economics_money_supply_m3,'economics_money_supply_m3_180days_backward')
    
    df=merge_for_economics(duration2,direction2,df,part_time_employment,'part_time_employment_180days_backward')
    df=merge_for_economics(duration2,direction2,df,personal_savings,'personal_savings_180days_backward')
    df=merge_for_economics(duration2,direction2,df,personal_spending,'personal_spending_180days_backward')
    df=merge_for_economics(duration2,direction2,df,price_to_rent_ratio,'price_to_rent_ratio_180days_backward')
    
    df=merge_for_economics(duration2,direction2,df,private_debt_to_gdp,'private_debt_to_gdp_180days_backward')
    df=merge_for_economics(duration2,direction2,df,private_sector_credit,'private_sector_credit_180days_backward')
    df=merge_for_economics(duration2,direction2,df,producer_prices,'producer_prices_180days_backward')
    df=merge_for_economics(duration2,direction2,df,producer_prices_change,'producer_prices_change_180days_backward')
    print("data length"+str(len(df)))
      
    df=merge_for_economics(duration2,direction2,df,productivity,'productivity_180days_backward')
    df=merge_for_economics(duration2,direction2,df,remittances,'remittances_180days_backward')
    df=merge_for_economics(duration2,direction2,df,retail_sales_mom,'retail_sales_mom_180days_backward')
    df=merge_for_economics(duration2,direction2,df,retail_sales_yoy,'retail_sales_yoy_180days_backward')
      
    df=merge_for_economics(duration2,direction2,df,retirement_age_men,'retirement_age_men_180days_backward')
    df=merge_for_economics(duration2,direction2,df,retirement_age_women,'retirement_age_women_180days_backward')
    #df=merge_for_economics(duration2,direction2,df,stock_market_indexes,'stock_market_indexes_180days_backward')
    df=merge_for_economics(duration2,direction2,df,interest_rate,'interest_rate_180days_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,terms_of_trade,'terms_of_trade_180days_backward')
    df=merge_for_economics(duration2,direction2,df,terrorism_index,'terrorism_index_180days_backward')
    df=merge_for_economics(duration2,direction2,df,tourism_revenues,'tourism_revenues_180days_backward')
    df=merge_for_economics(duration2,direction2,df,tourist_arrivals,'tourist_arrivals_180days_backward')
      
    df=merge_for_economics(duration2,direction2,df,unemployed_persons,'unemployed_persons_180days_backward')
    df=merge_for_economics(duration2,direction2,df,unemployment_rate,'unemployment_rate_180days_backward')
    df=merge_for_economics(duration2,direction2,df,wage_growth,'wage_growth_180days_backward')
    df=merge_for_economics(duration2,direction2,df,economics_wages,'economics_wages_180days_backward')
      
    df=merge_for_economics(duration2,direction2,df,weapons_sales,'weapons_sales_180days_backward')
    df=merge_for_economics(duration2,direction2,df,wages_in_manufacturing,'wages_in_manufacturing_180days_backward')
    df=merge_for_economics(duration2,direction2,df,youth_unemployment_rate,'youth_unemployment_rate_180days_backward')
    print("data length"+str(len(df)))
      
      
      
    
      
    
    df=merge_for_economics(duration2,direction2,df,food_inflation,'food_inflation_180days_backward')
    df=merge_for_economics(duration2,direction2,df,economics_export_data,'economics_export_data_180days_backward')
    df=merge_for_economics(duration2,direction2,df,balance_of_trade_data,'balance_of_trade_data_180days_backward')
    df=merge_for_economics(duration2,direction2,df,bank_lending_rate_data,'bank_lending_rate_data_180days_backward')
    df=merge_for_economics(duration2,direction2,df,banks_balance_sheet_data,'banks_balance_sheet_data_180days_backward')  
    #df=merge_for_economics(duration2,direction2,df,economics_bonds_data,'economics_bonds_data_180days_backward')
    df=merge_for_economics(duration2,direction2,df,cash_reserve_ratio_data,'cash_reserve_ratio_data_180days_backward')  
    df=merge_for_economics(duration2,direction2,df,building_permit_data,'building_permit_data_180days_backward')  
    df=merge_for_economics(duration2,direction2,df,capital_flows_data,'capital_flows_data_180days_backward')  
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,economics_consumer_confidence_data,'economics_consumer_confidence_data_180days_backward')  
    df=merge_for_economics(duration2,direction2,df,economics_consumer_credit_data,'economics_consumer_credit_data_180days_backward')   
    df=merge_for_economics(duration2,direction2,df,consumer_price_index_cpi_data,'consumer_price_index_cpi_data_180days_backward')   
    df=merge_for_economics(duration2,direction2,df,consumer_spending_data,'consumer_spending_data_180days_backward')   
    df=merge_for_economics(duration2,direction2,df,core_inflation_rate_data,'core_inflation_rate_data_180days_backward')  
    duration2="150d"
    direction2="backward"
    df=merge_for_economics(duration,direction1,df,food_inflation,'food_inflation_150days_backward')
    df=merge_for_economics(duration,direction1,df,economics_export_data,'economics_export_data_150days_backward')
    df=merge_for_economics(duration,direction1,df,balance_of_trade_data,'balance_of_trade_data_150days_backward')
    df=merge_for_economics(duration,direction1,df,bank_lending_rate_data,'bank_lending_rate_data_150days_backward')
    df=merge_for_economics(duration,direction1,df,banks_balance_sheet_data,'banks_balance_sheet_data_150days_backward')  
    #df=merge_for_economics(duration,direction1,df,economics_bonds_data,'economics_bonds_data_150days_backward')
    df=merge_for_economics(duration,direction1,df,cash_reserve_ratio_data,'cash_reserve_ratio_data_150days_backward')  
    df=merge_for_economics(duration,direction1,df,building_permit_data,'building_permit_data_150days_backward')  
    df=merge_for_economics(duration,direction1,df,capital_flows_data,'capital_flows_data_150days_backward')  
    print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,economics_consumer_confidence_data,'economics_consumer_confidence_data_150days_backward')  
    df=merge_for_economics(duration,direction1,df,economics_consumer_credit_data,'economics_consumer_credit_data_150days_backward')   
    df=merge_for_economics(duration,direction1,df,consumer_price_index_cpi_data,'consumer_price_index_cpi_data_150days_backward')   
    df=merge_for_economics(duration,direction1,df,consumer_spending_data,'consumer_spending_data_150days_backward')   
    df=merge_for_economics(duration,direction1,df,core_inflation_rate_data,'core_inflation_rate_data_150days_backward')  
    print("data length"+str(len(df)))
    #df=merge_for_economics(duration,direction1,df,economics_currencies_data,'economics_currencies_data_150days_backward')    
      
    df=merge_for_economics(duration2,direction2,df,home_ownership_rate,'home_ownership_rate_150days_backward')
    df=merge_for_economics(duration2,direction2,df,households_debt_to_gdp,'households_debt_to_gdp_150days_backward')
    df=merge_for_economics(duration2,direction2,df,debt_to_income,'debt_to_income_150days_backward')
    df=merge_for_economics(duration2,direction2,df,housing_index,'housing_index_150days_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,housing_starts,'housing_starts_150days_backward')
    df=merge_for_economics(duration2,direction2,df,import_prices,'import_prices_150days_backward')
    df=merge_for_economics(duration2,direction2,df,economics_imports,'economics_imports_150days_backward')
    df=merge_for_economics(duration2,direction2,df,lending_rate,'lending_rate_150days_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,labour_costs,'labour_costs_150days_backward')
    df=merge_for_economics(duration2,direction2,df,inflation_rate,'inflation_rate_150days_backward')
    df=merge_for_economics(duration2,direction2,df,inflation_expectations,'inflation_expectations_150days_backward')
    #df=merge_for_economics(duration2,direction2,df,jobless_claims,'jobless_claims_150days_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,inflation_rate_mom,'inflation_rate_mom_150days_backward')
    df=merge_for_economics(duration2,direction2,df,loans_to_private_sector,'loans_to_private_sector_150days_backward')
    df=merge_for_economics(duration2,direction2,df,loan_growth,'loan_growth_150days_backward')
    df=merge_for_economics(duration2,direction2,df,minimum_wages,'minimum_wages_150days_backward')
      
    df=merge_for_economics(duration2,direction2,df,long_term_unemployment_rate,'long_term_unemployment_rate_150days_backward')
    df=merge_for_economics(duration2,direction2,df,money_supply_m1,'money_supply_m1_150days_backward')
    df=merge_for_economics(duration2,direction2,df,natural_gas_imports,'natural_gas_imports_150days_backward')
    df=merge_for_economics(duration2,direction2,df,economics_money_supply_m3,'economics_money_supply_m3_150days_backward')
    
    df=merge_for_economics(duration2,direction2,df,part_time_employment,'part_time_employment_150days_backward')
    df=merge_for_economics(duration2,direction2,df,personal_savings,'personal_savings_150days_backward')
    df=merge_for_economics(duration2,direction2,df,personal_spending,'personal_spending_150days_backward')
    df=merge_for_economics(duration2,direction2,df,price_to_rent_ratio,'price_to_rent_ratio_150days_backward')
    
    df=merge_for_economics(duration2,direction2,df,private_debt_to_gdp,'private_debt_to_gdp_150days_backward')
    df=merge_for_economics(duration2,direction2,df,private_sector_credit,'private_sector_credit_150days_backward')
    df=merge_for_economics(duration2,direction2,df,producer_prices,'producer_prices_150days_backward')
    df=merge_for_economics(duration2,direction2,df,producer_prices_change,'producer_prices_change_150days_backward')
    print("data length"+str(len(df)))
      
    df=merge_for_economics(duration2,direction2,df,productivity,'productivity_150days_backward')
    df=merge_for_economics(duration2,direction2,df,remittances,'remittances_150days_backward')
    df=merge_for_economics(duration2,direction2,df,retail_sales_mom,'retail_sales_mom_150days_backward')
    df=merge_for_economics(duration2,direction2,df,retail_sales_yoy,'retail_sales_yoy_150days_backward')
      
    df=merge_for_economics(duration2,direction2,df,retirement_age_men,'retirement_age_men_150days_backward')
    df=merge_for_economics(duration2,direction2,df,retirement_age_women,'retirement_age_women_150days_backward')
    #df=merge_for_economics(duration2,direction2,df,stock_market_indexes,'stock_market_indexes_150days_backward')
    df=merge_for_economics(duration2,direction2,df,interest_rate,'interest_rate_150days_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,terms_of_trade,'terms_of_trade_150days_backward')
    df=merge_for_economics(duration2,direction2,df,terrorism_index,'terrorism_index_150days_backward')
    df=merge_for_economics(duration2,direction2,df,tourism_revenues,'tourism_revenues_150days_backward')
    df=merge_for_economics(duration2,direction2,df,tourist_arrivals,'tourist_arrivals_150days_backward')
      
    df=merge_for_economics(duration2,direction2,df,unemployed_persons,'unemployed_persons_150days_backward')
    df=merge_for_economics(duration2,direction2,df,unemployment_rate,'unemployment_rate_150days_backward')
    df=merge_for_economics(duration2,direction2,df,wage_growth,'wage_growth_150days_backward')
    df=merge_for_economics(duration2,direction2,df,economics_wages,'economics_wages_150days_backward')
      
    df=merge_for_economics(duration2,direction2,df,weapons_sales,'weapons_sales_150days_backward')
    df=merge_for_economics(duration2,direction2,df,wages_in_manufacturing,'wages_in_manufacturing_150days_backward')
    df=merge_for_economics(duration2,direction2,df,youth_unemployment_rate,'youth_unemployment_rate_150days_backward')
    print("data length"+str(len(df)))
      
      
      
    
      
    
    df=merge_for_economics(duration2,direction2,df,food_inflation,'food_inflation_150days_backward')
    df=merge_for_economics(duration2,direction2,df,economics_export_data,'economics_export_data_150days_backward')
    df=merge_for_economics(duration2,direction2,df,balance_of_trade_data,'balance_of_trade_data_150days_backward')
    df=merge_for_economics(duration2,direction2,df,bank_lending_rate_data,'bank_lending_rate_data_150days_backward')
    df=merge_for_economics(duration2,direction2,df,banks_balance_sheet_data,'banks_balance_sheet_data_150days_backward')  
    #df=merge_for_economics(duration2,direction2,df,economics_bonds_data,'economics_bonds_data_150days_backward')
    df=merge_for_economics(duration2,direction2,df,cash_reserve_ratio_data,'cash_reserve_ratio_data_150days_backward')  
    df=merge_for_economics(duration2,direction2,df,building_permit_data,'building_permit_data_150days_backward')  
    df=merge_for_economics(duration2,direction2,df,capital_flows_data,'capital_flows_data_150days_backward')  
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,economics_consumer_confidence_data,'economics_consumer_confidence_data_150days_backward')  
    df=merge_for_economics(duration2,direction2,df,economics_consumer_credit_data,'economics_consumer_credit_data_150days_backward')   
    df=merge_for_economics(duration2,direction2,df,consumer_price_index_cpi_data,'consumer_price_index_cpi_data_150days_backward')   
    df=merge_for_economics(duration2,direction2,df,consumer_spending_data,'consumer_spending_data_150days_backward')   
    df=merge_for_economics(duration2,direction2,df,core_inflation_rate_data,'core_inflation_rate_data_150days_backward')        
    duration2="120d"
    direction2="backward"
    df=merge_for_economics(duration,direction1,df,food_inflation,'food_inflation_120days_backward')
    df=merge_for_economics(duration,direction1,df,economics_export_data,'economics_export_data_120days_backward')
    df=merge_for_economics(duration,direction1,df,balance_of_trade_data,'balance_of_trade_data_120days_backward')
    df=merge_for_economics(duration,direction1,df,bank_lending_rate_data,'bank_lending_rate_data_120days_backward')
    df=merge_for_economics(duration,direction1,df,banks_balance_sheet_data,'banks_balance_sheet_data_120days_backward')  
    #df=merge_for_economics(duration,direction1,df,economics_bonds_data,'economics_bonds_data_120days_backward')
    df=merge_for_economics(duration,direction1,df,cash_reserve_ratio_data,'cash_reserve_ratio_data_120days_backward')  
    df=merge_for_economics(duration,direction1,df,building_permit_data,'building_permit_data_120days_backward')  
    df=merge_for_economics(duration,direction1,df,capital_flows_data,'capital_flows_data_120days_backward')  
    print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,economics_consumer_confidence_data,'economics_consumer_confidence_data_120days_backward')  
    df=merge_for_economics(duration,direction1,df,economics_consumer_credit_data,'economics_consumer_credit_data_120days_backward')   
    df=merge_for_economics(duration,direction1,df,consumer_price_index_cpi_data,'consumer_price_index_cpi_data_120days_backward')   
    df=merge_for_economics(duration,direction1,df,consumer_spending_data,'consumer_spending_data_120days_backward')   
    df=merge_for_economics(duration,direction1,df,core_inflation_rate_data,'core_inflation_rate_data_120days_backward')  
    print("data length"+str(len(df)))
    #df=merge_for_economics(duration,direction1,df,economics_currencies_data,'economics_currencies_data_120days_backward')    
      
    df=merge_for_economics(duration2,direction2,df,home_ownership_rate,'home_ownership_rate_120days_backward')
    df=merge_for_economics(duration2,direction2,df,households_debt_to_gdp,'households_debt_to_gdp_120days_backward')
    df=merge_for_economics(duration2,direction2,df,debt_to_income,'debt_to_income_120days_backward')
    df=merge_for_economics(duration2,direction2,df,housing_index,'housing_index_120days_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,housing_starts,'housing_starts_120days_backward')
    df=merge_for_economics(duration2,direction2,df,import_prices,'import_prices_120days_backward')
    df=merge_for_economics(duration2,direction2,df,economics_imports,'economics_imports_120days_backward')
    df=merge_for_economics(duration2,direction2,df,lending_rate,'lending_rate_120days_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,labour_costs,'labour_costs_120days_backward')
    df=merge_for_economics(duration2,direction2,df,inflation_rate,'inflation_rate_120days_backward')
    df=merge_for_economics(duration2,direction2,df,inflation_expectations,'inflation_expectations_120days_backward')
    #df=merge_for_economics(duration2,direction2,df,jobless_claims,'jobless_claims_120days_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,inflation_rate_mom,'inflation_rate_mom_120days_backward')
    df=merge_for_economics(duration2,direction2,df,loans_to_private_sector,'loans_to_private_sector_120days_backward')
    df=merge_for_economics(duration2,direction2,df,loan_growth,'loan_growth_120days_backward')
    df=merge_for_economics(duration2,direction2,df,minimum_wages,'minimum_wages_120days_backward')
      
    df=merge_for_economics(duration2,direction2,df,long_term_unemployment_rate,'long_term_unemployment_rate_120days_backward')
    df=merge_for_economics(duration2,direction2,df,money_supply_m1,'money_supply_m1_120days_backward')
    df=merge_for_economics(duration2,direction2,df,natural_gas_imports,'natural_gas_imports_120days_backward')
    df=merge_for_economics(duration2,direction2,df,economics_money_supply_m3,'economics_money_supply_m3_120days_backward')
    
    df=merge_for_economics(duration2,direction2,df,part_time_employment,'part_time_employment_120days_backward')
    df=merge_for_economics(duration2,direction2,df,personal_savings,'personal_savings_120days_backward')
    df=merge_for_economics(duration2,direction2,df,personal_spending,'personal_spending_120days_backward')
    df=merge_for_economics(duration2,direction2,df,price_to_rent_ratio,'price_to_rent_ratio_120days_backward')
    
    df=merge_for_economics(duration2,direction2,df,private_debt_to_gdp,'private_debt_to_gdp_120days_backward')
    df=merge_for_economics(duration2,direction2,df,private_sector_credit,'private_sector_credit_120days_backward')
    df=merge_for_economics(duration2,direction2,df,producer_prices,'producer_prices_120days_backward')
    df=merge_for_economics(duration2,direction2,df,producer_prices_change,'producer_prices_change_120days_backward')
    print("data length"+str(len(df)))
      
    df=merge_for_economics(duration2,direction2,df,productivity,'productivity_120days_backward')
    df=merge_for_economics(duration2,direction2,df,remittances,'remittances_120days_backward')
    df=merge_for_economics(duration2,direction2,df,retail_sales_mom,'retail_sales_mom_120days_backward')
    df=merge_for_economics(duration2,direction2,df,retail_sales_yoy,'retail_sales_yoy_120days_backward')
      
    df=merge_for_economics(duration2,direction2,df,retirement_age_men,'retirement_age_men_120days_backward')
    df=merge_for_economics(duration2,direction2,df,retirement_age_women,'retirement_age_women_120days_backward')
    #df=merge_for_economics(duration2,direction2,df,stock_market_indexes,'stock_market_indexes_120days_backward')
    df=merge_for_economics(duration2,direction2,df,interest_rate,'interest_rate_120days_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,terms_of_trade,'terms_of_trade_120days_backward')
    df=merge_for_economics(duration2,direction2,df,terrorism_index,'terrorism_index_120days_backward')
    df=merge_for_economics(duration2,direction2,df,tourism_revenues,'tourism_revenues_120days_backward')
    df=merge_for_economics(duration2,direction2,df,tourist_arrivals,'tourist_arrivals_120days_backward')
      
    df=merge_for_economics(duration2,direction2,df,unemployed_persons,'unemployed_persons_120days_backward')
    df=merge_for_economics(duration2,direction2,df,unemployment_rate,'unemployment_rate_120days_backward')
    df=merge_for_economics(duration2,direction2,df,wage_growth,'wage_growth_120days_backward')
    df=merge_for_economics(duration2,direction2,df,economics_wages,'economics_wages_120days_backward')
      
    df=merge_for_economics(duration2,direction2,df,weapons_sales,'weapons_sales_120days_backward')
    df=merge_for_economics(duration2,direction2,df,wages_in_manufacturing,'wages_in_manufacturing_120days_backward')
    df=merge_for_economics(duration2,direction2,df,youth_unemployment_rate,'youth_unemployment_rate_120days_backward')
    print("data length"+str(len(df)))
      
      
      
    
      
    
    df=merge_for_economics(duration2,direction2,df,food_inflation,'food_inflation_120days_backward')
    df=merge_for_economics(duration2,direction2,df,economics_export_data,'economics_export_data_120days_backward')
    df=merge_for_economics(duration2,direction2,df,balance_of_trade_data,'balance_of_trade_data_120days_backward')
    df=merge_for_economics(duration2,direction2,df,bank_lending_rate_data,'bank_lending_rate_data_120days_backward')
    df=merge_for_economics(duration2,direction2,df,banks_balance_sheet_data,'banks_balance_sheet_data_120days_backward')  
    #df=merge_for_economics(duration2,direction2,df,economics_bonds_data,'economics_bonds_data_120days_backward')
    df=merge_for_economics(duration2,direction2,df,cash_reserve_ratio_data,'cash_reserve_ratio_data_120days_backward')  
    df=merge_for_economics(duration2,direction2,df,building_permit_data,'building_permit_data_120days_backward')  
    df=merge_for_economics(duration2,direction2,df,capital_flows_data,'capital_flows_data_120days_backward')  
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,economics_consumer_confidence_data,'economics_consumer_confidence_data_120days_backward')  
    df=merge_for_economics(duration2,direction2,df,economics_consumer_credit_data,'economics_consumer_credit_data_120days_backward')   
    df=merge_for_economics(duration2,direction2,df,consumer_price_index_cpi_data,'consumer_price_index_cpi_data_120days_backward')   
    df=merge_for_economics(duration2,direction2,df,consumer_spending_data,'consumer_spending_data_120days_backward')   
    df=merge_for_economics(duration2,direction2,df,core_inflation_rate_data,'core_inflation_rate_data_120days_backward')        
    
      
    duration2="1y"
    direction2="nearest"
    df=merge_for_economics(duration,direction1,df,food_inflation,'food_inflation')
    df=merge_for_economics(duration,direction1,df,economics_export_data,'economics_export_data')
    df=merge_for_economics(duration,direction1,df,balance_of_trade_data,'balance_of_trade_data')
    df=merge_for_economics(duration,direction1,df,bank_lending_rate_data,'bank_lending_rate_data')
    df=merge_for_economics(duration,direction1,df,banks_balance_sheet_data,'banks_balance_sheet_data')  
    #df=merge_for_economics(duration,direction1,df,economics_bonds_data,'economics_bonds_data')
    df=merge_for_economics(duration,direction1,df,cash_reserve_ratio_data,'cash_reserve_ratio_data')  
    df=merge_for_economics(duration,direction1,df,building_permit_data,'building_permit_data')  
    df=merge_for_economics(duration,direction1,df,capital_flows_data,'capital_flows_data')  
    print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,economics_consumer_confidence_data,'economics_consumer_confidence_data')  
    df=merge_for_economics(duration,direction1,df,economics_consumer_credit_data,'economics_consumer_credit_data')   
    df=merge_for_economics(duration,direction1,df,consumer_price_index_cpi_data,'consumer_price_index_cpi_data')   
    df=merge_for_economics(duration,direction1,df,consumer_spending_data,'consumer_spending_data')   
    df=merge_for_economics(duration,direction1,df,core_inflation_rate_data,'core_inflation_rate_data')  
    print("data length"+str(len(df)))
    #df=merge_for_economics(duration,direction1,df,economics_currencies_data,'economics_currencies_data')    
      
    df=merge_for_economics(duration2,direction2,df,home_ownership_rate,'home_ownership_rate')
    df=merge_for_economics(duration2,direction2,df,households_debt_to_gdp,'households_debt_to_gdp')
    df=merge_for_economics(duration2,direction2,df,debt_to_income,'debt_to_income')
    df=merge_for_economics(duration2,direction2,df,housing_index,'housing_index')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,housing_starts,'housing_starts')
    df=merge_for_economics(duration2,direction2,df,import_prices,'import_prices')
    df=merge_for_economics(duration2,direction2,df,economics_imports,'economics_imports')
    df=merge_for_economics(duration2,direction2,df,lending_rate,'lending_rate')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,labour_costs,'labour_costs')
    df=merge_for_economics(duration2,direction2,df,inflation_rate,'inflation_rate')
    df=merge_for_economics(duration2,direction2,df,inflation_expectations,'inflation_expectations')
    #df=merge_for_economics(duration2,direction2,df,jobless_claims,'jobless_claims')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,inflation_rate_mom,'inflation_rate_mom')
    df=merge_for_economics(duration2,direction2,df,loans_to_private_sector,'loans_to_private_sector')
    df=merge_for_economics(duration2,direction2,df,loan_growth,'loan_growth')
    df=merge_for_economics(duration2,direction2,df,minimum_wages,'minimum_wages')
      
    df=merge_for_economics(duration2,direction2,df,long_term_unemployment_rate,'long_term_unemployment_rate')
    df=merge_for_economics(duration2,direction2,df,money_supply_m1,'money_supply_m1')
    df=merge_for_economics(duration2,direction2,df,natural_gas_imports,'natural_gas_imports')
    df=merge_for_economics(duration2,direction2,df,economics_money_supply_m3,'economics_money_supply_m3')
    
    df=merge_for_economics(duration2,direction2,df,part_time_employment,'part_time_employment')
    df=merge_for_economics(duration2,direction2,df,personal_savings,'personal_savings')
    df=merge_for_economics(duration2,direction2,df,personal_spending,'personal_spending')
    df=merge_for_economics(duration2,direction2,df,price_to_rent_ratio,'price_to_rent_ratio')
    
    df=merge_for_economics(duration2,direction2,df,private_debt_to_gdp,'private_debt_to_gdp')
    df=merge_for_economics(duration2,direction2,df,private_sector_credit,'private_sector_credit')
    df=merge_for_economics(duration2,direction2,df,producer_prices,'producer_prices')
    df=merge_for_economics(duration2,direction2,df,producer_prices_change,'producer_prices_change')
    print("data length"+str(len(df)))
      
    df=merge_for_economics(duration2,direction2,df,productivity,'productivity')
    df=merge_for_economics(duration2,direction2,df,remittances,'remittances')
    df=merge_for_economics(duration2,direction2,df,retail_sales_mom,'retail_sales_mom')
    df=merge_for_economics(duration2,direction2,df,retail_sales_yoy,'retail_sales_yoy')
      
    df=merge_for_economics(duration2,direction2,df,retirement_age_men,'retirement_age_men')
    df=merge_for_economics(duration2,direction2,df,retirement_age_women,'retirement_age_women')
    #df=merge_for_economics(duration2,direction2,df,stock_market_indexes,'stock_market_indexes')
    df=merge_for_economics(duration2,direction2,df,interest_rate,'interest_rate')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,terms_of_trade,'terms_of_trade')
    df=merge_for_economics(duration2,direction2,df,terrorism_index,'terrorism_index')
    df=merge_for_economics(duration2,direction2,df,tourism_revenues,'tourism_revenues')
    df=merge_for_economics(duration2,direction2,df,tourist_arrivals,'tourist_arrivals')
      
    df=merge_for_economics(duration2,direction2,df,unemployed_persons,'unemployed_persons')
    df=merge_for_economics(duration2,direction2,df,unemployment_rate,'unemployment_rate')
    df=merge_for_economics(duration2,direction2,df,wage_growth,'wage_growth')
    df=merge_for_economics(duration2,direction2,df,economics_wages,'economics_wages')
      
    df=merge_for_economics(duration2,direction2,df,weapons_sales,'weapons_sales')
    df=merge_for_economics(duration2,direction2,df,wages_in_manufacturing,'wages_in_manufacturing')
    df=merge_for_economics(duration2,direction2,df,youth_unemployment_rate,'youth_unemployment_rate')
    print("data length"+str(len(df)))
      
      
      
    
      
    
    df=merge_for_economics(duration2,direction2,df,food_inflation,'food_inflation')
    df=merge_for_economics(duration2,direction2,df,economics_export_data,'economics_export_data')
    df=merge_for_economics(duration2,direction2,df,balance_of_trade_data,'balance_of_trade_data')
    df=merge_for_economics(duration2,direction2,df,bank_lending_rate_data,'bank_lending_rate_data')
    df=merge_for_economics(duration2,direction2,df,banks_balance_sheet_data,'banks_balance_sheet_data')  
    #df=merge_for_economics(duration2,direction2,df,economics_bonds_data,'economics_bonds_data')
    df=merge_for_economics(duration2,direction2,df,cash_reserve_ratio_data,'cash_reserve_ratio_data')  
    df=merge_for_economics(duration2,direction2,df,building_permit_data,'building_permit_data')  
    df=merge_for_economics(duration2,direction2,df,capital_flows_data,'capital_flows_data')  
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,economics_consumer_confidence_data,'economics_consumer_confidence_data')  
    df=merge_for_economics(duration2,direction2,df,economics_consumer_credit_data,'economics_consumer_credit_data')   
    df=merge_for_economics(duration2,direction2,df,consumer_price_index_cpi_data,'consumer_price_index_cpi_data')   
    df=merge_for_economics(duration2,direction2,df,consumer_spending_data,'consumer_spending_data')   
    df=merge_for_economics(duration2,direction2,df,core_inflation_rate_data,'core_inflation_rate_data')  
    print("data length"+str(len(df)))    
  

  
    col.remove("XPCT_DLVRY_DT")
    col.remove("Days_Delayed")
   #if(training_set==True):


    
    numeric_features = [ ] #'Order Entry Date' 'Ordered Value'
    numeric_bin = []
    
    print("Encoding completed")
      
    
    return df































        duration="90d"
    direction1="backward"
    df= merge_for_other_features(df,air_quality_kolkata,"air_quality_kolkata") 
    df = merge_for_other_features(df,trends,"trends")
    df=merge_for_economics(duration,direction1,df,foreign_direct_investment,'foreign_direct_investment__3months_backward')
    #print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,foreign_exchange_reserves,'foreign_exchange_reserves__3months_backward')
    #print("data length"+str(len(df)))
    #df=merge_for_economics(duration,direction1,df,economics_unemployment_rate,'economics_unemployment_rate__3months_backward')
    print("data length"+str(len(df)))
    #df=merge_for_economics(duration,direction1,df,full_time_employment,'full_time_employment__3months_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,economics_gasoline_prices,'economics_gasoline_prices__3months_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,gdp_deflator,'gdp_deflator__3months_backward')
    df=merge_for_economics(duration,direction1,df,debt_to_gdp,'debt_to_gdp__3months_backward')
    #df=merge_for_economics(duration,direction1,df,harmonised_consumer_prices,'harmonised_consumer_prices__3months_backward')
    #print("data length"+str(len(df)))
      
    #df=merge_for_economics(duration,direction1,df,home_ownership_rate,'home_ownership_rate__3months_backward')
    df=merge_for_economics(duration,direction1,df,households_debt_to_gdp,'households_debt_to_gdp__3months_backward')
    #df=merge_for_economics(duration,direction1,df,debt_to_income,'debt_to_income__3months_backward')
    df=merge_for_economics(duration,direction1,df,housing_index,'housing_index__3months_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,housing_starts,'housing_starts__3months_backward')
    df=merge_for_economics(duration,direction1,df,import_prices,'import_prices__3months_backward')
    df=merge_for_economics(duration,direction1,df,economics_imports,'economics_imports__3months_backward')
    df=merge_for_economics(duration,direction1,df,lending_rate,'lending_rate__3months_backward')
    #print("data length"+str(len(df)))
    #df=merge_for_economics(duration,direction1,df,labour_costs,'labour_costs__3months_backward')
    df=merge_for_economics(duration,direction1,df,inflation_rate,'inflation_rate__3months_backward')
    df=merge_for_economics(duration,direction1,df,inflation_expectations,'inflation_expectations__3months_backward')
    #df=merge_for_economics(duration,direction1,df,jobless_claims,'jobless_claims__3months_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,inflation_rate_mom,'inflation_rate_mom__3months_backward')
    #df=merge_for_economics(duration,direction1,df,loans_to_private_sector,'loans_to_private_sector__3months_backward')
    df=merge_for_economics(duration,direction1,df,loan_growth,'loan_growth__3months_backward')
    df=merge_for_economics(duration,direction1,df,minimum_wages,'minimum_wages__3months_backward')
      
    #df=merge_for_economics(duration,direction1,df,long_term_unemployment_rate,'long_term_unemployment_rate__3months_backward')
    #df=merge_for_economics(duration,direction1,df,money_supply_m1,'money_supply_m1__3months_backward')
    #df=merge_for_economics(duration,direction1,df,natural_gas_imports,'natural_gas_imports__3months_backward')
    #df=merge_for_economics(duration,direction1,df,economics_money_supply_m3,'economics_money_supply_m3__3months_backward')
    
    #df=merge_for_economics(duration,direction1,df,part_time_employment,'part_time_employment__3months_backward')
    df=merge_for_economics(duration,direction1,df,personal_savings,'personal_savings__3months_backward')
    df=merge_for_economics(duration,direction1,df,personal_spending,'personal_spending__3months_backward')
    #df=merge_for_economics(duration,direction1,df,price_to_rent_ratio,'price_to_rent_ratio__3months_backward')
    
    df=merge_for_economics(duration,direction1,df,private_debt_to_gdp,'private_debt_to_gdp__3months_backward')
    #df=merge_for_economics(duration,direction1,df,private_sector_credit,'private_sector_credit__3months_backward')
    df=merge_for_economics(duration,direction1,df,producer_prices,'producer_prices__3months_backward')
    df=merge_for_economics(duration,direction1,df,producer_prices_change,'producer_prices_change__3months_backward')
    #print("data length"+str(len(df)))
      
    df=merge_for_economics(duration,direction1,df,productivity,'productivity__3months_backward')
    #df=merge_for_economics(duration,direction1,df,remittances,'remittances__3months_backward')
    df=merge_for_economics(duration,direction1,df,retail_sales_mom,'retail_sales_mom__3months_backward')
    df=merge_for_economics(duration,direction1,df,retail_sales_yoy,'retail_sales_yoy__3months_backward')
      
    #df=merge_for_economics(duration,direction1,df,retirement_age_men,'retirement_age_men__3months_backward')
    #df=merge_for_economics(duration,direction1,df,retirement_age_women,'retirement_age_women__3months_backward')
    #df=merge_for_economics(duration,direction1,df,stock_market_indexes,'stock_market_indexes__3months_backward')
    df=merge_for_economics(duration,direction1,df,interest_rate,'interest_rate__3months_backward')
    #print("data length"+str(len(df)))
    #df=merge_for_economics(duration,direction1,df,terms_of_trade,'terms_of_trade__3months_backward')
    #df=merge_for_economics(duration,direction1,df,terrorism_index,'terrorism_index__3months_backward')
    df=merge_for_economics(duration,direction1,df,tourism_revenues,'tourism_revenues__3months_backward')
    df=merge_for_economics(duration,direction1,df,tourist_arrivals,'tourist_arrivals__3months_backward')
      
    df=merge_for_economics(duration,direction1,df,unemployed_persons,'unemployed_persons__3months_backward')
    df=merge_for_economics(duration,direction1,df,unemployment_rate,'unemployment_rate__3months_backward')
    df=merge_for_economics(duration,direction1,df,wage_growth,'wage_growth__3months_backward')
    df=merge_for_economics(duration,direction1,df,economics_wages,'economics_wages__3months_backward')
      
    #df=merge_for_economics(duration,direction1,df,weapons_sales,'weapons_sales__3months_backward')
    #df=merge_for_economics(duration,direction1,df,wages_in_manufacturing,'wages_in_manufacturing__3months_backward')
    #df=merge_for_economics(duration,direction1,df,youth_unemployment_rate,'youth_unemployment_rate__3months_backward')
    #print("data length"+str(len(df)))
      

    duration="180d"
    direction1="backward"
    df=merge_for_economics(duration,direction1,df,foreign_direct_investment,'foreign_direct_investment__6months_backward')
    #print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,foreign_exchange_reserves,'foreign_exchange_reserves__6months_backward')
    #print("data length"+str(len(df)))
    #df=merge_for_economics(duration,direction1,df,economics_unemployment_rate,'economics_unemployment_rate__6months_backward')
    print("data length"+str(len(df)))
    #df=merge_for_economics(duration,direction1,df,full_time_employment,'full_time_employment__6months_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,economics_gasoline_prices,'economics_gasoline_prices__6months_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,gdp_deflator,'gdp_deflator__6months_backward')
    df=merge_for_economics(duration,direction1,df,debt_to_gdp,'debt_to_gdp__6months_backward')
    #df=merge_for_economics(duration,direction1,df,harmonised_consumer_prices,'harmonised_consumer_prices__6months_backward')
    #print("data length"+str(len(df)))
      
    #df=merge_for_economics(duration,direction1,df,home_ownership_rate,'home_ownership_rate__6months_backward')
    df=merge_for_economics(duration,direction1,df,households_debt_to_gdp,'households_debt_to_gdp__6months_backward')
    #df=merge_for_economics(duration,direction1,df,debt_to_income,'debt_to_income__6months_backward')
    df=merge_for_economics(duration,direction1,df,housing_index,'housing_index__6months_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,housing_starts,'housing_starts__6months_backward')
    df=merge_for_economics(duration,direction1,df,import_prices,'import_prices__6months_backward')
    df=merge_for_economics(duration,direction1,df,economics_imports,'economics_imports__6months_backward')
    df=merge_for_economics(duration,direction1,df,lending_rate,'lending_rate__6months_backward')
    #print("data length"+str(len(df)))
    #df=merge_for_economics(duration,direction1,df,labour_costs,'labour_costs__6months_backward')
    df=merge_for_economics(duration,direction1,df,inflation_rate,'inflation_rate__6months_backward')
    df=merge_for_economics(duration,direction1,df,inflation_expectations,'inflation_expectations__6months_backward')
    #df=merge_for_economics(duration,direction1,df,jobless_claims,'jobless_claims__6months_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,inflation_rate_mom,'inflation_rate_mom__6months_backward')
    #df=merge_for_economics(duration,direction1,df,loans_to_private_sector,'loans_to_private_sector__6months_backward')
    df=merge_for_economics(duration,direction1,df,loan_growth,'loan_growth__6months_backward')
    df=merge_for_economics(duration,direction1,df,minimum_wages,'minimum_wages__6months_backward')
      
    #df=merge_for_economics(duration,direction1,df,long_term_unemployment_rate,'long_term_unemployment_rate__6months_backward')
    #df=merge_for_economics(duration,direction1,df,money_supply_m1,'money_supply_m1__6months_backward')
    #df=merge_for_economics(duration,direction1,df,natural_gas_imports,'natural_gas_imports__6months_backward')
    #df=merge_for_economics(duration,direction1,df,economics_money_supply_m3,'economics_money_supply_m3__6months_backward')
    
    #df=merge_for_economics(duration,direction1,df,part_time_employment,'part_time_employment__6months_backward')
    df=merge_for_economics(duration,direction1,df,personal_savings,'personal_savings__6months_backward')
    df=merge_for_economics(duration,direction1,df,personal_spending,'personal_spending__6months_backward')
    #df=merge_for_economics(duration,direction1,df,price_to_rent_ratio,'price_to_rent_ratio__6months_backward')
    
    df=merge_for_economics(duration,direction1,df,private_debt_to_gdp,'private_debt_to_gdp__6months_backward')
    #df=merge_for_economics(duration,direction1,df,private_sector_credit,'private_sector_credit__6months_backward')
    df=merge_for_economics(duration,direction1,df,producer_prices,'producer_prices__6months_backward')
    df=merge_for_economics(duration,direction1,df,producer_prices_change,'producer_prices_change__6months_backward')
    #print("data length"+str(len(df)))
      
    df=merge_for_economics(duration,direction1,df,productivity,'productivity__6months_backward')
    #df=merge_for_economics(duration,direction1,df,remittances,'remittances__6months_backward')
    df=merge_for_economics(duration,direction1,df,retail_sales_mom,'retail_sales_mom__6months_backward')
    df=merge_for_economics(duration,direction1,df,retail_sales_yoy,'retail_sales_yoy__6months_backward')
      
    #df=merge_for_economics(duration,direction1,df,retirement_age_men,'retirement_age_men__6months_backward')
    #df=merge_for_economics(duration,direction1,df,retirement_age_women,'retirement_age_women__6months_backward')
    #df=merge_for_economics(duration,direction1,df,stock_market_indexes,'stock_market_indexes__6months_backward')
    df=merge_for_economics(duration,direction1,df,interest_rate,'interest_rate__6months_backward')
    #print("data length"+str(len(df)))
    #df=merge_for_economics(duration,direction1,df,terms_of_trade,'terms_of_trade__6months_backward')
    #df=merge_for_economics(duration,direction1,df,terrorism_index,'terrorism_index__6months_backward')
    df=merge_for_economics(duration,direction1,df,tourism_revenues,'tourism_revenues__6months_backward')
    df=merge_for_economics(duration,direction1,df,tourist_arrivals,'tourist_arrivals__6months_backward')
      
    df=merge_for_economics(duration,direction1,df,unemployed_persons,'unemployed_persons__6months_backward')
    df=merge_for_economics(duration,direction1,df,unemployment_rate,'unemployment_rate__6months_backward')
    df=merge_for_economics(duration,direction1,df,wage_growth,'wage_growth__6months_backward')
    df=merge_for_economics(duration,direction1,df,economics_wages,'economics_wages__6months_backward')
      
    #df=merge_for_economics(duration,direction1,df,weapons_sales,'weapons_sales__6months_backward')
    #df=merge_for_economics(duration,direction1,df,wages_in_manufacturing,'wages_in_manufacturing__6months_backward')
    #df=merge_for_economics(duration,direction1,df,youth_unemployment_rate,'youth_unemployment_rate__6months_backward')
    #print("data length"+str(len(df)))



    duration2="270d"
    direction2="backward"
    df=merge_for_economics(duration,direction1,df,food_inflation,'food_inflation__9months_backward')
    df=merge_for_economics(duration,direction1,df,economics_export_data,'economics_export_data__9months_backward')
    df=merge_for_economics(duration,direction1,df,balance_of_trade_data,'balance_of_trade_data__9months_backward')
    df=merge_for_economics(duration,direction1,df,bank_lending_rate_data,'bank_lending_rate_data__9months_backward')
    df=merge_for_economics(duration,direction1,df,banks_balance_sheet_data,'banks_balance_sheet_data__9months_backward')  
    #df=merge_for_economics(duration,direction1,df,economics_bonds_data,'economics_bonds_data__9months_backward')
    df=merge_for_economics(duration,direction1,df,cash_reserve_ratio_data,'cash_reserve_ratio_data__9months_backward')  
    df=merge_for_economics(duration,direction1,df,building_permit_data,'building_permit_data__9months_backward')  
    df=merge_for_economics(duration,direction1,df,capital_flows_data,'capital_flows_data__9months_backward')  
    print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,economics_consumer_confidence_data,'economics_consumer_confidence_data__9months_backward')  
    df=merge_for_economics(duration,direction1,df,economics_consumer_credit_data,'economics_consumer_credit_data__9months_backward')   
    df=merge_for_economics(duration,direction1,df,consumer_price_index_cpi_data,'consumer_price_index_cpi_data__9months_backward')   
    df=merge_for_economics(duration,direction1,df,consumer_spending_data,'consumer_spending_data__9months_backward')   
    df=merge_for_economics(duration,direction1,df,core_inflation_rate_data,'core_inflation_rate_data__9months_backward')  
    print("data length"+str(len(df)))
    #df=merge_for_economics(duration,direction1,df,economics_currencies_data,'economics_currencies_data__9months_backward')    
      
    df=merge_for_economics(duration2,direction2,df,home_ownership_rate,'home_ownership_rate__9months_backward')
    df=merge_for_economics(duration2,direction2,df,households_debt_to_gdp,'households_debt_to_gdp__9months_backward')
    df=merge_for_economics(duration2,direction2,df,debt_to_income,'debt_to_income__9months_backward')
    df=merge_for_economics(duration2,direction2,df,housing_index,'housing_index__9months_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,housing_starts,'housing_starts__9months_backward')
    df=merge_for_economics(duration2,direction2,df,import_prices,'import_prices__9months_backward')
    df=merge_for_economics(duration2,direction2,df,economics_imports,'economics_imports__9months_backward')
    df=merge_for_economics(duration2,direction2,df,lending_rate,'lending_rate__9months_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,labour_costs,'labour_costs__9months_backward')
    df=merge_for_economics(duration2,direction2,df,inflation_rate,'inflation_rate__9months_backward')
    df=merge_for_economics(duration2,direction2,df,inflation_expectations,'inflation_expectations__9months_backward')
    #df=merge_for_economics(duration2,direction2,df,jobless_claims,'jobless_claims__9months_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,inflation_rate_mom,'inflation_rate_mom__9months_backward')
    df=merge_for_economics(duration2,direction2,df,loans_to_private_sector,'loans_to_private_sector__9months_backward')
    df=merge_for_economics(duration2,direction2,df,loan_growth,'loan_growth__9months_backward')
    df=merge_for_economics(duration2,direction2,df,minimum_wages,'minimum_wages__9months_backward')
      
    df=merge_for_economics(duration2,direction2,df,long_term_unemployment_rate,'long_term_unemployment_rate__9months_backward')
    df=merge_for_economics(duration2,direction2,df,money_supply_m1,'money_supply_m1__9months_backward')
    df=merge_for_economics(duration2,direction2,df,natural_gas_imports,'natural_gas_imports__9months_backward')
    df=merge_for_economics(duration2,direction2,df,economics_money_supply_m3,'economics_money_supply_m3__9months_backward')
    
    df=merge_for_economics(duration2,direction2,df,part_time_employment,'part_time_employment__9months_backward')
    df=merge_for_economics(duration2,direction2,df,personal_savings,'personal_savings__9months_backward')
    df=merge_for_economics(duration2,direction2,df,personal_spending,'personal_spending__9months_backward')
    df=merge_for_economics(duration2,direction2,df,price_to_rent_ratio,'price_to_rent_ratio__9months_backward')
    
    df=merge_for_economics(duration2,direction2,df,private_debt_to_gdp,'private_debt_to_gdp__9months_backward')
    df=merge_for_economics(duration2,direction2,df,private_sector_credit,'private_sector_credit__9months_backward')
    df=merge_for_economics(duration2,direction2,df,producer_prices,'producer_prices__9months_backward')
    df=merge_for_economics(duration2,direction2,df,producer_prices_change,'producer_prices_change__9months_backward')
    print("data length"+str(len(df)))
      
    df=merge_for_economics(duration2,direction2,df,productivity,'productivity__9months_backward')
    df=merge_for_economics(duration2,direction2,df,remittances,'remittances__9months_backward')
    df=merge_for_economics(duration2,direction2,df,retail_sales_mom,'retail_sales_mom__9months_backward')
    df=merge_for_economics(duration2,direction2,df,retail_sales_yoy,'retail_sales_yoy__9months_backward')
      
    df=merge_for_economics(duration2,direction2,df,retirement_age_men,'retirement_age_men__9months_backward')
    df=merge_for_economics(duration2,direction2,df,retirement_age_women,'retirement_age_women__9months_backward')
    #df=merge_for_economics(duration2,direction2,df,stock_market_indexes,'stock_market_indexes__9months_backward')
    df=merge_for_economics(duration2,direction2,df,interest_rate,'interest_rate__9months_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,terms_of_trade,'terms_of_trade__9months_backward')
    df=merge_for_economics(duration2,direction2,df,terrorism_index,'terrorism_index__9months_backward')
    df=merge_for_economics(duration2,direction2,df,tourism_revenues,'tourism_revenues__9months_backward')
    df=merge_for_economics(duration2,direction2,df,tourist_arrivals,'tourist_arrivals__9months_backward')
      
    df=merge_for_economics(duration2,direction2,df,unemployed_persons,'unemployed_persons__9months_backward')
    df=merge_for_economics(duration2,direction2,df,unemployment_rate,'unemployment_rate__9months_backward')
    df=merge_for_economics(duration2,direction2,df,wage_growth,'wage_growth__9months_backward')
    df=merge_for_economics(duration2,direction2,df,economics_wages,'economics_wages__9months_backward')
      
    df=merge_for_economics(duration2,direction2,df,weapons_sales,'weapons_sales__9months_backward')
    df=merge_for_economics(duration2,direction2,df,wages_in_manufacturing,'wages_in_manufacturing__9months_backward')
    df=merge_for_economics(duration2,direction2,df,youth_unemployment_rate,'youth_unemployment_rate__9months_backward')
    print("data length"+str(len(df)))
      
      
      
    
      
    
    df=merge_for_economics(duration2,direction2,df,food_inflation,'food_inflation__9months_backward')
    df=merge_for_economics(duration2,direction2,df,economics_export_data,'economics_export_data__9months_backward')
    df=merge_for_economics(duration2,direction2,df,balance_of_trade_data,'balance_of_trade_data__9months_backward')
    df=merge_for_economics(duration2,direction2,df,bank_lending_rate_data,'bank_lending_rate_data__9months_backward')
    df=merge_for_economics(duration2,direction2,df,banks_balance_sheet_data,'banks_balance_sheet_data__9months_backward')  
    #df=merge_for_economics(duration2,direction2,df,economics_bonds_data,'economics_bonds_data__9months_backward')
    df=merge_for_economics(duration2,direction2,df,cash_reserve_ratio_data,'cash_reserve_ratio_data__9months_backward')  
    df=merge_for_economics(duration2,direction2,df,building_permit_data,'building_permit_data__9months_backward')  
    df=merge_for_economics(duration2,direction2,df,capital_flows_data,'capital_flows_data__9months_backward')  
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,economics_consumer_confidence_data,'economics_consumer_confidence_data__9months_backward')  
    df=merge_for_economics(duration2,direction2,df,economics_consumer_credit_data,'economics_consumer_credit_data__9months_backward')   
    df=merge_for_economics(duration2,direction2,df,consumer_price_index_cpi_data,'consumer_price_index_cpi_data__9months_backward')   
    df=merge_for_economics(duration2,direction2,df,consumer_spending_data,'consumer_spending_data__9months_backward')   
    df=merge_for_economics(duration2,direction2,df,core_inflation_rate_data,'core_inflation_rate_data__9months_backward')  

    duration2="365d"
    direction2="backward"
    df=merge_for_economics(duration,direction1,df,food_inflation,'food_inflation__12months_backward')
    df=merge_for_economics(duration,direction1,df,economics_export_data,'economics_export_data__12months_backward')
    df=merge_for_economics(duration,direction1,df,balance_of_trade_data,'balance_of_trade_data__12months_backward')
    df=merge_for_economics(duration,direction1,df,bank_lending_rate_data,'bank_lending_rate_data__12months_backward')
    df=merge_for_economics(duration,direction1,df,banks_balance_sheet_data,'banks_balance_sheet_data__12months_backward')  
    #df=merge_for_economics(duration,direction1,df,economics_bonds_data,'economics_bonds_data__12months_backward')
    df=merge_for_economics(duration,direction1,df,cash_reserve_ratio_data,'cash_reserve_ratio_data__12months_backward')  
    df=merge_for_economics(duration,direction1,df,building_permit_data,'building_permit_data__12months_backward')  
    df=merge_for_economics(duration,direction1,df,capital_flows_data,'capital_flows_data__12months_backward')  
    print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,economics_consumer_confidence_data,'economics_consumer_confidence_data__12months_backward')  
    df=merge_for_economics(duration,direction1,df,economics_consumer_credit_data,'economics_consumer_credit_data__12months_backward')   
    df=merge_for_economics(duration,direction1,df,consumer_price_index_cpi_data,'consumer_price_index_cpi_data__12months_backward')   
    df=merge_for_economics(duration,direction1,df,consumer_spending_data,'consumer_spending_data__12months_backward')   
    df=merge_for_economics(duration,direction1,df,core_inflation_rate_data,'core_inflation_rate_data__12months_backward')  
    print("data length"+str(len(df)))
    #df=merge_for_economics(duration,direction1,df,economics_currencies_data,'economics_currencies_data__12months_backward')    
      
    df=merge_for_economics(duration2,direction2,df,home_ownership_rate,'home_ownership_rate__12months_backward')
    df=merge_for_economics(duration2,direction2,df,households_debt_to_gdp,'households_debt_to_gdp__12months_backward')
    df=merge_for_economics(duration2,direction2,df,debt_to_income,'debt_to_income__12months_backward')
    df=merge_for_economics(duration2,direction2,df,housing_index,'housing_index__12months_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,housing_starts,'housing_starts__12months_backward')
    df=merge_for_economics(duration2,direction2,df,import_prices,'import_prices__12months_backward')
    df=merge_for_economics(duration2,direction2,df,economics_imports,'economics_imports__12months_backward')
    df=merge_for_economics(duration2,direction2,df,lending_rate,'lending_rate__12months_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,labour_costs,'labour_costs__12months_backward')
    df=merge_for_economics(duration2,direction2,df,inflation_rate,'inflation_rate__12months_backward')
    df=merge_for_economics(duration2,direction2,df,inflation_expectations,'inflation_expectations__12months_backward')
    #df=merge_for_economics(duration2,direction2,df,jobless_claims,'jobless_claims__12months_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,inflation_rate_mom,'inflation_rate_mom__12months_backward')
    df=merge_for_economics(duration2,direction2,df,loans_to_private_sector,'loans_to_private_sector__12months_backward')
    df=merge_for_economics(duration2,direction2,df,loan_growth,'loan_growth__12months_backward')
    df=merge_for_economics(duration2,direction2,df,minimum_wages,'minimum_wages__12months_backward')
      
    df=merge_for_economics(duration2,direction2,df,long_term_unemployment_rate,'long_term_unemployment_rate__12months_backward')
    df=merge_for_economics(duration2,direction2,df,money_supply_m1,'money_supply_m1__12months_backward')
    df=merge_for_economics(duration2,direction2,df,natural_gas_imports,'natural_gas_imports__12months_backward')
    df=merge_for_economics(duration2,direction2,df,economics_money_supply_m3,'economics_money_supply_m3__12months_backward')
    
    df=merge_for_economics(duration2,direction2,df,part_time_employment,'part_time_employment__12months_backward')
    df=merge_for_economics(duration2,direction2,df,personal_savings,'personal_savings__12months_backward')
    df=merge_for_economics(duration2,direction2,df,personal_spending,'personal_spending__12months_backward')
    df=merge_for_economics(duration2,direction2,df,price_to_rent_ratio,'price_to_rent_ratio__12months_backward')
    
    df=merge_for_economics(duration2,direction2,df,private_debt_to_gdp,'private_debt_to_gdp__12months_backward')
    df=merge_for_economics(duration2,direction2,df,private_sector_credit,'private_sector_credit__12months_backward')
    df=merge_for_economics(duration2,direction2,df,producer_prices,'producer_prices__12months_backward')
    df=merge_for_economics(duration2,direction2,df,producer_prices_change,'producer_prices_change__12months_backward')
    print("data length"+str(len(df)))
      
    df=merge_for_economics(duration2,direction2,df,productivity,'productivity__12months_backward')
    df=merge_for_economics(duration2,direction2,df,remittances,'remittances__12months_backward')
    df=merge_for_economics(duration2,direction2,df,retail_sales_mom,'retail_sales_mom__12months_backward')
    df=merge_for_economics(duration2,direction2,df,retail_sales_yoy,'retail_sales_yoy__12months_backward')
      
    df=merge_for_economics(duration2,direction2,df,retirement_age_men,'retirement_age_men__12months_backward')
    df=merge_for_economics(duration2,direction2,df,retirement_age_women,'retirement_age_women__12months_backward')
    #df=merge_for_economics(duration2,direction2,df,stock_market_indexes,'stock_market_indexes__12months_backward')
    df=merge_for_economics(duration2,direction2,df,interest_rate,'interest_rate__12months_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,terms_of_trade,'terms_of_trade__12months_backward')
    df=merge_for_economics(duration2,direction2,df,terrorism_index,'terrorism_index__12months_backward')
    df=merge_for_economics(duration2,direction2,df,tourism_revenues,'tourism_revenues__12months_backward')
    df=merge_for_economics(duration2,direction2,df,tourist_arrivals,'tourist_arrivals__12months_backward')
      
    df=merge_for_economics(duration2,direction2,df,unemployed_persons,'unemployed_persons__12months_backward')
    df=merge_for_economics(duration2,direction2,df,unemployment_rate,'unemployment_rate__12months_backward')
    df=merge_for_economics(duration2,direction2,df,wage_growth,'wage_growth__12months_backward')
    df=merge_for_economics(duration2,direction2,df,economics_wages,'economics_wages__12months_backward')
      
    df=merge_for_economics(duration2,direction2,df,weapons_sales,'weapons_sales__12months_backward')
    df=merge_for_economics(duration2,direction2,df,wages_in_manufacturing,'wages_in_manufacturing__12months_backward')
    df=merge_for_economics(duration2,direction2,df,youth_unemployment_rate,'youth_unemployment_rate__12months_backward')
    print("data length"+str(len(df)))
      
      
      
    
      
    
    df=merge_for_economics(duration2,direction2,df,food_inflation,'food_inflation__12months_backward')
    df=merge_for_economics(duration2,direction2,df,economics_export_data,'economics_export_data__12months_backward')
    df=merge_for_economics(duration2,direction2,df,balance_of_trade_data,'balance_of_trade_data__12months_backward')
    df=merge_for_economics(duration2,direction2,df,bank_lending_rate_data,'bank_lending_rate_data__12months_backward')
    df=merge_for_economics(duration2,direction2,df,banks_balance_sheet_data,'banks_balance_sheet_data__12months_backward')  
    #df=merge_for_economics(duration2,direction2,df,economics_bonds_data,'economics_bonds_data__12months_backward')
    df=merge_for_economics(duration2,direction2,df,cash_reserve_ratio_data,'cash_reserve_ratio_data__12months_backward')  
    df=merge_for_economics(duration2,direction2,df,building_permit_data,'building_permit_data__12months_backward')  
    df=merge_for_economics(duration2,direction2,df,capital_flows_data,'capital_flows_data__12months_backward')  
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,economics_consumer_confidence_data,'economics_consumer_confidence_data__12months_backward')  
    df=merge_for_economics(duration2,direction2,df,economics_consumer_credit_data,'economics_consumer_credit_data__12months_backward')   
    df=merge_for_economics(duration2,direction2,df,consumer_price_index_cpi_data,'consumer_price_index_cpi_data__12months_backward')   
    df=merge_for_economics(duration2,direction2,df,consumer_spending_data,'consumer_spending_data__12months_backward')   
    df=merge_for_economics(duration2,direction2,df,core_inflation_rate_data,'core_inflation_rate_data__12months_backward')    

    
  
    
      
    duration2="1y"
    direction2="nearest"
    df=merge_for_economics(duration,direction1,df,food_inflation,'food_inflation')
    df=merge_for_economics(duration,direction1,df,economics_export_data,'economics_export_data')
    df=merge_for_economics(duration,direction1,df,balance_of_trade_data,'balance_of_trade_data')
    df=merge_for_economics(duration,direction1,df,bank_lending_rate_data,'bank_lending_rate_data')
    df=merge_for_economics(duration,direction1,df,banks_balance_sheet_data,'banks_balance_sheet_data')  
    #df=merge_for_economics(duration,direction1,df,economics_bonds_data,'economics_bonds_data')
    df=merge_for_economics(duration,direction1,df,cash_reserve_ratio_data,'cash_reserve_ratio_data')  
    df=merge_for_economics(duration,direction1,df,building_permit_data,'building_permit_data')  
    df=merge_for_economics(duration,direction1,df,capital_flows_data,'capital_flows_data')  
    print("data length"+str(len(df)))
    df=merge_for_economics(duration,direction1,df,economics_consumer_confidence_data,'economics_consumer_confidence_data')  
    df=merge_for_economics(duration,direction1,df,economics_consumer_credit_data,'economics_consumer_credit_data')   
    df=merge_for_economics(duration,direction1,df,consumer_price_index_cpi_data,'consumer_price_index_cpi_data')   
    df=merge_for_economics(duration,direction1,df,consumer_spending_data,'consumer_spending_data')   
    df=merge_for_economics(duration,direction1,df,core_inflation_rate_data,'core_inflation_rate_data')  
    print("data length"+str(len(df)))
    #df=merge_for_economics(duration,direction1,df,economics_currencies_data,'economics_currencies_data')    
      
    df=merge_for_economics(duration2,direction2,df,home_ownership_rate,'home_ownership_rate')
    df=merge_for_economics(duration2,direction2,df,households_debt_to_gdp,'households_debt_to_gdp')
    df=merge_for_economics(duration2,direction2,df,debt_to_income,'debt_to_income')
    df=merge_for_economics(duration2,direction2,df,housing_index,'housing_index')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,housing_starts,'housing_starts')
    df=merge_for_economics(duration2,direction2,df,import_prices,'import_prices')
    df=merge_for_economics(duration2,direction2,df,economics_imports,'economics_imports')
    df=merge_for_economics(duration2,direction2,df,lending_rate,'lending_rate')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,labour_costs,'labour_costs')
    df=merge_for_economics(duration2,direction2,df,inflation_rate,'inflation_rate')
    df=merge_for_economics(duration2,direction2,df,inflation_expectations,'inflation_expectations')
    #df=merge_for_economics(duration2,direction2,df,jobless_claims,'jobless_claims')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,inflation_rate_mom,'inflation_rate_mom')
    df=merge_for_economics(duration2,direction2,df,loans_to_private_sector,'loans_to_private_sector')
    df=merge_for_economics(duration2,direction2,df,loan_growth,'loan_growth')
    df=merge_for_economics(duration2,direction2,df,minimum_wages,'minimum_wages')
      
    df=merge_for_economics(duration2,direction2,df,long_term_unemployment_rate,'long_term_unemployment_rate')
    df=merge_for_economics(duration2,direction2,df,money_supply_m1,'money_supply_m1')
    df=merge_for_economics(duration2,direction2,df,natural_gas_imports,'natural_gas_imports')
    df=merge_for_economics(duration2,direction2,df,economics_money_supply_m3,'economics_money_supply_m3')
    
    df=merge_for_economics(duration2,direction2,df,part_time_employment,'part_time_employment')
    df=merge_for_economics(duration2,direction2,df,personal_savings,'personal_savings')
    df=merge_for_economics(duration2,direction2,df,personal_spending,'personal_spending')
    df=merge_for_economics(duration2,direction2,df,price_to_rent_ratio,'price_to_rent_ratio')
    
    df=merge_for_economics(duration2,direction2,df,private_debt_to_gdp,'private_debt_to_gdp')
    df=merge_for_economics(duration2,direction2,df,private_sector_credit,'private_sector_credit')
    df=merge_for_economics(duration2,direction2,df,producer_prices,'producer_prices')
    df=merge_for_economics(duration2,direction2,df,producer_prices_change,'producer_prices_change')
    print("data length"+str(len(df)))
      
    df=merge_for_economics(duration2,direction2,df,productivity,'productivity')
    df=merge_for_economics(duration2,direction2,df,remittances,'remittances')
    df=merge_for_economics(duration2,direction2,df,retail_sales_mom,'retail_sales_mom')
    df=merge_for_economics(duration2,direction2,df,retail_sales_yoy,'retail_sales_yoy')
      
    df=merge_for_economics(duration2,direction2,df,retirement_age_men,'retirement_age_men')
    df=merge_for_economics(duration2,direction2,df,retirement_age_women,'retirement_age_women')
    #df=merge_for_economics(duration2,direction2,df,stock_market_indexes,'stock_market_indexes')
    df=merge_for_economics(duration2,direction2,df,interest_rate,'interest_rate')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,terms_of_trade,'terms_of_trade')
    df=merge_for_economics(duration2,direction2,df,terrorism_index,'terrorism_index')
    df=merge_for_economics(duration2,direction2,df,tourism_revenues,'tourism_revenues')
    df=merge_for_economics(duration2,direction2,df,tourist_arrivals,'tourist_arrivals')
      
    df=merge_for_economics(duration2,direction2,df,unemployed_persons,'unemployed_persons')
    df=merge_for_economics(duration2,direction2,df,unemployment_rate,'unemployment_rate')
    df=merge_for_economics(duration2,direction2,df,wage_growth,'wage_growth')
    df=merge_for_economics(duration2,direction2,df,economics_wages,'economics_wages')
      
    df=merge_for_economics(duration2,direction2,df,weapons_sales,'weapons_sales')
    df=merge_for_economics(duration2,direction2,df,wages_in_manufacturing,'wages_in_manufacturing')
    df=merge_for_economics(duration2,direction2,df,youth_unemployment_rate,'youth_unemployment_rate')
    print("data length"+str(len(df)))
      
      
      
    
      
    
    df=merge_for_economics(duration2,direction2,df,food_inflation,'food_inflation')
    df=merge_for_economics(duration2,direction2,df,economics_export_data,'economics_export_data')
    df=merge_for_economics(duration2,direction2,df,balance_of_trade_data,'balance_of_trade_data')
    df=merge_for_economics(duration2,direction2,df,bank_lending_rate_data,'bank_lending_rate_data')
    df=merge_for_economics(duration2,direction2,df,banks_balance_sheet_data,'banks_balance_sheet_data')  
    #df=merge_for_economics(duration2,direction2,df,economics_bonds_data,'economics_bonds_data')
    df=merge_for_economics(duration2,direction2,df,cash_reserve_ratio_data,'cash_reserve_ratio_data')  
    df=merge_for_economics(duration2,direction2,df,building_permit_data,'building_permit_data')  
    df=merge_for_economics(duration2,direction2,df,capital_flows_data,'capital_flows_data')  
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,economics_consumer_confidence_data,'economics_consumer_confidence_data')  
    df=merge_for_economics(duration2,direction2,df,economics_consumer_credit_data,'economics_consumer_credit_data')   
    df=merge_for_economics(duration2,direction2,df,consumer_price_index_cpi_data,'consumer_price_index_cpi_data')   
    df=merge_for_economics(duration2,direction2,df,consumer_spending_data,'consumer_spending_data')   
    df=merge_for_economics(duration2,direction2,df,core_inflation_rate_data,'core_inflation_rate_data')  
    print("data length"+str(len(df)))    
  

  
    col.remove("XPCT_DLVRY_DT")
    col.remove("Days_Delayed")
   #if(training_set==True):


    
    numeric_features = [ ] #'Order Entry Date' 'Ordered Value'
    numeric_bin = []
    
    print("Encoding completed")
      
    
    return df