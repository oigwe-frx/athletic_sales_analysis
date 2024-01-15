# -*- coding: utf-8 -*-
"""athletic_sales_analysis_starter_code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1heBm3OqbSn-OAy9KEgCz8N6PDLBuinTV

## **Context**

### Objective

You'll analyze sales data to gain insights into which cities in the U.S. have sold the most athletic wear over two years. Next, you'll determine which retailers had the greatest total sales for athletic wear, and which retailers sold the most women's athletic footwear. Finally, you'll determine which day and week had the highest sales for women's athletic footwear.

###<b> Mount the Drive
"""

from google.colab import drive
drive.mount('/content/drive')

"""### <b> Load Libraries"""

# Import Libraries and Dependencies
import pandas as pd

"""### <b> 1. Combine and Clean Data

#### Import CSVs
"""

# Read the CSV files into DataFrames.

# Load Data for Athletic Sales 2020
sales_2020 = '/content/athletic_sales_2020.csv'
df_2020 = pd.read_csv(sales_2020)

# Load Data for Athletic Sales 2021
sales_2021 = '/content/athletic_sales_2021.csv'
df_2021 = pd.read_csv(sales_2021)

# Display the 2020 sales DataFrame
df_2020.head()

# Display the 2021 sales DataFrame
df_2021.head()

"""#### Check the data types of each DataFrame"""

# Check the 2020 sales data types.
df_2020.info()

# Check the 2021 sales data types.
df_2021.info()

"""#### Combine the sales data by rows."""

# Combine the 2020 and 2021 sales DataFrames on the rows and reset the index.

# Combine the DataFrames on rows
combined_df = pd.concat([df_2020, df_2021])

# Reset the index
combined_df.reset_index(drop=True, inplace=True)

# Check if any values are null.

null_values = combined_df.isnull()

# Check if there are any null values in the entire DataFrame
if null_values.values.any():
    print("There are null values in the DataFrame.")
else:
    print("There are no null values in the DataFrame.")

# Check the data type of each column
combined_df.info()

# Convert the "invoice_date" to a datetime datatype
combined_df['invoice_date'] = pd.to_datetime(combined_df['invoice_date'])

# Confirm that the "invoice_date" data type has been changed.
combined_df.info()

"""### **2. Determine which Region Sold the Most Products**

#### Using `groupby`
"""

# Show the number products sold for region, state, and city.
# Rename the sum to "Total_Products_Sold".

# Group by 'region,' 'state,' and 'city' columns and sum the 'units_sold' column
grouped_units_sold = combined_df.groupby(['region', 'state', 'city'])['units_sold'].sum().reset_index()

# Rename the sum column to 'Total_Products_Sold'
grouped_units_sold.rename(columns={'units_sold': 'Total_Products_Sold'}, inplace=True)

# Show the top 5 results via groupby
print("Top Regions by Total Products Sold")
top_five_grouped_units_sold = grouped_units_sold.sort_values(by='Total_Products_Sold', ascending=False)[0:5]
top_five_grouped_units_sold

"""#### Using `pivot_table`"""

# Show the number products sold for region, state, and city.

# Create a pivot table to show the total products sold for region, state, and city
pivot_table_units_sold = pd.pivot_table(combined_df, values='units_sold', index=['region', 'state', 'city'], aggfunc='sum', fill_value=0)

# Reset the index to make the pivot table look like the previous result
pivot_table_units_sold.reset_index(inplace=True)

# Rename the sum column to 'Total_Products_Sold'
pivot_table_units_sold.rename(columns={'units_sold': 'Total_Products_Sold'}, inplace=True)


# Show the top 5 results via pivot table
print("Top Regions by Total Products Sold")
top_five_pivot_units_sold = pivot_table_units_sold.sort_values(by='Total_Products_Sold', ascending=False)[0:5]
top_five_pivot_units_sold

"""### <b>3. Determine which Region had the Most Sales

#### Using `groupby`
"""

# Show the total sales for the products sold for each region, state, and city.
# Rename the "total_sales" column to "Total Sales"

# Group by 'region,' 'state,' and 'city' columns and sum the 'total_sales' column
grouped_total_sales = combined_df.groupby(['region', 'state', 'city'])['total_sales'].sum().reset_index()

# Rename the total_sales column to 'Total Sales'
grouped_total_sales.rename(columns={'total_sales': 'Total Sales'}, inplace=True)

# Show the top 5 results via groupby
print("Top Regions by Total Sales")
top_five_grouped_total_sales = grouped_total_sales.sort_values(by='Total Sales', ascending=False)[0:5]
top_five_grouped_total_sales

"""#### Using `pivot_table`"""

# Show the total sales for the products sold for each region, state, and city.
# Optional: Rename the "total_sales" column to "Total Sales"


# Create a pivot table to show the total products sold for region, state, and city
pivot_table_total_sales = pd.pivot_table(combined_df, values='total_sales', index=['region', 'state', 'city'], aggfunc='sum', fill_value=0)

# Reset the index
pivot_table_total_sales.reset_index(inplace=True)

# Rename the total_sales column to 'Total_Products_Sold'
pivot_table_total_sales.rename(columns={'total_sales': 'Total Sales'}, inplace=True)


# Show the top 5 results via pivot table
print("Top Regions by Total Sales")
top_five_pivot_total_sales = pivot_table_total_sales.sort_values(by='Total Sales', ascending=False)[0:5]
top_five_pivot_total_sales

"""### <b> 4. Determine which Retailer had the Most Sales

#### Using `groupby`
"""

# Show the total sales for the products sold for each retailer, region, state, and city.
# Rename the "total_sales" column to "Total Sales"

# Group by 'region,' 'state,' and 'city' columns and sum the 'total_sales' column
grouped_total_sales_retailer = combined_df.groupby(['retailer','region', 'state', 'city'])['total_sales'].sum().reset_index()

# Rename the total_sales column to 'Total Sales'
grouped_total_sales_retailer.rename(columns={'total_sales': 'Total Sales'}, inplace=True)

# Show the top 5 results via groupby
print("Top Regions by Total Sales")
top_five_grouped_retailer_total_sales = grouped_total_sales_retailer.sort_values(by='Total Sales', ascending=False)[0:5]
top_five_grouped_retailer_total_sales

"""#### Using `pivot_table`"""

# Show the total sales for the products sold for each retailer, region, state, and city.
# Optional: Rename the "total_sales" column to "Total Sales"


# Create a pivot table to show the total products sold for region, state, and city
pivot_table_total_sales_retailer = pd.pivot_table(combined_df, values='total_sales', index=['retailer', 'region', 'state', 'city'], aggfunc='sum', fill_value=0)

# Reset the index
pivot_table_total_sales_retailer.reset_index(inplace=True)

# Rename the total_sales column to 'Total_Products_Sold'
pivot_table_total_sales_retailer.rename(columns={'total_sales': 'Total Sales'}, inplace=True)


# Show the top 5 results via pivot table
print("Top Regions by Total Sales")
top_five_pivot_total_sales_retailer = pivot_table_total_sales_retailer.sort_values(by='Total Sales', ascending=False)[0:5]
top_five_pivot_total_sales_retailer

"""### <b>5. Determine which Retailer Sold the Most Women's Athletic Footwear"""

# Filter the sales data to get the women's athletic footwear sales data.

"""#### Using `groupby`"""

# Show the total number of women's athletic footwear sold for each retailer, region, state, and city.
# Rename the "units_sold" column to "Womens_Footwear_Units_Sold"

# Group by 'region,' 'state,' and 'city' columns and sum the 'total_sales' column
grouped_units_sold = combined_df.groupby(['retailer','region', 'state', 'city', 'product'])['units_sold'].sum().reset_index()


# Create an empty list to store sales_dictionaries
temp_data_list = []

# Loop through the established DataFrame (grouped_total_product)
for index, row in combined_df.iterrows():
    # Process the row and create a new DataFrame or list of DataFrames
      if row['product'] == "Women's Athletic Footwear":
        new_data = {'retailer': row['retailer'], 'region': row['region'], 'state': row['state'], 'city': row['city'], 'product': row['product'], 'units_sold': row['units_sold'] }
        temp_data_list.append(new_data)

# Create the new DataFrame with the empty DataFrame
grouped_total_product_womens_footwear = pd.DataFrame(temp_data_list).groupby(['retailer','region', 'state', 'city', 'product'])['units_sold'].sum().reset_index()


# Rename the units_sold column to 'Total_Products_Sold'
grouped_total_product_womens_footwear.rename(columns={'units_sold': 'Total_Products_Sold'}, inplace=True)

# Show the top 5 results via groupby

top_five_grouped_retailer_total_sales_womens_footwear = grouped_total_product_womens_footwear.sort_values(by='Total_Products_Sold', ascending=False)[0:5]

print("Top Regions by Total Sales")
top_five_grouped_retailer_total_sales_womens_footwear

"""#### Using `pivot_table`"""

# Show the total number of women's athletic footwear sold for each retailer, region, state, and city.

# Create a pivot table to show the total number of women's athletic footwear sold for each retailer, region, state, and city
pivot_table_total_product_womens_footwear = pd.pivot_table(combined_df[combined_df['product'] == "Women's Athletic Footwear"],
                             values='units_sold',
                             index=['retailer', 'region', 'state', 'city'],
                             aggfunc='sum',
                             fill_value=0)

# Reset the index
pivot_table_total_product_womens_footwear.reset_index(inplace=True)

# Rename the units_sold column to 'Womens_Footwear_Units_Sold'
pivot_table_total_product_womens_footwear.rename(columns={'units_sold': 'Womens_Footwear_Units_Sold'}, inplace=True)

# Show the top 5 results
print("Top Regions by Total Sales (Women's Athletic Footwear)")
top_five_pivot_table_total_product_womens_footwear = pivot_table_total_product_womens_footwear.sort_values(by='Womens_Footwear_Units_Sold', ascending=False)[0:5]
top_five_pivot_table_total_product_womens_footwear

"""### <b>6. Determine the Day with the Most Women's Athletic Footwear Sales"""

# Create a pivot table with the 'invoice_date' column is the index, and the "total_sales" as the values.
# Optional: Rename the "total_sales" column to "Total Sales"

pivot_table_day_most_womens_footwear = pd.pivot_table(combined_df[combined_df['product'] == "Women's Athletic Footwear"],
                                                      values = 'total_sales',
                                                      index=['invoice_date'],
                                                      aggfunc='sum',
                                                      fill_value=0)

# Reset the index
pivot_table_day_most_womens_footwear.reset_index(inplace=True)

# Rename the 'total_sales' column to 'Total Sales'
pivot_table_day_most_womens_footwear.rename(columns={'total_sales': 'Total Sales'}, inplace=True)

# Show the top 10 results
print("Top 10 Days by Total Sales")
pivot_table_day_most_womens_footwear = pivot_table_day_most_womens_footwear.sort_values(by='Total Sales', ascending=False)[0:10]
pivot_table_day_most_womens_footwear

# Resample the pivot table into daily bins, and get the total sales for each day.
# Sort the resampled pivot table in ascending order on "Total Sales".


pivot_table_daily_most_womens_footwear = pd.pivot_table(combined_df[combined_df['product'] == "Women's Athletic Footwear"],
                                                      values = 'total_sales',
                                                      index=['invoice_date'],
                                                      aggfunc='sum',
                                                      fill_value=0)

# Resample the data into daily bins and sum the values for each day
resampled_df_daily_womens_footwear_sales = pivot_table_daily_most_womens_footwear.resample('D').sum()

# Rename the resampled column to 'Total Sales'
resampled_df_daily_womens_footwear_sales.rename(columns={'total_sales': 'Total Sales'}, inplace=True)

# Show the top 10 results
print("Top 10 Days by Total Sales")
top_ten_resampled_df_daily_womens_footwear_sales = resampled_df_daily_womens_footwear_sales.sort_values(by='Total Sales', ascending=False)[0:10]
top_ten_resampled_df_daily_womens_footwear_sales

"""### 7.  Determine the Week with the Most Women's Athletic Footwear Sales"""

# Resample the pivot table into weekly bins, and get the total sales for each week.
# Sort the resampled pivot table in ascending order on "Total Sales".

pivot_table_weekly_most_womens_footwear = pd.pivot_table(combined_df[combined_df['product'] == "Women's Athletic Footwear"],
                                                      values = 'total_sales',
                                                      index=['invoice_date'],
                                                      aggfunc='sum',
                                                      fill_value=0)

# Resample the data into daily bins and sum the values for each day
resampled_df_weekly_womens_footwear_sales = pivot_table_weekly_most_womens_footwear.resample('W').sum()

# Rename the resampled column to 'Total Sales'
resampled_df_weekly_womens_footwear_sales.rename(columns={'total_sales': 'Total Sales'}, inplace=True)

# Show the top 10 results
print("Top 10 Days by Total Sales")
top_ten_resampled_df_weekly_womens_footwear_sales = resampled_df_weekly_womens_footwear_sales.sort_values(by='Total Sales', ascending=False)[0:10]
top_ten_resampled_df_weekly_womens_footwear_sales