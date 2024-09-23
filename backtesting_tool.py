
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Function to implement a simple moving average crossover strategy
def moving_average_strategy(data, short_window=40, long_window=100):
    """
    Backtest a moving average crossover strategy.
    :param data: DataFrame containing 'Close' prices.
    :param short_window: Window for short moving average.
    :param long_window: Window for long moving average.
    :return: DataFrame with trading signals and portfolio value.
    """
    signals = pd.DataFrame(index=data.index)
    signals['price'] = data['Close']

    # Create short and long moving averages
    signals['short_mavg'] = data['Close'].rolling(window=short_window, min_periods=1).mean()
    signals['long_mavg'] = data['Close'].rolling(window=long_window, min_periods=1).mean()

    # Create trading signals (1 for buy, 0 for sell)
    signals['signal'] = 0.0
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0, 0.0)

    # Calculate positions
    signals['positions'] = signals['signal'].diff()

    return signals

# Function to backtest the strategy and calculate portfolio performance
def backtest_strategy(data, initial_capital=100000.0, shares=1000):
    """
    Backtest the trading strategy and calculate portfolio performance.
    :param data: DataFrame containing signals and price data.
    :param initial_capital: Starting portfolio value.
    :param shares: Number of shares to trade.
    :return: Portfolio performance metrics and value over time.
    """
    # Create a DataFrame to store portfolio values
    portfolio = pd.DataFrame(index=data.index)
    portfolio['positions'] = shares * data['signal'] * data['price']
    portfolio['cash'] = initial_capital - (data['positions'] * data['price']).cumsum()
    portfolio['total'] = portfolio['positions'] + portfolio['cash']

    # Calculate portfolio returns
    portfolio['returns'] = portfolio['total'].pct_change()
    portfolio['cumulative_returns'] = (1 + portfolio['returns']).cumprod()

    return portfolio

# Function to plot portfolio performance
def plot_performance(portfolio, signals):
    """
    Plot the strategy's performance over time.
    :param portfolio: DataFrame containing portfolio values.
    :param signals: DataFrame containing buy/sell signals.
    """
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot closing price and moving averages
    ax.plot(signals['price'], label='Price', alpha=0.3)
    ax.plot(signals['short_mavg'], label='Short Moving Average', alpha=0.9)
    ax.plot(signals['long_mavg'], label='Long Moving Average', alpha=0.9)

    # Plot buy signals
    ax.plot(signals.loc[signals.positions == 1.0].index, 
            signals.short_mavg[signals.positions == 1.0], 
            '^', markersize=10, color='g', lw=0, label='Buy')

    # Plot sell signals
    ax.plot(signals.loc[signals.positions == -1.0].index, 
            signals.short_mavg[signals.positions == -1.0], 
            'v', markersize=10, color='r', lw=0, label='Sell')

    ax.set_title('Moving Average Strategy Backtest')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend()

    plt.show()

# Example data (simulated price data for testing)
dates = pd.date_range('2023-01-01', periods=100)
price_data = pd.DataFrame(index=dates)
price_data['Close'] = np.random.randn(100).cumsum() + 100

# Run the backtest
signals = moving_average_strategy(price_data)
portfolio = backtest_strategy(signals)

# Plot the results
plot_performance(portfolio, signals)
