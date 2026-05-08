import pandas as pd

def clean_claims_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(subset=["claim_id"])
    df["amount"] = df["amount"].fillna(0)
    return df

