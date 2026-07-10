from src.reader import read_log_file
from src.parser import parse_log_line
from src.analyzer import analyze_logs

#ecture du fichier
logs = read_log_file("logs/example.log") #prends le fichier log cible

#isole les infos
parsed_logs = []

for log in logs:
    result = parse_log_line(log)

    if result:
        parsed_logs.append(result)

#analyse 
report = analyze_logs(parsed_logs)
print("log report")
print()
print("stats")
for level, count in report["stats"].items():
    print(f"{level}: {count}")
print()
print("Errors dected:")
for error in report["errors"]:
    print(".", error["message"])