def incremental_investment_table_template() :

    data = {
        'Planned Incremental Funds Allocation (cr)': [
            'Product Development & Technology',
            'Sales',
            'Marketing',
            'Operations',
            'Miscellaneous',
        ],
        'Year 1': ['', '', '', '', ''],
        'Year 2': ['', '', '', '', ''],
        'Year 3': ['', '', '', '', ''],
        'Year 4': ['', '', '', '', ''],
    }

    return data

def total_fund_investment_table_template() :

    data = {
        'Planned Total Funds Allocation (cr)': [
            'Product Development & Technology',
            'Sales',
            'Marketing',
            'Operations',
            'Miscellaneous',
        ],
        'Year 1': ['', '', '', '', ''],
        'Year 2': ['', '', '', '', ''],
        'Year 3': ['', '', '', '', ''],
        'Year 4': ['', '', '', '', ''],
    }

    return data

def income_status_plan_template(buffer) :

    data = {
        'Cash in Hand (cr)': [
            'Start of the year',
            'Desired end of the year (from non-operations)',
            'Planned Incremental Investments',
            'Total Planned Expense (cr)'
        ],
        'Year 1': ['', buffer, '', ''],
        'Year 2': ['', buffer, '', ''],
        'Year 3': ['', buffer, '', ''],
        'Year 4': ['', buffer, '', '']
    }

    return data

def number_of_customers_template(CAC, churn):
    
    data = {
        'Metric': [
            'Start of Year (in Millions)', 'Incremental', 'Marketing Spend (in cr)', 
            'CAC (Cost of Customer Acquisition)', 'Churn (in %)', 'End of Year', 'Average'
        ],
        'Year 1': ['', '', '', CAC[0], churn[0], '', ''],
        'Year 2': ['', '', '', CAC[1], churn[1], '', ''],
        'Year 3': ['', '', '', CAC[2], churn[2], '', ''],
        'Year 4': ['', '', '', CAC[3], churn[3], '', '']
    }

    return data

def end_year_summary_template():

    data = {
        'Metric': [
            'Customers (annual average, in Millions)', 'Price Point (annual)', 'Annual Revenue (cr)', 
            'Net Income %', 'Net Income (cr)', 'Cash in Hand (cr)'
        ],
        'Year 1': ['', '', '', '', '', ''],
        'Year 2': ['', '', '', '', '', ''],
        'Year 3': ['', '', '', '', '', ''],
        'Year 4': ['', '', '', '', '', '']
    }

    return data