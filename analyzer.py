import sys

def read_logs(file_path):
    with open(file_path, "r") as file:
        return file.readlines()

import sys
    
def analyze_logs(lines):
    results = {"INFO": 0, "WARNING": 0, "ERROR": 0, "errors": []}

    for line in lines:
       if "INFO" in line:
        results["INFO"] += 1

       elif"WARNING" in line:
        results["WARNING"] += 1

       elif"ERROR" in line:
        results["ERROR"] += 1
        results["errors"].append(line.strip())

    return results
       
def generate_report(results, output_path="report.txt"):
   with open(output_path, "w") as report:
    report.write("LOG ANALYSIS REPORT\n")
    report.write("=====================\n\n")
    report.write(f"INFO: {results['INFO']}\n")
    report.write(f"WARNING: {results['WARNING']}\n")
    report.write(f"ERROR: {results['ERROR']}\n\n")

    report.write("ERROR DETAILS:\n")
    for error in results["errors"]:
      report.write(f"- {error}\n")

def main():
    # CLI argurment handling
    file_path = sys.argv[1] if len(sys.argv) > 1 else "logs/sample.log"
    
    lines = read_logs(file_path)
    results = analyze_logs(lines)
    generate_report(results)

    print(f"Analysis completed for: {file_path}")

    
if __name__ == "__main__":
    main()
