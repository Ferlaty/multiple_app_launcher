import configparser
import subprocess
import time
import os
import ctypes
import sys

#Start
print("To exit the app, simply close this window.")

#Read the config file
config = configparser.ConfigParser()
config.sections()

config.read('launcher.ini')

#Apps
app_1 = config.get('Apps', '1')
app_2 = config.get('Apps', '2')
app_3 = config.get('Apps', '3')
app_4 = config.get('Apps', '4')
app_5 = config.get('Apps', '5')

app1_dir = os.path.dirname(app_1)
app2_dir = os.path.dirname(app_2)
app3_dir = os.path.dirname(app_3)
app4_dir = os.path.dirname(app_4)
app5_dir = os.path.dirname(app_5)

#Get time
time_between = int(config.get('Time', 'time_between'))

#Main app logic
def run_commands():
  if not app_1:
    print("Command #1 is not configured. Exiting the app and opening the settings app.")
    ctypes.windll.user32.MessageBoxW(0, u"Command #1 is not configured. Exiting the app and opening the settings app.", u"Error", 0+16)
    subprocess.Popen(["settings.exe"])
    sys.exit()
  else:
    subprocess.Popen([app_1], cwd=app1_dir)
    print("Command #1 successfully executed.")
  time.sleep(time_between)
  if not app_2:
    print("Command #2 is not configured. Configure it in the settings.")
  else:
    subprocess.Popen([app_2], cwd=app2_dir)
    print("Command #2 successfully executed.")
  time.sleep(time_between)
  if not app_3:
    print("Command #3 is not configured. Configure it in the settings.")
  else:
    subprocess.Popen([app_3], cwd=app3_dir)
    print("Command #3 successfully executed.")
  time.sleep(time_between)
  if not app_4:
    print("Command #4 is not configured. Configure it in the settings.")
  else:
    subprocess.Popen([app_4], cwd=app4_dir)
    print("Command #4 successfully executed.")
  time.sleep(time_between)
  if not app_5:
    print("Command #5 is not configured. Configure it in the settings.")
  else:
    subprocess.Popen([app_5], cwd=app5_dir)
    print("Command #5 successfully executed.")

run_commands()

#Exiting  
while True:
  quiting = input("The app run all the commands. If you want to exit, type 'exit', 'restart' to run the commands again.\n")
  if quiting == "exit":
    sys.exit()
  elif quiting == "restart":
     run_commands()
  else:
    print("Wrong input.")