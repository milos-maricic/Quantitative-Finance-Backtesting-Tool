# Quantitative Finance Backtesting Tool

This tool backtests a moving average crossover strategy using historical stock data. It generates buy/sell signals based on short and long moving averages, calculates portfolio performance, and provides visualizations of the strategy's returns.

## Features
- Simple moving average crossover strategy.
- Customizable short and long moving averages.
- Portfolio performance metrics (returns, cumulative returns).
- Visualization of price, moving averages, and buy/sell signals.

## How It Works
1. **Input Data**: The tool uses a CSV file or simulated data containing the stock's `Close` prices.
2. **Moving Average Crossover**: The strategy generates a buy signal when the short-term moving average crosses above the long-term moving average, and a sell signal when it crosses below.
3. **Portfolio Performance**: It simulates portfolio performance using initial capital and displays metrics such as returns and cumulative returns.

## Example Usage
You can load your own data or use the example in the code:

```python
# Example of running the tool with simulated data
dates = pd.date_range('2023-01-01', periods=100)
price_data = pd.DataFrame(index=dates)
price_data['Close'] = np.random.randn(100).cumsum() + 100

signals = moving_average_strategy(price_data)
portfolio = backtest_strategy(signals)

plot_performance(portfolio, signals)
```

## How to Use
1. Clone or download the repository.
2. Prepare your stock price data in a CSV file or use the example data.
3. Run the Python script:
   ```bash
   python backtesting_tool.py
   ```
4. Customize the short and long moving average windows:
   ```python
   signals = moving_average_strategy(price_data, short_window=50, long_window=150)
   ```

## Requirements
- Python 3.x
- Libraries: `pandas`, `matplotlib`, `numpy`

To install dependencies, run:
```bash
pip install pandas matplotlib numpy
```

## License
This project is licensed under the [MIT License](LICENSE).

## Contributing
Feel free to submit issues or pull requests for improvements or suggestions!
