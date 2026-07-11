from src.reader import read_log_file
from src.parser import parse_log_line
from src.analyzer import analyze_logs
from src.rapport import generate_rapport
import argparse #on récupère ce que l'user à écrit

#on fait un analysateur de commandes
parser = argparse.ArgumentParser(
    description="Analyseur de fichiers de logs"
)
parser.add_argument(
    "file", #pour récupèrer un fichier
    help="Chemin vers le fichier de logs à analyser"
)
args = parser.parse_args()
log_file = args.file #on récupère le chemin du fichier

#lire le fichier
logs = read_log_file(log_file)

#ecture du fichier
#logs = read_log_file("logs/example.log") prends le fichier log cible

if not logs: #condition Bool pour si liste vide donc false
    print("No logs to analyze.")
    exit()

#isole les infos
parsed_logs = []

invalid_logs=0 #on créer le compteur

for log in logs:
    result = parse_log_line(log)

    if result:
        parsed_logs.append(result)
    else: 
        invalid_logs += 1

#analyse 
report = analyze_logs(parsed_logs) #on génère le rapport
report["invalid_logs"] = invalid_logs

print("log report")
print() #ligne vide pour retour à la ligne
print("stats")
for level, count in report["statistics"].items(): #items() pour parcourir le dico
    print(f"{level}: {count}")
print()
print("Errors detected:")
for error in report["errors"]:
    print(".", error["message"])

generate_rapport(report, "reports/report.txt")
print("\nReport generated : reports/report.txt")