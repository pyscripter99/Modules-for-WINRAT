def run():
    print("Get pc info")
    import platform, os
    info = {"username": os.getlogin(), "platform": platform.platform()}
    print(info)