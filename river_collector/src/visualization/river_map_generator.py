import folium
import json
from abc import ABC, abstractmethod
from src.utils.config import Config
from src.utils.logger import logger

class MapGenerator(ABC):
    @abstractmethod
    def generate_map(self, data, bbox):
        pass

class RiverMapGenerator(MapGenerator):
    def generate_map(self, data, bbox):
        south, west, north, east = map(float, bbox.split(','))
        m = folium.Map(location=[(south + north) / 2, (west + east) / 2], zoom_start=10)
        
        for feature in data:
            self._add_feature_to_map(feature, m)
        
        return m
    
    def _add_feature_to_map(self, feature, m):
        if feature['type'] == 'way':
            self._add_way_to_map(feature, m)
        elif feature['type'] == 'relation':
            self._add_relation_to_map(feature, m)
    
    def _add_way_to_map(self, feature, m):
        coords = [(node['lat'], node['lon']) for node in feature['geometry']]
        self._create_polyline(coords, feature['tags'].get('name', 'Unnamed river'), m)
    
    def _add_relation_to_map(self, feature, m):
        for member in feature['geometry']:
            if member['type'] == 'way':
                coords = [(node['lat'], node['lon']) for node in member['geometry']]
                self._create_polyline(coords, feature['tags'].get('name', 'Unnamed river'), m)
    
    def _create_polyline(self, coords, name, m):
        folium.PolyLine(coords, color="blue", weight=2, opacity=0.8, tooltip=name).add_to(m)

class MapVisualizationService:
    def __init__(self, map_generator: MapGenerator):
        self.map_generator = map_generator
    
    def create_visualization(self, data_file, bbox):
        try:
            data = self._load_data(data_file)
            map_obj = self.map_generator.generate_map(data, bbox)
            self._save_map(map_obj)
        except Exception as e:
            logger.error(f"An error occurred while creating map visualization: {e}")
            raise
    
    def _load_data(self, data_file):
        with open(data_file, 'r') as f:
            return json.load(f)
    
    def _save_map(self, map_obj):
        map_obj.save(f"{Config.OUTPUT_DIR}/map.html")
