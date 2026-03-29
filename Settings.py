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

config = configparser.ConfigParser()

# Read the existing file
config.read('launcher.ini')

def app_1():
  file_path1 = filedialog.askopenfilename(
    title="Select a file",
    filetypes=[("Executables", "*.exe"), ("Batch files", "*.bat"), ("All files", "*.*")]
  )    
  section = 'Apps'
  key = '1'
  value = file_path1  # new value

# If the section does not exist, create it
  if not config.has_section(section):
      config.add_section(section)

# Set the key/value
  config.set(section, key, value)

# Write changes back to the file
  with open('launcher.ini', 'w') as configfile:
     config.write(configfile)

def app_2():
  file_path1 = filedialog.askopenfilename(
    title="Select a file",
    filetypes=[("Executables", "*.exe"), ("Batch files", "*.bat"), ("All files", "*.*")]
  )    
  section = 'Apps'
  key = '2'
  value = file_path1  # new value

# If the section does not exist, create it
  if not config.has_section(section):
      config.add_section(section)

# Set the key/value
  config.set(section, key, value)

# Write changes back to the file
  with open('launcher.ini', 'w') as configfile:
     config.write(configfile)

def app_3():
  file_path1 = filedialog.askopenfilename(
    title="Select a file",
    filetypes=[("Executables", "*.exe"), ("Batch files", "*.bat"), ("All files", "*.*")]
  )    
  section = 'Apps'
  key = '3'
  value = file_path1  # new value

# If the section does not exist, create it
  if not config.has_section(section):
      config.add_section(section)

# Set the key/value
  config.set(section, key, value)

# Write changes back to the file
  with open('launcher.ini', 'w') as configfile:
     config.write(configfile)

def app_4():
  file_path1 = filedialog.askopenfilename(
    title="Select a file",
    filetypes=[("Executables", "*.exe"), ("Batch files", "*.bat"), ("All files", "*.*")]
  )    
  section = 'Apps'
  key = '4'
  value = file_path1  # new value

# If the section does not exist, create it
  if not config.has_section(section):
      config.add_section(section)

# Set the key/value
  config.set(section, key, value)

# Write changes back to the file
  with open('launcher.ini', 'w') as configfile:
     config.write(configfile)

def app_5():
  file_path1 = filedialog.askopenfilename(
    title="Select a file",
    filetypes=[("Executables", "*.exe"), ("Batch files", "*.bat"), ("All files", "*.*")]
  )    
  section = 'Apps'
  key = '5'
  value = file_path1  # new value

# If the section does not exist, create it
  if not config.has_section(section):
      config.add_section(section)

# Set the key/value
  config.set(section, key, value)

# Write changes back to the file
  with open('launcher.ini', 'w') as configfile:
     config.write(configfile)

def app_6():
  file_path1 = filedialog.askopenfilename(
    title="Select a file",
    filetypes=[("Executables", "*.exe"), ("Batch files", "*.bat"), ("All files", "*.*")]
  )    
  section = 'Apps'
  key = '6'
  value = file_path1  # new value

# If the section does not exist, create it
  if not config.has_section(section):
      config.add_section(section)

# Set the key/value
  config.set(section, key, value)

# Write changes back to the file
  with open('launcher.ini', 'w') as configfile:
     config.write(configfile)     

def app_7():
  file_path1 = filedialog.askopenfilename(
    title="Select a file",
    filetypes=[("Executables", "*.exe"), ("Batch files", "*.bat"), ("All files", "*.*")]
  )    
  section = 'Apps'
  key = '7'
  value = file_path1  # new value

# If the section does not exist, create it
  if not config.has_section(section):
      config.add_section(section)

# Set the key/value
  config.set(section, key, value)

# Write changes back to the file
  with open('launcher.ini', 'w') as configfile:
     config.write(configfile)

def app_8():
  file_path1 = filedialog.askopenfilename(
    title="Select a file",
    filetypes=[("Executables", "*.exe"), ("Batch files", "*.bat"), ("All files", "*.*")]
  )    
  section = 'Apps'
  key = '8'
  value = file_path1  # new value

# If the section does not exist, create it
  if not config.has_section(section):
      config.add_section(section)

# Set the key/value
  config.set(section, key, value)

# Write changes back to the file
  with open('launcher.ini', 'w') as configfile:
     config.write(configfile)

def app_9():
  file_path1 = filedialog.askopenfilename(
    title="Select a file",
    filetypes=[("Executables", "*.exe"), ("Batch files", "*.bat"), ("All files", "*.*")]
  )    
  section = 'Apps'
  key = '9'
  value = file_path1  # new value

# If the section does not exist, create it
  if not config.has_section(section):
      config.add_section(section)

# Set the key/value
  config.set(section, key, value)

# Write changes back to the file
  with open('launcher.ini', 'w') as configfile:
     config.write(configfile)     

def app_10():
  file_path1 = filedialog.askopenfilename(
    title="Select a file",
    filetypes=[("Executables", "*.exe"), ("Batch files", "*.bat"), ("All files", "*.*")]
  )    
  section = 'Apps'
  key = '10'
  value = file_path1  # new value

# If the section does not exist, create it
  if not config.has_section(section):
      config.add_section(section)

# Set the key/value
  config.set(section, key, value)

# Write changes back to the file
  with open('launcher.ini', 'w') as configfile:
     config.write(configfile)



def time_between():
  time_between_new = input_text_time.get()
  
  if not time_between_new.isdigit():
     ctypes.windll.user32.MessageBoxW(0, u"The value you entered is not a valid digit. Try entering a digit without decimals, space, letter or not negative number.", u"Error. Not valid digit!", 0+16)
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
       with open('launcher.ini', 'w') as configfile:
        config.write(configfile)     

       ctypes.windll.user32.MessageBoxW(0, u"The value you entered was succesfully saved and will be used by the launcher.", u"Success!", 0+64) 
def clear_config():
  confirm = messagebox.askyesno("Clear settings", "Clear all command settings?")
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
        with open('launcher.ini', 'w') as configfile:
            config.write(configfile)
        messagebox.showinfo("Done clearing", "Command settings cleared.")

#Open website of the project
def openWebsite():
   webbrowser.open("https://ferlaty.pages.dev/multiple_app_launcher")

#Open the config file (launcher.ini)
def openConfigFile():
   configFile = 'launcher.ini'
   if platform.system() == "Windows":
     os.startfile(configFile)        

# Main GUI
root = Tk()
frm = ttk.Frame(root, padding=5)
frm.grid()
root.title("Multiple App Launcher")
root.iconbitmap("icon.ico")
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
ttk.Button(frm, text="Command #1", command=app_1, style="TButton").grid(column=0, row=2)
ttk.Button(frm, text="Command #2", command=app_2, style="TButton").grid(column=0, row=3)
ttk.Button(frm, text="Command #3", command=app_3, style="TButton").grid(column=0, row=4)
ttk.Button(frm, text="Command #4", command=app_4, style="TButton").grid(column=0, row=5)
ttk.Button(frm, text="Command #5", command=app_5, style="TButton").grid(column=0, row=6)
ttk.Button(frm, text="Command #6", command=app_6, style="TButton").grid(column=0, row=7)
ttk.Button(frm, text="Command #7", command=app_7, style="TButton").grid(column=0, row=8)
ttk.Button(frm, text="Command #8", command=app_8, style="TButton").grid(column=0, row=9)
ttk.Button(frm, text="Command #9", command=app_9, style="TButton").grid(column=0, row=10)
ttk.Button(frm, text="Command #10", command=app_10, style="TButton").grid(column=0, row=11)
ttk.Label(frm, text="Time delay between executing\nthe commands in seconds (s):", style="style3.TLabel").grid(column=1, row=3)
ttk.Entry(frm, textvariable=input_text_time, font = ('Consolas', 13, 'bold')).grid(column=1, row=4)
ttk.Button(frm, text="Save", command=time_between, style="Accent.TButton").grid(column=1, row=5)
ttk.Button(frm, text="Reset to defualt", command=clear_config, style="Accent.TButton").grid(column=1, row=8)
ttk.Button(frm, text="Open config file\n in text editor", command=openConfigFile, style="Accent.TButton").grid(column=1, row=11)
ttk.Button(frm, text="Quit", command=root.destroy, style="Accent.TButton").grid(column=1, row=15, sticky="e")
ttk.Label(frm, text="").grid(column=0, row=12)
ttk.Button(frm, text="", image=watermark, command=openWebsite).grid(column=0, row=13, sticky="w")
ttk.Label(frm, text="© 2026 Ferlaty. All rights reserved.", style="footer.TLabel").grid(column=0, row=15, sticky="sw")

root.mainloop()