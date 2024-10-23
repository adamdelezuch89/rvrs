import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    BASE_DIR = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )
    OUTPUT_DIR = os.path.join(BASE_DIR, "output")
    OSM_API_URL = "https://overpass-api.de/api/interpreter"
    DEBUG = True

    @staticmethod
    def ensure_output_dir(directory=None):
        if directory is None:
            directory = Config.OUTPUT_DIR
        os.makedirs(directory, exist_ok=True)
