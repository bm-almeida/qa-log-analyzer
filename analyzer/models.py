from dataclasses import dataclass

# Standardized data structure for a single parsed log line
@dataclass
class LogEntry:
    timestamp: str  # Format: YYYY-MM-DD HH:MM:SS,mmms
    level: str      # INFO, WARNING, or ERROR
    message: str    # The log description payload