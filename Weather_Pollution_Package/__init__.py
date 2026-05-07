# Weather_Pollution_Package/__init__.py

from .data_fetching import fetch_weather_data, fetch_pollutant_data
from .data_processing import clean_weather_data, clean_pollutant_data
from .data_integration import integrate_datasets
from .analysis import compute_correlation
from .visualization import (
    plot_weather_trends,
    plot_pollutant_trends,
    plot_combined_data,
    plot_additional_pollutant_trends,
    plot_no2_combined_trends,
    plot_no2_distributions,
)

__all__ = [
    "fetch_weather_data",
    "fetch_pollutant_data",
    "clean_weather_data",
    "clean_pollutant_data",
    "integrate_datasets",
    "compute_correlation",
    "plot_weather_trends",
    "plot_pollutant_trends",
    "plot_combined_data",
    "plot_additional_pollutant_trends",
    "plot_no2_combined_trends",
    "plot_no2_distributions",
]