import streamlit as st
import constants
from util import *

def update_income_status_plan(df, company, market_summary_df, incremental_investment_data_df):

    cash_in_hand_yr_0 = rupee_to_float(market_summary_df.loc[market_summary_df['Company Name'] == company, 'Cash in Hand (cr)'].values[0])

    cash_in_hand_yearwise = {
        'Year 1' : cash_in_hand_yr_0,
        'Year 2' : "-" ,
        'Year 3' : "-" ,
        'Year 4' : "-" ,
    }

    for year in df.columns[1:]:
        
        df.at[0, year] = cash_in_hand_yearwise[year]
        df.at[2, year] = yearwise_incremental_investment_sum(incremental_investment_data_df, year)
        try : 
            df.at[3, year] = df.at[0, year] - df.at[1, year] + df.at[2, year] 
        except :
            df.at[3, year] = "-"
        
        df[year] = df[year].apply(currency)

    return df

def update_number_of_customers(df, company, market_summary_df, total_fund_investment_df):

    for year in df.columns[1:]:
        
        df.at[0, year] = get_initial_customer_count(df, year, company, market_summary_df)
        df.at[2, year] = total_fund_investment_df.at[2, year]

        try : 
            df.at[1, year] = int((float(df.at[2, year])*10000000)/rupee_to_float(df.at[3, year]))
            df.at[5, year] = round(df.at[0, year]*(1-percent_to_float(df.at[4, year])) + df.at[1, year]/1000000,2) 
            df.at[6, year] = round((df.at[0, year] + df.at[5, year])/2, 2)
        except :
            df.at[1, year] = "-"
            df.at[5, year] = "-"
            df.at[6, year] = "-"

    for year in df.columns[1:]:
        for numeric_row in [2] :
            df.at[numeric_row, year] = currency(df.at[numeric_row, year])

    return df

def update_end_year_summary_table(df, company, market_summary_df, customer_df):

    for year in df.columns[1:]:
        
        df.at[0, year] = customer_df.at[6, year]
        df.at[1, year] = market_summary_df.loc[market_summary_df['Company Name'] == company, 'Price Point (annual)'].values[0]
        df.at[3, year] = market_summary_df.loc[market_summary_df['Company Name'] == company, 'Net Income %'].values[0]

        price = rupee_to_float(df.at[1, year])
        net_income_percent = percent_to_float(df.at[3, year])

        try : 
            df.at[2, year] = round ((df.at[0, year] * price) / 10, 2)
            df.at[4, year] = round ((df.at[2, year] * net_income_percent), 2)
            df.at[5, year] = df.at[4, year] + constants.buffer_amount
        except :
            df.at[2, year] = "-"
            df.at[4, year] = "-"
            df.at[5, year] = "-"

    for year in df.columns[1:]:
        for numeric_row in [2, 4, 5] :
            df.at[numeric_row, year] = currency(df.at[numeric_row, year])

    return df


def yearwise_incremental_investment_sum(incremental_investment_data_df, year = -1):
    
    column_sums = incremental_investment_data_df.sum().to_dict()

    if year == -1 :
        return column_sums

    else :
        return column_sums[year]

def get_initial_customer_count(df, year, company, market_summary_df):
    if year == "Year 1":
        return market_summary_df.loc[market_summary_df['Company Name'] == company, 'Number of customers (in millions)'].values[0]
    else :
        prev_year = int(year[5:])-1
        return df.at[5, "Year " + str(prev_year)]