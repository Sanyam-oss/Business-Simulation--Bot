import streamlit as st
import pandas as pd
import constants
from util import *
from tables_logic import *
from tables_templates import *

st.set_page_config(layout="wide")

# Sample data for the tables
data = {
    'T0': {'title' : "### Market Situation for Year 0", 'df' : read_tables("MarketSituationYr0.csv")},
    'T1': {'title' : f"#### :green[Plan the Incremental Funds (cr) over 4 years] \n ##### Total Budget : **₹{constants.incremental_fund} cr**", 'df' : pd.DataFrame(incremental_investment_table_template())},
    'T2': {'title' : "#### Income Statement Plans", 'df' : pd.DataFrame(income_status_plan_template(constants.buffer_amount))},
    'T3': {'title' : f"##### :green[Allocate Total Funds (cr) over 4 years]", 'df' : pd.DataFrame(total_fund_investment_table_template()) },
    'T4': {'title' : "#### Number of Customers", 'df' : pd.DataFrame(number_of_customers_template(constants.CAC, constants.churn))},
    'T5': {'title' : f"##### :blue[Company Summary at end of Year 1]", 'df' : pd.DataFrame(end_year_summary_template())}
} 

st.title('Business  Simulation  Bot')

# Print the Main Summary Table with Company Data and Market Situation for Year 0
market_summary_df = PrintEditableTable(data['T0'])

# Different Tabs for Different Company Simulations

# tab1, tab2 .... = st.tabs(market_summary_df['Company Name'].tolist())
tab1, tab2 = st.tabs(["AI Doc", "Health AI"])

incremental_investment_data_df = PrintEditableTable(data['T1'])

for col in incremental_investment_data_df.columns[1:]:
    incremental_investment_data_df[col] = incremental_investment_data_df[col].apply(convert_to_float)

total_invested_sum = incremental_investment_data_df[incremental_investment_data_df.columns[1:]].sum().sum()

st.write(f"###### :orange[Budget Utilized : **₹ {total_invested_sum} cr** ]")
st.write(f"###### :red[Budget Left : **₹ {constants.incremental_fund - total_invested_sum} cr** ]")

st.divider()

update_income_status_plan(data['T2']['df'], "AI Doc", market_summary_df, incremental_investment_data_df)

PrintTable(data['T2'])

st.divider() 

total_fund_investment_df = PrintEditableTable(data['T3'])

update_number_of_customers(data['T4']['df'], 'AI Doc', market_summary_df, total_fund_investment_df)
PrintTable(data['T4'])

st.divider()

st.header("Result")

update_end_year_summary_table(data['T5']['df'], 'AI Doc', market_summary_df, data['T4']['df'])
PrintTable(data['T5'])


if __name__ == '__main__':
    st.write("Running Streamlit App")
