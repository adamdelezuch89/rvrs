import json
from src.utils.config import Config
from src.utils.logger import logger

class DataProcessor:
    def process_river_data(self, raw_data):
        processed_data = []
        
        for element in raw_data.get('elements', []):
            if element['type'] in ['way', 'relation']:
                processed_element = {
                    'osm_id': element['id'],
                    'type': element['type'],
                    'tags': element.get('tags', {}),
                    'geometry': self._extract_geometry(element)
                }
                processed_data.append(processed_element)
        
        return processed_data

    def _extract_geometry(self, element):
        if element['type'] == 'way':
            return [node for node in element.get('geometry', [])]
        elif element['type'] == 'relation':
            return [member for member in element.get('members', []) if member['type'] == 'way']

    def save_processed_data(self, data, output_path):
        with open(output_path, 'w') as f:
            json.dump(data, f, indent=2)
        logger.info(f"Processed data saved to {output_path}")
