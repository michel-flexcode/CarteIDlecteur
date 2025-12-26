CARTEIDLECTEUR/
├── README.md
├── LICENSE
│
├── app/
│   ├── main.py                 # ton CLI (ou GUI)
│   ├── network_audit.py        # audit réseau
│   ├── apdu.py                 # APDU autorisées (whitelist) (les apdu ne sont pas fournies par le gvt belge) > libbeidpkcs11.so sait
│   ├── read_identity.py        # via package ?
│   └── __init__.py
│
├── packaging/
│   ├── deb/
│   │   ├── control             # paquet Debian
│   │   ├── postinst            # démarre pcscd
│   │   └── rules               # permissions udev lecteur
│   │
│   ├── appimage/
│   │   └── AppRun
│   │
│   └── pyinstaller.spec        # build binaire
│
├── scripts/
│   ├── install.sh              # installateur IT (1 fois)
│   ├── check_env.sh            # vérifie pcscd, lecteur
│   └── run_safe.sh             # unshare + audit réseau
│
├── docs/
│   ├── SECURITY.md             # modèle de menace
│   ├── ARCHITECTURE.md         # séparation OS / app
│   └── COMPLIANCE.md           # ce qui est légal / pas
│
├── requirements.txt            # pyscard seulement
└── Makefile


Penser désinstallation 


Penser sécurité et audit

isolation Linux native
aucune syscall réseau possible
audit écrit noir sur blanc
pas de dépendance cloud

Principes 
SOC,