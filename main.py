#!/usr/bin/env python3
"""
CLI simple pour lire une carte d'identité (Belgique) via PC/SC.

Fonctions:
- lister les lecteurs
- connecter à un lecteur et afficher l'ATR
- envoyer un APDU hexadécimal arbitraire

Ce script est volontairement minimal pour exploration et tests.
"""

import argparse # Core dev python
from smartcard.System import readers # Via pyscard
from smartcard.util import toHexString # Via pyscard (remplacable)


def list_readers():
	r = readers()
	if not r:
		print("Aucun lecteur détecté.")
		return
	for i, reader in enumerate(r):
		print(f"{i}: {reader}")


def connect(reader_index=0):
	r = readers()
	if not r:
		raise SystemExit("Aucun lecteur détecté.")
	if reader_index >= len(r):
		raise SystemExit("Index lecteur invalide.")
	connection = r[reader_index].createConnection()
	connection.connect()
	atr = connection.getATR()
	print("ATR:", toHexString(atr))
	return connection


def send_apdu(connection, apdu_hex):
	try:
		apdu_bytes = bytes.fromhex(apdu_hex)
	except ValueError:
		print("APDU invalide — fournir une chaîne hex sans espaces.")
		return
	apdu = list(apdu_bytes)
	resp, sw1, sw2 = connection.transmit(apdu)
	print("Réponse:", toHexString(resp), f"SW1=0x{sw1:02X}", f"SW2=0x{sw2:02X}")


def main():
	parser = argparse.ArgumentParser(description="Lecteur eID simple (Belgique)")
	sub = parser.add_subparsers(dest="cmd")
	sub.add_parser("list", help="Lister les lecteurs")
	connp = sub.add_parser("connect", help="Connecter et afficher l'ATR")
	connp.add_argument("-r", "--reader", type=int, default=0)
	apdu = sub.add_parser("apdu", help="Envoyer un APDU hex (ex: 00A4040007A0000002770101)")
	apdu.add_argument("apdu_hex")
	apdu.add_argument("-r", "--reader", type=int, default=0)
	args = parser.parse_args()
	if args.cmd == "list":
		list_readers()
	elif args.cmd == "connect":
		connect(args.reader)
	elif args.cmd == "apdu":
		conn = connect(args.reader)
		send_apdu(conn, args.apdu_hex)
	else:
		parser.print_help()


if __name__ == "__main__":
	main()
