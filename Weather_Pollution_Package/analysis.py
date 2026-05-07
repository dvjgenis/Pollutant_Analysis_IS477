# Weather_Pollution_Package/analysis.py

import pandas as pd

def compute_correlation(df: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the correlation matrix for weather factors and NO₂ levels.
    
    Parameters:
        df (pd.DataFrame): Integrated dataset.
        
    Returns:
        pd.DataFrame: Correlation matrix.
    """
    variables = ['arithmetic_mean', 'air_temperature', 'humidity', 'wind_speed']
    correlation_matrix = df[variables].corr()
    print("Correlation matrix computed.")
    return correlation_matrix