def analyze_logs(entries):
    """Calculates log metrics and aggregates a list of error descriptions."""
    # Initialize the results dictionary to accumulate metrics
    results = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0,
        "errors": [],
        "TOTAL": 0
    }

    # Process each log entry to update counts and collect error data
    for entry in entries:
        results["TOTAL"] += 1

        if entry.level == "INFO":
            results["INFO"] += 1

        elif entry.level == "WARNING":
            results["WARNING"] += 1

        elif entry.level == "ERROR":
            results["ERROR"] += 1
            # Fixed: Removed () since message is a string attribute, not a function
            results["errors"].append(entry.message)

    # Protect against ZeroDivisionError if the log file was completely empty
    error_rate = (
        (results["ERROR"] / results["TOTAL"] * 100)
        if results["TOTAL"] > 0
        else 0
    )        

    # Round off decimal points for clean report metrics
    results["ERROR_RATE"] = round(error_rate, 2)

    return results