# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 23:28:23 2022

@author: DELL
"""

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



def preprocess(dataset1,X_name,y_name,training_set):
        #print(os.getcwd())
        forex=pd.read_csv("./MyApp/ext_data/forex_historical_data_202211230838.csv").reset_index()
        risk=pd.read_csv("./MyApp/ext_data/geo_political_risk.csv").reset_index()
        trends=pd.read_csv("./MyApp/ext_data/amazon_trends.csv").reset_index()
        india_cpi=pd.read_csv("./MyApp/ext_data/india_cpi.csv").reset_index()
        pet_consumption=pd.read_csv("./MyApp/ext_data/pet_consumption.csv").reset_index()
        railway_goods=pd.read_csv("./MyApp/ext_data/railway_goods.csv").reset_index()
        rainfall_india=pd.read_csv("./MyApp/ext_data/rainfall_india.csv").reset_index()
        air_quality_newdehli=pd.read_csv("./MyApp/ext_data/air_quality_newdelhi.csv").reset_index()
        air_quality_kolkata=pd.read_csv("./MyApp/ext_data/air_quality_kolkata.csv").reset_index()
        gasoline_price=pd.read_csv("./MyApp/ext_data/gasoline_price.csv").reset_index()
        motor_vehicles=pd.read_csv("./MyApp/ext_data/motor_vehicles.csv").reset_index()
        motor_vehicles_class_type=pd.read_csv("./MyApp/ext_data/motor_vehicles_class_type.csv").reset_index()
        economics_export=pd.read_csv("./MyApp/ext_data/economics_export.csv").reset_index()
        balance_of_trade=pd.read_csv("./MyApp/ext_data/balance_of_trade.csv").reset_index()
        bank_lending_rate=pd.read_csv("./MyApp/ext_data/bank_lending_rate.csv").reset_index()
        banks_balance_sheet=pd.read_csv("./MyApp/ext_data/banks_balance_sheet.csv").reset_index()
        #economics_bonds=pd.read_csv("./ext_data/economics_bonds.csv").reset_index()
        economics_bonds=None
        cash_reserve_ratio=pd.read_csv("./MyApp/ext_data/cash_reserve_ratio.csv").reset_index()
        building_permit=pd.read_csv("./MyApp/ext_data/building_permit.csv").reset_index()
        capital_flows=pd.read_csv("./MyApp/ext_data/capital_flows.csv").reset_index()
        economics_consumer_confidence=pd.read_csv("./MyApp/ext_data/economics_consumer_confidence.csv").reset_index()
        economics_consumer_credit=pd.read_csv("./MyApp/ext_data/economics_consumer_credit.csv").reset_index()
        consumer_price_index_cpi=pd.read_csv("./MyApp/ext_data/consumer_price_index_cpi.csv").reset_index()
        consumer_spending=pd.read_csv("./MyApp/ext_data/consumer_spending.csv").reset_index()
        core_inflation_rate=pd.read_csv("./MyApp/ext_data/core_inflation_rate.csv").reset_index()
        #economics_currencies=pd.read_csv("./ext_data/economics_currencies.csv").reset_index()
        economics_currencies=None
        food_inflation=pd.read_csv("./MyApp/ext_data/trading_economics_food_inflation_202210241958.csv").reset_index()
        foreign_direct_investment=pd.read_csv("./MyApp/ext_data/trading_economics_foreign_direct_investment_202210241959.csv").reset_index()
        foreign_exchange_reserves= pd.read_csv("./MyApp/ext_data/trading_economics_foreign_exchange_reserves_202210241959.csv").reset_index()
        economics_unemployment_rate=pd.read_csv("./MyApp/ext_data/trading_economics_unemployment_rate_202210242000.csv").reset_index()
        full_time_employment=pd.read_csv("./MyApp/ext_data/trading_economics_full_time_employment_202210242000.csv").reset_index()
        economics_gasoline_prices=pd.read_csv("./MyApp/ext_data/trading_economics_gasoline_prices_202210242003.csv").reset_index()
        gdp_deflator=pd.read_csv("./MyApp/ext_data/trading_economics_gdp_deflator_202210242123.csv").reset_index()
        debt_to_gdp=pd.read_csv("./MyApp/ext_data/trading_economics_government_debt_to_gdp_202210242159.csv").reset_index()
        #gdp_deflator=pd.read_csv("./ext_data/trading_economics_gdp_deflator_202210242159.csv").reset_index()
        harmonised_consumer_prices=pd.read_csv("./MyApp/ext_data/trading_economics_harmonised_consumer_prices_202210242200.csv").reset_index()
        home_ownership_rate=pd.read_csv("./MyApp/ext_data/trading_economics_home_ownership_rate_202210242201.csv").reset_index()
        households_debt_to_gdp=pd.read_csv("./MyApp/ext_data/trading_economics_households_debt_to_gdp_202210242202.csv").reset_index()
        debt_to_income=pd.read_csv("./MyApp/ext_data/trading_economics_households_debt_to_income_202210242203.csv").reset_index()
        housing_index=pd.read_csv("./MyApp/ext_data/trading_economics_housing_index_202210242203.csv").reset_index()
        housing_starts=pd.read_csv("./MyApp/ext_data/trading_economics_housing_starts_202210242204.csv").reset_index()
        import_prices=pd.read_csv("./MyApp/ext_data/trading_economics_import_prices_202210242205.csv").reset_index()
        economics_imports=pd.read_csv("./MyApp/ext_data/trading_economics_imports_202210242206.csv").reset_index()
        lending_rate=pd.read_csv("./MyApp/ext_data/trading_economics_lending_rate_202210242211.csv").reset_index()
        labour_costs=pd.read_csv("./MyApp/ext_data/trading_economics_labour_costs_202210242215.csv").reset_index()
        inflation_rate=pd.read_csv("./MyApp/ext_data/trading_economics_inflation_rate_202210242218.csv").reset_index()
        inflation_expectations=pd.read_csv("./MyApp/ext_data/trading_economics_inflation_expectations_202210242220.csv").reset_index()
        jobless_claims=pd.read_csv("./MyApp/ext_data/trading_economics_initial_jobless_claims_202210242221.csv").reset_index()
        inflation_rate_mom=pd.read_csv("./MyApp/ext_data/trading_economics_inflation_rate_mom_202210242223.csv").reset_index()
        #interbank_rate=pd.read_csv("trading_economics_interbank_rate_202210242226.csv").reset_index()
        loans_to_private_sector=pd.read_csv("./MyApp/ext_data/trading_economics_loans_to_private_sector_202210242233.csv").reset_index()
        interest_rate=pd.read_csv("./MyApp/ext_data/trading_economics_interest_rate_202210242224.csv").reset_index()
        loan_growth=pd.read_csv("./MyApp/ext_data/trading_economics_loan_growth_202210242233.csv").reset_index()
        minimum_wages=pd.read_csv("./MyApp/ext_data/trading_economics_minimum_wages_202210242235.csv").reset_index()
        long_term_unemployment_rate=pd.read_csv("./MyApp/ext_data/trading_economics_long_term_unemployment_rate_202210242235.csv").reset_index()
        money_supply_m1=pd.read_csv("./MyApp/ext_data/trading_economics_money_supply_m1_202210242235.csv").reset_index()
        natural_gas_imports=pd.read_csv("./MyApp/ext_data/trading_economics_natural_gas_imports_from_russia_202210242248.csv").reset_index()
        economics_money_supply_m3=pd.read_csv("./MyApp/ext_data/trading_economics_money_supply_m3_202210242249.csv").reset_index()
        part_time_employment=pd.read_csv("./MyApp/ext_data/trading_economics_part_time_employment_202210242251.csv").reset_index()
        personal_savings=pd.read_csv("./MyApp/ext_data/trading_economics_personal_savings_202210242251.csv").reset_index()
        personal_spending=pd.read_csv("./MyApp/ext_data/trading_economics_personal_spending_202210242251.csv").reset_index()
        price_to_rent_ratio=pd.read_csv("./MyApp/ext_data/trading_economics_price_to_rent_ratio_202210242251.csv").reset_index()
        private_debt_to_gdp=pd.read_csv("./MyApp/ext_data/trading_economics_private_debt_to_gdp_202210242251.csv").reset_index()
        private_sector_credit=pd.read_csv("./MyApp/ext_data/trading_economics_private_sector_credit_202210242251.csv").reset_index()
        
        
        producer_prices=pd.read_csv("./MyApp/ext_data/trading_economics_producer_prices_202210242251.csv").reset_index()
        producer_prices_change=pd.read_csv("./MyApp/ext_data/trading_economics_producer_prices_change_202210242251.csv").reset_index()
        productivity=pd.read_csv("./MyApp/ext_data/trading_economics_productivity_202210242251.csv").reset_index()
        remittances=pd.read_csv("./MyApp/ext_data/trading_economics_remittances_202210242251.csv").reset_index()
        retail_sales_mom=pd.read_csv("./MyApp/ext_data/trading_economics_retail_sales_mom_202210242251.csv").reset_index()
        retail_sales_yoy=pd.read_csv("./MyApp/ext_data/trading_economics_retail_sales_yoy_202210242251.csv").reset_index()
        retirement_age_men=pd.read_csv("./MyApp/ext_data/trading_economics_retirement_age_men_202210242251.csv").reset_index()
        retirement_age_women=pd.read_csv("./MyApp/ext_data/trading_economics_retirement_age_women_202210242251.csv").reset_index()
        stock_market_indexes=pd.read_csv("./MyApp/ext_data/trading_economics_stock_market_indexes_202210242251.csv").reset_index()
        interest_rate=pd.read_csv("./MyApp/ext_data/trading_economics_interest_rate_202210242224.csv").reset_index()
        
        
        terms_of_trade=pd.read_csv("./MyApp/ext_data/trading_economics_terms_of_trade_202210242251.csv").reset_index()
        terrorism_index=pd.read_csv("./MyApp/ext_data/trading_economics_terrorism_index_202210242251.csv").reset_index()
        tourism_revenues=pd.read_csv("./MyApp/ext_data/trading_economics_tourism_revenues_202210242251.csv").reset_index()
        tourist_arrivals=pd.read_csv("./MyApp/ext_data/trading_economics_tourist_arrivals_202210242251.csv").reset_index()
        unemployed_persons=pd.read_csv("./MyApp/ext_data/trading_economics_unemployed_persons_202210242251.csv").reset_index()
        unemployment_rate=pd.read_csv("./MyApp/ext_data/trading_economics_unemployment_rate_202210242251.csv").reset_index()
        
        wage_growth=pd.read_csv("./MyApp/ext_data/trading_economics_wage_growth_202210242251.csv").reset_index()
        economics_wages=pd.read_csv("./MyApp/ext_data/trading_economics_wages_202210242251.csv").reset_index()
        weapons_sales=pd.read_csv("./MyApp/ext_data/trading_economics_weapons_sales_202210242251.csv").reset_index()
        wages_in_manufacturing=pd.read_csv("./MyApp/ext_data/trading_economics_wages_in_manufacturing_202210242251.csv").reset_index()
        youth_unemployment_rate=pd.read_csv("./MyApp/ext_data/trading_economics_youth_unemployment_rate_202210242251.csv").reset_index()
        
        
        wage_growth=pd.read_csv("./MyApp/ext_data/trading_economics_wage_growth_202210242251.csv").reset_index()
        economics_wages=pd.read_csv("./MyApp/ext_data/trading_economics_wages_202210242251.csv").reset_index()
        weapons_sales=pd.read_csv("./MyApp/ext_data/trading_economics_weapons_sales_202210242251.csv").reset_index()
        wages_in_manufacturing=pd.read_csv("./MyApp/ext_data/trading_economics_wages_in_manufacturing_202210242251.csv").reset_index()
        youth_unemployment_rate=pd.read_csv("./MyApp/ext_data/trading_economics_youth_unemployment_rate_202210242251.csv").reset_index()
        
        
        
        
        
        try:
          dataset=dataset1.drop(['Unnamed: 15','Unnamed: 12'],axis=1) #,'PO_ID'
        except:
          print("Not founded in axis")
          dataset=dataset1
        #dataset=dataset1[dataset1['FD Location']=='USA']
        col=['ITEM_COST_WAC','ITEM_DSCR','CNCL_QTY','RCV_QTY','ORIG_ORD_QTY','CNCL_DT','DELIVERY_DT','PO_ORD_DT','XPCT_DLVRY_DT','EM_ITEM_NUM','GNRC_NAME','THERAP_CLASS','FD Location','API Location','DC_NUM','SPLR_VENDOR_NUM','SPLR_NAME','SPLR_REGION','SPLR_POSTAL_CODE','SPLR_COUNTRY','Days_Delayed'] #'RCV_QTY',
        
        dataset=dataset[col].dropna(subset=['XPCT_DLVRY_DT','Days_Delayed']) #.drop_duplicates().dropna(subset=['XPCT_DLVRY_DT','Days_Delayed'])
        merged=merging_encoding(dataset,forex,risk,trends,india_cpi,pet_consumption,railway_goods,rainfall_india,air_quality_kolkata,air_quality_newdehli,gasoline_price,motor_vehicles,motor_vehicles_class_type,economics_export,balance_of_trade,bank_lending_rate,banks_balance_sheet,economics_bonds,cash_reserve_ratio,building_permit,capital_flows,economics_consumer_confidence,economics_consumer_credit,consumer_price_index_cpi,consumer_spending,core_inflation_rate,economics_currencies,food_inflation,foreign_direct_investment,foreign_exchange_reserves,economics_unemployment_rate,full_time_employment,economics_gasoline_prices,gdp_deflator,debt_to_gdp,harmonised_consumer_prices,home_ownership_rate,households_debt_to_gdp,debt_to_income,housing_index,housing_starts,import_prices,economics_imports,lending_rate,labour_costs,inflation_rate,inflation_expectations,jobless_claims,inflation_rate_mom,loans_to_private_sector,loan_growth,minimum_wages,long_term_unemployment_rate,money_supply_m1,natural_gas_imports,economics_money_supply_m3,part_time_employment,personal_savings,personal_spending,price_to_rent_ratio,private_debt_to_gdp,private_sector_credit,producer_prices,producer_prices_change,productivity,remittances,retail_sales_mom,retail_sales_yoy,retirement_age_men,retirement_age_women,stock_market_indexes,interest_rate,terms_of_trade,terrorism_index,tourism_revenues,tourist_arrivals,unemployed_persons,unemployment_rate,wage_growth,economics_wages,weapons_sales,wages_in_manufacturing,youth_unemployment_rate,col,training_set)
        
        
        merged=merged.drop(["index"],axis=1)
        
        #merged=merged.drop(["time"],axis=1)
        
        #merged=merged.drop(["Unnamed: 0"],axis=1)
        #merged=merged.drop(["level_0"],axis=1)
        y= merged['Days_Delayed'] #(>10).astype(np.int8)
        merged=merged.drop(["Days_Delayed"],axis=1)
        merged.to_csv("./"+X_name+"_processed.csv")
        y.to_csv("./"+y_name+"_processed.csv")
        return merged,y