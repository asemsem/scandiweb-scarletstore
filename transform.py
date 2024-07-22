import pandas as pd

def clean_revenue_column(df):
    # Convert price column to numeric, coercing errors to NaN
    df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')

def clean_outlier_revenue(df):
    # Process: If the transaction ID is not set, therefore there shouldnt be subsequent value for revenue.    
    clean_revenue_column(df) # Ensure Data Type for revenue to be Numeric
    df.loc[df['transaction_id'].isna(), 'revenue'] = pd.NA
    df.loc[df['transaction_id'].str.lower() == '(not set)', 'revenue'] = pd.NA

def clean_item_category(df):
    # Process: Mark a purchased item_category with NaN as "Unassigned"

    df.loc[
        df['transaction_id'].str.isnumeric() &
        df['item_category'].isna(), 'item_category'    
    ]= 'Unassigned'


def transform(input_file, output_file):
    # Read the specified sheet from the Excel file
    df = pd.read_csv(input_file, dtype={'transaction_id': object, 'item_category': object}, low_memory=False)
    #print(df.dtypes)

    # Remove Revenue outliers + Handle unassigned categories
    clean_outlier_revenue(df)
    clean_item_category(df)

    # Write the modified DataFrame back to Excel
    df.to_csv(output_file, index=False)


if __name__ == "__main__":
    input_file = '/home/ahmad/Koofr/Scandiweb Interview/Scarlet Store/Scareletstore-Oct2022-raw.csv'
    output_file = '/home/ahmad/Koofr/Scandiweb Interview/Scarlet Store/Scareletstore-Oct2022-cleaned.csv'

    transform(input_file, output_file)