import pandas as pd

class ComplaintLoader:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def load_data(self) -> pd.DataFrame:
        try:
            df = pd.read_csv(self.filepath, low_memory=False)
            print(f"Loaded {len(df):,} rows from {self.filepath}")
            return df
        except Exception as e:
            print(f"Error loading data: {e}")
            return pd.DataFrame()
