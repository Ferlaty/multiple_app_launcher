from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import configparser
from tkinter import messagebox
import ctypes
import sv_ttk
import webbrowser
import os
import platform
import logging
import subprocess
import modules


appVersion = "1.4.1"
CONFIG_FILE = "launcher.ini"

userName = os.getlogin()
workingDir = os.getcwd()

config = configparser.ConfigParser()

# Read the existing file
launcherINI = config.read(CONFIG_FILE)

if not launcherINI:
  config['Apps'] = {'1': '',
                     '2': '',
                     '3': '',
                     '4': '',
                     '5': '',
                     '6': '',
                     '7': '',
                     '8': '',
                     '9': '',
                     '10': ''}
  config['Time'] = {'time_between': '5'}
  with open(CONFIG_FILE, 'w') as configfile:
   config.write(configfile)

logging.basicConfig(filename="settings.log", filemode="w", format="%(levelname)s: [%(asctime)s] - %(message)s", level=logging.INFO)

# Log basic info
logging.info("Multiple App Launcher")
logging.info(f"Version: {appVersion}")
logging.info(platform.platform())
logging.info(f"Username: {userName}")
logging.info(f"Working directory: {workingDir}\n----------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n")


# Set the dir to launch each command
def set_app(number):

   if platform.system() == "Windows":
     filetypes1=[("Executables", "*.exe"), ("Batch files", "*.bat *.cmd"), ("Windows Installer package", "*.msi"), ("Powershell script", "*.ps1"), ("VBScript", "*.vbs "), ("All files", "*.*")]
   elif platform.system() == "Linux":
      filetypes1=[("No extension", "*"), ("Shell Script", "*.sh"),("Generic Binary Executable", "*.bin"), ("Executable and Linkable Format", "*.elf"), ("Self-Contained Installer/Binary", "*.run"), ("All files", "*.*")]

   file_path1 = filedialog.askopenfilename(
    title="Select a file",
    filetypes=filetypes1
  )    
   section = 'Apps'
   key = f'{number}'
   value = file_path1  # new value

# If the section does not exist, create it
   if not config.has_section(section):
      config.add_section(section)

# Set the key/value
   config.set(section, key, value)

# Write changes back to the file
   with open(CONFIG_FILE, 'w') as configfile:
     config.write(configfile)

   logging.info(f"New value for app_{number}: {file_path1}")



def time_between():
  time_between_new = input_text_time.get()
  
  if not time_between_new.isdigit():
     if platform.system() == 'Windows':
      ctypes.windll.user32.MessageBoxW(0, u"The value you entered is not a valid digit. Try entering a digit without decimals, space, letter or not negative number.", u"Error: Not valid digit!", 0+16)
     elif platform.system() == "Linux":
        messagebox.showerror("Error: Not valid digit!", "The value you entered is not a valid digit. Try entering a digit without decimals, space, letter or not negative number.") 
  else:
       section = 'Time'
       key = 'time_between'
       value = time_between_new  # new value

      # If the section does not exist, create it
       if not config.has_section(section):
        config.add_section(section)

# Set the key/value
       config.set(section, key, value)

# Write changes back to the file
       with open(CONFIG_FILE, 'w') as configfile:
        config.write(configfile)     
       if platform.system() == 'Windows':
         ctypes.windll.user32.MessageBoxW(0, u"The value you entered was succesfully saved and will be used by the launcher.", u"Success!", 0+64)
       elif platform.system() == "Linux":
           messagebox.showinfo("Success!", "The value you entered was succesfully saved and will be used by the launcher.")
       logging.info(f"New value for time_between: {time_between_new}")  
def clear_config():
  confirm = messagebox.askyesno("Reset settings", "Reset all settings?")
  if confirm:
        config = configparser.ConfigParser()
        config['Apps'] = {
            '1': '',
            '2': '',
            '3': '',
            '4': '',
            '5': '',
            '6': '',
            '7': '',
            '8': '',
            '9': '',
            '10': '',
        }
        config['Time'] = {
          'time_between': '5'
        }
        with open(CONFIG_FILE, 'w') as configfile:
            config.write(configfile)
        messagebox.showinfo("Reseted", "Reseted the settings to the defualt one.")
        logging.info(f"Reseted the settings.") 

#Open website of the project
def openWebsite():
   modules.openProjectPage()

#Open the config file (launcher.ini)
def openConfigFile():
   configFile = CONFIG_FILE
   if platform.system() == "Windows":
     os.startfile(configFile)
   elif platform.system() == "Linux":
      subprocess.run(["xdg-open", configFile])

   logging.info(f"Opened the {CONFIG_FILE} file in text editor.")         

# Main GUI
root = Tk()
frm = ttk.Frame(root, padding=5)
frm.grid()
root.title("Multiple App Launcher")
if platform.system() == 'Windows':
   root.iconbitmap("icon.ico")
elif platform.system() == 'Linux':
   imgICO = PhotoImage(file='ico.png')
   root.iconphoto(False, imgICO)   
root.resizable(False, False)

watermark = PhotoImage(file="icon.png")

sv_ttk.set_theme("dark")
#style #1 for labels
style1 = ttk.Style()
style1.configure('style1.TLabel', font=('Segoe UI', 18, 'bold'))

#style #2 for labels
style3 = ttk.Style()
style3.configure('style3.TLabel', font=('Segoe UI', 12))

#btns
style2 = ttk.Style()
style2.configure("TButton", font=("Segoe UI", 14))

#style #3 for labels
style4 = ttk.Style()
style4.configure('style4.TLabel', font=('Segoe UI', 13, 'bold'))

#style for footer
style4 = ttk.Style()
style4.configure('footer.TLabel', font=('Segoe UI', 10))

input_text_time = StringVar()

#Buttons + txt
ttk.Label(frm, text="Multiple App Launcher", style="style1.TLabel").grid(column=0, row=0)
ttk.Label(frm, text="").grid(column=0, row=1)

for noOfBtns in range (1, 11):
   currentRow = noOfBtns + 1
   ttk.Button(frm, text=f"Command #{noOfBtns}", command=lambda n=noOfBtns: set_app(n), style="TButton").grid(column=0, row=currentRow)
ttk.Label(frm, text="Time delay between executing\nthe commands in seconds (s):", style="style3.TLabel").grid(column=1, row=3)
ttk.Entry(frm, textvariable=input_text_time, font = ('Consolas', 13, 'bold')).grid(column=1, row=4)
ttk.Button(frm, text="Save", command=time_between, style="Accent.TButton").grid(column=1, row=5)
ttk.Button(frm, text="Reset to defualt", command=clear_config, style="Accent.TButton").grid(column=1, row=8)
ttk.Button(frm, text="Open config file\n in text editor", command=openConfigFile, style="Accent.TButton").grid(column=1, row=11)
ttk.Button(frm, text="Quit", command=root.destroy, style="Accent.TButton").grid(column=1, row=15, sticky="e")
ttk.Label(frm, text="").grid(column=0, row=12)
openWebsiteBtn = ttk.Label(frm, text="", image=watermark)
openWebsiteBtn.grid(column=0, row=13, sticky="w")
openWebsiteBtn.bind('<Button-1>', lambda event: openWebsite())
ttk.Label(frm, text="© 2026 Ferlaty. Licensed under Apache License 2.0 license.", style="footer.TLabel").grid(column=0, row=15, sticky="sw")

root.mainloop()