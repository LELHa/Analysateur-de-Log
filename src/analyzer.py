def analyze_logs(logs):
    """
    Analyse une liste de logs et retourne des statistiques.
    """

    statistics = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0,
        "CRITICAL": 0 #on déf par défauts les compteurs
    }

    errors = []

    for log in logs:
        level = log["level"]

        if level in statistics:
            statistics[level] += 1 #on add comme un compteur

        if level == "ERROR" or level == "CRITICAL":
            errors.append(log) #on garder les erreurs pour faire des stats

    return {
        "total" : len(logs),
        "statistics": statistics,
        "errors": errors
    }

#le log obtenu est de la forme level : info, message : login