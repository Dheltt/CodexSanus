import logging
import os

LOG_DIR = "logs"
LOG_FILE = "agent.log"

# Aseguramos que exista el directorio de logs
os.makedirs(LOG_DIR, exist_ok=True)

# Configuración básica del logger
logging.basicConfig(
    filename=os.path.join(LOG_DIR, LOG_FILE),
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    encoding='utf-8'
)

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)
