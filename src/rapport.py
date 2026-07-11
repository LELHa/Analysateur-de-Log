def generate_rapport(rapport, output_file):
    """
    Génère un rapport texte avec les stats 
    et la liste d'erreurs détectées.
    """
    with open(output_file, "w", encoding="utf-8") as file: #en mode écriture
        file.write("RAPPORT DE LOG\n\n")
        file.write(f"Total events: {rapport['total']}\n\n")
        file.write(f"Invalid lines: {rapport['invalid_logs']}\n\n")
        file.write("Stats:\n")
        for level, count in rapport["statistics"].items():
            file.write(f"{level}:{count}\n")
        file.write("\nErrors detected:\n")

        if rapport["errors"]:
            for error in rapport["errors"]:
                file.write(f"-{error['message']}\n")
        else: 
            file.write("No errors detected.\n")