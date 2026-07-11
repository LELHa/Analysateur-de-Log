def read_log_file(filepath):
    """
    Lit un fichier de logs et retourne une liste de lignes.
    """
    try: 
        with open(filepath, "r", encoding="utf-8") as file: #r pour le mode read
            #si fichier n'existe pas
            #pas de permission pour lire
            #le disque est inaccessible
            return file.readlines()
    except FileNotFoundError: 
        print(f"Error: File '{filepath}' not found.")
        return [] #liste vide pour éviter l'erreur
    except PermissionError:
        print(f"Error: Permission denied for '{filepath}'.")
        return []

