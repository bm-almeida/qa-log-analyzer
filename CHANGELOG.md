# Changelog

All notable changes to the QA Log Analyzer project will be documented in this file.


## [v0.4] - 2026-06-25
### Completed Phase 4: Statistics Engine
- Expanded calculation engine in `analyzer/stats.py` to calculate floating-point warning rates.
- Updated JSON and text schemas in `analyzer/reporter.py` to output comprehensive metrics.
- Hardened pipeline against zero-division faults when analyzing blank telemetry datasets.

## [v0.3] - 2026-06-25
### Completed Phase 3: Robust Error Handling
- Added graceful `FileNotFoundError` and `PermissionError` safeguards at the application boundaries.
- Implemented automated report directory creation (`os.makedirs`) to prevent system crashes during file IO.
- Structured parser exception handlers to isolate and skip corrupted lines on a per-entry basis without interrupting the loop pipeline.
- Handled empty log files gracefully to prevent logical bugs like `ZeroDivisionError`.

## [v0.2] - 2026-06-22
### Completed Phase 2: Object-Oriented Refactor & Validation
- Implemented the `LogEntry` dataclass to transition from loose string parsing to strongly typed objects.
- Integrated standard regex capturing groups matching the pattern: `YYYY-MM-DD HH:MM:SS,mmm - LEVEL - Message`.
- Added malformed log detection to filter and isolate system anomalies inside `app.log`.
- Refactored code architecture into a clean, separated module package (`analyzer/`).