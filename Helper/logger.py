import logging
import os
import allure

def setup_logger(log_level=logging.INFO):
    """
    Set up a logger to log messages to both a file and Allure reports.
    """
    log_dir = "logs"
    log_file = os.path.join(log_dir, "test_log.log")

    # Ensure the logs directory exists
    os.makedirs(log_dir, exist_ok=True)

    # Create a logger instance
    logger = logging.getLogger("TestLogger")
    logger.setLevel(log_level)

    # Avoid duplicate handlers
    if logger.handlers:
        return logger

    # File handler: Logs messages to a file
    file_handler = logging.FileHandler(log_file, mode="a")
    file_handler.setLevel(log_level)
    file_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(file_format)

    # Stream handler: Logs messages to console
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(log_level)
    stream_handler.setFormatter(file_format)

    # Allure handler: Attach logs only if a test is running
    class AllureHandler(logging.Handler):
        def emit(self, record):
            try:
                log_message = self.format(record)
                if record.levelno >= logging.ERROR:
                    allure.attach(log_message, name="ERROR LOG", attachment_type=allure.attachment_type.TEXT)
                else:
                    allure.attach(log_message, name="LOG", attachment_type=allure.attachment_type.TEXT)
            except KeyError:
                # Skip attaching logs if Allure context is not active
                pass

    allure_handler = AllureHandler()
    allure_handler.setFormatter(file_format)

    # Add all handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    logger.addHandler(allure_handler)

    # Log to file and console only (not Allure) to confirm setup
    logger.info("Logger has been set up successfully!")

    return logger
