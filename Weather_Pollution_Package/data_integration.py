# Weather_Pollution_Package/data_integration.py

import pandas as pd

def integrate_datasets(df_weather: pd.DataFrame, df_pollutant: pd.DataFrame) -> pd.DataFrame:
    """
    Integrates weather and pollutant datasets based on Date.
    
    Parameters:
        df_weather (pd.DataFrame): Cleaned weather data.
        df_pollutant (pd.DataFrame): Cleaned pollutant data.
        
    Returns:
        pd.DataFrame: Integrated dataset.
    """
    df_weather['Date'] = pd.to_datetime(df_weather['Date'], errors='coerce')
    df_pollutant['date_local'] = pd.to_datetime(df_pollutant['date_local'], errors='coerce')
    
    df_combined = pd.merge(df_pollutant, df_weather, left_on='date_local', right_on='Date', how='inner')
    
    df_combined.drop(columns=['Date'], inplace=True)
    print("Datasets integrated.")
    return df_combined