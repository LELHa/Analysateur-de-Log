def read_log_file(filepath):
    """
    Lit un fichier de logs et retourne une liste de lignes.
    """

    with open(filepath, "r", encoding="utf-8") as file: #r pour le mode read
        lines = file.readlines() #on aura des espaces

    return lines