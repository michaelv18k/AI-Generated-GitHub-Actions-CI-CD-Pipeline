import pandas as pd
from pipeline.healthcare_etl import clean_claims_data

def test_clean_claims_data_removes_null_claim_id():
    data = {
        "claim_id": [1, None, 3],
        "amount": [100, 200, None],
    }
    df = pd.DataFrame(data)
    result = clean_claims_data(df)

    assert len(result) == 2
    assert result["claim_id"].isnull().sum() == 0

test_clean_claims_data_removes_null_claim_id()