import argparse
import os
import json
from src.data.osm_downloader import OSMDownloader
from src.data.data_processor import DataProcessor
from src.visualization.gis_formatter import GISFormatter
from src.utils.config import Config
from src.utils.logger import logger
from src.visualization.river_map_generator import (
    MapVisualizationService,
    RiverMapGenerator,
)
from src.utils.geocoding import get_region_bbox


def parse_arguments():
    parser = argparse.ArgumentParser(description="River Mapping Project")
    parser.add_argument(
        "--region", type=str, required=True, help="Name of the region to map"
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    region = args.region
    output_dir = os.path.join(Config.OUTPUT_DIR, region)
    Config.ensure_output_dir(output_dir)

    bbox = get_region_bbox(region)
    if not bbox:
        logger.error(f"Could not process region: {region}")
        return

    downloader = OSMDownloader()
    processor = DataProcessor()
    formatter = GISFormatter()

    processed_data_file = os.path.join(output_dir, "processed_river_data.json")

    try:
        if os.path.exists(processed_data_file):
            logger.info(f"Reading existing data for {region}")
            with open(processed_data_file, 'r') as f:
                processed_data = json.load(f)
        else:
            logger.info(f"Downloading and processing data for {region}")
            raw_data = downloader.download_river_data(bbox)
            processed_data = processor.process_river_data(raw_data)
            processor.save_processed_data(processed_data, processed_data_file)

        gdf = formatter.format_for_gis(processed_data)
        print(f"output_dir: {output_dir}")
        formatter.save_gis_data(gdf, os.path.join(output_dir, "river_data.gpkg"))

        river_map_generator = RiverMapGenerator()
        map_visualization_service = MapVisualizationService(river_map_generator)
        map_visualization_service.create_visualization(processed_data_file, bbox)

        logger.info("River data processing and map creation completed successfully")
    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=Config.DEBUG)


if __name__ == "__main__":
    main()
