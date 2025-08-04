import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("DreamsMusic")

# Logger setup
LOGGER = logging.getLogger("DreamsMusic")
LOGGER.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

if not LOGGER.hasHandlers():
    LOGGER.addHandler(console_handler)
