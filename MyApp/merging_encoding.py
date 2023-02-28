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
    duration2="90d"
    direction2="backward"
    df= merge_for_other_features(df,air_quality_kolkata,"air_quality_kolkata") 
    df = merge_for_other_features(df,trends,"trends")
    df=merge_for_economics(duration2,direction2,df,foreign_direct_investment,'foreign_direct_investment__3months_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,foreign_exchange_reserves,'foreign_exchange_reserves__3months_backward')
    #print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,economics_unemployment_rate,'economics_unemployment_rate__3months_backward')
    print("data length"+str(len(df)))
    #df=merge_for_economics(duration2,direction2,df,full_time_employment,'full_time_employment__3months_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,economics_gasoline_prices,'economics_gasoline_prices__3months_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,gdp_deflator,'gdp_deflator__3months_backward')
    df=merge_for_economics(duration2,direction2,df,debt_to_gdp,'debt_to_gdp__3months_backward')

    df=merge_for_economics(duration2,direction2,df,food_inflation,'food_inflation_3months_backward')
    df=merge_for_economics(duration2,direction2,df,economics_export_data,'economics_export_data_3months_backward')
    df=merge_for_economics(duration2,direction2,df,balance_of_trade_data,'balance_of_trade_data_3months_backward')
    df=merge_for_economics(duration2,direction2,df,bank_lending_rate_data,'bank_lending_rate_data_3months_backward')
    #=merge_for_economics(duration2,direction2,df,banks_balance_sheet_data,'banks_balance_sheet_data_3months_backward')  
    #df=merge_for_economics(duration2,direction2,df,economics_bonds_data,'economics_bonds_data_3months_backward')
    df=merge_for_economics(duration2,direction2,df,cash_reserve_ratio_data,'cash_reserve_ratio_data_3months_backward')  
    #df=merge_for_economics(duration2,direction2,df,building_permit_data,'building_permit_data_3months_backward')  
    df=merge_for_economics(duration2,direction2,df,capital_flows_data,'capital_flows_data_3months_backward')  
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,economics_consumer_confidence_data,'economics_consumer_confidence_data_3months_backward')  
    #df=merge_for_economics(duration2,direction2,df,economics_consumer_credit_data,'economics_consumer_credit_data_3months_backward')   
    df=merge_for_economics(duration2,direction2,df,consumer_price_index_cpi_data,'consumer_price_index_cpi_data_3months_backward')   
   # df=merge_for_economics(duration2,direction2,df,consumer_spending_data,'consumer_spending_data_3months_backward')   
    df=merge_for_economics(duration2,direction2,df,core_inflation_rate_data,'core_inflation_rate_data_3months_backward')  
    print("data length"+str(len(df)))



    #df=merge_for_economics(duration2,direction2,df,harmonised_consumer_prices,'harmonised_consumer_prices__3months_backward')
    #print("data length"+str(len(df)))
      
    #df=merge_for_economics(duration2,direction2,df,home_ownership_rate,'home_ownership_rate__3months_backward')
    df=merge_for_economics(duration2,direction2,df,households_debt_to_gdp,'households_debt_to_gdp__3months_backward')
    #df=merge_for_economics(duration2,direction2,df,debt_to_income,'debt_to_income__3months_backward')
    df=merge_for_economics(duration2,direction2,df,housing_index,'housing_index__3months_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,housing_starts,'housing_starts__3months_backward')
    df=merge_for_economics(duration2,direction2,df,import_prices,'import_prices__3months_backward')
    df=merge_for_economics(duration2,direction2,df,economics_imports,'economics_imports__3months_backward')
    df=merge_for_economics(duration2,direction2,df,lending_rate,'lending_rate__3months_backward')
    #print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,labour_costs,'labour_costs__3months_backward')
    df=merge_for_economics(duration2,direction2,df,inflation_rate,'inflation_rate__3months_backward')
    df=merge_for_economics(duration2,direction2,df,inflation_expectations,'inflation_expectations__3months_backward')
    #df=merge_for_economics(duration2,direction2,df,jobless_claims,'jobless_claims__3months_backward')
    print("data length"+str(len(df)))
    df=merge_for_economics(duration2,direction2,df,inflation_rate_mom,'inflation_rate_mom__3months_backward')
    #df=merge_for_economics(duration2,direction2,df,loans_to_private_sector,'loans_to_private_sector__3months_backward')
    df=merge_for_economics(duration2,direction2,df,loan_growth,'loan_growth__3months_backward')
    #df=merge_for_economics(duration2,direction2,df,minimum_wages,'minimum_wages__3months_backward')
      
    # df=merge_for_economics(duration2,direction2,df,long_term_unemployment_rate,'long_term_unemployment_rate__3months_backward')
    # df=merge_for_economics(duration2,direction2,df,money_supply_m1,'money_supply_m1__3months_backward')
    # df=merge_for_economics(duration2,direction2,df,natural_gas_imports,'natural_gas_imports__3months_backward')
    # df=merge_for_economics(duration2,direction2,df,economics_money_supply_m3,'economics_money_supply_m3__3months_backward')
    
    #df=merge_for_economics(duration2,direction2,df,part_time_employment,'part_time_employment__3months_backward')
    #df=merge_for_economics(duration2,direction2,df,personal_savings,'personal_savings__3months_backward')
    df=merge_for_economics(duration2,direction2,df,personal_spending,'personal_spending__3months_backward')
    df=merge_for_economics(duration2,direction2,df,price_to_rent_ratio,'price_to_rent_ratio__3months_backward')
    
    df=merge_for_economics(duration2,direction2,df,private_debt_to_gdp,'private_debt_to_gdp__3months_backward')
    #df=merge_for_economics(duration2,direction2,df,private_sector_credit,'private_sector_credit__3months_backward')
    df=merge_for_economics(duration2,direction2,df,producer_prices,'producer_prices__3months_backward')
    df=merge_for_economics(duration2,direction2,df,producer_prices_change,'producer_prices_change__3months_backward')
    #print("data length"+str(len(df)))
      
    df=merge_for_economics(duration2,direction2,df,productivity,'productivity__3months_backward')
    #df=merge_for_economics(duration2,direction2,df,remittances,'remittances__3months_backward')
    #df=merge_for_economics(duration2,direction2,df,retail_sales_mom,'retail_sales_mom__3months_backward')
    #df=merge_for_economics(duration2,direction2,df,retail_sales_yoy,'retail_sales_yoy__3months_backward')
      
    #df=merge_for_economics(duration2,direction2,df,retirement_age_men,'retirement_age_men__3months_backward')
    #df=merge_for_economics(duration2,direction2,df,retirement_age_women,'retirement_age_women__3months_backward')
    #df=merge_for_economics(duration2,direction2,df,stock_market_indexes,'stock_market_indexes__3months_backward')
    df=merge_for_economics(duration2,direction2,df,interest_rate,'interest_rate__3months_backward')
    #print("data length"+str(len(df)))
    #df=merge_for_economics(duration2,direction2,df,terms_of_trade,'terms_of_trade__3months_backward')
    #df=merge_for_economics(duration2,direction2,df,terrorism_index,'terrorism_index__3months_backward')
    #df=merge_for_economics(duration2,direction2,df,tourism_revenues,'tourism_revenues__3months_backward')
    #df=merge_for_economics(duration2,direction2,df,tourist_arrivals,'tourist_arrivals__3months_backward')
      
    #df=merge_for_economics(duration2,direction2,df,unemployed_persons,'unemployed_persons__3months_backward')
    #df=merge_for_economics(duration2,direction2,df,unemployment_rate,'unemployment_rate__3months_backward')
    df=merge_for_economics(duration2,direction2,df,wage_growth,'wage_growth__3months_backward')
    df=merge_for_economics(duration2,direction2,df,economics_wages,'economics_wages__3months_backward')
      
    #df=merge_for_economics(duration2,direction2,df,weapons_sales,'weapons_sales__3months_backward')
   # df=merge_for_economics(duration2,direction2,df,wages_in_manufacturing,'wages_in_manufacturing__3months_backward')
    #df=merge_for_economics(duration2,direction2,df,youth_unemployment_rate,'youth_unemployment_rate__3months_backward')
    #print("data length"+str(len(df)))
      


    duration2="120d"
    direction2="backward"

    df=merge_for_economics(duration2,direction2,df,foreign_direct_investment,'foreign_direct_investment__4months_backward')
    print("data length"+str(len(df)))
  #   df=merge_for_economics(duration2,direction2,df,foreign_exchange_reserves,'foreign_exchange_reserves__4months_backward')
  #   #print("data length"+str(len(df)))
  #   df=merge_for_economics(duration2,direction2,df,economics_unemployment_rate,'economics_unemployment_rate__4months_backward')
  #   print("data length"+str(len(df)))
  #   #df=merge_for_economics(duration2,direction2,df,full_time_employment,'full_time_employment__4months_backward')
  #   print("data length"+str(len(df)))
  #   df=merge_for_economics(duration2,direction2,df,economics_gasoline_prices,'economics_gasoline_prices__4months_backward')
  #   print("data length"+str(len(df)))
  #   df=merge_for_economics(duration2,direction2,df,gdp_deflator,'gdp_deflator__4months_backward')
  #   df=merge_for_economics(duration2,direction2,df,debt_to_gdp,'debt_to_gdp__4months_backward')
  #   df=merge_for_economics(duration2,direction2,df,food_inflation,'food_inflation_4months_backward')
  #   df=merge_for_economics(duration2,direction2,df,economics_export_data,'economics_export_data_4months_backward')
  #   df=merge_for_economics(duration2,direction2,df,balance_of_trade_data,'balance_of_trade_data_4months_backward')
  #   df=merge_for_economics(duration2,direction2,df,bank_lending_rate_data,'bank_lending_rate_data_4months_backward')
  #   #=merge_for_economics(duration2,direction2,df,banks_balance_sheet_data,'banks_balance_sheet_data_4months_backward')  
  #   #df=merge_for_economics(duration2,direction2,df,economics_bonds_data,'economics_bonds_data_4months_backward')
  #   df=merge_for_economics(duration2,direction2,df,cash_reserve_ratio_data,'cash_reserve_ratio_data_4months_backward')  
  #   #df=merge_for_economics(duration2,direction2,df,building_permit_data,'building_permit_data_4months_backward')  
  #   df=merge_for_economics(duration2,direction2,df,capital_flows_data,'capital_flows_data_4months_backward')  
  #   print("data length"+str(len(df)))
  #   df=merge_for_economics(duration2,direction2,df,economics_consumer_confidence_data,'economics_consumer_confidence_data_4months_backward')  
  #   #df=merge_for_economics(duration2,direction2,df,economics_consumer_credit_data,'economics_consumer_credit_data_4months_backward')   
  #   df=merge_for_economics(duration2,direction2,df,consumer_price_index_cpi_data,'consumer_price_index_cpi_data_4months_backward')   
  #   #df=merge_for_economics(duration2,direction2,df,consumer_spending_data,'consumer_spending_data_4months_backward')   
  #   df=merge_for_economics(duration2,direction2,df,core_inflation_rate_data,'core_inflation_rate_data_4months_backward')  
  #   print("data length"+str(len(df)))
  #   #df=merge_for_economics(duration2,direction2,df,economics_currencies_data,'economics_currencies_data_4months_backward')    
       
  #   #df=merge_for_economics(duration2,direction2,df,home_ownership_rate,'home_ownership_rate_4months_backward')
  #   df=merge_for_economics(duration2,direction2,df,households_debt_to_gdp,'households_debt_to_gdp_4months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,debt_to_income,'debt_to_income_4months_backward')
  #   df=merge_for_economics(duration2,direction2,df,housing_index,'housing_index_4months_backward')
  #   print("data length"+str(len(df)))
  #   df=merge_for_economics(duration2,direction2,df,housing_starts,'housing_starts_4months_backward')
  #   df=merge_for_economics(duration2,direction2,df,import_prices,'import_prices_4months_backward')
  #   df=merge_for_economics(duration2,direction2,df,economics_imports,'economics_imports_4months_backward')
  #   df=merge_for_economics(duration2,direction2,df,lending_rate,'lending_rate_4months_backward')
  #   print("data length"+str(len(df)))
  #   df=merge_for_economics(duration2,direction2,df,labour_costs,'labour_costs_4months_backward')
  #   df=merge_for_economics(duration2,direction2,df,inflation_rate,'inflation_rate_4months_backward')
  #   df=merge_for_economics(duration2,direction2,df,inflation_expectations,'inflation_expectations_4months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,jobless_claims,'jobless_claims_4months_backward')
  #   print("data length"+str(len(df)))
  #   df=merge_for_economics(duration2,direction2,df,inflation_rate_mom,'inflation_rate_mom_4months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,loans_to_private_sector,'loans_to_private_sector_4months_backward')
  #   df=merge_for_economics(duration2,direction2,df,loan_growth,'loan_growth_4months_backward')
  #  # df=merge_for_economics(duration2,direction2,df,minimum_wages,'minimum_wages_4months_backward')
      
  #   # df=merge_for_economics(duration2,direction2,df,long_term_unemployment_rate,'long_term_unemployment_rate_4months_backward')
  #   # df=merge_for_economics(duration2,direction2,df,money_supply_m1,'money_supply_m1_4months_backward')
  #   # df=merge_for_economics(duration2,direction2,df,natural_gas_imports,'natural_gas_imports_4months_backward')
  #   # df=merge_for_economics(duration2,direction2,df,economics_money_supply_m3,'economics_money_supply_m3_4months_backward')
    
  #   #df=merge_for_economics(duration2,direction2,df,part_time_employment,'part_time_employment_4months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,personal_savings,'personal_savings_4months_backward')
  #   df=merge_for_economics(duration2,direction2,df,personal_spending,'personal_spending_4months_backward')
  #   df=merge_for_economics(duration2,direction2,df,price_to_rent_ratio,'price_to_rent_ratio_4months_backward')
    
  #   df=merge_for_economics(duration2,direction2,df,private_debt_to_gdp,'private_debt_to_gdp_4months_backward')
  #   df=merge_for_economics(duration2,direction2,df,private_sector_credit,'private_sector_credit_4months_backward')
  #   df=merge_for_economics(duration2,direction2,df,producer_prices,'producer_prices_4months_backward')
  #   df=merge_for_economics(duration2,direction2,df,producer_prices_change,'producer_prices_change_4months_backward')
  #   print("data length"+str(len(df)))
      
  #   df=merge_for_economics(duration2,direction2,df,productivity,'productivity_4months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,remittances,'remittances_4months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,retail_sales_mom,'retail_sales_mom_4months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,retail_sales_yoy,'retail_sales_yoy_4months_backward')
      
  #   #df=merge_for_economics(duration2,direction2,df,retirement_age_men,'retirement_age_men_4months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,retirement_age_women,'retirement_age_women_4months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,stock_market_indexes,'stock_market_indexes_4months_backward')
  #   df=merge_for_economics(duration2,direction2,df,interest_rate,'interest_rate_4months_backward')
  #   print("data length"+str(len(df)))
  #   #df=merge_for_economics(duration2,direction2,df,terms_of_trade,'terms_of_trade_4months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,terrorism_index,'terrorism_index_4months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,tourism_revenues,'tourism_revenues_4months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,tourist_arrivals,'tourist_arrivals_4months_backward')
      
  #   #df=merge_for_economics(duration2,direction2,df,unemployed_persons,'unemployed_persons_4months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,unemployment_rate,'unemployment_rate_4months_backward')
  #   df=merge_for_economics(duration2,direction2,df,wage_growth,'wage_growth_4months_backward')
  #   df=merge_for_economics(duration2,direction2,df,economics_wages,'economics_wages_4months_backward')
      
  #   #df=merge_for_economics(duration2,direction2,df,weapons_sales,'weapons_sales_4months_backward')
  #  # df=merge_for_economics(duration2,direction2,df,wages_in_manufacturing,'wages_in_manufacturing_4months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,youth_unemployment_rate,'youth_unemployment_rate_4months_backward')
  #   print("data length"+str(len(df)))
      
      
      
    
      
    
  #   # df=merge_for_economics(duration2,direction2,df,food_inflation,'food_inflation_4months_backward')
  #   # df=merge_for_economics(duration2,direction2,df,economics_export_data,'economics_export_data_4months_backward')
  #   # df=merge_for_economics(duration2,direction2,df,balance_of_trade_data,'balance_of_trade_data_4months_backward')
  #   # df=merge_for_economics(duration2,direction2,df,bank_lending_rate_data,'bank_lending_rate_data_4months_backward')
  #   # #df=merge_for_economics(duration2,direction2,df,banks_balance_sheet_data,'banks_balance_sheet_data_4months_backward')  
  #   # #df=merge_for_economics(duration2,direction2,df,economics_bonds_data,'economics_bonds_data_4months_backward')
  #   # df=merge_for_economics(duration2,direction2,df,cash_reserve_ratio_data,'cash_reserve_ratio_data_4months_backward')  
  #   # df=merge_for_economics(duration2,direction2,df,building_permit_data,'building_permit_data_4months_backward')  
  #   # df=merge_for_economics(duration2,direction2,df,capital_flows_data,'capital_flows_data_4months_backward')  
  #   # print("data length"+str(len(df)))
  #   # #df=merge_for_economics(duration2,direction2,df,economics_consumer_confidence_data,'economics_consumer_confidence_data_4months_backward')  
  #   # #df=merge_for_economics(duration2,direction2,df,economics_consumer_credit_data,'economics_consumer_credit_data_4months_backward')   
  #   # df=merge_for_economics(duration2,direction2,df,consumer_price_index_cpi_data,'consumer_price_index_cpi_data_4months_backward')   
  #   # df=merge_for_economics(duration2,direction2,df,consumer_spending_data,'consumer_spending_data_4months_backward')   
  #   # df=merge_for_economics(duration2,direction2,df,core_inflation_rate_data,'core_inflation_rate_data_4months_backward')  

  #   print("extracting 150")
  #   duration2="150d"
  #   direction2="backward"
  #   df=merge_for_economics(duration2,direction2,df,foreign_direct_investment,'foreign_direct_investment__5months_backward')
  #   print("data length"+str(len(df)))
  #   df=merge_for_economics(duration2,direction2,df,foreign_exchange_reserves,'foreign_exchange_reserves__5months_backward')
  #   #print("data length"+str(len(df)))
  #   df=merge_for_economics(duration2,direction2,df,economics_unemployment_rate,'economics_unemployment_rate__5months_backward')
  #   print("data length"+str(len(df)))
  #   #df=merge_for_economics(duration2,direction2,df,full_time_employment,'full_time_employment__5months_backward')
  #   print("data length"+str(len(df)))
  #   df=merge_for_economics(duration2,direction2,df,economics_gasoline_prices,'economics_gasoline_prices__5months_backward')
  #   print("data length"+str(len(df)))
  #   df=merge_for_economics(duration2,direction2,df,gdp_deflator,'gdp_deflator__5months_backward')
  #   df=merge_for_economics(duration2,direction2,df,debt_to_gdp,'debt_to_gdp__5months_backward')
  #   df=merge_for_economics(duration2,direction2,df,food_inflation,'food_inflation_5months_backward')
  #   df=merge_for_economics(duration2,direction2,df,economics_export_data,'economics_export_data_5months_backward')
  #   df=merge_for_economics(duration2,direction2,df,balance_of_trade_data,'balance_of_trade_data_5months_backward')
  #   df=merge_for_economics(duration2,direction2,df,bank_lending_rate_data,'bank_lending_rate_data_5months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,banks_balance_sheet_data,'banks_balance_sheet_data_5months_backward')  
  #   #df=merge_for_economics(duration2,direction2,df,economics_bonds_data,'economics_bonds_data_5months_backward')
  #   df=merge_for_economics(duration2,direction2,df,cash_reserve_ratio_data,'cash_reserve_ratio_data_5months_backward')  
  #   #df=merge_for_economics(duration2,direction2,df,building_permit_data,'building_permit_data_5months_backward')  
  #   df=merge_for_economics(duration2,direction2,df,capital_flows_data,'capital_flows_data_5months_backward')  
  #   print("data length"+str(len(df)))
  #   df=merge_for_economics(duration2,direction2,df,economics_consumer_confidence_data,'economics_consumer_confidence_data_5months_backward')  
  #   #df=merge_for_economics(duration2,direction2,df,economics_consumer_credit_data,'economics_consumer_credit_data_5months_backward')   
  #   df=merge_for_economics(duration2,direction2,df,consumer_price_index_cpi_data,'consumer_price_index_cpi_data_5months_backward')   
  #  # df=merge_for_economics(duration2,direction2,df,consumer_spending_data,'consumer_spending_data_5months_backward')   
  #   df=merge_for_economics(duration2,direction2,df,core_inflation_rate_data,'core_inflation_rate_data_5months_backward')  
  #   print("data length"+str(len(df)))
  #   #df=merge_for_economics(duration2,direction2,df,economics_currencies_data,'economics_currencies_data_5months_backward')    
      
  #   #df=merge_for_economics(duration2,direction2,df,home_ownership_rate,'home_ownership_rate_5months_backward')
  #   df=merge_for_economics(duration2,direction2,df,households_debt_to_gdp,'households_debt_to_gdp_5months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,debt_to_income,'debt_to_income_5months_backward')
  #   df=merge_for_economics(duration2,direction2,df,housing_index,'housing_index_5months_backward')
  #   print("data length"+str(len(df)))
  #   df=merge_for_economics(duration2,direction2,df,housing_starts,'housing_starts_5months_backward')
  #   df=merge_for_economics(duration2,direction2,df,import_prices,'import_prices_5months_backward')
  #   df=merge_for_economics(duration2,direction2,df,economics_imports,'economics_imports_5months_backward')
  #   df=merge_for_economics(duration2,direction2,df,lending_rate,'lending_rate_5months_backward')
  #   print("data length"+str(len(df)))
  #   df=merge_for_economics(duration2,direction2,df,labour_costs,'labour_costs_5months_backward')
  #   df=merge_for_economics(duration2,direction2,df,inflation_rate,'inflation_rate_5months_backward')
  #   df=merge_for_economics(duration2,direction2,df,inflation_expectations,'inflation_expectations_5months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,jobless_claims,'jobless_claims_5months_backward')
  #   print("data length"+str(len(df)))
  #   df=merge_for_economics(duration2,direction2,df,inflation_rate_mom,'inflation_rate_mom_5months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,loans_to_private_sector,'loans_to_private_sector_5months_backward')
  #   df=merge_for_economics(duration2,direction2,df,loan_growth,'loan_growth_5months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,minimum_wages,'minimum_wages_5months_backward')
      
  #   # df=merge_for_economics(duration2,direction2,df,long_term_unemployment_rate,'long_term_unemployment_rate_5months_backward')
  #   # df=merge_for_economics(duration2,direction2,df,money_supply_m1,'money_supply_m1_5months_backward')
  #   # df=merge_for_economics(duration2,direction2,df,natural_gas_imports,'natural_gas_imports_5months_backward')
  #   # df=merge_for_economics(duration2,direction2,df,economics_money_supply_m3,'economics_money_supply_m3_5months_backward')
    
  #   #df=merge_for_economics(duration2,direction2,df,part_time_employment,'part_time_employment_5months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,personal_savings,'personal_savings_5months_backward')
  #   df=merge_for_economics(duration2,direction2,df,personal_spending,'personal_spending_5months_backward')
  #   df=merge_for_economics(duration2,direction2,df,price_to_rent_ratio,'price_to_rent_ratio_5months_backward')
    
  #   df=merge_for_economics(duration2,direction2,df,private_debt_to_gdp,'private_debt_to_gdp_5months_backward')
  #   df=merge_for_economics(duration2,direction2,df,private_sector_credit,'private_sector_credit_5months_backward')
  #   df=merge_for_economics(duration2,direction2,df,producer_prices,'producer_prices_5months_backward')
  #   df=merge_for_economics(duration2,direction2,df,producer_prices_change,'producer_prices_change_5months_backward')
  #   print("data length"+str(len(df)))
      
  #   df=merge_for_economics(duration2,direction2,df,productivity,'productivity_5months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,remittances,'remittances_5months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,retail_sales_mom,'retail_sales_mom_5months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,retail_sales_yoy,'retail_sales_yoy_5months_backward')
      
  #   #df=merge_for_economics(duration2,direction2,df,retirement_age_men,'retirement_age_men_5months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,retirement_age_women,'retirement_age_women_5months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,stock_market_indexes,'stock_market_indexes_5months_backward')
  #   df=merge_for_economics(duration2,direction2,df,interest_rate,'interest_rate_5months_backward')
  #   print("data length"+str(len(df)))
  #   #df=merge_for_economics(duration2,direction2,df,terms_of_trade,'terms_of_trade_5months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,terrorism_index,'terrorism_index_5months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,tourism_revenues,'tourism_revenues_5months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,tourist_arrivals,'tourist_arrivals_5months_backward')
      
  #   #df=merge_for_economics(duration2,direction2,df,unemployed_persons,'unemployed_persons_5months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,unemployment_rate,'unemployment_rate_5months_backward')
  #   df=merge_for_economics(duration2,direction2,df,wage_growth,'wage_growth_5months_backward')
  #   df=merge_for_economics(duration2,direction2,df,economics_wages,'economics_wages_5months_backward')
      
  #   #df=merge_for_economics(duration2,direction2,df,weapons_sales,'weapons_sales_5months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,wages_in_manufacturing,'wages_in_manufacturing_5months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,youth_unemployment_rate,'youth_unemployment_rate_5months_backward')
  #   print("data length"+str(len(df)))
      
      
      
    
      
    
  #   # df=merge_for_economics(duration2,direction2,df,food_inflation,'food_inflation_5months_backward')
  #   # df=merge_for_economics(duration2,direction2,df,economics_export_data,'economics_export_data_5months_backward')
  #   # df=merge_for_economics(duration2,direction2,df,balance_of_trade_data,'balance_of_trade_data_5months_backward')
  #   # df=merge_for_economics(duration2,direction2,df,bank_lending_rate_data,'bank_lending_rate_data_5months_backward')
  #   # #df=merge_for_economics(duration2,direction2,df,banks_balance_sheet_data,'banks_balance_sheet_data_5months_backward')  
  #   # #df=merge_for_economics(duration2,direction2,df,economics_bonds_data,'economics_bonds_data_5months_backward')
  #   # df=merge_for_economics(duration2,direction2,df,cash_reserve_ratio_data,'cash_reserve_ratio_data_5months_backward')  
  #   # #df=merge_for_economics(duration2,direction2,df,building_permit_data,'building_permit_data_5months_backward')  
  #   # df=merge_for_economics(duration2,direction2,df,capital_flows_data,'capital_flows_data_5months_backward')  
  #   # print("data length"+str(len(df)))
  #   # #df=merge_for_economics(duration2,direction2,df,economics_consumer_confidence_data,'economics_consumer_confidence_data_5months_backward')  
  #   # #df=merge_for_economics(duration2,direction2,df,economics_consumer_credit_data,'economics_consumer_credit_data_5months_backward')   
  #   # df=merge_for_economics(duration2,direction2,df,consumer_price_index_cpi_data,'consumer_price_index_cpi_data_5months_backward')   
  #   # df=merge_for_economics(duration2,direction2,df,consumer_spending_data,'consumer_spending_data_5months_backward')   
  #   # df=merge_for_economics(duration2,direction2,df,core_inflation_rate_data,'core_inflation_rate_data_5months_backward')    

    
    
  #   print("Now extractingfor nerest")
  #   duration2="180d"
  #   direction2="backward"
  #   df=merge_for_economics(duration2,direction2,df,foreign_direct_investment,'foreign_direct_investment__6months_backward')
  #   print("data length"+str(len(df)))
  #   df=merge_for_economics(duration2,direction2,df,foreign_exchange_reserves,'foreign_exchange_reserves__6months_backward')
  #   #print("data length"+str(len(df)))
  #   df=merge_for_economics(duration2,direction2,df,economics_unemployment_rate,'economics_unemployment_rate__6months_backward')
  #   print("data length"+str(len(df)))
  #   #df=merge_for_economics(duration2,direction2,df,full_time_employment,'full_time_employment__6months_backward')
  #   print("data length"+str(len(df)))
  #   df=merge_for_economics(duration2,direction2,df,economics_gasoline_prices,'economics_gasoline_prices__6months_backward')
  #   print("data length"+str(len(df)))
  #   df=merge_for_economics(duration2,direction2,df,gdp_deflator,'gdp_deflator__6months_backward')
  #   df=merge_for_economics(duration2,direction2,df,debt_to_gdp,'debt_to_gdp__6months_backward')
  #   df=merge_for_economics(duration2,direction2,df,food_inflation,'food_inflation_6months_backward')
  #   df=merge_for_economics(duration2,direction2,df,economics_export_data,'economics_export_data_6months_backward')
  #   df=merge_for_economics(duration2,direction2,df,balance_of_trade_data,'balance_of_trade_data_6months_backward')
  #   df=merge_for_economics(duration2,direction2,df,bank_lending_rate_data,'bank_lending_rate_data_6months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,banks_balance_sheet_data,'banks_balance_sheet_data_6months_backward')  
  #   #df=merge_for_economics(duration2,direction2,df,economics_bonds_data,'economics_bonds_data_6months_backward')
  #   df=merge_for_economics(duration2,direction2,df,cash_reserve_ratio_data,'cash_reserve_ratio_data_6months_backward')  
  #   #df=merge_for_economics(duration2,direction2,df,building_permit_data,'building_permit_data_6months_backward')  
  #   df=merge_for_economics(duration2,direction2,df,capital_flows_data,'capital_flows_data_6months_backward')  
  #   print("data length"+str(len(df)))
  #   df=merge_for_economics(duration2,direction2,df,economics_consumer_confidence_data,'economics_consumer_confidence_data_6months_backward')  
  #  # #df=merge_for_economics(duration2,direction2,df,economics_consumer_credit_data,'economics_consumer_credit_data_6months_backward')   
  #   df=merge_for_economics(duration2,direction2,df,consumer_price_index_cpi_data,'consumer_price_index_cpi_data_6months_backward')   
  #   #df=merge_for_economics(duration2,direction2,df,consumer_spending_data,'consumer_spending_data_6months_backward')   
  #   df=merge_for_economics(duration2,direction2,df,core_inflation_rate_data,'core_inflation_rate_data_6months_backward')  
  #   print("data length"+str(len(df)))
  #   #df=merge_for_economics(duration2,direction2,df,economics_currencies_data,'economics_currencies_data_6months_backward')    
      
  #   #df=merge_for_economics(duration2,direction2,df,home_ownership_rate,'home_ownership_rate_6months_backward')
  #   df=merge_for_economics(duration2,direction2,df,households_debt_to_gdp,'households_debt_to_gdp_6months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,debt_to_income,'debt_to_income_6months_backward')
  #   df=merge_for_economics(duration2,direction2,df,housing_index,'housing_index_6months_backward')
  #   print("data length"+str(len(df)))
  #   df=merge_for_economics(duration2,direction2,df,housing_starts,'housing_starts_6months_backward')
  #   df=merge_for_economics(duration2,direction2,df,import_prices,'import_prices_6months_backward')
  #   df=merge_for_economics(duration2,direction2,df,economics_imports,'economics_imports_6months_backward')
  #   df=merge_for_economics(duration2,direction2,df,lending_rate,'lending_rate_6months_backward')
  #   print("data length"+str(len(df)))
  #   df=merge_for_economics(duration2,direction2,df,labour_costs,'labour_costs_6months_backward')
  #   df=merge_for_economics(duration2,direction2,df,inflation_rate,'inflation_rate_6months_backward')
  #   df=merge_for_economics(duration2,direction2,df,inflation_expectations,'inflation_expectations_6months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,jobless_claims,'jobless_claims_6months_backward')
  #   print("data length"+str(len(df)))
  #   df=merge_for_economics(duration2,direction2,df,inflation_rate_mom,'inflation_rate_mom_6months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,loans_to_private_sector,'loans_to_private_sector_6months_backward')
  #   df=merge_for_economics(duration2,direction2,df,loan_growth,'loan_growth_6months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,minimum_wages,'minimum_wages_6months_backward')
      
  #   # df=merge_for_economics(duration2,direction2,df,long_term_unemployment_rate,'long_term_unemployment_rate_6months_backward')
  #   # df=merge_for_economics(duration2,direction2,df,money_supply_m1,'money_supply_m1_6months_backward')
  #   # df=merge_for_economics(duration2,direction2,df,natural_gas_imports,'natural_gas_imports_6months_backward')
  #   # df=merge_for_economics(duration2,direction2,df,economics_money_supply_m3,'economics_money_supply_m3_6months_backward')
    
  #   #df=merge_for_economics(duration2,direction2,df,part_time_employment,'part_time_employment_6months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,personal_savings,'personal_savings_6months_backward')
  #   df=merge_for_economics(duration2,direction2,df,personal_spending,'personal_spending_6months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,price_to_rent_ratio,'price_to_rent_ratio_6months_backward')
    
  #   #df=merge_for_economics(duration2,direction2,df,private_debt_to_gdp,'private_debt_to_gdp_6months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,private_sector_credit,'private_sector_credit_6months_backward')
  #   df=merge_for_economics(duration2,direction2,df,producer_prices,'producer_prices_6months_backward')
  #   df=merge_for_economics(duration2,direction2,df,producer_prices_change,'producer_prices_change_6months_backward')
  #   print("data length"+str(len(df)))
      
  #   df=merge_for_economics(duration2,direction2,df,productivity,'productivity_6months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,remittances,'remittances_6months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,retail_sales_mom,'retail_sales_mom_6months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,retail_sales_yoy,'retail_sales_yoy_6months_backward')
      
  #   #df=merge_for_economics(duration2,direction2,df,retirement_age_men,'retirement_age_men_6months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,retirement_age_women,'retirement_age_women_6months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,stock_market_indexes,'stock_market_indexes_6months_backward')
  #   df=merge_for_economics(duration2,direction2,df,interest_rate,'interest_rate_6months_backward')
  #   print("data length"+str(len(df)))
  #   #df=merge_for_economics(duration2,direction2,df,terms_of_trade,'terms_of_trade_6months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,terrorism_index,'terrorism_index_6months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,tourism_revenues,'tourism_revenues_6months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,tourist_arrivals,'tourist_arrivals_6months_backward')
      
  #   #df=merge_for_economics(duration2,direction2,df,unemployed_persons,'unemployed_persons_6months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,unemployment_rate,'unemployment_rate_6months_backward')
  #   df=merge_for_economics(duration2,direction2,df,wage_growth,'wage_growth_6months_backward')
  #   df=merge_for_economics(duration2,direction2,df,economics_wages,'economics_wages_6months_backward')
      
  #   #df=merge_for_economics(duration2,direction2,df,weapons_sales,'weapons_sales_6months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,wages_in_manufacturing,'wages_in_manufacturing_6months_backward')
  #   #df=merge_for_economics(duration2,direction2,df,youth_unemployment_rate,'youth_unemployment_rate_6months_backward')
  #   print("data length"+str(len(df)))
      
      
      
    
      
    
    #df=merge_for_economics(duration2,direction2,df,food_inflation,'food_inflation_6months_backward')
    #df=merge_for_economics(duration2,direction2,df,economics_export_data,'economics_export_data_6months_backward')
    #df=merge_for_economics(duration2,direction2,df,balance_of_trade_data,'balance_of_trade_data_6months_backward')
    #df=merge_for_economics(duration2,direction2,df,bank_lending_rate_data,'bank_lending_rate_data_6months_backward')
    #df=merge_for_economics(duration2,direction2,df,banks_balance_sheet_data,'banks_balance_sheet_data_6months_backward')  
    #df=merge_for_economics(duration2,direction2,df,economics_bonds_data,'economics_bonds_data_6months_backward')
    #df=merge_for_economics(duration2,direction2,df,cash_reserve_ratio_data,'cash_reserve_ratio_data_6months_backward')  
    #df=merge_for_economics(duration2,direction2,df,building_permit_data,'building_permit_data_6months_backward')  
    #df=merge_for_economics(duration2,direction2,df,capital_flows_data,'capital_flows_data_6months_backward')  
    print("data length"+str(len(df)))
    #df=merge_for_economics(duration2,direction2,df,economics_consumer_confidence_data,'economics_consumer_confidence_data_6months_backward')  
    #df=merge_for_economics(duration2,direction2,df,economics_consumer_credit_data,'economics_consumer_credit_data_6months_backward')   
    #df=merge_for_economics(duration2,direction2,df,consumer_price_index_cpi_data,'consumer_price_index_cpi_data_6months_backward')   
    #df=merge_for_economics(duration2,direction2,df,consumer_spending_data,'consumer_spending_data_6months_backward')   
    #df=merge_for_economics(duration2,direction2,df,core_inflation_rate_data,'core_inflation_rate_data_6months_backward')  
    print("data length"+str(len(df)))

    print("data length"+str(len(df)))    
    print("data length"+str(len(df)))    
  

  
    col.remove("XPCT_DLVRY_DT")
    col.remove("Days_Delayed")
   #if(training_set==True):


    
    numeric_features = [ ] #'Order Entry Date' 'Ordered Value'
    numeric_bin = []
    
    print("Encoding completed")
      
    
    return df