#!/usr/bin/env bash
set -e

APP_DIR="/opt/eid-client"
PYTHON="/usr/bin/python3"
APP="$APP_DIR/app/main.py"

echo "[+] Starting eID client in network-isolated mode"

# Vérification pcscd
if ! systemctl is-active --quiet pcscd; then
  echo "[-] pcscd is not running"
  exit 1
fi

# Audit réseau AVANT
echo "[+] Network sockets BEFORE:"
$PYTHON $APP_DIR/app/network_audit.py --snapshot before

# Lancement isolé réseau
unshare -n --fork --mount-proc bash <<EOF
  echo "[+] Inside isolated network namespace"

  # Vérification : aucune interface
  ip a

  # Lancement app
  exec $PYTHON $APP
EOF

# Audit réseau APRÈS
echo "[+] Network sockets AFTER:"
$PYTHON $APP_DIR/app/network_audit.py --snapshot after

echo "[+] eID client exited safely"
