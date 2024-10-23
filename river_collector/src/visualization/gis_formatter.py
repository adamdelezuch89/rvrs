import geopandas as gpd
from shapely.geometry import LineString
from src.utils.logger import logger
from src.utils.config import Config

class GISFormatter:
    def format_for_gis(self, processed_data):
        gdf_data = []
        
        for feature in processed_data:
            if feature['type'] == 'way':
                geometry = LineString([(node['lon'], node['lat']) for node in feature['geometry']])
                gdf_data.append({
                    'osm_id': feature['osm_id'],
                    'name': feature['tags'].get('name'),
                    'waterway': feature['tags'].get('waterway'),
                    'geometry': geometry
                })
        
        gdf = gpd.GeoDataFrame(gdf_data, crs="EPSG:4326")
        return gdf

    def save_gis_data(self, gdf, output_path):
        gdf.to_file(output_path, driver="GPKG")
        logger.info(f"GIS data saved to {output_path}")
