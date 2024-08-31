import logging

# Set up logging
logging.basicConfig(
    filename='pyselenium_project_log.txt',  # Specify the log file name
    filemode='a',  # Append to the file instead of overwriting ('w' for overwrite)
    # Formatting the logging msg: timestamp - severity level - message
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log message format
    level=logging.INFO  # Log level
)