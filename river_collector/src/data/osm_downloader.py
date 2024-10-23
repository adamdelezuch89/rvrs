import requests
from src.utils.config import Config
from src.utils.logger import logger

class OSMDownloader:
    def __init__(self):
        self.api_url = Config.OSM_API_URL

    def download_river_data(self, bbox):
        query = f"""
        [out:json];
        (
          way["waterway"="river"]({bbox});
          relation["waterway"="river"]({bbox});
        );
        out geom;
        """
        
        try:
            response = requests.get(self.api_url, params={"data": query})
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Error downloading river data: {e}")
            raise
