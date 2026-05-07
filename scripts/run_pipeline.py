# scripts/run_pipeline.py

import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from Weather_Pollution_Package import (
    fetch_weather_data,
    fetch_pollutant_data,
    clean_weather_data,
    clean_pollutant_data,
    integrate_datasets,
    compute_correlation,
    plot_weather_trends,
    plot_pollutant_trends,
    plot_combined_data,
    plot_additional_pollutant_trends,
    plot_no2_combined_trends,
    plot_no2_distributions
)

def main():
    output_data_dir = "output"
    output_plots_dir = os.path.join(output_data_dir, "plots")
    os.makedirs(output_plots_dir, exist_ok=True)
    
    # Get EPA API credentials from environment variables
    epa_email = os.getenv("EPA_API_EMAIL", "")
    epa_api_key = os.getenv("EPA_API_KEY", "")
    
    if not epa_email or not epa_api_key:
        raise ValueError(
            "EPA API credentials not found. Please set the following environment variables:\n"
            "  export EPA_API_EMAIL='your_email@example.com'\n"
            "  export EPA_API_KEY='your_api_key'\n"
            "\nTo obtain an API key, register at: https://aqs.epa.gov/aqsweb/documents/data_api.html"
        )
    
    weather_url = "https://data.cityofchicago.org/resource/k7hf-8y75.json"
    pollutant_urls = [
        f"https://aqs.epa.gov/data/api/dailyData/bySite?email={epa_email}&key={epa_api_key}&param=42602&bdate=20220101&edate=20221231&state=17&county=031&site=0219",
        f"https://aqs.epa.gov/data/api/dailyData/bySite?email={epa_email}&key={epa_api_key}&param=42602&bdate=20230101&edate=20231231&state=17&county=031&site=0219"
    ]
    
    print("Fetching weather data...")
    df_weather_raw = fetch_weather_data(weather_url)
    print("Fetching pollutant data...")
    df_pollutant_raw = fetch_pollutant_data(pollutant_urls)
    

    print("Cleaning weather data...")
    df_weather_clean = clean_weather_data(df_weather_raw)
    print("Cleaning pollutant data...")
    df_pollutant_clean = clean_pollutant_data(df_pollutant_raw)
    

    print("Integrating datasets...")
    df_combined = integrate_datasets(df_weather_clean, df_pollutant_clean)
    


    print("Computing correlations...")
    correlation_matrix = compute_correlation(df_combined)
    print("Correlation Matrix:")
    print(correlation_matrix)
    

    print("Plotting weather trends...")
    plot_weather_trends(df_weather_clean, output_plots_dir)
    print("Plotting pollutant trends...")
    plot_pollutant_trends(df_pollutant_clean, output_plots_dir)
    print("Plotting combined data visualizations...")
    plot_combined_data(df_combined, output_plots_dir)
    

    print("Plotting additional pollutant trends...")
    plot_additional_pollutant_trends(df_pollutant_clean, output_plots_dir)
    

    print("Plotting combined NO₂ trends...")
    plot_no2_combined_trends(df_pollutant_clean, output_plots_dir)
    

    print("Plotting NO₂ distributions...")
    plot_no2_distributions(df_pollutant_clean, output_plots_dir)
    

    output_csv_path = os.path.join(output_data_dir, "integrated_weather_pollution_data.csv")
    df_combined.to_csv(output_csv_path, index=False)
    print(f"Integrated data saved to '{output_csv_path}'.")
    print(f"All plots have been saved to '{output_plots_dir}/'.")

if __name__ == "__main__":
    main()