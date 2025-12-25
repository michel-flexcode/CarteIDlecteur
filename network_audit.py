import os
import time
import threading
import sys

def list_net_sockets():
    sockets = set()
    for proto in ("tcp", "tcp6", "udp", "udp6"):
        path = f"/proc/net/{proto}"
        if not os.path.exists(path):
            continue
        with open(path) as f:
            next(f)  # skip header
            for line in f:
                parts = line.split()
                local = parts[1]
                remote = parts[2]
                state = parts[3]
                sockets.add((proto, local, remote, state))
    return sockets


class NetworkAudit:
    def __init__(self, interval=0.2):
        self.interval = interval
        self.baseline = list_net_sockets()
        self.running = False

    def _watch(self):
        while self.running:
            current = list_net_sockets()
            diff = current - self.baseline
            if diff:
                print("❌ ACTIVITÉ RÉSEAU DÉTECTÉE :", file=sys.stderr)
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
