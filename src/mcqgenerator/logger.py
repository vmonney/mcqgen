"""Logging configuration for the project."""
import logging
from datetime import datetime
from pathlib import Path

import pytz

swiss_tz = pytz.timezone("Europe/Zurich")
LOG_FILE = f"{datetime.now(swiss_tz).strftime('%Y_%m_%d_%H_%M_%S')}.log"

log_path = Path.cwd() / "logs"

log_path.mkdir(parents=True, exist_ok=True)

LOG_FILEPATH = log_path / LOG_FILE

logging.basicConfig(
    level=logging.INFO,
    filename=LOG_FILEPATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
)
