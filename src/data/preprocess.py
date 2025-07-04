import pandas as pd
import re

class ComplaintPreprocessor:
    def __init__(self, allowed_products=None):
        if allowed_products is None:
            allowed_products = [
                "Credit card", "Personal loan", "Buy Now, Pay Later",
                "Savings account", "Money transfers"
            ]
        self.allowed_products = allowed_products

    def clean_text(self, text: str) -> str:
        if not isinstance(text, str):
            return ""
        text = text.lower()
        text = re.sub(r"[^a-z0-9\s]", " ", text)  # remove special characters
        text = re.sub(r"\s+", " ", text)          # collapse multiple spaces
        return text.strip()

    def filter_and_clean(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df[df["Product"].isin(self.allowed_products)]
        df = df.dropna(subset=["Consumer complaint narrative"])
        df["Cleaned Narrative"] = df["Consumer complaint narrative"].apply(self.clean_text)
        return df.reset_index(drop=True)
