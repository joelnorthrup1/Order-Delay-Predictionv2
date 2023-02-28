# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 19:58:25 2022

@author: DELL
"""

import numpy as np
import pandas as pd



# Given a dataframe of shipments, creates column for number of days delayed 
# and returns as a pd.Series with matching indices
# Label uses the difference between MemoDate and ReceiptDate
# Optionally will drop all rows with NaN labels
def create_days_delayed(df: pd.DataFrame, DROP_NANS: bool = True) -> pd.Series:
    def apply_fn(row):
        try:
            if pd.isna(row['DepartureDate']) or pd.isna(row['Requested Ship Date']):
                return np.nan
        except KeyError: 
            if pd.isna(row['DepartureDate']) or pd.isna(row['Requested Ship Date']):
                return np.nan
        try:
            return (row['DepartureDate'] - row['Requested Ship Date']).days #Receipt Date Memo Date
        except KeyError: 
            return (row['DepartureDate'] - row['Requested Ship Date']).days
    
    labels = df.apply(apply_fn, axis=1)

    if DROP_NANS:
        try:
            df = df.dropna(subset=["Memo Date", "Receipt Date"])
        except KeyError:
            df = df.dropna(subset=["Requested Ship Date", "Receipt Date"])
        labels = labels.dropna()

    return labels


# Given df with days_delayed column, returns a labels column is_delayed with labels as 0 or 1
# indicating whether the delay was more than N days
def create_labels(df: pd.DataFrame, N: int) -> pd.Series:
    labels = df.apply(
        lambda x: x['days_delayed'] > N,
        axis=1
    )
    return labels