import sys
import logging

from analyzer.parser import read_logs, parse_lines
from analyzer.stats import analyze_logs
from analyzer.reporter import generate_report

# Configure root logger to track runtime events and parsing warnings/errors
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log",
    filemode="w"
)

def main():
    # Use command-line argument if provided, otherwise fall back to default sample log
    file_path = sys.argv[1] if len(sys.argv) > 1 else "logs/sample.log"

    logging.info("Starting log analysis")

    # Step 1: Read raw strings from the log file
    lines = read_logs(file_path)
    
    # Step 2: Safe execution block for string parsing engine
    try:
        entries = parse_lines(lines)
    except Exception as e:    
        print(f"Parsing failed: {e}")
        return
    
    # Step 3: Run metric calculations on structured entries
    results = analyze_logs(entries)

    # Step 4: Output text and JSON reports to filesystem
    generate_report(results, "reports/report.txt")

    print(f"Analysis completed for: {file_path}")

if __name__ == "__main__":
    main()