# Data Dictionary

This document provides detailed descriptions of all variables in the integrated dataset. Variables are organized by source (Weather Data and Pollutant Data) with clear explanations of their meaning, units, and usage in our analysis.

---

## 📊 Overview

Our integrated dataset combines two sources:

1. **Weather Data**: Hourly measurements from Chicago's beach weather stations, aggregated to daily averages
2. **Pollutant Data**: Daily NO₂ concentration measurements from EPA monitoring sites

**Key Variables Used in Analysis:**
- `air_temperature` - Air temperature in Celsius
- `wind_speed` - Wind speed in meters per second
- `humidity` - Relative humidity percentage
- `arithmetic_mean` - Daily average NO₂ concentration (primary pollutant metric)
- `aqi` - Air Quality Index for NO₂

---

## 1. Weather Data Variables

These variables come from the **City of Chicago Beach Weather Stations Automated Sensors** dataset. The data is collected hourly and aggregated to daily averages for integration with pollutant data.

### Core Variables (Used in Analysis)

| Variable Name | Description | Data Type | Units | Notes |
|--------------|-------------|-----------|-------|-------|
| `station_name` | Name of the weather station | Text | - | In this study: "Oak Street Weather Station" |
| `measurement_timestamp` | Date and time of measurement | Timestamp | YYYY-MM-DD HH:MM:SS | Original hourly timestamp before aggregation |
| `Date` | Date (aggregated from hourly data) | Date | YYYY-MM-DD | Created during data processing for integration |
| `air_temperature` | Air temperature at time of measurement | Number | Celsius (°C) | **Primary variable** - used in correlation analysis |
| `wind_speed` | Wind speed at time of measurement | Number | Meters per second (m/s) | **Primary variable** - used in correlation analysis |
| `humidity` | Relative humidity percentage | Number | Percent (%) | **Primary variable** - used in correlation analysis |

### Additional Weather Variables (Available but Not Used in Main Analysis)

| Variable Name | Description | Data Type | Units | Notes |
|--------------|-------------|-----------|-------|-------|
| `wet_bulb_temperature` | Wet bulb temperature | Number | Celsius (°C) | Alternative temperature measure |
| `rain_intensity` | Rainfall intensity | Number | mm/hour | Current rain rate |
| `interval_rain` | Rain since last measurement | Number | mm | Hourly accumulation |
| `total_rain` | Total rain since midnight | Number | mm | Daily cumulative rainfall |
| `precipitation_type` | Type of precipitation | Integer | Code | 0=None, 60=Liquid, 70=Solid, 40=Unspecified |
| `wind_direction` | Wind direction | Number | Degrees | 0° = North, 90° = East, etc. |
| `maximum_wind_speed` | Maximum wind speed in 2-minute period | Number | m/s | Peak wind gust measurement |
| `barometric_pressure` | Atmospheric pressure | Number | Hectopascals (hPa) | Air pressure at station level |
| `solar_radiation` | Solar radiation intensity | Number | Watts/m² | Solar energy received |
| `heading` | Wind sensor orientation | Number | Degrees | Calibration angle (ideally 0° = True North) |
| `battery_life` | Battery status | NA | NA | Sensor power level (often unavailable) |
| `measurement_timestamp_label` | Human-readable timestamp | Text | - | Formatted date/time string |
| `measurement_id` | Unique measurement identifier | Text | - | Internal tracking ID |

**Why We Focus on Temperature, Wind Speed, and Humidity:**

These three variables were selected because:
- They have the strongest theoretical relationships with pollutant dispersion
- They show measurable correlations with NO₂ levels in preliminary analysis
- They are consistently measured across all time periods
- They represent key meteorological factors affecting air quality

---

## 2. Pollutant Data Variables

These variables come from the **U.S. Environmental Protection Agency (EPA) Air Quality System (AQS)**. The data represents daily NO₂ measurements from monitoring site 0219 in Chicago.

### Core Variables (Used in Analysis)

| Variable Name | Description | Data Type | Units | Notes |
|--------------|-------------|-----------|-------|-------|
| `date_local` | Local date of measurement | Date | YYYY-MM-DD | Used for merging with weather data |
| `arithmetic_mean` | Daily average NO₂ concentration | Number | Parts per billion (ppb) | **Primary pollutant metric** - average of hourly readings |
| `aqi` | Air Quality Index for NO₂ | Integer | Index (0-500) | EPA's standardized air quality rating |
| `first_max_value` | Maximum hourly NO₂ reading | Number | ppb | Highest concentration during the day |
| `first_max_hour` | Hour of maximum reading | Integer | Hour (0-23) | When peak concentration occurred |

### Site and Metadata Variables

| Variable Name | Description | Data Type | Notes |
|--------------|-------------|-----------|-------|
| `state_code` | FIPS state code | Integer | 17 = Illinois |
| `county_code` | FIPS county code | Integer | 031 = Cook County |
| `site_number` | EPA monitoring site ID | Integer | 0219 = Kennedy Near Road 2 |
| `parameter_code` | Pollutant parameter code | Integer | 42602 = NO₂ |
| `parameter` | Full parameter name | Text | "Nitrogen dioxide (NO₂)" |
| `poc` | Parameter Occurrence Code | Integer | Monitoring activity type |
| `local_site_name` | Site name | Text | "Kennedy Near Road 2" |
| `site_address` | Site location address | Text | "Kennedy Expressway West" |
| `latitude` | Site latitude coordinate | Number | Decimal degrees (WGS84) |
| `longitude` | Site longitude coordinate | Number | Decimal degrees (WGS84) |
| `state` | State name | Text | "Illinois" |
| `county` | County name | Text | "Cook" |
| `city` | City name | Text | "Chicago" |

### Measurement Method Variables

| Variable Name | Description | Data Type | Notes |
|--------------|-------------|-----------|-------|
| `method_code` | EPA method identifier | Integer | Measurement technique code |
| `method` | Method description | Text | e.g., "Teledyne Model T500U..." |
| `sample_duration_code` | Sampling duration code | Integer | Length of measurement period |
| `sample_duration` | Duration description | Text | e.g., "1 HOUR" |
| `datum` | Coordinate reference system | Text | e.g., "NAD83" |

### Statistical and Quality Variables

| Variable Name | Description | Data Type | Notes |
|--------------|-------------|-----------|-------|
| `observation_count` | Number of hourly readings | Integer | Used to calculate daily mean |
| `observation_percent` | Percentage of valid readings | Number | Data completeness indicator |
| `units_of_measure` | Unit of measurement | Text | "Parts per billion" |
| `pollutant_standard` | Regulatory standard | Text | EPA threshold for comparison |
| `validity_indicator` | Data quality flag | Text | Validation status |
| `date_of_last_change` | Last record update | Date | Metadata timestamp |
| `cbsa_code` | Metropolitan area code | Integer | Core-Based Statistical Area |
| `cbsa` | Metropolitan area name | Text | "Chicago-Naperville-Elgin, IL-IN-WI" |
| `event_type` | Special event indicator | Text | e.g., "None", "Excluded", "Concurred" |

**Why We Focus on `arithmetic_mean`:**

The `arithmetic_mean` (daily average NO₂ in ppb) is our primary metric because:
- It represents the overall daily exposure level
- It's the most stable and reliable measure for daily comparisons
- It aligns with EPA's standard reporting methods
- It integrates all hourly fluctuations into a single comparable value

**Understanding Air Quality Index (AQI):**

The AQI converts pollutant concentrations into a standardized 0-500 scale:
- **0-50**: Good (Green) - Air quality is satisfactory
- **51-100**: Moderate (Yellow) - Acceptable for most people
- **101-150**: Unhealthy for Sensitive Groups (Orange)
- **151-200**: Unhealthy (Red)
- **201-300**: Very Unhealthy (Purple)
- **301-500**: Hazardous (Maroon)

---

## 3. Integrated Dataset Variables

When weather and pollutant data are merged, the resulting dataset contains:

### Combined Variables

- All weather variables (with `Date` renamed to match `date_local`)
- All pollutant variables
- **Matching Key**: Data is matched on `date_local` = `Date` (after aggregation)

### Data Quality Notes

- **Missing Values**: Some days may have missing weather or pollutant data
- **Time Alignment**: Weather data aggregated from hourly to daily (mean)
- **Spatial Alignment**: Oak Street Weather Station (~4 km from monitoring site 0219)
- **Temporal Coverage**: 2022-2023 (730 potential days, actual may be fewer due to missing data)

### Usage in Analysis

The integrated dataset enables:
- **Correlation Analysis**: Relationships between weather variables and NO₂ levels
- **Time Series Analysis**: Trends over the two-year period
- **Scatter Plots**: Visual examination of relationships
- **Statistical Modeling**: Regression and predictive analysis

---

## 📝 Notes on Data Quality

### Handling Missing Values
- Weather data: Missing hourly readings are excluded from daily averages
- Pollutant data: Days with incomplete hourly measurements may have lower `observation_percent`
- Integration: Only days with both weather and pollutant data are included in final analysis

### Outlier Detection
- Visual inspection of scatter plots reveals unusual values
- Statistical tests (e.g., Z-scores) identify extreme outliers
- Outliers are investigated but typically retained unless clearly erroneous

### Data Integrity
- SHA-256 checksums verify data hasn't been corrupted during processing
- Checksums are calculated after data fetching and at key processing steps
- This ensures reproducibility and data trustworthiness

---

## 🔍 Variable Selection for This Study

### Primary Analysis Variables

**Weather:**
- `air_temperature` - How temperature affects pollutant chemistry
- `wind_speed` - How wind disperses pollutants
- `humidity` - How moisture affects pollutant behavior

**Pollution:**
- `arithmetic_mean` - Primary metric for NO₂ concentration
- `aqi` - Standardized air quality assessment

### Excluded Variables

We excluded many available variables to:
- **Reduce complexity**: Focus on the strongest relationships
- **Avoid redundancy**: Many variables are highly correlated
- **Maintain clarity**: Too many variables can obscure key patterns

**Future studies** could incorporate:
- Precipitation data (may wash out pollutants)
- Barometric pressure (affects atmospheric mixing)
- Solar radiation (drives photochemistry)
- Wind direction (reveals source locations)

---

## 📚 Additional Resources

- **EPA AQS Data Dictionary**: https://aqs.epa.gov/aqsweb/documents/data_mart_welcome.html
- **Chicago Open Data Portal**: https://data.cityofchicago.org/
- **EPA AQI Guide**: https://www.airnow.gov/aqi/aqi-basics/

---

*This data dictionary is part of the Pollutant-Weather Analysis project. For project metadata and citations, see [metadata.json](metadata.json) and [README.md](README.md).*
