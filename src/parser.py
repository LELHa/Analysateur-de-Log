#parsing = séparer et isoler les infos du fichier log
import re #on cherche des motifs dans du texte


def parse_log_line(line): #on déf la fct qui lit la ligne de log
    """
    Analyse une ligne de log et extrait ses informations.
    """

    pattern = r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.+)" #on décrit le pattern du log
  #le motif étant date heure type message
    match = re.match(pattern, line) #on vérifie la correspondance avec le format

    if match:
        date, time, level, message = match.groups()

        return { #on créer le dico
            "date": date,
            "time": time,
            "level": level,
            "message": message
        }

    return None