import webbrowser
import datetime
import time
from urllib import request

# url
url = f'https://vtl.causewaylink.com.my/'

# Windows Chrome Path
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

# Get User Input time
Set_Hour = int(input('Input Hours in 24 hours format: '))
Set_Minute = int(input('Input Minutes: '))


if __name__ == "__main__":

    substring = "queue-it"

    while True:
        time.sleep(30)   # Recheck time every 30 seconds
        TimeNow_Obj = datetime.datetime.now()
        TimeNow_Hour = TimeNow_Obj.hour
        TimeNow_Minute = TimeNow_Obj.minute
        print(f'Time Now: {TimeNow_Hour}:{TimeNow_Minute}')

        if TimeNow_Hour == Set_Hour and TimeNow_Minute == Set_Minute:
            webbrowser.get(chrome_path).open(url)
            print("done")
            break




