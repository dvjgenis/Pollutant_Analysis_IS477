# Weather_Pollution_Package/visualization.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_weather_trends(df: pd.DataFrame, output_path: str):
    """
    Plots weather variables over time and saves the plots as images.
    
    Parameters:
        df (pd.DataFrame): Cleaned weather data.
        output_path (str): Directory path to save the plots.
    """
    os.makedirs(output_path, exist_ok=True)
    
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Date', y='air_temperature', data=df, label='Air Temperature')
    plt.xlabel("Date")
    plt.ylabel("Air Temperature (°C)")
    plt.title("Air Temperature Over Time")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'air_temperature_trend.png'))
    plt.close()
    
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Date', y='humidity', data=df, label='Humidity', color='green')
    plt.xlabel("Date")
    plt.ylabel("Humidity (%)")
    plt.title("Humidity Over Time")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'humidity_trend.png'))
    plt.close()
    
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Date', y='wind_speed', data=df, label='Wind Speed', color='orange')
    plt.xlabel("Date")
    plt.ylabel("Wind Speed (m/s)")
    plt.title("Wind Speed Over Time")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'wind_speed_trend.png'))
    plt.close()

def plot_pollutant_trends(df: pd.DataFrame, output_path: str):
    """
    Plots pollutant trends over time and saves the plots as images.
    
    Parameters:
        df (pd.DataFrame): Cleaned pollutant data.
        output_path (str): Directory path to save the plots.
    """
    os.makedirs(output_path, exist_ok=True)
    
    plt.figure(figsize=(14, 6))
    sns.lineplot(x='date_local', y='arithmetic_mean', data=df, label='Arithmetic Mean')
    plt.xlabel("Date")
    plt.ylabel("Arithmetic Mean (ppb)")
    plt.title("Daily Average NO₂ Concentration Over Time")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'arithmetic_mean_trend.png'))
    plt.close()
    
    plt.figure(figsize=(14, 6))
    sns.lineplot(x='date_local', y='aqi', data=df, label='AQI', color='red')
    plt.xlabel("Date")
    plt.ylabel("AQI")
    plt.title("AQI Over Time")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'aqi_trend.png'))
    plt.close()

def plot_combined_data(df: pd.DataFrame, output_path: str):
    """
    Plots NO₂ measures and weather factors and saves the plots as images.
    
    Parameters:
        df (pd.DataFrame): Integrated dataset.
        output_path (str): Directory path to save the plots.
    """
    os.makedirs(output_path, exist_ok=True)
    
    plt.figure(figsize=(14, 6))
    sns.lineplot(x='date_local', y='arithmetic_mean', data=df, label='NO₂ Arithmetic Mean')
    sns.lineplot(x='date_local', y='aqi', data=df, label='AQI', linestyle='--')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title('NO₂ Measures Over Time')
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'no2_measures_over_time.png'))
    plt.close()
    
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='air_temperature', y='arithmetic_mean', data=df, alpha=0.5)
    plt.xlabel('Air Temperature (°C)')
    plt.ylabel('NO₂ Arithmetic Mean (ppb)')
    plt.title('NO₂ Levels vs Air Temperature')
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'no2_vs_air_temperature.png'))
    plt.close()
    
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='humidity', y='arithmetic_mean', data=df, alpha=0.5, color='green')
    plt.xlabel('Humidity (%)')
    plt.ylabel('NO₂ Arithmetic Mean (ppb)')
    plt.title('NO₂ Levels vs Humidity')
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'no2_vs_humidity.png'))
    plt.close()
    
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='wind_speed', y='arithmetic_mean', data=df, alpha=0.5, color='orange')
    plt.xlabel('Wind Speed (m/s)')
    plt.ylabel('NO₂ Arithmetic Mean (ppb)')
    plt.title('NO₂ Levels vs Wind Speed')
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'no2_vs_wind_speed.png'))
    plt.close()

def plot_additional_pollutant_trends(df: pd.DataFrame, output_path: str):
    """
    Plots additional pollutant trends and saves the plots as images.
    
    Parameters:
        df (pd.DataFrame): Pollutant data.
        output_path (str): Directory path to save the plots.
    """
    os.makedirs(output_path, exist_ok=True)
    
    plt.figure(figsize=(14, 6))
    sns.lineplot(x='date_local', y='arithmetic_mean', data=df, label="Daily Average Concentration")
    plt.xlabel("Date")
    plt.ylabel("Arithmetic Mean (ppb)")
    plt.title("Time Series of Daily Average Concentration")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'time_series_daily_average_concentration.png'))
    plt.close()
    
    plt.figure(figsize=(14, 6))
    sns.lineplot(x='date_local', y='aqi', data=df, label="AQI", color='orange')
    plt.xlabel("Date")
    plt.ylabel("AQI")
    plt.title("Time Series of AQI")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'time_series_aqi.png'))
    plt.close()
    
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='first_max_hour', y='first_max_value', data=df, alpha=0.5)
    plt.xlabel("Hour of Day")
    plt.ylabel("First Max Value (ppb)")
    plt.title("Daily Maximum Pollutant Concentration by Hour")
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'daily_max_concentration_by_hour.png'))
    plt.close()
    
    plt.figure(figsize=(10, 6))
    sns.histplot(df['aqi'], bins=20, kde=False, edgecolor='black')
    plt.xlabel("AQI")
    plt.ylabel("Frequency")
    plt.title("Distribution of AQI")
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'distribution_aqi.png'))
    plt.close()

def plot_no2_combined_trends(df: pd.DataFrame, output_path: str):
    """
    Plots combined NO₂ measures over time and saves the plot as an image.
    
    Parameters:
        df (pd.DataFrame): Pollutant data.
        output_path (str): Directory path to save the plot.
    """
    os.makedirs(output_path, exist_ok=True)
    
    plt.figure(figsize=(14, 6))
    sns.lineplot(x='date_local', y='arithmetic_mean', data=df, label='Arithmetic Mean', linestyle='-')
    sns.lineplot(x='date_local', y='first_max_value', data=df, label='First Max Value', linestyle='--')
    sns.lineplot(x='date_local', y='aqi', data=df, label='AQI', linestyle=':')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title('NO₂ Measures Over Time')
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'no2_combined_trends.png'))
    plt.close()

def plot_no2_distributions(df: pd.DataFrame, output_path: str):
    """
    Plots the distribution of NO₂ measures and saves the plot as an image.
    
    Parameters:
        df (pd.DataFrame): Pollutant data.
        output_path (str): Directory path to save the plot.
    """
    os.makedirs(output_path, exist_ok=True)
    
    plt.figure(figsize=(14, 6))
    sns.histplot(df['arithmetic_mean'], bins=20, kde=False, color='blue', label='Arithmetic Mean', alpha=0.5, edgecolor='black')
    sns.histplot(df['first_max_value'], bins=20, kde=False, color='green', label='First Max Value', alpha=0.5, edgecolor='black')
    sns.histplot(df['aqi'], bins=20, kde=False, color='orange', label='AQI', alpha=0.5, edgecolor='black')
    plt.xlabel('Value (ppb / AQI)')
    plt.ylabel('Frequency')
    plt.title('Distribution of NO₂ Measures')
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'distribution_no2_measures.png'))
    plt.close()