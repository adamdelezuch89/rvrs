from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable
from src.utils.logger import logger


def get_region_bbox(region_name):
    geolocator = Nominatim(user_agent="river_mapping_project")
    try:
        location = geolocator.geocode(
            region_name, exactly_one=True
        )
        if location:
            return f"{location.raw['boundingbox'][0]},{location.raw['boundingbox'][2]},{location.raw['boundingbox'][1]},{location.raw['boundingbox'][3]}"
        else:
            logger.error(f"Could not find bounding box for {region_name}")
            return None
    except (GeocoderTimedOut, GeocoderUnavailable) as e:
        logger.error(f"Geocoding error: {e}")
        return None
