def run():
    print("Get pc info")
    import platform, os
    info = {"username": os.getlogin(), "platform": platform.platform(), "uname": platform.uname()}
    print(info)

run()
