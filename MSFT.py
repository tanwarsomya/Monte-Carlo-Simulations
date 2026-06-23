import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


TICKER = "MSFT"
N_SIMULATIONS = 1000
T_DAYS = 252

# Fetching Data
ticker = yf.Ticker(TICKER)
hist = ticker.history(period="2y")
close_prices = hist["Close"].dropna()
current_price = float(close_prices.iloc[-1])
print(f"Latest Close: ${current_price:.2f}")
print(f"Trading days loaded: {len(close_prices)}")

# Computing and Calculations
log_returns = np.log(close_prices / close_prices.shift(1))  # Daily change in log
mu = log_returns.mean()     # Mean
sigma = log_returns.std()   # Standard Deviation
print(f"MSFT grows by ~ {mu * 252 * 100:.2f}%")
print(f"MSFT has a volatility of ~ {sigma * np.sqrt(252) * 100:.2f}%")
Z = np.random.standard_normal((T_DAYS, N_SIMULATIONS))  
daily_returns = np.exp((mu - sigma**2 /2) + sigma * Z)
price_paths = np.zeros((T_DAYS + 1, N_SIMULATIONS))
price_paths[0] = current_price

for t in range (1, T_DAYS + 1):
    price_paths[t] = price_paths[t - 1] * daily_returns[t - 1]
    
final_prices = price_paths[-1]

print(f"Mean final price: {final_prices.mean():.2f}")
print(f"5th percentile: {np.percentile(final_prices, 5):.2f}")
print(f"95th percentile: {np.percentile(final_prices, 95):.2f}")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Price paths
ax1.plot(price_paths, alpha=0.1, linewidth=0.5)
ax1.axhline(current_price, color="red", linestyle="--", linewidth=1.5, label=f"Start ${current_price:.2f}")
ax1.set_title("Simulated MSFT price paths")
ax1.set_xlabel("Trading days")
ax1.set_ylabel("Price (USD)")
ax1.legend()

# Final price distribution
ax2.hist(final_prices, bins=50, edgecolor="none")
ax2.axvline(current_price, color="red", linestyle="--", linewidth=1.5, label=f"Start ${current_price:.2f}")
ax2.axvline(final_prices.mean(), color="green", linestyle="--", linewidth=1.5, label=f"Mean ${final_prices.mean():.2f}")
ax2.set_title("Distribution of final prices")
ax2.set_xlabel("Final price (USD)")
ax2.set_ylabel("Frequency")
ax2.legend()

plt.tight_layout()
plt.show()
