import configparser
import subprocess
import time
import os
import ctypes
import sys
import datetime
import logging
import platform

appVersion = "1.4.0-pre"
if platform.system() == "Windows":
  settingsAppPre = "settings.exe"
else:
  settingsAppPre = "settings"  
settingsApp = os.path.join(os.getcwd(), settingsAppPre)
CONFIG_FILE = "launcher.ini"

userName = os.getlogin()
workingDir = os.getcwd()

# Configure logging with a custom format
logging.basicConfig(filename="main.log", filemode="w", format="%(levelname)s: [%(asctime)s] - %(message)s", level=logging.INFO)

# Log basic info
logging.info("Multiple App Launcher")
logging.info(f"Version: {appVersion}")
logging.info(platform.platform())
logging.info(f"Username: {userName}")
logging.info(f"Settings app path: {settingsApp}")
logging.info(f"Working directory: {workingDir}\n----------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n")


#Read the config file
config = configparser.ConfigParser()
config.sections()

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

#Get app directories from the launcher.ini file
app_1 = config.get('Apps', '1')
app_2 = config.get('Apps', '2')
app_3 = config.get('Apps', '3')
app_4 = config.get('Apps', '4')
app_5 = config.get('Apps', '5')
app_6 = config.get('Apps', '6')
app_7 = config.get('Apps', '7')
app_8 = config.get('Apps', '8')
app_9 = config.get('Apps', '9')
app_10 = config.get('Apps', '10')

#Convert the stored strings to directories
app1_dir = os.path.dirname(app_1)
app2_dir = os.path.dirname(app_2)
app3_dir = os.path.dirname(app_3)
app4_dir = os.path.dirname(app_4)
app5_dir = os.path.dirname(app_5)
app6_dir = os.path.dirname(app_6)
app7_dir = os.path.dirname(app_7)
app8_dir = os.path.dirname(app_8)
app9_dir = os.path.dirname(app_9)
app10_dir = os.path.dirname(app_10)

#Get filenames
app1_name = os.path.basename(app_1)
app2_name = os.path.basename(app_2)
app3_name = os.path.basename(app_3)
app4_name = os.path.basename(app_4)
app5_name = os.path.basename(app_5)
app6_name = os.path.basename(app_6)
app7_name = os.path.basename(app_7)
app8_name = os.path.basename(app_8)
app9_name = os.path.basename(app_9)
app10_name = os.path.basename(app_10)

#Get time
time_between = int(config.get('Time', 'time_between'))

#Get current local time
def getCurrentTime():
  global currentTime
  currentTime = datetime.datetime.now()

#Start
getCurrentTime()
print(f"Multiple App Launcher\nVersion: {appVersion}\n")
print(f"[{currentTime.strftime("%X")}] To exit the app, simply close this window or pres CTRL + C.\nHint: you can configure everything in the settings.exe app, even the delay time!")

#Main app logic
def run_commands():
  #App #1
  if not app_1:
     getCurrentTime()
     print(f"[{currentTime.strftime("%X")}] Command #1 is not configured. Exiting the app and opening the settings app.")
     logging.critical("Command #1 is not configured. Exiting the app and opening the settings app.")
     if platform.system() == 'Windows':
      ctypes.windll.user32.MessageBoxW(0, u"Command #1 is not configured. Exiting the app and opening the settings app.", u"Error", 0+16)
     try:
      subprocess.Popen([settingsApp])
     except FileNotFoundError:
       getCurrentTime()
       print(f"[{currentTime.strftime("%X")}] CRITICAL: Can not open settings.exe because it was moved or deleted.")
       logging.critical("Can not open settings.exe because it was moved or deleted.")
       if platform.system() == 'Windows':
        ctypes.windll.user32.MessageBoxW(0, u"Can not open settings.exe because it was moved or deleted.", u"Error: settings.exe not found.", 0+16)
     sys.exit()
  else:
     try:
      subprocess.Popen([app_1], cwd=app1_dir)
      getCurrentTime()
      print(f"[{currentTime.strftime("%X")}] Launching (#1): {app1_name} ({app_1})")
      logging.info(f"Launching (#1): {app1_name} ({app_1})")
      time.sleep(time_between)

     except FileNotFoundError:
      getCurrentTime()
      print(f"[{currentTime.strftime("%X")}] WARNING at command #1: The file {app_1} was moved or deleted.")
      logging.warning(f"The file {app_1} was moved or deleted.")

     except Exception as e:
      getCurrentTime()
      print(f"[{currentTime.strftime("%X")}] CRITICAL: An error occurred: {e}")
      logging.critical(f"An error occurred at command #1: {e}")
      getCurrentTime()
      print(f"[{currentTime.strftime("%X")}] INFO: Error type: {type(e).__name__}")
      logging.info(f"Error type: {type(e).__name__}")
      if platform.system() == 'Windows':
        ctypes.windll.user32.MessageBoxW(0, f"An error ocurred: {e}\nExiting the launcher.", f"Error: {type(e).__name__}", 0+16)
      sys.exit()

  #Main loop 2-10
  for noOfCommands in range (2, 11):
    currentCommand = f"app_{noOfCommands}"
    app_x = globals().get(currentCommand)

    currentCommand_name = f"app{noOfCommands}_name"
    appx_name = globals().get(currentCommand_name)

    currentCommand_dir = f"app{noOfCommands}_dir"
    appx_dir = globals().get(currentCommand_dir)

    if not app_x:
      getCurrentTime()
      print(f"[{currentTime.strftime("%X")}] Command #{noOfCommands} is not configured. Configure it in the settings.")
      logging.warning(f"Command #{noOfCommands} is not configured. Configure it in the settings.")
    else:
        try:
          subprocess.Popen([app_x], cwd=appx_dir)
          getCurrentTime()
          print(f"[{currentTime.strftime("%X")}] Launching (#{noOfCommands}): {appx_name} ({app_x})")
          logging.info(f"Launching (#{noOfCommands}): {appx_name} ({app_x})")
        except  FileNotFoundError:
         getCurrentTime()
         print(f"[{currentTime.strftime("%X")}] WARNING at command #{noOfCommands}: The file {app_x} was moved or deleted.")
         logging.warning(f"The file {app_x} was moved or deleted.") 
        except Exception as e:
          getCurrentTime()
          print(f"[{currentTime.strftime("%X")}] CRITICAL: An error occurred at command #{noOfCommands} ({app_x}): {e}")
          logging.critical(f"An error occurred: {e}")
          getCurrentTime()
          print(f"[{currentTime.strftime("%X")}] INFO: Error type: {type(e).__name__}")
          logging.info(f"Error type: {type(e).__name__}")
          if platform.system() == 'Windows':
            ctypes.windll.user32.MessageBoxW(0, f"An error ocurred at command #{noOfCommands} ({app_x}): {e}", f"Error: {type(e).__name__}", 0+16) 

    time.sleep(time_between)
 

run_commands()

#Exiting  
while True:
  getCurrentTime()
  quiting = input(f"[{currentTime.strftime("%X")}] The app ran all the commands.\n > Action(restart/exit/settings):")
  logging.info("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nThe launcher ran all the commands.")
  if quiting == "exit":
    logging.info("Exiting...")
    sys.exit()
  elif quiting == "restart":
     logging.info("Running the commands again.\n----------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
     run_commands()
  elif quiting == "settings":
    logging.info("Opening the settings app...")  
    try:
      subprocess.Popen([settingsApp])
    except FileNotFoundError:
       print("CRITICAL: Can not open settings.exe because it was moved or deleted.")
       logging.critical("Can not open settings.exe because it was moved or deleted.")
       if platform.system() == 'Windows':
        ctypes.windll.user32.MessageBoxW(0, u"Can not open settings.exe because it was moved or deleted.", u"Error: settings.exe not found.", 0+16)
    sys.exit() 
  else:
    print("Wrong input.")