import logging
import sys

def setup_logging(log_file=None, verbose=False):
    """Setup logging configuration."""
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    log_level = logging.DEBUG if verbose else logging.INFO

    handlers = [logging.StreamHandler(sys.stdout)]
    if log_file:
        handlers.append(logging.FileHandler(log_file))

    logging.basicConfig(level=log_level, format=log_format, handlers=handlers)

    global logger
    logger = logging.getLogger(__name__)

# Initialize default logger
setup_logging()

# Expose logger globally
__all__ = ["logger"]
