import pandas as pd

# Load historical price data
data = pd.read_csv('historical_data.csv')

# Define the parameters for backtesting
initial_capital = 100000  # Initial capital in your account
position = 0  # Current position (0 = out of market, 1 = long, -1 = short)
strategy_profit = 0  # Total profit from the strategy
trades = []  # List to store trade details

# Define your trading strategy
def trading_strategy(row):
    # Implement your trading strategy logic here
    # Return 1 to enter a long position, -1 to enter a short position, or 0 to stay out of the market
    return 0

# Iterate over the historical data and backtest the strategy
for index, row in data.iterrows():
    # Execute the trading strategy
    signal = trading_strategy(row)

    if signal == 1 and position != 1:  # Enter long position
        if position == -1:  # Exit short position
            trades.append((-1, row['Close']))  # Record the exit trade
        trades.append((1, row['Close']))  # Record the entry trade
        position = 1  # Update the position
    elif signal == -1 and position != -1:  # Enter short position
        if position == 1:  # Exit long position
            trades.append((1, row['Close']))  # Record the exit trade
        trades.append((-1, row['Close']))  # Record the entry trade
        position = -1  # Update the position

    if position == 1 and signal == 0:  # Exit long position
        trades.append((1, row['Close']))  # Record the exit trade
        position = 0  # Update the position
    elif position == -1 and signal == 0:  # Exit short position
        trades.append((-1, row['Close']))  # Record the exit trade
        position = 0  # Update the position

# Calculate the final capital and strategy profit
final_capital = initial_capital
for trade in trades:
    trade_type, trade_price = trade
    if trade_type == 1:  # Long trade
        final_capital *= (trade_price / trades[0][1])
    elif trade_type == -1:  # Short trade
        final_capital *= (trades[0][1] / trade_price)
    strategy_profit = final_capital - initial_capital

# Print the results
print(f"Initial Capital: {initial_capital}")
print(f"Final Capital: {final_capital}")
print(f"Strategy Profit: {strategy_profit}")

