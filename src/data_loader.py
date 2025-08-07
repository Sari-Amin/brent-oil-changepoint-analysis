import pandas as pd
import numpy as np

class DataLoader:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.df = None

    def load_data(self):

        try:
            self.df = pd.read_csv(self.filepath)
            self.df.columns = self.df.columns.str.strip()  # Clean header
            self.df['Date'] = pd.to_datetime(self.df['Date'], dayfirst=True)
            self.df = self.df.sort_values('Date').reset_index(drop=True)
            return self.df
        
        except Exception as e :
            print("file not loaded:", e)

    def compute_log_returns(self):
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        self.df['LogReturn'] = (self.df['Price'].apply(lambda x: float(x))).apply(lambda x: np.log(x)).diff()
        return self.df
