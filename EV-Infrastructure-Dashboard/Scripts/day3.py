import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("=== DAY 3: ANALYSIS & VISUALIZATION START ===")

# 1. Data Load Karo
forecast = pd.read_csv('EV_Forecast_2026.csv')
stations = pd.read_csv('Station_Count_StateWise.csv')
forecast['Date'] = pd.to_datetime(forecast['Date'])

# 2. Future EV_per_Station Nikalo
future_df = forecast[forecast['Date'] >= '2025-01-01'].copy()
future_df = pd.merge(future_df, stations, on='State', how='left')
future_df['Current_Stations'] = future_df['Current_Stations'].fillna(1)
future_df['EV_per_Station_Future'] = future_df['Predicted_Sales'] / future_df['Current_Stations']

# 3. 2026 Ka Yearly Summary
summary_2026 = future_df[future_df['Date'].dt.year == 2026].groupby('State').agg({
    'Predicted_Sales': 'sum',
    'Current_Stations': 'first',
    'EV_per_Station_Future': 'mean'
}).reset_index()
summary_2026.columns = ['State', 'Total_EV_2026', 'Stations', 'Avg_EV_per_Station']
summary_2026['Stations_Needed'] = (summary_2026['Total_EV_2026'] / 50).round()  # 1 station per 50 EVs
summary_2026['Gap'] = summary_2026['Stations_Needed'] - summary_2026['Stations']
summary_2026 = summary_2026.sort_values('Gap', ascending=False)

summary_2026.to_csv('EV_Gap_Analysis_2026.csv', index=False)
print("\n=== TOP 10 STATES - CHARGING STATION GAP 2026 ===")
print(summary_2026.head(10)[['State', 'Total_EV_2026', 'Stations', 'Stations_Needed', 'Gap']])

# 4. Graph 1: Top 5 States Forecast
plt.figure(figsize=(12, 6))
top5_states = summary_2026.head(5)['State'].tolist()
for state in top5_states:
    state_data = future_df[future_df['State'] == state]
    plt.plot(state_data['Date'], state_data['Predicted_Sales'], label=state, marker='o')
plt.title('Top 5 States - EV Sales Forecast till 2026', fontsize=14, fontweight='bold')
plt.xlabel('Date')
plt.ylabel('Predicted Monthly EV Sales')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('Top5_States_Forecast.png', dpi=300)
print("\nGraph Saved: Top5_States_Forecast.png")

# 5. Graph 2: Gap Analysis Bar Chart
plt.figure(figsize=(12, 6))
top10_gap = summary_2026.head(10)
colors = ['red' if x > 0 else 'green' for x in top10_gap['Gap']]
plt.barh(top10_gap['State'], top10_gap['Gap'], color=colors)
plt.title('Top 10 States - Charging Station Gap by 2026', fontsize=14, fontweight='bold')
plt.xlabel('Additional Stations Needed')
plt.axvline(x=0, color='black', linestyle='--')
plt.tight_layout()
plt.savefig('Station_Gap_Analysis.png', dpi=300)
print("Graph Saved: Station_Gap_Analysis.png")

print("\n=== DAY 3 COMPLETE ===")
print("Files Created: EV_Gap_Analysis_2026.csv, Top5_States_Forecast.png, Station_Gap_Analysis.png")
print("\nProject Complete! 🚀")