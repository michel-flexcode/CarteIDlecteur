#!/usr/bin/env python3
"""
CLI simple pour lire une carte d'identité (Belgique) via PKCS#11 (middleware eID).
"""

import argparse
import sys
from network_audit import NetworkAudit  # 🔐 audit réseau
from read_identity import read_eid_identity  # lecture via PKCS#11
from check_middleware import ensure_eid_middleware

# Vérification middleware eID
if not ensure_eid_middleware():
    sys.exit("Le middleware eID est requis pour continuer. Fin du programme.")
print("Middleware eID détecté ✅")

def show_identity():
    """Récupère et affiche nom, prénom et date de naissance."""
    data = read_eid_identity()
    if not data:
        print("Impossible de lire la carte eID.")
        return
    print("Nom      :", data.get("surname"))
    print("Prénom   :", data.get("givenname"))
    print("Naissance:", data.get("birthdate"))


def main():
    parser = argparse.ArgumentParser(description="Lecteur eID simple (Belgique) via PKCS#11")
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("identity", help="Lire identité (nom, prénom, date de naissance)")

    args = parser.parse_args()

    if args.cmd == "identity":
        show_identity()
    else:
        parser.print_help()


if __name__ == "__main__":
    with NetworkAudit():  # 🔐 audit actif sur tout le runtime
        main()
