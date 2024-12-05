import logging
import os

def setup_logger():
    """
    Configure and return a logger instance.
    """
    log_dir = "logs"  # Directory for log files
    try:
        # Ensure the logs directory exists
        os.makedirs(log_dir, exist_ok=True)
        print(f"Logs directory created or exists at: {os.path.abspath(log_dir)}")
    except Exception as e:
        print(f"Failed to create logs directory: {e}")
        raise

    log_file = os.path.join(log_dir, 'test_log.log')
    print(f"Log file path: {log_file}")  # Debugging log file path

    # Clear any existing handlers to avoid conflicts
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # Configure logging to file
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger()

    # Add a console handler for debugging
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Add a test log entry to confirm initialization
    logger.info("Logger initialized with file and console handlers.")
    print("Logger initialized.")  # Debug confirmation
    return logger
