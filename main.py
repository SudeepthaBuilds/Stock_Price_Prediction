#Stock Price Prediction
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Download stock data
stock = input("Enter Stock Symbol (e.g., AAPL, TSLA): ")

df = yf.download(stock, start="2020-01-01", end="2025-01-01")

# Keep important columns
df = df[['Open', 'High', 'Low', 'Volume', 'Close']]

# Create target column (next day's closing price)
df['Target'] = df['Close'].shift(-1)

# Remove last row with NaN target
df.dropna(inplace=True)

# Features and target
X = df[['Open', 'High', 'Low', 'Volume']]
y = df['Target']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
mae = mean_absolute_error(y_test, predictions)
print(f"\nMean Absolute Error: {mae:.2f}")

# Predict next day price
latest_data = X.iloc[-1:].values
next_day_price = model.predict(latest_data)

print(f"\nPredicted Next Day Closing Price: {next_day_price[0]:.2f}")

# Plot
plt.figure(figsize=(10, 5))
plt.plot(y_test.values[:100], label="Actual Price")
plt.plot(predictions[:100], label="Predicted Price")
plt.title(f"{stock} Stock Price Prediction")
plt.xlabel("Days")
plt.ylabel("Price")
plt.legend()
plt.show()