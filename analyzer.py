import sys
import json
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log",
    filemode="w"
)

def read_logs(file_path):
    with open(file_path, "r") as file:
        return file.readlines()

def analyze_logs(lines):
    results = {"INFO": 0, "WARNING": 0, "ERROR": 0, "errors": []}

    for line in lines:
        if "INFO" in line:
            results["INFO"] += 1
        elif "WARNING" in line:
            results["WARNING"] += 1
        elif "ERROR" in line:
            results["ERROR"] += 1
            results["errors"].append(line.strip())

    return results

def generate_report(results, output_path="report.txt"):
    # Text Report
    with open(output_path, "w") as report:
        report.write("LOG ANALYSIS REPORT\n")
        report.write("=====================\n\n")

        report.write(f"INFO: {results['INFO']}\n")
        report.write(f"WARNING: {results['WARNING']}\n")
        report.write(f"ERROR: {results['ERROR']}\n\n")

        report.write("ERROR DETAILS:\n")
        for error in results["errors"]:
            report.write(f"- {error}\n")

    # Json report
    json_data = {
        "INFO": results["INFO"],
        "WARNING": results["WARNING"],
        "ERROR": results["ERROR"],
        "errors": results["errors"]
    }

    with open("report.json", "w") as json_file:
        json.dump(json_data, json_file)
def main():
    # CLI argurment handling
    file_path = sys.argv[1] if len(sys.argv) > 1 else "logs/sample.log"
    
    logging.info("Starting log analysis")

    lines = read_logs(file_path)
    logging.info(f"Loaded log file {file_path}")

    results = analyze_logs(lines)
    logging.info("Log analysis completed")
    
    generate_report(results)

    print(f"Analysis completed for: {file_path}")

    
if __name__ == "__main__":
    main()
