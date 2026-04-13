# EUR/USD Exchange Rate Forecast

Time series forecasting project using Meta's Prophet model to predict EUR/USD exchange rates for the next 6 months.

## Overview

This project fetches historical EUR/USD exchange rate data and uses Facebook Prophet to generate a 6-month forecast with confidence intervals.

## Features

- **Data Source**: Federal Reserve Economic Data (FRED) via pandas_datareader
- **Model**: Prophet (additive regression model)
- **Visualization**: Matplotlib with historical data and forecast
- **Output**: PNG chart with confidence intervals

## Requirements

```bash
pip install -r requirements.txt
```

## Usage

```bash
python currency_plot.py
```

This will generate `currency_plot.png` in the current directory.

## Output

The generated chart shows:
- **Gray line**: Historical EUR/USD exchange rates (5 years)
- **Red dashed line**: 6-month forecast
- **Shaded area**: 95% confidence interval

## Tech Stack

- Python 3.7+
- [pandas-datareader](https://github.com/pydata/pandas-datareader) - Data ingestion
- [Prophet](https://facebook.github.io/prophet/) - Time series forecasting
- [Matplotlib](https://matplotlib.org/) - Visualization
