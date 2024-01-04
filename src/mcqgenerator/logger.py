"""Logging configuration for the project."""

import logging
from datetime import datetime
from pathlib import Path

import pytz

# Timezone for Zurich
swiss_tz = pytz.timezone("Europe/Zurich")

# Get the current time in the Swiss timezone
now_swiss = datetime.now(swiss_tz)

# Directory for logs
log_path = Path.cwd() / "logs"
log_path.mkdir(parents=True, exist_ok=True)

# Generate log file name based on the current Swiss time
log_filename = now_swiss.strftime("log_%Y_%m_%d_%H.log")
log_filepath = log_path / log_filename

# Basic logging configuration
logging.basicConfig(
    level=logging.INFO,
    filename=log_filepath.as_posix(),
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    filemode="a",  # Append mode
)
