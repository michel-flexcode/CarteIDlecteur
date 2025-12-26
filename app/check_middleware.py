import os
import subprocess
import shutil
import sys

PKCS11_LIB_PATH = "/usr/lib/x86_64-linux-gnu/libbeidpkcs11.so"

def is_eid_installed():
    """Vérifie si la librairie PKCS#11 du middleware eID existe."""
    return os.path.exists(PKCS11_LIB_PATH)

def install_eid_middleware():
    """Installe automatiquement le middleware eID sur Linux Debian/Ubuntu."""
    print("Middleware eID non trouvé. Tentative d'installation...")
    try:
        # Met à jour les dépôts
        subprocess.run(["sudo", "apt", "update"], check=True)
        # Installe le middleware
        subprocess.run(["sudo", "apt", "install", "-y", "eid-mw"], check=True)
        print("Installation du middleware eID terminée ✅")
        return True
    except subprocess.CalledProcessError:
        print("Erreur lors de l'installation du middleware. Veuillez l'installer manuellement.")
        return False

def ensure_eid_middleware():
    """Vérifie et installe le middleware si nécessaire."""
    if is_eid_installed():
        return True
    return install_eid_middleware()
