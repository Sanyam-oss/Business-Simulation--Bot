import pandas as pd
from tabulate import tabulate
import streamlit as st

def read_tables(filename):
    df = pd.read_csv(
        filename,
        delimiter=',',             # Change this to the correct delimiter if it's not a comma
        header=0,                  # Specify which row contains the headers (0-indexed)
        quotechar='"',             # Handle data enclosed in quotes
        na_values=['NA', 'NULL'],  # Handle missing values
    )
    return df

def PrintEditableTable(df):
    st.write(df['title'])
    return st.data_editor(df['df'])

def PrintTable(df):
    st.write(df['title'])
    st.dataframe(df['df'], width = 1200, hide_index = True)

def convert_to_float(value):
    if value == '':
        return 0.0
    else:
        return float(value)

def currency(num):
    try :
        return '₹ '+ str(float(num))
    except :
        return "-"

def rupee_to_float(currency):
    return float(currency[2:].replace(',', ''))

def percent_to_float(percent):
    return 0.01*float(percent[:-1])

# df = read_tables("MarketSituationYr0.csv")
# print(2)
# print(tabulate(df, headers='keys', tablefmt='psql'))


