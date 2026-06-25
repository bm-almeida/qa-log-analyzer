import os
import json

def generate_report(results, output_path="reports/report.txt"):
    """Generates text and JSON summary reports from the analysis results."""
    # Ensure the output directory exists before writing files
    os.makedirs("reports", exist_ok=True)

    try:
        # Write the human-readable text report
        with open(output_path, "w") as report:
            report.write("LOG ANALYSIS REPORT\n")
            report.write("===================\n\n")

            report.write(f"TOTAL ENTRIES: {results['TOTAL']}\n")
            report.write(f"INFO: {results['INFO']}\n")
            report.write(f"WARNING: {results['WARNING']}\n")
            report.write(f"ERROR: {results['ERROR']}\n")
            report.write(f"ERROR RATE: {results['ERROR_RATE']}%\n\n")

            report.write("ERROR DETAILS:\n")

            if results["errors"]:
                for error in results["errors"]:
                    report.write(f"- {error}\n")
            else:
                report.write("No errors found.\n")

        # Format structured data for the machine-readable JSON output
        json_data = {
            "INFO": results["INFO"],
            "WARNING": results["WARNING"],
            "ERROR": results["ERROR"],
            "errors": results["errors"]
        }

        # Save structured results to JSON for potential API or dashboard integration
        with open("reports/report.json", "w") as json_file:
            json.dump(json_data, json_file, indent=4)

    except Exception as e:
        # Prevent file system write issues from crashing the script execution
        print(f"Failed to create report: {e}")