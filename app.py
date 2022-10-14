from tkinter import Frame, Tk, ttk, StringVar, IntVar
from turtle import update
from threading import Thread 

from _app import * 


JSDATA  = load_json()

App = Tk()
App.title("Sedentary Alert")
App.iconbitmap(APP_ICO)
App.resizable(False,False)

#user interface
frame =ttk.Frame(App,padding=10)
frame.grid(row=0,column=0,padx=0,pady=10)


sedentary_alert = IntVar()
sedentary_alert.set(
  
1 if JSDATA["sedentary_alert"] else 0)

def toggle_sed_alert():
  JSDATA["sedentary_alert"] = bool(sedentary_alert.get())
  update_json(JSDATA)

  if JSDATA["sedentary_alert"] and\
    not SED_THREAD.is_alive():
      init_sed_thread()
      SED_THREAD.start()
      







sed_check = ttk.Checkbutton(
  frame,variable=sedentary_alert,
  text="Sedentary Alert", command=toggle_sed_alert
)
sed_check.grid(row=0, column=0,columnspan = 2,pady=5)


sed_lbl  = ttk.Label(frame, text="Interval")
sed_lbl.grid(row=1,column=0,pady=5)

interval_options = ["15 Min","20 Min","30 Min","45 Min"]
interval_period = StringVar()









def interval_change(interval:str):
  JSDATA["interval"] = int(interval.split()[0])
  update_json(JSDATA)




interval_dropdown = ttk.OptionMenu(
  frame,interval_period,"Select", *interval_options,command=interval_change
)
interval_dropdown.grid(row=1,column =1, pady=5, padx=(10,0))
interval_period.set(f"{JSDATA['interval']} Min")

#threading
def init_sed_thread():
  global SED_THREAD
  SED_THREAD = Thread(target=sed_alert,daemon =True )
  
  
init_sed_thread()

if JSDATA["sedentary_alert"]:
  SED_THREAD.start()


App.mainloop()