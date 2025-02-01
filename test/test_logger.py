import logging

from cli_utils.logger import setup_logging

logger = logging.getLogger("deployment_logger")


def test_logger_info(caplog):
    """Test logger info messages."""
    setup_logging(verbose=False)
    with caplog.at_level(logging.INFO):
        logger.info("Test log message")
    assert "Test log message" in caplog.text


def test_logger_debug(caplog):
    """Test logger debug messages with verbose mode."""
    setup_logging(verbose=True)
    with caplog.at_level(logging.DEBUG):
        logger.debug("Debug log")
    assert "Debug log" in caplog.text
