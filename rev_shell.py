import json, requests, subprocess, socket

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
        s.send(b"Hello There!")
        print(s.recv(1024))
        s.close()
        break
    except: pass
print("Exiting!")
