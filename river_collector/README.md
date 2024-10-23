# River Data Collector

## Overview

The River Data Collector is a Python-based tool that downloads, processes, and visualizes river data for a specified region using OpenStreetMap (OSM) data. It generates both GIS-compatible data files and an interactive web map.

## Features

- Download river data from OpenStreetMap for a specified region
- Process and clean the raw OSM data
- Generate GIS-compatible data files (GeoPackage format)
- Create an interactive web map using Folium
- Flexible and extensible architecture using abstract base classes

## Project Structure
src/
├── data/
│ ├── data_processor.py
│ └── osm_downloader.py
├── visualization/
│ ├── gis_formatter.py
│ └── river_map_generator.py
├── utils/
│ ├── config.py
│ ├── logger.py
│ └── geocoding.py
└── main.py


## Requirements

- Python 3.7+
- Required Python packages (install via `pip install -r requirements.txt`):
  - requests
  - geopandas
  - python-dotenv
  - folium
  - geopy

## Setup

1. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Configure the project by editing `src/utils/config.py` if needed.

## Usage

Run the main script with the desired region name as an argument:

```
python -m src.main --region "Poland"
```

This will:
1. Download river data for the specified region from OpenStreetMap
2. Process and clean the data
3. Save the processed data as a JSON file
4. Generate a GeoPackage file for GIS applications
5. Create an interactive HTML map

The output files will be saved in the directory specified in `Config.OUTPUT_DIR`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.