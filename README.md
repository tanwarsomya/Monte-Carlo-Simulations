# Monte Carlo Stock Price Simulator

A Python script that simulates future stock price paths using Monte Carlo methods and Geometric Brownian Motion (GBM). Demonstrated with Microsoft (MSFT), but works with any ticker supported by Yahoo Finance.

## Example Output

Running 1,000 simulations of MSFT over 252 trading days produces:

- **Simulated price paths** — a fan chart showing the range of possible trajectories
- **Final price distribution** — a histogram of where the stock lands after one year, with the mean and starting price highlighted

## How It Works

The simulation uses **Geometric Brownian Motion**, the standard model for stock price dynamics:

```
S(t) = S(t-1) × exp((μ - σ²/2) + σ × Z)
```

Where:
- `μ` — mean daily log return (drift), estimated from 2 years of historical data
- `σ` — daily volatility (standard deviation of log returns)
- `Z` — random draw from a standard normal distribution

Each of the 1,000 simulations independently evolves the price day-by-day for one trading year (252 days).

## Requirements

```
numpy
pandas
yfinance
matplotlib
```

Install dependencies with:

```bash
pip install numpy pandas yfinance matplotlib
```

## Usage

```bash
python MSFT.py
```

To simulate a different stock, change the ticker at the top of the file:

```python
TICKER = "AAPL"   # or "GOOGL", "TSLA", etc.
```

You can also adjust the simulation parameters:

```python
N_SIMULATIONS = 1000   # number of simulated paths
T_DAYS = 252           # forecast horizon in trading days (~1 year)
```

## Output Metrics

The script prints a summary to the console:

| Metric | Description |
|--------|-------------|
| Latest close | Most recent closing price used as the starting point |
| Annual drift | Annualised mean log return from historical data |
| Annual volatility | Annualised standard deviation of log returns |
| Mean final price | Average simulated price after `T_DAYS` |
| 5th percentile | Pessimistic outcome — 95% of paths finish above this |
| 95th percentile | Optimistic outcome — 95% of paths finish below this |

## Disclaimer

This tool is for educational and research purposes only. Monte Carlo simulations based on historical returns are not a reliable predictor of future prices and should not be used as financial advice.
