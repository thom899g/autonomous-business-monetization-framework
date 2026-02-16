import logging
from typing import Any
from datetime import datetime

class MonetizationLogger:
    def __init__(self, config):
        self.config = config
        self.logger = None
        self._setup_logger()
    
    def _setup_logger(self) -> None:
        """Initialize the logger with specified configuration."""
        logging.basicConfig(
            level=self.config['logging']['level'],
            format='%(asctime)s - %(levelname)s - %(message)s',
            filename=self.config['logging']['file']
        )
        self.logger = logging.getLogger(__name__)
    
    def log_event(self, message: str, level: str = 'INFO') -> None:
        """Log events with timestamp and appropriate level."""
        levels = {
            'DEBUG': logging.DEBUG,
            'INFO': logging.INFO,
            'WARNING': logging.WARNING,
            'ERROR': logging.ERROR,
            'CRITICAL': logging.CRITICAL
        }
        
        if level not in levels:
            raise ValueError("Invalid log level")
            
        self.logger.log(levels[level], message)
    
    def log_error(self, error: Exception) -> None:
        """Log errors with additional context."""
        self.log_event(
            f"Error occurred at {datetime.now()}: {str(error)}", 
            level='ERROR'
        )