import re

REPORT_CONFIG = {
    "max_int": 100000,
    "line_width": 14
}

PATTERN = {
    "report": r"\d*"
}

def get_report_digits(raw_reports: list) -> list:
    filtered_strings = list()
    resulting_list = list()

    for raw_report in raw_reports:
        if len(raw_report) > REPORT_CONFIG["line_width"]:
            raise Exception("Input must be smaller than 14 characters.")

        if sum(filtered_strings) > REPORT_CONFIG["max_int"]:
            raise ValueError("Resulting number must be smaller than 100000.")

        filtered_strings = [int(value) for value in re.findall(PATTERN["report"], raw_report) if value != '']
        
        resulting_list.append(sum(filtered_strings))


    return resulting_list

amount = int(input("Amount of reports: "))
reports = list()

for i in range(amount):
    reports.append(input(f"[{i + 1}] Report: "))

results = get_report_digits(reports)

print('\nResults: ')
for i in range(len(results)):
    print(f"[{i + 1}] {results[i]}")
