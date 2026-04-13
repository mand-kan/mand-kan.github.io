import pandas_datareader as pdr
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

OUTPUT_DIR = "."

# Step 1: Download EUR/USD data using pandas_datareader (FRED)
data = pdr.get_data_fred("DEXUSEU", start="2020-01-01")
if data.empty:
    raise ValueError("No data received from FRED")
df = data.reset_index()
df.columns = ['ds', 'y']
df['ds'] = pd.to_datetime(df['ds'])
df = df.dropna()

# Step 2: Initialize and train the Prophet model
model = Prophet(daily_seasonality=True, yearly_seasonality=True)
model.fit(df)

# Step 3: Create a future dataframe for the next 6 months (180 days)
future = model.make_future_dataframe(periods=180)
forecast = model.predict(future)

# Step 4: Create the Matplotlib Visualization
plt.style.use('seaborn-whitegrid')
fig, ax = plt.subplots(figsize=(12, 6))

historical = forecast[forecast['ds'] <= df['ds'].max()]
forecast_future = forecast[forecast['ds'] > df['ds'].max()]

ax.plot(df['ds'], df['y'], color='#636e72', linewidth=1.5, label='Historical Rate')
ax.plot(forecast_future['ds'], forecast_future['yhat'], color='#8b0000', 
        linewidth=2, linestyle='--', label='6-Month Prediction')
ax.fill_between(forecast_future['ds'], forecast_future['yhat_lower'], 
                forecast_future['yhat_upper'], color='#8b0000', alpha=0.1, 
                label='Confidence Interval')

ax.set_title('EUR/USD Exchange Rate Forecast', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Exchange Rate', fontsize=12)
ax.legend(loc='upper left')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=6))
plt.xticks(rotation=45)

plt.savefig(f"{OUTPUT_DIR}/currency_plot.png", format='png', dpi=150, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.close()

print("Successfully created currency_plot.png")
