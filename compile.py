import subprocess
import platform
import os
import shutil

def run_build():
    system = platform.system()
    print(f"Detected System: {system}")

    script = str(input("Select the script to compile:\n1 : launcher\n2 : settings\n> "))
    

    if script == "launcher" or script == "1":
        # Common flags for both systems
        # --onefile: Bundles everything into one .exe or binary
        # --clean: Cleans PyInstaller cache
        base_cmd = ["pyinstaller", "--console", "--onedir", "--noupx", "--name=multiple_app_launcher", "MultipleAppLauncher.py"]

        if system == "Windows":
         # --noconsole: Hide the terminal popup on Windows
            # --icon: Point to your .ico file
            cmd = base_cmd + ["--icon=icon.ico", "--version-file=versioninfo.txt"]
    
        elif system == "Linux":
            # On Linux, we usually keep the console capability for launchers
            # but you can add --windowed if you want it strictly GUI
            cmd = base_cmd + ["--icon=ico.png"]
    
        else:
            print("OS not supported for auto-build.")
            return

        print(f"Running command: {' '.join(cmd)}")
        subprocess.run(cmd)

    elif script == "settings" or script == "2":
        base_cmd = ["pyinstaller", "--noconsole", "--onefile", "--noupx", "--name=settings", "Settings.py"]

        if system == "Windows":
         # --noconsole: Hide the terminal popup on Windows
            # --icon: Point to your .ico file
            cmd = base_cmd + ["--icon=icon.ico", "--version-file=versioninfo1.txt"]
    
        elif system == "Linux":
            # On Linux, we usually keep the console capability for launchers
            # but you can add --windowed if you want it strictly GUI
            cmd = base_cmd + ["--icon=ico.png"]
    
        else:
            print("OS not supported for auto-build.")
            return

        print(f"Running command: {' '.join(cmd)}")
        subprocess.run(cmd)

    else:
        print("Wrong input.")
        run_build()    

if __name__ == "__main__":
    run_build()
    print("\nDone! Check the 'dist' folder for your executable.")