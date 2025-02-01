import logging
import sys


def setup_logging(log_file=None, verbose=False):
    """Setup logging configuration."""
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    log_level = logging.DEBUG if verbose else logging.INFO

    global logger
    logger = logging.getLogger("deployment_logger")
    logger.setLevel(log_level)

    # Remove existing handlers to prevent duplicates
    if logger.hasHandlers():
        logger.handlers.clear()

    # Console handler (prints to terminal)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level)
    console_handler.setFormatter(logging.Formatter(log_format))
    logger.addHandler(console_handler)

    # File handler (writes logs to file if provided)
    if log_file:
        file_handler = logging.FileHandler(log_file, mode="a")  # Append mode
        file_handler.setLevel(log_level)
        file_handler.setFormatter(logging.Formatter(log_format))
        logger.addHandler(file_handler)

    # Ensure logs are written immediately
    for handler in logger.handlers:
        handler.flush()

# Expose logger globally
__all__ = ["logger", "setup_logging"]
