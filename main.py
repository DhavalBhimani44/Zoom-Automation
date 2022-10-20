from datetime import datetime
import os
import pyautogui
import time
import pandas as pd

def sign_in(meetingid, password):
    #opens zoom app
    zoompath = "C:/Users/dhava/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Zoom/Zoom.lnk"
    os.startfile(zoompath)

    time.sleep(2)

    #clicks the join button 
    join_button = pyautogui.locateCenterOnScreen("E:\Zoom automation\images\join_button.png")
    pyautogui.moveTo(join_button)
    pyautogui.click()

    #meeting id
    meeting_id_btn = pyautogui.locateCenterOnScreen("E:\Zoom automation\images\meetingid_button.png")
    pyautogui.moveTo(meeting_id_btn)
    pyautogui.click()
    pyautogui.write(meetingid)

    #Disable mic and video
    media_button = pyautogui.locateAllOnScreen("E:\Zoom automation\images\media_button.png")
    for btn in media_button:
        pyautogui.moveTo(btn)
        pyautogui.click()
        time.sleep(3)
    
    #Hits the join button
    join_btn = pyautogui.locateCenterOnScreen("E:\Zoom automation\images\join_btn.png")
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    
    time.sleep(5)

    #Types the password and hits enter
    meeting_pswd_btn = pyautogui.locateCenterOnScreen("E:\Zoom automation\images\meeting_pswd_btn.png")    
    pyautogui.moveTo(meeting_pswd_btn)
    pyautogui.click()
    pyautogui.write(password)
    pyautogui.press('enter')
       
sign_in("23432432432", "2342342")



    