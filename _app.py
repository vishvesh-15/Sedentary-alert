import os
import json
import platform
from os import path
from time import sleep
import winsound
from win10toast import ToastNotifier



toaster = ToastNotifier()











# assets

APP_ICO = path.join("assets","app.ico")
COFFEE_ICO = path.join("assets","coffee.ico")
TAUNT_WAV=  path.join("assets","taunt.wav")


JSDATA:dict



def load_json():
  with open("appdata.json") as jsfile:
    return json.load(jsfile)
  
 
 

def update_json(data:dict):
  with open("appdata.json","w") as jsfile:
    json.dump(data,jsfile,indent=2)
    
    
    
#notifier

def _notify(msg, icon=COFFEE_ICO, title=None,Soundfile =TAUNT_WAV ):
  toaster.show_toast(title=title if title else "Notification",
                     msg=msg,
                     icon_path=icon,
                     threaded = True)

  if Soundfile:
    winsound.PlaySound(Soundfile,flags=winsound.SND_FILENAME)
    
    
    
def sed_alert():
  dt = load_json()
  
  if dt['sedentary_alert']:
    interval_secs = dt["interval"] * 6
    sleep(interval_secs)
    
    _notify(
      
    msg="Blink Your eyes",)
    
    sed_alert()    
    