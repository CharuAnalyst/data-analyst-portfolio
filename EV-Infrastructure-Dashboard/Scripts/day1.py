import pandas as pd
import numpy as np

print("=== day 1: DATA CLEANING START ===")

# 1. CLEAN EV SALES DATA
print("\n1. Loading Sales Data...")
sales = pd.read_csv('../Data/EV_Dataset.csv')
sales['Date'] = pd.to_datetime(sales['Date'], dayfirst=True, errors='coerce')
sales = sales.dropna(subset=['Date'])
sales_monthly = sales.groupby(['Date', 'State'])['EV_Sales_Quantity'].sum().reset_index()
sales_monthly.rename(columns={'EV_Sales_Quantity': 'Total_EV_Sales'}, inplace=True)
sales_monthly = sales_monthly[sales_monthly['Total_EV_Sales'] > 0]
print("Sales Data Ready. Rows:", len(sales_monthly))

# 2. CLEAN CHARGING STATIONS DATA
print("\n2. Loading Stations Data...")
stations = pd.read_csv('../Data/ev-charging-stations-india.csv')
stations['state'] = stations['state'].str.strip().str.title()
station_count = stations.groupby('state').size().reset_index(name='Current_Stations')
station_count.rename(columns={'state': 'State'}, inplace=True)
print("Total Stations Found:", station_count['Current_Stations'].sum())

# 3. CLEAN WEATHER DATA
print("\n3. Loading Weather Data...")
weather = pd.read_csv('../Data/DailyDelhiClimate.csv')
weather['date'] = pd.to_datetime(weather['date'])
weather['Year'] = weather['date'].dt.year
weather['Month'] = weather['date'].dt.month
weather_monthly = weather.groupby(['Year', 'Month']).agg({
    'meantemp': 'mean',
    'humidity': 'mean'
}).reset_index()
weather_monthly['Date'] = pd.to_datetime(weather_monthly[['Year', 'Month']].assign(day=1))
weather_monthly = weather_monthly[['Date', 'meantemp', 'humidity']]
print("Weather Data Ready. Rows:", len(weather_monthly))

# 4. MERGE ALL DATASETS- FIXED HERE
print("\n4. Merging All Data...")
master = pd.merge(sales_monthly, station_count, on='State', how='left')
master['Current_Stations'] = master['Current_Stations'].fillna(1)

master = pd.merge(master, weather_monthly, on='Date', how='left')
master[['meantemp', 'humidity']] = master[['meantemp', 'humidity']].ffill()  # ← YE LINE BADLI

master['EV_per_Station'] = master['Total_EV_Sales'] / master['Current_Stations']

# 5.  SAVE OUTPUT
master.to_csv('EV_Master_Data.csv', index=False)
station_count.to_csv('Station_Count_StateWise.csv', index=False)

print("\n=== day 1 COMPLETE ===")
print("Files Created: EV_Master_Data.csv, Station_Count_StateWise.csv")
print(master.head())
print("\nTotal Records:", len(master))
