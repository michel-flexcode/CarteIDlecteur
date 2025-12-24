# Lecteur eID simple (Belgique)

Ce petit outil permet d'explorer une carte d'identité électronique belge via PC/SC.

Installation

1. Assurez-vous que `pcscd` est installé et en cours d'exécution sur votre système.
2. Installez les dépendances Python:

```bash
python3 -m pip install -r requirements.txt
```

Utilisation

- Lister les lecteurs:

```bash
python3 main.py list
```

- Connecter au lecteur #0 et afficher l'ATR:

```bash
python3 main.py connect -r 0
```

- Envoyer un APDU hexadécimal arbitraire (exemple de SELECT):

```bash
python3 main.py apdu 00A4040007A0000002770101 -r 0
```

Remarques

- Cet outil est minimal et destiné à des tests/expérimentations. L'accès aux données personnelles sur la eID nécessite le respect des règles de sécurité, le PIN et la connaissance des APDUs/structures de fichiers spécifiques.
- Pour un accès complet et documenté au contenu eID (lecture des données signées, certificats), consultez les projets officiels et la documentation `eID` belge (middleware et spécifications ISO7816/APDU).

License: usage personnel / expérimentation.
