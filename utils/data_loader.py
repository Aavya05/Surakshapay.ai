import pandas as pd
import numpy as np

def generate_mock_data():
    return pd.DataFrame({
        "amount": np.random.randint(100, 10000, 100),
        "is_fraud": np.random.randint(0, 2, 100)
    })
