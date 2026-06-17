# QA Log Analyzer

A simple Python-based log analysis tool designed for QA and debugging workflows. It reads system log files, categorizes events, and generates a structured report highlighting system behavior, warnings, and errors.

---

## Purpose

This project simulates a real-world QA automation task: analyzing application or system logs to identify issues, monitor system health, and produce actionable reports.

It is inspired by environments such as:

- Industrial control systems
- EV charging infrastructure
- Backend service monitoring

---

## Features

- Reads structured log files
- Counts log levels:

    * **INFO**
    * **WARNING**
    * **ERROR**
- Extracts and lists error events
- Generates a summary report (`report.txt`)
- Simple and readable Python implementation

---

## Project Structure

qa-log-analyzer/
│
├── logs/
│   └── sample.log        # Input log file
│
├── analyzer.py           # Main Python script
├── report.txt            # Generated output report
└── README.md

---

## Example Input (log format)

2026-06-17 10:00:01 INFO System started
2026-06-17 10:01:15 WARNING High memory usage
2026-06-17 10:02:00 ERROR Database connection lost

---

## Example Output

LOG ANALYSIS REPORT
=====================

INFO: 3
WARNING: 1
ERROR: 2
---

## How to Run

### 1. Clone the repository

```git clone https://github.com/bm-almeida/qa-log-analyzer.git ```

### 2. Navigate into the project

```bash cd qa-log-analyzer ```

### 3. Run the script

```bash python analyzer.py ```

---

## Skills Demonstrated

- Python scripting
- File handling
- String parsing
- Basic data analysis
- QA mindset (log inspection and defect identification)

---

## Future Improvements

- Add **CLI** arguments (file input selection)
- Add **JSON** report export
- Improve log parsing with regex
- Add severity classification system
- Convert into automated QA test utility

---

## Author

Built as a QA learning project to demonstrate Python scripting and log analysis capabilities.
