#!/usr/bin/env bash
set -e

echo "[+] Installing eID client system package"

if [ "$EUID" -ne 0 ]; then
  echo "This installer must be run as root"
  exit 1
fi

# Install the .deb package
dpkg -i packaging/deb/eid-client.deb || apt -f install -y

echo "[+] Installation complete"
