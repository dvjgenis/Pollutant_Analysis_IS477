# Weather_Pollution_Package/data_fetching.py

import requests
import pandas as pd
import hashlib
import io

def calculate_checksum(df: pd.DataFrame) -> str:
    """
    Calculates a SHA-256 checksum for the given DataFrame by converting it to a CSV string in memory.
    
    Parameters:
        df (pd.DataFrame): The DataFrame to hash.
    
    Returns:
        str: The SHA-256 checksum in hexadecimal format.
    """
    # Convert DataFrame to CSV in memory
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_data = csv_buffer.getvalue().encode('utf-8')
    
    # Calculate SHA-256 checksum
    sha256_hash = hashlib.sha256(csv_data).hexdigest()
    return sha256_hash


def fetch_weather_data(url: str, batch_size: int = 1000) -> pd.DataFrame:
    """
    Fetches weather data from the API for specific stations and date range.
    
    Parameters:
        url (str): API endpoint to fetch data from.
        batch_size (int): Number of rows to retrieve per request.
        
    Returns:
        pd.DataFrame: Weather data as a pandas DataFrame.
    """
    all_data = []
    station_names = ["Oak Street Weather Station", "Foster Weather Station"]
    for station_name in station_names:
        offset = 0
        while True:
            params = {
                "$limit": batch_size,
                "$offset": offset,
                "station_name": station_name,
                "$where": "measurement_timestamp between '2022-01-01T00:00:00' and '2023-12-31T23:59:59'"
            }
            response = requests.get(url, params=params)
            if response.status_code != 200:
                print(f"Error fetching data for {station_name}. Status code: {response.status_code}")
                break

            data = response.json()
            if not data:
                break

            all_data.extend(data)
            offset += batch_size
            print(f"Fetched {len(data)} rows for {station_name} with offset {offset - batch_size}.")

    df_weather = pd.DataFrame(all_data)
    print(f"Total weather data fetched: {len(df_weather)} rows.")

    # Calculate and print checksum for the weather DataFrame
    weather_checksum = calculate_checksum(df_weather)
    print(f"Weather data SHA-256 checksum: {weather_checksum}")

    return df_weather

def fetch_pollutant_data(urls: list) -> pd.DataFrame:
    """
    Fetches pollutant data from a list of URLs and concatenates them.
    
    Parameters:
        urls (list): List of URLs to fetch pollutant data from.
        
    Returns:
        pd.DataFrame: Pollutant data as a pandas DataFrame.
    """
    frames = []
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            df_pollutant = pd.DataFrame(data["Data"])
            frames.append(df_pollutant)
            print(f"Pollutant data fetched from {url}")
        else:
            print(f"Error fetching pollutant data from {url}. Status code: {response.status_code}")

    if frames:
        df_pollutant = pd.concat(frames, ignore_index=True)
        print(f"Total pollutant data fetched: {len(df_pollutant)} rows.")
        
        # Calculate and print checksum for the pollutant DataFrame
        pollutant_checksum = calculate_checksum(df_pollutant)
        print(f"Pollutant data SHA-256 checksum: {pollutant_checksum}")

        return df_pollutant
    else:
        print("No pollutant data fetched.")
        return pd.DataFrame()