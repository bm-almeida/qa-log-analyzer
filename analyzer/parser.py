import re
import logging
from analyzer.models import LogEntry

# Strict regex matching standard log layout: YYYY-MM-DD HH:MM:SS,mmm - LEVEL - Message
LOG_PATTERN = re.compile(
    r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) - (INFO|WARNING|ERROR) - (.*)$"
)

def read_logs(file_path):
    """Safely reads lines from the target log file with granular error trapping."""
    try:
        with open(file_path, "r") as file:
            return file.readlines()

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []

    except PermissionError:
        print(f"Error: Permission denied to access '{file_path}'.")
        return []

    except Exception as e:
        print(f"Unexpected error while reading file: {e}")
        return []

def parse_lines(lines):
    """Iterates through lines and parses them into structured LogEntry objects."""
    entries = []

    for line in lines:
        try:
            line = line.strip() # Strip tracking newlines and whitespace
            
            if not line: # Ignore blank spacing lines without raising warnings
                continue
                
            match = LOG_PATTERN.match(line)
            
            if match:
                # Capture regex groups explicitly
                timestamp = match.group(1)
                level = match.group(2)
                message = match.group(3)
                
                entries.append(LogEntry(timestamp=timestamp, level=level, message=message))
            else:
                # Catch lines that exist but fail to conform to standard specification
                logging.warning(f"Skipped invalid log format line: '{line}'")
                
        except Exception as e:
            # Isolates inner loop processing failures so one corrupt line won't crash the pipeline
            logging.error(f"Failed to parse line: {line} - Error: {e}")
            
    return entries