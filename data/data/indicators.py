import numpy as np
import pandas as pd

TRADING_DAYS = 252

def returns(close: pd.Series) -> pd.Series:
    return close.pct_change().replace([np.inf, -np.inf], np.nan)

def cagr(close: pd.Series, periods_per_year: int = TRADING_DAYS) -> float:
    c = close.dropna()
    if len(c) < 2:
        return np.nan
    total = c.iloc[-1] / c.iloc[0]
    years = (len(c) - 
