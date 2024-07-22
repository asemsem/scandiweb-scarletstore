import pandas as pd

# Load the data
data = pd.read_csv('Scareletstore-Oct2022-cleaned.csv', dtype={'transaction_id': object, 'item_category': object}, low_memory=False)

# Filter out rows without item_category
#data = data[data['item_category'].notna()]
data = data[data['transaction_id'].notna()]
data = data[data['transaction_id'].str.isnumeric()]

# Calculate metrics
metrics = (
    data.groupby('item_category')
    .agg(
        total_revenue=('revenue', 'sum'),
        number_of_transactions=('transaction_id', lambda x: x.nunique()),
        buy_to_view_rate=('event_name', lambda x: 
            (x[x == 'purchase'].count() / x[x == 'view_item'].count()) if x[x == 'view_item'].count() > 0 else 0),
    )
    .reset_index()
)

# Sort by total_revenue
metrics = metrics.sort_values(by='total_revenue', ascending=False)

# Display the results
print(metrics)