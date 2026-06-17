info_account = 0
warning_count = 0
error_count = 0

with open("logs/sample.log", "r") as file:
    lines = file.readlines()

for line in lines:

    if "INFO" in line:
        info_account += 1

    elif"WARNING" in line:
        warning_count += 1

    elif"ERROR" in line:
        error_count += 1        

with open("report.txt", "w") as report:

    report.write("LOG ANALYSIS REPORT\n")
    report.write("=====================\n\n")

    report.write(f"INFO: {info_account}\n")
    report.write(f"WARNING: {warning_count}\n")
    report.write(f"ERROR: {error_count}\n")

    print("Analysis completed! Check report.txt file for detailed information.")