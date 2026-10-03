# Exemple de liste de coupes. Copie ce fichier dans le dossier de ton projet sous le nom edit.py.
# Claude l'écrit pour toi après avoir lu les transcriptions (.txt).
SRC = "/Users/TON_NOM/Downloads/Mes rushs"   # dossier des vidéos

A, B = "CLIP_0001", "CLIP_0002"   # noms des rushs, sans l'extension
EDIT = [
    # (rush, début en s, fin en s, partie, ce qu'on entend)
    (A, 12.4, 18.9, "ACCROCHE", "La phrase qui donne envie de regarder la suite."),
    (B, 3.0, 11.5, "CONTEXTE", "On explique ce qui se passe."),
    (A, 40.2, 52.0, "MOMENT FORT", "La réaction, le rebondissement."),
    (B, 80.0, 86.3, "FIN", "La conclusion + appel à l'action."),
]
