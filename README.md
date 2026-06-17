# QA Log Analyzer

A Python-based QA automation tool for analyzing system logs, generating reports, and validating system behavior.

---

## Purpose

This project simulates real-world QA automation by processing application/system logs to:

- Detect issues
- Monitor system behavior
- Generate structured reports
- Validate results using automated tests

Inspired by real environments such as:

- EV charging systems
- Industrial monitoring systems
- Backend service logging pipelines

---

## Features

- Log parsing (INFO / WARNING / ERROR)
- Error extraction and reporting
- CLI support for different log files
- Structured report generation (`report.txt`)
- JSON output (`report.json`)
- Execution logging (`app.log`)
- Automated tests with pytest

---

## Project Structure

```
qa-log-analyzer/
│
├── logs/
│   └── sample.log
│
├── analyzer.py
├── test_analyzer.py
├── report.txt
├── report.json
├── app.log
└── README.md
```

---

## How to Run

### Run analysis
```bash
python analyzer.py logs/sample.log
```

### Run tests
```bash
python -m pytest
```

---

## Skills Demonstrated

- Python scripting
- File handling
- CLI argument parsing
- Logging (debugging & traceability)
- Automated testing (pytest)
- QA automation mindset

---

## Future Improvements

- CI/CD integration (GitHub Actions)
- HTML report generation
- Advanced regex-based parsing
- Severity classification system

---

## Author

QA automation project built to demonstrate Python scripting, testing, and log analysis skills.