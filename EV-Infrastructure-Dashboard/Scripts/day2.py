import pandas as pd
from prophet import Prophet
import warnings

warnings.filterwarnings('ignore')

print("=== DAY 2: PROPHET FORECASTING START ===")

# 1.  LOAD DATA
df = pd.read_csv('../EV_Master_Data.csv')
df['Date'] = pd.to_datetime(df['Date'])
print(f"Total States: {df['State'].nunique()}")
print(f"Data Range: {df['Date'].min().date()} to {df['Date'].max().date()}")

# 2.  FORECAST FOR EACH STATE
all_forecasts = []
states = df['State'].unique()

for i, state in enumerate(states):
    print(f"\n[{i + 1}/{len(states)}] Forecasting for {state}...")

    state_df = df[df['State'] == state][['Date', 'Total_EV_Sales']].copy()
    state_df.columns = ['ds', 'y']

    if len(state_df) < 12:
        print(f"   Skipping {state} - Only {len(state_df)} months data")
        continue

    state_df['floor'] = 0  # ← FIX 1: Negative nahi jayega

    model = Prophet(yearly_seasonality=True,
                    weekly_seasonality=False,
                    daily_seasonality=False)
    model.fit(state_df)

    future = model.make_future_dataframe(periods=36, freq='MS')
    future['floor'] = 0  # ← FIX 2: Future me bhi floor
    future = future[future['ds'] <= '2026-12-01']

    forecast = model.predict(future)

    forecast_df = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].copy()  # yhat add kiya
    forecast_df['State'] = state
    forecast_df['Actual'] = state_df.set_index('ds').reindex(forecast_df['ds'])['y'].values
    all_forecasts.append(forecast_df)

    print(f"   Done. Forecast till {forecast_df['ds'].max().date()}")

# 3.  COMBINE ALL FORECASTS
final_forecast = pd.concat(all_forecasts, ignore_index=True)
final_forecast.rename(columns={
    'ds': 'Date',
    'yhat': 'Predicted_Sales',
    'yhat_lower': 'Lower_Bound',
    'yhat_upper': 'Upper_Bound'
}, inplace=True)

# 4. SAVE OUTPUT - FIX 3: Clip Negative Values
final_forecast['Lower_Bound'] = final_forecast['Lower_Bound'].clip(lower=0)
final_forecast['Upper_Bound'] = final_forecast['Upper_Bound'].clip(lower=0)
final_forecast['Predicted_Sales'] = final_forecast['Predicted_Sales'].clip(lower=0)

final_forecast.to_csv('EV_Forecast_2026.csv', index=False)

print("\n=== DAY 2 COMPLETE ===")
print("File Created: EV_Forecast_2026.csv")
print(f"Total Forecast Rows: {len(final_forecast)}")
print(f"States Forecasted: {final_forecast['State'].nunique()}")
print("\nSample Forecast:")
print(final_forecast[final_forecast['Date'] > '2025-01-01'].head())