import os
import subprocess
import sys

PKCS11_LIB_PATH = "/usr/lib/x86_64-linux-gnu/libbeidpkcs11.so"

def ensure_eid_middleware():
    if os.path.exists(PKCS11_LIB_PATH):
        return True

    print("⚠️ Middleware eID (libbeidpkcs11.so) introuvable.")
    print("Tentative d'installation automatique...")

    # Détecte la distro
    try:
        with open("/etc/os-release") as f:
            os_release = f.read()
    except Exception:
        os_release = ""

    if "Ubuntu" in os_release or "Debian" in os_release:
        cmd = ["sudo", "apt", "update"]
        subprocess.run(cmd, check=True)
        cmd = ["sudo", "apt", "install", "-y", "libbeidpkcs11"]
        subprocess.run(cmd, check=True)
    else:
        print("❌ OS non supporté pour installation automatique.")
        return False

    if os.path.exists(PKCS11_LIB_PATH):
        print("✅ Middleware eID installé et disponible.")
        return True
    else:
        print("❌ Impossible d'installer le middleware automatiquement.")
        return False
