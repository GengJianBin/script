import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log(message):
    logger.info(f"{message}")  # 默认会包含时间戳和行号
