import json
from analyzer.models import LogEntry
from analyzer.stats import analyze_logs

def test_log_analysis():
    """Simulates a pipeline output to verify metrics calculation logic."""
    # Mock data: Instantiate LogEntry dataclasses to mirror actual parser output
    sample_logs = [
        LogEntry(timestamp="2026-06-25 10:00:00,000", level="INFO", message="System started"),
        LogEntry(timestamp="2026-06-25 10:01:00,000", level="WARNING", message="Low memory"),
        LogEntry(timestamp="2026-06-25 10:02:00,000", level="ERROR", message="Database failed"),
    ]
    
    # Run the statistical analysis function on the structured mock data
    result = analyze_logs(sample_logs)

    # Print a clean JSON snapshot to easily inspect calculation results
    print("=== DEMO OUTPUT ===")
    print(json.dumps(result, indent=4))

if __name__ == "__main__":
    test_log_analysis()