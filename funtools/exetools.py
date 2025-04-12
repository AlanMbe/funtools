import subprocess
import os

def pack_with_pyinstaller(pyfile, datas=[], onefile=True, windowed=False, icon=None):
    cmd = ["pyinstaller"]
    if onefile: cmd.append("--onefile")
    if windowed: cmd.append("--windowed")
    if icon: cmd += ["--icon", icon]
    
    for src, dest in datas:
        sep = ";" if os.name == "nt" else ":"
        cmd += ["--add-data", f"{src}{sep}{dest}"]

    cmd.append(pyfile)
    print("run command:", " ".join(cmd))
    subprocess.run(cmd)
