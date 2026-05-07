# Weather_Pollution_Package/data_processing.py

import pandas as pd

def clean_weather_data(df: pd.DataFrame, station_name: str = "Oak Street Weather Station") -> pd.DataFrame:
    """
    Cleans and preprocesses the weather data for the specified station.
    
    Parameters:
        df (pd.DataFrame): Raw weather data.
        station_name (str): Name of the weather station to focus on.
        
    Returns:
        pd.DataFrame: Cleaned and processed weather data.
    """
    df['air_temperature'] = pd.to_numeric(df['air_temperature'], errors='coerce')
    df['humidity'] = pd.to_numeric(df['humidity'], errors='coerce')
    df['wind_speed'] = pd.to_numeric(df['wind_speed'], errors='coerce')
    df['measurement_timestamp'] = pd.to_datetime(df['measurement_timestamp'], errors='coerce')
    df['Date'] = pd.to_datetime(df['measurement_timestamp']).dt.date
    
    df = df[df['station_name'] == station_name]
    
    df.dropna(subset=['air_temperature', 'humidity', 'wind_speed'], inplace=True)
    
    df = df.groupby(['Date', 'station_name']).mean(numeric_only=True).reset_index()
    print(f"Weather data cleaned for {station_name}.")
    return df

def clean_pollutant_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and preprocesses the pollutant data.
    
    Parameters:
        df (pd.DataFrame): Raw pollutant data.
        
    Returns:
        pd.DataFrame: Cleaned and processed pollutant data.
    """
    columns_to_drop = [
        'state_code', 'county_code', 'site_number', 'parameter_code', 'poc', 
        'latitude', 'longitude', 'datum', 'parameter', 'sample_duration_code',
        'method_code', 'method', 'local_site_name', 'site_address', 
        'state', 'county', 'city', 'cbsa_code', 'cbsa', 'sample_duration', 'pollutant_standard',
        'units_of_measure', 'event_type', 'observation_count', 'observation_percent', 
        'validity_indicator', 'date_of_last_change'
    ]
    
    df = df.drop(columns=columns_to_drop, errors='ignore')
    df['date_local'] = pd.to_datetime(df['date_local'], errors='coerce')
    
    df.dropna(subset=['date_local', 'arithmetic_mean'], inplace=True)
    
    df['arithmetic_mean'] = pd.to_numeric(df['arithmetic_mean'], errors='coerce')
    
    df = df.drop_duplicates()
    print("Pollutant data cleaned.")
    return df