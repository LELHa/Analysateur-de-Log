from src.reader import read_log_file
from src.parser import parse_log_line
from src.analyzer import analyze_logs
from src.rapport import generate_rapport

#ecture du fichier
logs = read_log_file("logs/example.log") #prends le fichier log cible

if not logs: #condition Bool pour si liste vide donc false
    print("No logs to analyze.")
    exit()

#isole les infos
parsed_logs = []

for log in logs:
    result = parse_log_line(log)

    if result:
        parsed_logs.append(result)

#analyse 
report = analyze_logs(parsed_logs)
print("log report")
print() #ligne vide pour retour à la ligne
print("stats")
for level, count in report["statistics"].items(): #items() pour parcourir le dico
    print(f"{level}: {count}")
print()
print("Errors dected:")
for error in report["errors"]:
    print(".", error["message"])

generate_rapport(report, "reports/report.txt")
print("\nReport generated : reports/report.txt")