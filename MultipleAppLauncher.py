import configparser
import subprocess
import time
import os
import ctypes
import sys
import datetime


#Read the config file
config = configparser.ConfigParser()
config.sections()

config.read('launcher.ini')

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
print(f"[{currentTime.strftime("%X")}] To exit the app, simply close this window or pres CTRL + C.\nHint: you can configure everything in the settings.exe app, even the delay time!")

#Main app logic
def run_commands():
  #App #1
  if not app_1:
    print("Command #1 is not configured. Exiting the app and opening the settings app.")
    ctypes.windll.user32.MessageBoxW(0, u"Command #1 is not configured. Exiting the app and opening the settings app.", u"Error", 0+16)
    subprocess.Popen(["settings.exe"])
    sys.exit()
  else:
    subprocess.Popen([app_1], cwd=app1_dir)
    getCurrentTime()
    print(f"[{currentTime.strftime("%X")}] Launching(#1): {app1_name} ({app_1})")
  time.sleep(time_between)
  #App #2
  if not app_2:
    getCurrentTime()
    print(f"[{currentTime.strftime("%X")}] Command #2 is not configured. Configure it in the settings.")
  else:
    subprocess.Popen([app_2], cwd=app2_dir)
    getCurrentTime()
    print(f"[{currentTime.strftime("%X")}] Launching(#2): {app2_name} ({app_2})")
  time.sleep(time_between)
  #App #3
  if not app_3:
    getCurrentTime()
    print(f"[{currentTime.strftime("%X")}] Command #3 is not configured. Configure it in the settings.")
  else:
    subprocess.Popen([app_3], cwd=app3_dir)
    getCurrentTime()
    print(f"[{currentTime.strftime("%X")}] Launching(#3): {app3_name} ({app_3})")
  time.sleep(time_between)
  #App #4
  if not app_4:
    getCurrentTime()
    print(f"[{currentTime.strftime("%X")}] Command #4 is not configured. Configure it in the settings.")
  else:
    subprocess.Popen([app_4], cwd=app4_dir)
    getCurrentTime()
    print(f"[{currentTime.strftime("%X")}] Launching(#4): {app4_name} ({app_4})")
  time.sleep(time_between)
  #App #5
  if not app_5:
    getCurrentTime()
    print(f"[{currentTime.strftime("%X")}] Command #5 is not configured. Configure it in the settings.")
  else:
    subprocess.Popen([app_5], cwd=app5_dir)
    getCurrentTime()
    print(f"[{currentTime.strftime("%X")}] Launching(#5): {app5_name} ({app_5})")
  time.sleep(time_between)
  #App #6
  if not app_6:
    getCurrentTime()
    print(f"[{currentTime.strftime("%X")}] Command #6 is not configured. Configure it in the settings.")
  else:
    subprocess.Popen([app_6], cwd=app6_dir)
    getCurrentTime()
    print(f"[{currentTime.strftime("%X")}] Launching(#6): {app6_name} ({app_6})")
  time.sleep(time_between)
  #App #7
  if not app_7:
    getCurrentTime()
    print(f"[{currentTime.strftime("%X")}] Command #7 is not configured. Configure it in the settings.")
  else:
    subprocess.Popen([app_7], cwd=app7_dir)
    getCurrentTime()
    print(f"[{currentTime.strftime("%X")}] Launching(#7): {app7_name} ({app_7})")
  time.sleep(time_between)
  #App #8
  if not app_8:
    getCurrentTime()
    print(f"[{currentTime.strftime("%X")}] Command #8 is not configured. Configure it in the settings.")
  else:
    subprocess.Popen([app_8], cwd=app8_dir)
    getCurrentTime()
    print(f"[{currentTime.strftime("%X")}] Launching(#8): {app8_name} ({app_8})")
  time.sleep(time_between)
  #App #9
  if not app_9:
    getCurrentTime()
    print(f"[{currentTime.strftime("%X")}] Command #9 is not configured. Configure it in the settings.")
  else:
    subprocess.Popen([app_9], cwd=app9_dir)
    getCurrentTime()
    print(f"[{currentTime.strftime("%X")}] Launching(#9): {app9_name} ({app_9})")
  time.sleep(time_between)
  #App #10
  if not app_10:
    getCurrentTime()
    print(f"[{currentTime.strftime("%X")}] Command #10 is not configured. Configure it in the settings.")
  else:
    subprocess.Popen([app_10], cwd=app10_dir)
    getCurrentTime()
    print(f"[{currentTime.strftime("%X")}] Launching(#10): {app10_name} ({app_10})")

run_commands()

#Exiting  
while True:
  getCurrentTime()
  quiting = input(f"[{currentTime.strftime("%X")}] The app run all the commands. If you want to exit, type 'exit', 'restart' to run the commands again.\n")
  if quiting == "exit":
    sys.exit()
  elif quiting == "restart":
     run_commands()
  else:
    print("Wrong input.")