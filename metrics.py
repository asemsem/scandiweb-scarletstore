import pandas as pd

# Load the data
data = pd.read_csv('Scareletstore-Oct2022-cleaned.csv', dtype={'transaction_id': object, 'item_category': object}, low_memory=False)

# Filter out rows without item_category
data = data[data['item_category'].notna()]

# Initialize a list to store results
results = []

# Get unique item categories
item_categories = data['item_category'].unique()

# Calculate metrics for each category
for category in item_categories:
    category_data = data[data['item_category'] == category]
    
    total_revenue = category_data['revenue'].sum()
    
    purchase_count = category_data[category_data['event_name'] == 'purchase'].shape[0]
    view_count = category_data[category_data['event_name'] == 'view_item'].shape[0]
    
    buy_to_view_rate = (purchase_count * 100 / view_count) if view_count > 0 else 0
    
    results.append({
        'item_category': category,
        'total_revenue': total_revenue,
        'views': view_count,
        'purchases': purchase_count,
        'buy_to_view_rate': round(buy_to_view_rate,2)
    })

# Convert results to a DataFrame
results_df = pd.DataFrame(results)

# Sort by total_revenue
results_df = results_df.sort_values(by='total_revenue', ascending=False)

# Display the results
print(results_df)