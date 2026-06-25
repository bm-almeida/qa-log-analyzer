# QA Log Analyzer

A Python-based log analysis tool designed to process, validate, and report on production and validation logs. The project is being developed as a learning exercise in software engineering, QA automation, and industrial validation workflows, with a long-term goal of evolving into a solar inverter production validation tool.

## Project Objectives

* Parse and analyze structured log files
* Generate human-readable and machine-readable reports
* Detect errors and validation issues efficiently
* Improve software engineering practices through incremental development
* Build a foundation for industrial QA and manufacturing validation tools

---

## Current Features

### Log Processing
* Reads log files from disk
* Supports structured log format validation
* Parses log entries into strongly typed objects
* Skips malformed log entries safely
* Handles empty lines and invalid records

### Analysis
* Counts INFO, WARNING, and ERROR entries
* Calculates total valid log entries
* Calculates error rate percentage
* Collects detailed error messages for reporting

### Reporting
* Generates text reports
* Generates JSON reports
* Provides summary statistics
* Includes detailed error information

### Error Handling
- Missing file detection
- Permission error handling
- Empty file detection
- Invalid log format detection
- Malformed log logging (non-crashing)
- Parser-level exception protection per entry
- Safe report generation with directory auto-creation
- Graceful handling of unexpected runtime errors
---

## Project Structure

```text
qa-log-analyzer/

├── main.py
├── analyzer/
│   ├── __init__.py
│   ├── models.py
│   ├── parser.py
│   ├── reporter.py
│   └── stats.py
├── logs/
├── reports/
└── tests/
```

---

## Architecture

### LogEntry Model

The application uses a structured data model based on Python dataclasses.

```python
@dataclass
class LogEntry:
    timestamp: str
    level: str
    message: str
```

This provides a cleaner and more maintainable approach compared to processing raw strings throughout the application.

### Processing Pipeline

```text
Log File
    ↓
read_logs()
    ↓
parse_lines()
    ↓
LogEntry Objects
    ↓
analyze_logs()
    ↓
generate_report()
    ↓
Text + JSON Reports
```

---

## Development Progress

### Phase 1 – Project Structure

* Completed
* Log reading
* Log analysis
* Report generation
* Basic metrics
* Modular architecture

### Phase 2 – LogEntry Model

* Completed
* Introduced LogEntry dataclass
* Refactored parser to return structured objects
* Added regex-based log validation
* Added malformed log detection
* Improved maintainability and documentation

### Phase 3 – Robust Error Handling
- Completed
- Missing file handling
- Permission error handling
- Empty file detection
- Malformed log detection
- Parser exception protection
- Report generation safety
- Automatic reports directory creation
- Graceful failure handling
- Improved fault tolerance across pipeline


#### Phase 4 - Statistics Engine
- Completed
* Warning rate calculation
* Error trends tracking
* Frequency analysis overtimeline splits
* Isolation of most common strutctural exceptions

### Planned Future Phases

#### Solar Inverter Validation

* Fault code recognition
* Fault categorization
* Validation rules
* PASS / FAIL evaluation

#### Production QA Features

* Batch log processing
* Yield calculations
* CSV exports
* Validation dashboards

---

## Example Log Format

```text
2026-06-17 10:00:01 INFO System boot initiated
2026-06-17 10:00:20 WARNING Sensor calibration delay detected
2026-06-17 10:02:00 ERROR Database connection lost
```

---

## Running the Application

```bash
python main.py logs/sample.log
```

If no file is provided, the application will use the default sample log.

---

## Project Goals

This project is intentionally being developed in incremental phases to simulate a real-world software engineering workflow. The focus is not only on functionality but also on maintainability, architecture, testing, error handling, and long-term scalability.

Future versions will target industrial validation use cases, particularly for solar inverter production and quality assurance environments.
