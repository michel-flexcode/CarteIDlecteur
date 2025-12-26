# network_audit.py
import os
import time
import threading
import sys


def _list_net_sockets():
	sockets = set()
	for proto in ("tcp", "tcp6", "udp", "udp6"):
		path = f"/proc/net/{proto}"
		if not os.path.exists(path):
			continue
		with open(path) as f:
			next(f)  # skip header
			for line in f:
				p = line.split()
				sockets.add((proto, p[1], p[2], p[3]))
	return sockets


class NetworkAudit:
	def __init__(self, interval=0.2):
		self.interval = interval
		self.baseline = _list_net_sockets()
		self.running = False

	def _watch(self):
		while self.running:
			current = _list_net_sockets()
			diff = current - self.baseline
			if diff:
				print("❌ ACTIVITÉ RÉSEAU DÉTECTÉE", file=sys.stderr)
				for d in diff:
					print(d, file=sys.stderr)
				os._exit(1)
			time.sleep(self.interval)

	def __enter__(self):
		self.running = True
		self.thread = threading.Thread(target=self._watch, daemon=True)
		self.thread.start()
		return self

	def __exit__(self, exc_type, exc, tb):
		self.running = False
