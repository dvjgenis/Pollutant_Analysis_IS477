# Snakefile

import os

WEATHER_URL = "https://data.cityofchicago.org/resource/k7hf-8y75.json"

# Get EPA API credentials from environment variables
EPA_EMAIL = os.getenv("EPA_API_EMAIL", "")
EPA_API_KEY = os.getenv("EPA_API_KEY", "")

# Validate API credentials
if not EPA_EMAIL or not EPA_API_KEY:
    raise ValueError(
        "EPA API credentials not found. Please set the following environment variables:\n"
        "  export EPA_API_EMAIL='your_email@example.com'\n"
        "  export EPA_API_KEY='your_api_key'\n"
        "\nTo obtain an API key, register at: https://aqs.epa.gov/aqsweb/documents/data_api.html"
    )

# Build pollutant URLs with environment variables
POLLUTANT_URLS = [
    f"https://aqs.epa.gov/data/api/dailyData/bySite?email={EPA_EMAIL}&key={EPA_API_KEY}&param=42602&bdate=20220101&edate=20221231&state=17&county=031&site=0219",
    f"https://aqs.epa.gov/data/api/dailyData/bySite?email={EPA_EMAIL}&key={EPA_API_KEY}&param=42602&bdate=20230101&edate=20231231&state=17&county=031&site=0219"
]

shell("mkdir -p data output/plots")

final_csv = "output/integrated_weather_pollution_data.csv"

weather_plots = [
    "output/plots/air_temperature_trend.png",
    "output/plots/humidity_trend.png",
    "output/plots/wind_speed_trend.png"
]

pollutant_plots = [
    "output/plots/arithmetic_mean_trend.png",
    "output/plots/aqi_trend.png"
]

combined_data_plots = [
    "output/plots/no2_measures_over_time.png",
    "output/plots/no2_vs_air_temperature.png",
    "output/plots/no2_vs_humidity.png",
    "output/plots/no2_vs_wind_speed.png"
]

additional_plots = [
    "output/plots/time_series_daily_average_concentration.png",
    "output/plots/time_series_aqi.png",
    "output/plots/daily_max_concentration_by_hour.png",
    "output/plots/distribution_aqi.png"
]

no2_combined_plots = [
    "output/plots/no2_combined_trends.png"
]

no2_distribution_plots = [
    "output/plots/distribution_no2_measures.png"
]

all_plots = weather_plots + pollutant_plots + combined_data_plots + additional_plots + no2_combined_plots + no2_distribution_plots

rule all:
    input:
        final_csv,
        all_plots

############################################
# Fetch Data
############################################

rule fetch_weather_data:
    output: "data/weather_data_raw.csv"
    shell:
        "python -c \""
        "import sys; from Weather_Pollution_Package import fetch_weather_data;"
        "import pandas as pd;"
        f"df=fetch_weather_data('{WEATHER_URL}');"
        "df.to_csv('data/weather_data_raw.csv', index=False)\""

rule fetch_pollutant_data:
    output: "data/pollutant_data_raw.csv"
    shell:
        "python -c \""
        "import sys; from Weather_Pollution_Package import fetch_pollutant_data;"
        "import pandas as pd;"
        f"df=fetch_pollutant_data({POLLUTANT_URLS});"
        "df.to_csv('data/pollutant_data_raw.csv', index=False)\""

############################################
# Clean Data
############################################

rule clean_weather_data:
    input: "data/weather_data_raw.csv"
    output: "data/weather_data_clean.csv"
    shell:
        "python -c \""
        "import sys; import pandas as pd;"
        "from Weather_Pollution_Package import clean_weather_data;"
        "df=pd.read_csv('data/weather_data_raw.csv');"
        "df_clean=clean_weather_data(df);"
        "df_clean.to_csv('data/weather_data_clean.csv', index=False)\""

rule clean_pollutant_data:
    input: "data/pollutant_data_raw.csv"
    output: "data/pollutant_data_clean.csv"
    shell:
        "python -c \""
        "import sys; import pandas as pd;"
        "from Weather_Pollution_Package import clean_pollutant_data;"
        "df=pd.read_csv('data/pollutant_data_raw.csv');"
        "df_clean=clean_pollutant_data(df);"
        "df_clean.to_csv('data/pollutant_data_clean.csv', index=False)\""

############################################
# Integrate Data
############################################

rule integrate_datasets:
    input:
        weather="data/weather_data_clean.csv",
        pollutant="data/pollutant_data_clean.csv"
    output: final_csv
    shell:
        "python -c \""
        "import sys; import pandas as pd;"
        "from Weather_Pollution_Package import integrate_datasets;"
        "dfw=pd.read_csv('data/weather_data_clean.csv');"
        "dfp=pd.read_csv('data/pollutant_data_clean.csv');"
        "df_combined=integrate_datasets(dfw, dfp);"
        "df_combined.to_csv('output/integrated_weather_pollution_data.csv', index=False)\""

############################################
# Compute Correlation
############################################

rule compute_correlation:
    input: final_csv
    output: "output/correlation_matrix.csv"
    shell:
        "python -c \""
        "import sys; import pandas as pd;"
        "from Weather_Pollution_Package import compute_correlation;"
        "df=pd.read_csv('output/integrated_weather_pollution_data.csv');"
        "corr=compute_correlation(df);"
        "corr.to_csv('output/correlation_matrix.csv', index=False)\""

############################################
# Plotting
############################################

rule plot_weather_trends:
    input: "data/weather_data_clean.csv"
    output: weather_plots
    shell:
        "python -c \""
        "import sys; import pandas as pd;"
        "from Weather_Pollution_Package import plot_weather_trends;"
        "df=pd.read_csv('data/weather_data_clean.csv');"
        "plot_weather_trends(df, 'output/plots')\""

rule plot_pollutant_trends:
    input: "data/pollutant_data_clean.csv"
    output: pollutant_plots
    shell:
        "python -c \""
        "import sys; import pandas as pd;"
        "from Weather_Pollution_Package import plot_pollutant_trends;"
        "df=pd.read_csv('data/pollutant_data_clean.csv');"
        "plot_pollutant_trends(df, 'output/plots')\""

rule plot_combined_data:
    input: final_csv
    output: combined_data_plots
    shell:
        "python -c \""
        "import sys; import pandas as pd;"
        "from Weather_Pollution_Package import plot_combined_data;"
        "df=pd.read_csv('output/integrated_weather_pollution_data.csv');"
        "plot_combined_data(df, 'output/plots')\""

rule plot_additional_pollutant_trends:
    input: "data/pollutant_data_clean.csv"
    output: additional_plots
    shell:
        "python -c \""
        "import sys; import pandas as pd;"
        "from Weather_Pollution_Package import plot_additional_pollutant_trends;"
        "df=pd.read_csv('data/pollutant_data_clean.csv');"
        "plot_additional_pollutant_trends(df, 'output/plots')\""

rule plot_no2_combined_trends:
    input: "data/pollutant_data_clean.csv"
    output: no2_combined_plots
    shell:
        "python -c \""
        "import sys; import pandas as pd;"
        "from Weather_Pollution_Package import plot_no2_combined_trends;"
        "df=pd.read_csv('data/pollutant_data_clean.csv');"
        "plot_no2_combined_trends(df, 'output/plots')\""

rule plot_no2_distributions:
    input: "data/pollutant_data_clean.csv"
    output: no2_distribution_plots
    shell:
        "python -c \""
        "import sys; import pandas as pd;"
        "from Weather_Pollution_Package import plot_no2_distributions;"
        "df=pd.read_csv('data/pollutant_data_clean.csv');"
        "plot_no2_distributions(df, 'output/plots')\""