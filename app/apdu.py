# app/apdu.py
"""
Fichier centralisant les APDU autorisées pour le projet eID.
But : sécurité et audit, on n'envoie que des commandes prévues.
"""

# Dictionnaire des APDU autorisées
ALLOWED_APDU = {
    # Sélectionner l'application eID sur la carte
    # APDU classique pour accéder à la carte belge
    # CLA=0x00, INS=0xA4 (SELECT), P1=0x04, P2=0x00, Lc=07, Data=A0000002770101
    "select_eid": "00A4040007A0000002770101",

    # Lire un fichier standard (exemple générique)
    # INS=0xCA (GET DATA), P1=P2=00 pour l'exemple
    "get_data": "00CA000000",

    # Exemple de lecture de numéro de série ou autre info (à adapter selon doc eID)
    "read_serial": "00B0950000",  # INS=READ BINARY fictif
}

# Liste blanche pour sécurité et audit
# Seules les clés présentes ici peuvent être utilisées pour envoyer des APDU
def is_allowed(apdu_name: str) -> bool:
    """Vérifie si le nom de l'APDU est autorisé"""
    return apdu_name in ALLOWED_APDU

# Exemple d'utilisation
if __name__ == "__main__":
    for name, apdu in ALLOWED_APDU.items():
        print(f"{name}: {apdu}")
