import logging

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s | %(levelname)-8s | %(name)s | %(thread)d | %(filename)s:%(lineno)d | %(message)s'
    )
    return logging.getLogger(__name__)

logger = setup_logger()
