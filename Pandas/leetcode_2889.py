import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return pd.pivot(weather, values = 'temperature', index = 'month', columns = ['city'])