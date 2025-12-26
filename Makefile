# ===========================
# eID Client - Makefile
# ===========================

APP_NAME := eid-client
PREFIX   := /opt/$(APP_NAME)
BIN      := /usr/local/bin/$(APP_NAME)

PYTHON   := /usr/bin/python3

SCRIPTS  := scripts
APP      := app

.PHONY: help check run install uninstall audit clean

help:
	@echo "Targets disponibles:"
	@echo "  make check       Vérifie l'environnement (pcscd, lecteur)"
	@echo "  make run         Lance l'application en mode sécurisé (no network)"
	@echo "  make install     Installe l'application (admin / IT)"
	@echo "  make uninstall   Désinstalle complètement"
	@echo "  make audit       Audit réseau manuel"
	@echo "  make clean       Nettoyage basique"

# ===========================
# Vérifications environnement
# ===========================

check:
	bash $(SCRIPTS)/check_env.sh

# ===========================
# Exécution sécurisée
# ===========================

run:
	bash $(SCRIPTS)/run_safe.sh

# ===========================
# Installation système
# ===========================

install:
	@echo "[+] Installing $(APP_NAME)"
	sudo bash $(SCRIPTS)/install.sh
	@echo "[+] Installation terminée"

# ===========================
# Désinstallation propre
# ===========================

uninstall:
	@echo "[+] Removing $(APP_NAME)"
	sudo rm -rf $(PREFIX)
	sudo rm -f $(BIN)
	sudo rm -f /etc/udev/rules.d/99-eid.rules
	sudo systemctl restart udev || true
	@echo "[+] Désinstallation complète"

# ===========================
# Audit réseau standalone
# ===========================

audit:
	$(PYTHON) $(APP)/network_audit.py

# ===========================
# Nettoyage
# ===========================

clean:
	find . -name "__pycache__" -type d -exec rm -rf {} +
