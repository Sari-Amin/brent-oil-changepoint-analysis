import matplotlib.pyplot as plt

class OilPriceVisualizer:
    def __init__(self, df):
        self.df = df

    def plot_prices(self):
        plt.figure(figsize=(12, 4))
        plt.plot(self.df['Date'], self.df['Price'], label='Brent Oil Price')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.title('Brent Oil Prices Over Time')
        plt.legend()
        plt.tight_layout()
        plt.show()

    def plot_log_returns(self):
        plt.figure(figsize=(12, 4))
        plt.plot(self.df['Date'], self.df['LogReturn'], color='orange', label='Log Return')
        plt.xlabel('Date')
        plt.ylabel('Log Return')
        plt.title('Log Returns Over Time')
        plt.legend()
        plt.tight_layout()
        plt.show()
